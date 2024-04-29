from .Tile import Tile

class NormalTile(Tile):
    """
    Class representing a normal tile on the game board.
    """

    def __init__(self, row, col, symbol, dragon):
        """
        Initialize the NormalTile object.

        Args:
        - row (int): The row index of the tile.
        - col (int): The column index of the tile.
        - symbol (str): The symbol representing the tile.
        - dragon (Dragon): The dragon currently occupying the tile.
        """
        super().__init__(row, col, symbol, dragon)
        # Animal symbol of the cave
        self.symbol = symbol
        self.is_occupied_by = dragon

    def place_dragon(dragon):
        pass
    
