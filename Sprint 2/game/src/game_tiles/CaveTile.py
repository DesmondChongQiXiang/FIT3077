from .Tile import Tile

class CaveTile(Tile):

    def __init__(self, row, col, symbol, dragon, player_number):
        super().__init__(row, col, symbol, dragon)
        self.row = row
        self.col = col
        # Chit symbol of the cave
        self.symbol = symbol
        # The dragon's cave identifier
        self.player_number = player_number
        self.is_occupied_by = dragon

    # After placing the dragon on tile, checks if the dragon has returned to its own cave
    def place_dragon_on_tile(dragon):
        pass