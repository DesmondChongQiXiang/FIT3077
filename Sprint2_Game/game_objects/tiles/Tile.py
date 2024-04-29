from abc import ABC
from typing import Optional
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.characters.PlayableCharacter import PlayableCharacter
from utils.pygame_utils import get_coords_for_center_drawing_in_rect


# TODO: Implement abstract methods later (see class diagram)


class Tile(ABC, DrawableByAsset):
    """Represents a tile that a character can stand on.

    Author: Shen
    """

    def __init__(self, draw_data: Optional[DrawProperties], character: Optional[PlayableCharacter] = None):
        """
        Args:
            draw_data (Optional): The data specifying how to draw the tile
            character (Optional): The character on the tile
        """
        self.__draw_data = draw_data
        self.__character = character

    def get_draw_data(self) -> Optional[DrawProperties]:
        """Returns the data required to draw the tile if it exists.

        Returns:
            The data required to draw the tile
        """
        return self.__draw_data

    def set_draw_data(self, draw_data: DrawProperties) -> None:
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

    def _get_character_draw_instructions(self) -> list[DrawAssetInstruction]:
        """Get the drawing instructions for showing the character currently on the tile.

        Returns:
            List of drawing instructions
        """
        instructions: list[DrawAssetInstruction] = []
        if self.__draw_data is None:
            return instructions

        tile_width, tile_height = self.__draw_data.get_size()
        character = self.get_character_on_tile()

        if character is not None:
            char_width, char_height = int(tile_width), int(tile_height)
            char_x, char_y = get_coords_for_center_drawing_in_rect(self.__draw_data.get_coordinates(), self.__draw_data.get_size(), (char_width, char_height))
            character.set_draw_properties(DrawProperties((char_x, char_y), (char_width, char_height)))

            for inst in character.get_draw_assets_instructions():
                instructions.append(inst)

        return instructions
