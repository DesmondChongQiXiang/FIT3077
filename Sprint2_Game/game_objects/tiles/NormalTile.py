from game_objects.tiles.Tile import Tile
from game_objects.tiles.TileDrawData import TileDrawData
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.animals.Animal import Animal
from screen.DrawAssetInstruction import DrawAssetInstruction
from typing import Optional


class NormalTile(Tile):
    """Represents a tile that has a representing animal.

    Author: Shen
    """

    def __init__(self, animal: Animal, draw_data: Optional[TileDrawData] = None, character: Optional[PlayableCharacter] = None):
        """
        Args:
            animal: The animal to be represented by the tile
            draw_data (Optional): The data specifying how to draw the tile
            character (Optional): The character on the tile
        """
        self.__animal = animal
        super().__init__(draw_data, character)

    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """Draw the tile based on the tile's draw data. If there is no data, the tile is not drawn.

        Returns:
            [Instruction to draw the game board tile]
        """
        draw_data = self.get_draw_data()
        if draw_data is None:  # don't draw anything if no draw data
            return []
        x, y = draw_data.get_coordinates()
        return [DrawAssetInstruction("assets/game_board/game_board_normal_tile.png", x, y, draw_data.get_size())]

    def get_animal(self) -> Animal:
        """Gets the animal the tile represents.

        Returns:
            The animal
        """
        return self.__animal
