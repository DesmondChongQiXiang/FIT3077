from abc import ABC, abstractmethod

class Tile(ABC):
    """
    Abstract base class representing a tile on the game board.
    """

    def __init__(self, row, col, symbol, dragon):
        """
        Initialize the Tile object.

        Args:
        - row (int): The row index of the tile.
        - col (int): The column index of the tile.
        - symbol (str): The symbol representing the tile.
        - dragon (Dragon): The dragon currently occupying the tile.
        """
        
        self.row = row
        self.col = col
        self.tile_symbol = symbol
        self.is_occupied_by = dragon

    @abstractmethod
    def place_dragon_on_tile(dragon):
        pass