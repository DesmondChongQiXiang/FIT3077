from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.tiles.TileDrawData import TileDrawData
from game_objects.animals.Animal import Animal
from screen.DrawAssetInstruction import DrawAssetInstruction
from typing import Optional

# TODO: Implement CaveTile

class CaveTile(Tile):
    def __init__(self, animal: Animal, draw_data: Optional[TileDrawData] = None, character: Optional[PlayableCharacter] = None):
        pass

    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        return []