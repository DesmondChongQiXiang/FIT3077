from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.animals.Animal import Animal
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from utils.pygame_utils import get_coords_for_center_drawing_in_rect
from typing import Optional


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

    # ------- DrawableByAsset interface --------------------------------------------------------------------------
    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """Draw the tile based on the tile's draw data, its animal, and any characters on it. If there is no data,
        the tile is not drawn.

        Returns:
            [Instructions to draw the game board tile]
        """
        tile_draw_data = self.get_draw_data()
        if tile_draw_data is None:  # don't draw anything if no draw data
            return []

        instructions: list[DrawAssetInstruction] = []
        tile_x, tile_y = tile_draw_data.get_coordinates()
        animal = self.get_animal()
        animal_size = int(tile_draw_data.get_size()[0] / NormalTile.__ANIMAL_DRAW_SIZE_FACTOR)
        animal_x, animal_y = get_coords_for_center_drawing_in_rect(tile_draw_data.get_coordinates(), tile_draw_data.get_size(), (animal_size, animal_size))

        instructions.append(DrawAssetInstruction("assets/tiles/normal_tile.png", tile_x, tile_y, tile_draw_data.get_size()))
        if animal is not None:  # animal is never none
            instructions.append(DrawAssetInstruction(f"assets/animals/{animal.value}.png", animal_x, animal_y, (animal_size, animal_size)))
        for instruction in self._get_character_draw_instructions():
            instructions.append(instruction)

        return instructions
