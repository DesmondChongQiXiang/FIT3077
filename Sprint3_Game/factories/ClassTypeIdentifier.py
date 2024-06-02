from enum import Enum


class ClassTypeIdentifier(Enum):
    """Identifiers that identify the type of a python class in the game.

    Author: Shen
    """

    tile_cave = "tile_cave"
    tile_normal = "tile_normal"
    player_dragon = "player_dragon"
    chit_card_animal = "chit_card_animal"
    chit_card_pirate = "chit_card_pirate"
