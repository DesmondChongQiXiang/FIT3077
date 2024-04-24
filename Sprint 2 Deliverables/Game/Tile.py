from Constants import *


class Tile:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_outer_row = row == 0 or row == ROWS - 1
        self.is_outer_col = col == 0 or col == COLUMNS - 1
        self.is_second_outer_row = row == 1 or row == ROWS - 2
        self.is_second_outer_col = col == 1 or col == COLUMNS - 2

    def is_outer_tile(self):
        return self.is_outer_row or self.is_outer_col

    def is_second_outer_tile(self):
        return self.is_second_outer_row or self.is_second_outer_col

    def draw(self, win):
        if self.is_outer_tile():
            pygame.draw.rect(win, YELLOW, (self.col * IMAGE_TILE_SIZE, self.row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
        elif self.is_second_outer_tile():
            pygame.draw.rect(win, WHITE, (self.col * IMAGE_TILE_SIZE, self.row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
            pygame.draw.rect(win, BLACK, (self.col * IMAGE_TILE_SIZE, self.row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)
        else:
            pygame.draw.rect(win, WHITE, (self.col * IMAGE_TILE_SIZE, self.row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))