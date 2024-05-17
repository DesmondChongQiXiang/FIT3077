"""Module containing game presets for configuring the game.

Author: Shen
"""

from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.animals.Animal import Animal
from game_objects.chit_cards.AnimalChitCard import AnimalChitCard
from game_objects.chit_cards.PirateChitCard import PirateChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.NormalTile import NormalTile


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
