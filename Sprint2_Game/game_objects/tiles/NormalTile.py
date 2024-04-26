from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.animals.Animal import Animal
from screen.DrawAssetInstruction import DrawAssetInstruction
from typing import Optional


class NormalTile(Tile):
    """Represents a tile that has a representing animal.

    Author: Shen
    """

    def __init__(self, coordinates: tuple[int, int], size: tuple[int, int], animal: Animal, character: Optional[PlayableCharacter] = None):
        """
        Args:
            coordinates: The coordinate of the tile in form (x, y)
            size: The size of the tile in pixels in form (width, height)
            animal: The animal the tile represents
            character (Optional): The character on the tile
        """
        self.__animal = animal
        super().__init__(coordinates, size, character)

    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """Draw a game board tile.

        Returns:
            [Instruction to draw the game board tile]
        """
        x, y = self.get_coordinates()
        return [DrawAssetInstruction("assets/game_board/game_board_tile.png", x, y, self.get_size())]
