from abc import ABC, abstractmethod
from typing import Optional
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.tiles.TileDrawData import TileDrawData

# TODO: incomplete. refer to class diagram

class Tile(ABC, DrawableByAsset):
    """Represents a tile that a character can stand on.

    Author: Shen
    """

    def __init__(self, draw_data: Optional[TileDrawData], character: Optional[PlayableCharacter] = None):
        """
        Args:
            draw_data (Optional): The data specifying how to draw the tile
            character (Optional): The character on the tile
        """
        self.__draw_data = draw_data
        self.__character = character

    def get_draw_data(self) -> Optional[TileDrawData]:
        """Returns the data required to draw the tile if it exists.

        Returns:
            The data required to draw the tile
        """
        return self.__draw_data

    def set_draw_data(self, draw_data: TileDrawData) -> None:
        """Set the data specifying how to draw the tile.
        
        Args:
            draw_data: The draw data
        """
        self.__draw_data = draw_data

    def get_character_on_tile(self) -> Optional[PlayableCharacter]:
        """Returns the character currently on the tile if there is one.

        Returns:
            The character currently on the tile
        """
        return self.__character
