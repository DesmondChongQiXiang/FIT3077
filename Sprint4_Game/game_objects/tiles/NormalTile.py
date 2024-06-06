from __future__ import annotations
from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.animals.Animal import Animal
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from factories.ClassTypeIdentifier import ClassTypeIdentifier

from typing import Optional, Any


class NormalTile(Tile):
    """Represents a tile that has a representing animal.

    Author: Shen
    """

    __ANIMAL_DRAW_SIZE_FACTOR: float = 1.7  # higher means smaller animal

    def __init__(self, animal: Animal, draw_data: Optional[DrawProperties] = None, character: Optional[PlayableCharacter] = None):
        """
        Args:
            animal: The animal to be represented by the tile
            draw_data (Optional): The data specifying how to draw the tile
            character (Optional): The character on the tile
        """
        super().__init__(draw_data, character, animal)

    # ------- Tile abstract class --------------------------------------------------------------------------
    def place_character_on_tile(self, character: PlayableCharacter, perform_effect: bool) -> None:
        """Place a character on the tile.

        Args:
            character: The character to place on the tile
            perform_effect: Whether to perform the effect the tile has if any
        """
        self.set_character_on_tile(character)

    def _on_draw_request(self, draw_properties: DrawProperties) -> list[DrawAssetInstruction]:
        """On draw request, return instructions to draw the normal tile, animal and character on top if there is one.

        Args:
            draw_properties: The draw properties requesting how to draw this object

        Returns:
            A list the drawing instructions to draw this object.
        """
        instructions: list[DrawAssetInstruction] = []
        tile_x, tile_y = draw_properties.get_coordinates()

        instructions.append(DrawAssetInstruction(f"assets/tiles/normal_tile.png", tile_x, tile_y, draw_properties.get_size(), draw_properties.get_rotation()))
        instructions.extend(self._default_animal_draw_instructions(NormalTile.__ANIMAL_DRAW_SIZE_FACTOR))
        instructions.extend(self._default_character_draw_instructions())

        return instructions

    def on_save(self, to_write: dict[str, Any]) -> Optional[Any]:
        """When requested on save, return a JSON compatible object describing this tile.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.

        Returns:
            A JSON compatible object that describes this tile

        Raises:
            Exception if animal was none when saving.
        """
        animal: Optional[Animal] = self.get_animal()
        if animal is None:
            raise Exception("Animal was none for NormalTile when attempting to save.")
        return {"type": ClassTypeIdentifier.tile_normal.value, "animal": animal.value}

    @classmethod
    def create_from_json_save(cls, save_data: dict[str, Any]) -> NormalTile:
        """Create a cave tile based on a normal tile type json save data object.

        Args:
            save_data: The dictionary representing the JSON save data object for a normal tile type

        Returns:
            A normal tile matching the save data
        """
        try:
            return cls(Animal(save_data["animal"]))
        except:
            raise Exception(f"Save data must have attributes 'animal'. Passed in={save_data}")
