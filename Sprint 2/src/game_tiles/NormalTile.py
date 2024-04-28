from .Tile import Tile

class NormalTile(Tile):

    def __init__(self, row, col, symbol, dragon):
        super().__init__(row, col, symbol, dragon)
        # Chit symbol of the cave
        self.symbol = symbol
        self.is_occupied_by = dragon

    def place_dragon(dragon):
        pass
    