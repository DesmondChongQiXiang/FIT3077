from abc import ABC, abstractmethod


class Tile(ABC):
    def __init__(self, row, col, symbol, dragon):
        self.row = row
        self.col = col
        self.tile_symbol = symbol
        self.is_occupied_by = dragon

    @abstractmethod
    def place_dragon_on_tile(dragon):
        ...