from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.animals.Animal import Animal
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from codec.saves.JSONSaveClassTypeIdentifiers import JSONSaveClassTypeIdentifiers

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
    def place_character_on_tile(self, character: PlayableCharacter) -> None:
        """Place a character on the tile.

        Args:
            character: The character to place on the tile
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

    def on_save(self, to_write: dict[str, Any]) -> None:
        """Upon save request, add the object describing this tile to the respective volcano card sequence.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to JSON.

        Raises:
            Exception if the animal was none when saving.
        """
        animal: Optional[Animal] = self.get_animal()
        if animal is None:
            raise Exception("Animal must not be none for the cave tile on save.")

        sequence_list: list[Any] = to_write["volcano_card_sequence"][-1]  # last element in 'volcano_card_sequence' is the sequence currently being determined
        sequence_list.append({"type": JSONSaveClassTypeIdentifiers.tile_normal.value, "animal": animal.value})
