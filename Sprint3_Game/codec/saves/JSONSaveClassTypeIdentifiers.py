from enum import Enum


class JSONSaveClassTypeIdentifiers(Enum):
    """Identifiers for identifiying the type of class when saving into a JSON file. Values must be strings.

    Author: Shen
    """

    tile_cave = "tile_cave"
    tile_normal = "tile_normal"
