"""Module containing game presets for configuring the game.

Author: Shen, Rohan
"""

from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.animals.Animal import Animal
from game_objects.chit_cards.AnimalChitCard import AnimalChitCard
from game_objects.chit_cards.PirateChitCard import PirateChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.NormalTile import NormalTile

import random


# --------- CONSTANTS ----------------------------------------------------------------------------------------------------------------

# VOLCANO_CARDS
# The volcano cards used for volcano card generation methods.
VOLCANO_CARDS: list[tuple[Tile, Tile, Tile]] = [
    (NormalTile(Animal.BABY_DRAGON), NormalTile(Animal.BAT), NormalTile(Animal.SPIDER)),
    (NormalTile(Animal.SALAMANDER), NormalTile(Animal.SPIDER), NormalTile(Animal.BAT)),
    (NormalTile(Animal.SPIDER), NormalTile(Animal.SALAMANDER), NormalTile(Animal.BABY_DRAGON)),
    (NormalTile(Animal.BAT), NormalTile(Animal.SPIDER), NormalTile(Animal.BABY_DRAGON)),
    (NormalTile(Animal.SPIDER), NormalTile(Animal.BAT), NormalTile(Animal.SALAMANDER)),
    (NormalTile(Animal.BABY_DRAGON), NormalTile(Animal.SALAMANDER), NormalTile(Animal.BAT)),
    (NormalTile(Animal.BAT), NormalTile(Animal.BABY_DRAGON), NormalTile(Animal.SALAMANDER)),
    (NormalTile(Animal.SALAMANDER), NormalTile(Animal.BABY_DRAGON), NormalTile(Animal.SPIDER)),
]


# --------- METHODS -----------------------------------------------------------------------------------------------------------
def add_animal_chit_cards_in_animal_sequence(number: int, chit_cards: list[ChitCard]) -> None:
    """Generate animal chit cards in sequence of animals in Animal enum and symbol count (i.e 1,2,3) and appends
    them to the end of the list.

    Args:
        number: number of chit card to generate
        chit_cards: the list of chit cards to append to
    """
    generated: int = 0

    while generated < number:  # for case where all 1-3 and animal combinations < number
        for i in range(1, 4):
            for animal in Animal:
                chit_cards.append(AnimalChitCard(animal, i))
                generated += 1

                if generated >= number:
                    return


def add_dragon_pirate_chit_cards_in_sequence(number: int, chit_cards: list[ChitCard]) -> None:
    """Generate dragon pirate chit cards with symbol count 1 and 2 in sequence and appends them to the end of
    the list.

    Args:
        number: number of chit cards to generate
        chit_cards: the list of chit cards to append to
    """
    generated: int = 0

    while generated < number:
        for i in range(1, 3):
            chit_cards.append(PirateChitCard(i))
            generated += 1

            if generated >= number:
                return


def normal_tiles_in_animal_sequence(number: int) -> list[Tile]:
    """Generate normal tiles in sequence of animals in Animal enum.

    Args:
        number: number of tiles to generate

    Returns:
        The list of generated tiles
    """
    tiles: list[Tile] = []
    generated = 0

    while True:  # generate until enough tiles
        for animal in Animal:
            tiles.append(NormalTile(animal))
            generated += 1

            if generated >= number:
                return tiles


def randomised_volcano_card_sequence(n: int) -> list[Tile]:
    """Generate a tile sequence in order that is composed of the specified number of random volcano cards in sequence.

    Volcano cards are a preset sequence of 3 tiles. Volcano cards are chosen randomly without replacement. Once volcano
    cards are exhausted, the volcano cards are replenished and once again chosen randomly.

    Utilises the presets.VOLCANO_CARDS constant as the volcano cards.

    Args:
        n: The number of volcano cards to generate

    Returns:
        The tiles composing the generated sequence.
    """
    generated: int = 0
    tiles: list[Tile] = []
    choices: list[int] = [i for i in range(len(VOLCANO_CARDS))]

    while generated < n:
        # if available choices for volcano cards are empty, replenish choices
        if len(choices) == 0:
            choices = [i for i in range(len(VOLCANO_CARDS))]

        # randomly choose from available volcano cards without replacement, and add its tiles to the growing tile sequence
        rand_i = random.choice(choices)
        rand_volcano_card = VOLCANO_CARDS[rand_i]

        tiles.extend(rand_volcano_card)

        choices.remove(rand_i)  # choose without replacement
        generated += 1

    return tiles
