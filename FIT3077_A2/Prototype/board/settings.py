import pygame
from .non_cave_tile import NonCaveTile
from .animal import Animal

WIDTH,HEIGHT = 900,900
ROWS,COLS = 9,9
SQUARE_SIZE = WIDTH//COLS

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,20,0)

NON_CAVE_TILE_COORDINATES = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],
                             [2,1],[3,1],[4,1],[5,1],[6,1],[7,1],
                             [7,2],[7,3],[7,4],[7,5],[7,6],[7,7],
                             [2,7],[3,7],[4,7],[5,7],[6,7]]


VOLCANO_TILE_1 = [Animal.BABY_DRAGON,Animal.BAT,Animal.SPIDER]
VOLCANO_TILE_2 = [Animal.SALAMANDER,Animal.SPIDER,Animal.BAT]
VOLCANO_TILE_3 = [Animal.SPIDER,Animal.SALAMANDER,Animal.BABY_DRAGON]
VOLCANO_TILE_4 = [Animal.BAT,Animal.SPIDER,Animal.BABY_DRAGON]
VOLCANO_TILE_5 = [Animal.SPIDER,Animal.BAT,Animal.SALAMANDER]
VOLCANO_TILE_6 = [Animal.BABY_DRAGON,Animal.SALAMANDER,Animal.BAT]
VOLCANO_TILE_7 = [Animal.BAT,Animal.BABY_DRAGON,Animal.SALAMANDER]
VOLCANO_TILE_8 = [Animal.SALAMANDER,Animal.BABY_DRAGON,Animal.SPIDER]

NON_CAVE_TILE_ANIMALS = [Animal.BABY_DRAGON,Animal.BAT,Animal.SPIDER,
                         Animal.SALAMANDER,Animal.SPIDER,Animal.BAT,
                         Animal.SPIDER,Animal.SALAMANDER,Animal.BABY_DRAGON,
                         Animal.BAT,Animal.SPIDER,Animal.BABY_DRAGON,
                         Animal.SPIDER,Animal.BAT,Animal.SALAMANDER,
                         Animal.BABY_DRAGON,Animal.SALAMANDER,Animal.BAT,
                         Animal.BAT,Animal.BABY_DRAGON,Animal.SALAMANDER,
                         Animal.SALAMANDER,Animal.BABY_DRAGON,Animal.SPIDER]

