from Constants import *
from game_tiles import *
import pygame
import os


class Board:

    def __init__(self):
        self.tiles = []
        self.chit_cards = []
        self.dragons = []

    def draw_board(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLUMNS):
                # Drawing cave tiles
                if (row == 0 and col == CENTER_COL) or (row == ROWS - 1 and col == CENTER_COL) or \
                (row == CENTER_ROW and col == 0) or (row == CENTER_ROW and col == COLUMNS - 1):
                    pygame.draw.rect(win, YELLOW, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
                    pygame.draw.rect(win, BLACK, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)
                # Drawing normal tiles
                elif 1 <= row <= ROWS - 2 and 1 <= col <= COLUMNS - 2:
                    pygame.draw.rect(win, WHITE, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
                    pygame.draw.rect(win, BLACK, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)
        
        # Drawing chit card section
        rect_size = 5
        rect_width = rect_size * IMAGE_TILE_SIZE
        pygame.draw.rect(win, YELLOW, ((CENTER_COL - 2) * IMAGE_TILE_SIZE + 1, (CENTER_ROW - 2) * IMAGE_TILE_SIZE + 1, rect_width - 2, rect_width - 2))
                      
        self.load_images(win)


    def load_images(self, win):
        # Getting reference to the assets directory
        images_dir = os.path.join(os.path.dirname(__file__), 'assets')

        salamander_img = pygame.image.load(os.path.join(images_dir, 'salamander.png'))
        bat_img = pygame.image.load(os.path.join(images_dir, 'bat.png'))
        spider_img = pygame.image.load(os.path.join(images_dir, 'spider.png'))
        baby_dragon_img = pygame.image.load(os.path.join(images_dir, 'baby_dragon.png'))
        cave_img = pygame.image.load(os.path.join(images_dir, 'cave.jpeg'))

        # Scaling the images
        baby_dragon = pygame.transform.scale(baby_dragon_img, IMAGE_SIZE)
        bat = pygame.transform.scale(bat_img, IMAGE_SIZE)
        spider = pygame.transform.scale(spider_img, IMAGE_SIZE)
        salamander = pygame.transform.scale(salamander_img, IMAGE_SIZE)
        cave = pygame.transform.scale(cave_img, IMAGE_SIZE)

        # Adding the animal image onto the tiles
        win.blit(baby_dragon, (IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(spider, (2 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(baby_dragon, (3 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(bat, (4 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(spider, (5 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(spider, (6 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(bat, (7 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(salamander, (7 * IMAGE_TILE_SIZE + 1, 2 * IMAGE_TILE_SIZE + 1))
        win.blit(salamander, (7 * IMAGE_TILE_SIZE + 1, 3 * IMAGE_TILE_SIZE + 1))
        win.blit(spider, (7 * IMAGE_TILE_SIZE + 1, 4 * IMAGE_TILE_SIZE + 1))
        win.blit(bat, (7 * IMAGE_TILE_SIZE + 1, 5 * IMAGE_TILE_SIZE + 1))
        win.blit(baby_dragon, (7 * IMAGE_TILE_SIZE + 1, 6 * IMAGE_TILE_SIZE + 1))
        win.blit(salamander, (7 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(bat, (6 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(spider, (5 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(salamander, (4 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(baby_dragon, (3 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(bat, (2 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(baby_dragon, (IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(salamander, (IMAGE_TILE_SIZE + 1, 6 * IMAGE_TILE_SIZE + 1))
        win.blit(bat, (IMAGE_TILE_SIZE + 1, 5 * IMAGE_TILE_SIZE + 1))
        win.blit(spider, (IMAGE_TILE_SIZE + 1, 4 * IMAGE_TILE_SIZE + 1))
        win.blit(baby_dragon, (IMAGE_TILE_SIZE + 1, 3 * IMAGE_TILE_SIZE + 1))
        win.blit(salamander, (IMAGE_TILE_SIZE + 1, 2 * IMAGE_TILE_SIZE + 1))

        # Adding the cave tile
        win.blit(cave, (4 * IMAGE_TILE_SIZE + 1, 0 * IMAGE_TILE_SIZE + 1))
        win.blit(cave, (4 * IMAGE_TILE_SIZE + 1, 8 * IMAGE_TILE_SIZE + 1))
        win.blit(cave, (0 * IMAGE_TILE_SIZE + 1, 4 * IMAGE_TILE_SIZE + 1))
        win.blit(cave, (8 * IMAGE_TILE_SIZE + 1, 4 * IMAGE_TILE_SIZE + 1))
        







