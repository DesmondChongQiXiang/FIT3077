from game_objects.tiles.Tile import Tile
from game_objects.tiles.CaveTileVariant import CaveTileVariant
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.animals.Animal import Animal
from game_concepts.events.WinEventPublisher import WinEventPublisher
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from factories.ClassTypeIdentifier import ClassTypeIdentifier

from typing import Optional, Any


class CaveTile(Tile):
    """Tile that can trigger a win condition upon entering for a second time.

    Author: Shen
    """

    __ANIMAL_DRAW_SIZE_FACTOR: float = 1.7  # higher means smaller animal

    def __init__(self, animal: Animal, variant: CaveTileVariant, draw_data: Optional[DrawProperties] = None, character: Optional[PlayableCharacter] = None):
        """
        Args:
            animal: The animal to be represented by the tile
            variant: The cave tile variant to use
            draw_data (Optional): The data specifying how to draw the tile
            character (Optional): The character on the tile
        """
        super().__init__(draw_data, character, animal)
        self.__variant = variant

    # ------- Tile abstract class --------------------------------------------------------------------------
    def place_character_on_tile(self, character: PlayableCharacter) -> None:
        """Places the character on the tile and triggers a win for the character.

        Args:
            character: The character to place on the tile
        """
        self.set_character_on_tile(character)
        WinEventPublisher.instance().notify_subscribers(character)

    def _on_draw_request(self, draw_properties: DrawProperties) -> list[DrawAssetInstruction]:
        """On draw request, return instructions to draw the cave tile, animal and character on top if there is one.

        Args:
            draw_properties: The draw properties requesting how to draw this object

        Returns:
            A list the drawing instructions to draw this object.
        """
        instructions: list[DrawAssetInstruction] = []
        tile_x, tile_y = draw_properties.get_coordinates()

        instructions.append(
            DrawAssetInstruction(
                f"assets/tiles/cave_tiles/cave_tile_{self.__variant.value}.png", tile_x, tile_y, draw_properties.get_size(), draw_properties.get_rotation()
            )
        )
        instructions.extend(self._default_animal_draw_instructions(CaveTile.__ANIMAL_DRAW_SIZE_FACTOR))
        instructions.extend(self._default_character_draw_instructions())

        return instructions

    def on_save(self, to_write: dict[str, Any]) -> Optional[Any]:
        """When requested on save, return a JSON compatible object describing this cave tile.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.

        Returns:
            A JSON compatible object describing this cave tile.

        Raises:
            Exception if animal was none when saving.
        """
        animal: Optional[Animal] = self.get_animal()
        if animal is None:
            raise Exception("Animal was none for CaveTile when attempting to save.")
        return {"type": ClassTypeIdentifier.tile_cave.value, "variant": self.__variant.value, "animal": animal.value}
