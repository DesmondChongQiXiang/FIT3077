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
        self._draw_data: Optional[DrawProperties] = draw_data
        self.__character: Optional[PlayableCharacter] = character
        self.__animal: Optional[Animal] = animal

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

    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """Get the instructions required to draw the tiles.

        Returns:
            A list containing the instructions to draw the tile

        Raises:
            Exception if the draw properties were not set prior to a request to draw.
        """
        if self._draw_data is None:
            raise Exception("Tried drawing, but the draw properties (properties required for drawing) weren't set.")
        return self._on_draw_request(self._draw_data)

    @abstractmethod
    def _on_draw_request(self, draw_properties: DrawProperties) -> list[DrawAssetInstruction]:
        """Called when a request is made to draw this object. The implementation must provide the instructions
        required to draw itself on the pygame screen.

        Args:
            draw_properties: The draw properties requesting how to draw this object

        Returns:
            A list the drawing instructions to draw this object.
        """
        ...

    def _default_animal_draw_instructions(self, draw_size_factor: float) -> list[DrawAssetInstruction]:
        """A set of default drawing instructions that shows the animal on top of the tile if there is one.

        Args:
            draw_size_factor: A float that determines how large the animal should be drawn. Higher = smaller

        Returns:
            List of drawing instructions to draw the animal, or an empty list if there is no animal

        Raises:
            Exception if the draw properties for the tile was not set when calling this method
        """
        instructions: list[DrawAssetInstruction] = []
        if self._draw_data is None:
            raise Exception("The draw properties was not set when attempting to get default animal drawing instructions.")
        if self.__animal is None:
            return instructions

        animal_size = int(self._draw_data.get_size()[0] / draw_size_factor)
        animal_x, animal_y = get_coords_for_center_drawing_in_rect(self._draw_data.get_coordinates(), self._draw_data.get_size(), (animal_size, animal_size))
        instructions.append(DrawAssetInstruction(f"assets/animals/{self.__animal.value}.png", animal_x, animal_y, (animal_size, animal_size)))

        return instructions

    def _default_character_draw_instructions(self) -> list[DrawAssetInstruction]:
        """A set of default drawing instructions that shows the character directly on top of the tile if it exists.

        Returns:
            List of drawing instructions to draw the character

        Raises:
            Exception if the draw properties for the tile was not set when calling this method
        """
        instructions: list[DrawAssetInstruction] = []
        if self._draw_data is None:
            raise Exception("The draw properties was not set when attempting to get default character drawing instructions.")

        tile_width, tile_height = self._draw_data.get_size()
        character = self.get_character_on_tile()

        if character is not None:
            char_width, char_height = int(tile_width), int(tile_height)
            char_x, char_y = get_coords_for_center_drawing_in_rect(self._draw_data.get_coordinates(), self._draw_data.get_size(), (char_width, char_height))
            character.set_draw_properties(DrawProperties((char_x, char_y), (char_width, char_height)))

            for inst in character.get_draw_assets_instructions():
                instructions.append(inst)

        return instructions
