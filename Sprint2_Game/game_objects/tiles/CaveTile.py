from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawAssetInstruction import DrawAssetInstruction
from typing import Optional

# TODO: Implement CaveTile

class CaveTile(Tile):
    def __init__(self, coordinates: tuple[int, int], size: tuple[int, int], character: Optional[PlayableCharacter] = None):
        pass

    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        return []