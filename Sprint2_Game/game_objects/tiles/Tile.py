from abc import ABC, abstractmethod
from typing import Optional
from screen.DrawableByAsset import DrawableByAsset
from game_objects.characters.PlayableCharacter import PlayableCharacter

# TODO: Incomplete


class Tile(ABC, DrawableByAsset):
    """Represents a tile that a character can stand on.

    Author: Shen
    """

    def __init__(self, coordinates: tuple[int, int], size: tuple[int, int], character: Optional[PlayableCharacter] = None):
        """
        Args:
            coordinates: The coordinate of the tile in form (x, y)
            size: The size of the tile in pixels in form (width, height)
            character (Optional): The character on the tile
        """
        self.__coordinates = coordinates
        self.__size = size
        self.__character = character

    def get_coordinates(self) -> tuple[int, int]:
        """Returns the coordinates of the tile.

        Returns:
            The coordinates of the tile in (x, y)
        """
        return self.__coordinates

    def get_size(self) -> tuple[int, int]:
        """Returns the size of the tile.

        Returns:
           The size of the tile in form (width px, height px)
        """
        return self.__size
