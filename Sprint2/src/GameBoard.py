import pygame
import random
from constants import CELL_WIDTH,CELL_HEIGHT
from ChitCard import ForwardChitCard, BackwardChitCard
from Cave import Cave
from Tile import Tile
from Animal import Animal
from DragonToken import DragonToken
TILE_WIDTH = CELL_WIDTH - 5
TILE_HEIGHT = CELL_HEIGHT - 5
class GameBoard:
    def __init__(self):
        self.occupiable = []
        self.chit_card_list = []
        self.cave = []
        self.dragon_token = []
        self.turn = 0

    def create_tile(self, screen):
        # top row
        top_row = [Animal.BABYDRAGON,Animal.SPIDER,Animal.BABYDRAGON,Animal.BAT,Animal.SPIDER,Animal.SPIDER]
        row_range = range(1,2)
        col_range = range(1,7)
        self.create_tiles_rowcolumn(screen, row_range, col_range, top_row)

        # right column
        right_column = [Animal.BAT,Animal.SALAMANDER,Animal.SALAMANDER,Animal.SPIDER,Animal.BAT,Animal.BABYDRAGON]
        row_range = range(1,7)
        col_range = range(7,8)
        self.create_tiles_rowcolumn(screen, row_range, col_range, right_column, False)

        # bottom row
        bottom_row = [None,Animal.BAT, Animal.BABYDRAGON,Animal.SALAMANDER,Animal.SPIDER,Animal.BAT,Animal.SALAMANDER]
        row_range = range(7,8)
        col_range = range(7,1,-1)
        self.create_tiles_rowcolumn(screen, row_range, col_range, bottom_row, True)

        # left column
        left_column = [None,Animal.SALAMANDER, Animal.BABYDRAGON,Animal.SPIDER,Animal.BAT,Animal.SALAMANDER,Animal.BABYDRAGON]
        row_range = range(7,1,-1)
        col_range = range(1,2)
        self.create_tiles_rowcolumn(screen, row_range, col_range, left_column, False)

    def draw_tiles(self,screen):
        for i in range(len(self.occupiable)):
            self.occupiable[i].draw(screen)

