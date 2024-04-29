from .Tile import Tile

class CaveTile(Tile):
    """
    Class representing a cave tile on the game board.
    """

    def __init__(self, row, col, symbol, dragon, player_number):
        """
        Initialize the CaveTile object.

        Args:
        - row (int): The row index of the tile.
        - col (int): The column index of the tile.
        - symbol (str): The symbol representing the tile.
        - dragon (Dragon): The dragon currently occupying the tile.
        - player_number (int): The dragon's cave identifier.
        """
        super().__init__(row, col, symbol, dragon)
        self.player_number = player_number

    
    def place_dragon_on_tile(dragon):
        pass