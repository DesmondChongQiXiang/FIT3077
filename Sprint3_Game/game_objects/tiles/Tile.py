from abc import ABC, abstractmethod
from typing import Optional
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.animals.Animal import Animal
from utils.pygame_utils import get_coords_for_center_drawing_in_rect


class Tile(ABC, DrawableByAsset):
    """Represents a tile that a character can stand on.

    Author: Shen
    """

    def __init__(self, draw_data: Optional[DrawProperties], character: Optional[PlayableCharacter] = None, animal: Optional[Animal] = None):
        """
        Args:
            draw_data (Optional): The data specifying how to draw the tile
            character (Optional): The character on the tile
            animal (Optional): The animal on the tile
        """
        self._draw_data = draw_data
        self.__character = character
        self.__animal = animal

    def set_draw_data(self, draw_data: DrawProperties) -> None:
        """Set the data specifying how to draw the tile.

        Args:
            draw_data: The draw data
        """
        self._draw_data = draw_data

    def get_animal(self) -> Optional[Animal]:
        """Get the animal on the tile if it has one.

        Returns:
            The animal on the tile
        """
        return self.__animal

    def get_character_on_tile(self) -> Optional[PlayableCharacter]:
        """Returns the character currently on the tile if there is one.

        Returns:
            The character currently on the tile
        """
        return self.__character

    def set_character_on_tile(self, character: Optional[PlayableCharacter]) -> None:
        """Set the character that is on the tile.

        Args:
            character (optional): The character
        """
        self.__character = character

    @abstractmethod
    def place_character_on_tile(self, character: PlayableCharacter) -> None:
        """Place the character on the tile and perform any functionalities.

        Args:
            character: The character to be placed on the tile.
        """
        ...

    def _get_character_draw_instructions(self) -> list[DrawAssetInstruction]:
        """Get the drawing instructions for showing the character currently on the tile.

        Returns:
            List of drawing instructions
        """
        instructions: list[DrawAssetInstruction] = []
        if self._draw_data is None:
            return instructions

        tile_width, tile_height = self._draw_data.get_size()
        character = self.get_character_on_tile()

        if character is not None:
            char_width, char_height = int(tile_width), int(tile_height)
            char_x, char_y = get_coords_for_center_drawing_in_rect(self._draw_data.get_coordinates(), self._draw_data.get_size(), (char_width, char_height))
            character.set_draw_properties(DrawProperties((char_x, char_y), (char_width, char_height)))

            for inst in character.get_draw_assets_instructions():
                instructions.append(inst)

        return instructions
