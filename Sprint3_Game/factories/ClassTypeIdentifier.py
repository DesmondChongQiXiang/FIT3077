from enum import Enum


class ClassTypeIdentifier(Enum):
    """Identifiers that uniquely identify the type of a python class in the game.

    Author: Shen
    """

    tile_cave = "tile_cave"
    tile_normal = "tile_normal"
    player_dragon = "player_dragon"
    chit_card_animal = "chit_card_animal"
    chit_card_pirate = "chit_card_pirate"
    chit_card_power = "chit_card_power"
    power_skip = "power_skip"
    power_swap = "power_swap"
