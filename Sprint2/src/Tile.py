from Animal import Animal
from constants import CELL_WIDTH,CELL_HEIGHT
import pygame
TILE_WIDTH = CELL_WIDTH - 5
TILE_HEIGHT = CELL_HEIGHT - 5
class Tile:
    def __init__(self,animal:Animal,x_pos,y_pos):
        self.animal = animal
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self,screen):
        image = pygame.image.load("../assets/{}tile.jpg".format(self.animal.name)).convert_alpha()
        image = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))
        screen.blit(image, (self.x_pos + 2, self.y_pos + 2))