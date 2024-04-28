from .Tile import Tile

class CaveTile(Tile):

    def __init__(self, row, col, symbol, dragon, player_number):
        super().__init__(row, col, symbol, dragon)
        # The dragon's cave identifier
        self.player_number = player_number

    # After placing the dragon on tile, checks if the dragon has returned to its own cave
    def place_dragon_on_tile(dragon):
        pass