from Constants import *
from abc import ABC, abstractmethod


class Tile:
    def __init__(self, row, col, symbol, dragon):
        self.row = row
        self.col = col
        self.tile_symbol = symbol
        self.is_occupied_by = dragon

    