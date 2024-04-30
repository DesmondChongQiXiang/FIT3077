"""Module containing game presets for configuring the game.

Author: Shen
"""

from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.animals.Animal import Animal
from game_objects.chit_cards.AnimalChitCard import AnimalChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.NormalTile import NormalTile


def animal_chit_cards_in_animal_sequence(number: int) -> list[ChitCard]:
    """Generate animal chit cards in sequence of animals in Animal enum and symbol count (i.e 1,2,3).

    Args:
        number: number of chit card to generate

    Returns:
        The list of generated chit cards
    """
    chit_cards: list[ChitCard] = []
    generated = 0

    while generated < number:  # for case where all 1-3 and animal combinations < number
        for i in range(1, 4):
            for animal in Animal:
                chit_cards.append(AnimalChitCard(animal, i))
                generated += 1

                if generated >= number:
                    return chit_cards
    return chit_cards


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
