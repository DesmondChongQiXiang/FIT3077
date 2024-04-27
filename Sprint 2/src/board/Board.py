from .BoardConfig import *
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
        current_dir = os.path.dirname(__file__)
        images_dir = os.path.join(current_dir, '..', 'assets')
        # images_dir = os.path.join(os.path.dirname(__file__), 'assets')

        images = {}

        tile_types = {
            'baby_dragon': 'baby_dragon.png',
            'baby_dragon_2': 'baby_dragon_2.png',
            'baby_dragon_3': 'baby_dragon_3.png',
            'salamander': 'salamander.png',
            'salamander_2': 'salamander_2.png',
            'salamander_3': 'salamander_3.png',
            'bat': 'bat.png',
            'bat_2': 'bat_2.png',
            'bat_3': 'bat_3.png',
            'spider': 'spider.png',
            'spider_2': 'spider_2.png',
            'spider_3': 'spider_3.png',
            'cave_salamander': 'cave_salamander.png',
            'cave_bat': 'cave_bat.png',
            'cave_spider': 'cave_spider.png',
            'cave_baby_dragon': 'cave_baby_dragon.png'
        }

        for tile_type, image_path in tile_types.items():
            image = pygame.image.load(os.path.join(images_dir, image_path))
            images[tile_type] = pygame.transform.scale(image, IMAGE_SIZE)

        # Adding the animal image onto the tiles
        win.blit(images['baby_dragon'], (IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(images["spider"], (2 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(images['baby_dragon'], (3 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(images['bat'], (4 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(images["spider"], (5 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(images["spider"], (6 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(images['bat'], (7 * IMAGE_TILE_SIZE + 1, IMAGE_TILE_SIZE + 1))
        win.blit(images['salamander'], (7 * IMAGE_TILE_SIZE + 1, 2 * IMAGE_TILE_SIZE + 1))
        win.blit(images['salamander'], (7 * IMAGE_TILE_SIZE + 1, 3 * IMAGE_TILE_SIZE + 1))
        win.blit(images["spider"], (7 * IMAGE_TILE_SIZE + 1, 4 * IMAGE_TILE_SIZE + 1))
        win.blit(images['bat'], (7 * IMAGE_TILE_SIZE + 1, 5 * IMAGE_TILE_SIZE + 1))
        win.blit(images['baby_dragon'], (7 * IMAGE_TILE_SIZE + 1, 6 * IMAGE_TILE_SIZE + 1))
        win.blit(images['salamander'], (7 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(images['bat'], (6 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(images["spider"], (5 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(images['salamander'], (4 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(images['baby_dragon'], (3 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(images['bat'], (2 * IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(images['baby_dragon'], (IMAGE_TILE_SIZE + 1, 7 * IMAGE_TILE_SIZE + 1))
        win.blit(images['salamander'], (IMAGE_TILE_SIZE + 1, 6 * IMAGE_TILE_SIZE + 1))
        win.blit(images['bat'], (IMAGE_TILE_SIZE + 1, 5 * IMAGE_TILE_SIZE + 1))
        win.blit(images["spider"], (IMAGE_TILE_SIZE + 1, 4 * IMAGE_TILE_SIZE + 1))
        win.blit(images['baby_dragon'], (IMAGE_TILE_SIZE + 1, 3 * IMAGE_TILE_SIZE + 1))
        win.blit(images['salamander'], (IMAGE_TILE_SIZE + 1, 2 * IMAGE_TILE_SIZE + 1))

        # Adding the cave tile
        win.blit(images['cave_salamander'], (4 * IMAGE_TILE_SIZE + 1, 0 * IMAGE_TILE_SIZE + 1))
        win.blit(images['cave_bat'], (4 * IMAGE_TILE_SIZE + 1, 8 * IMAGE_TILE_SIZE + 1))
        win.blit(images['cave_baby_dragon'], (0 * IMAGE_TILE_SIZE + 1, 4 * IMAGE_TILE_SIZE + 1))
        win.blit(images['cave_spider'], (8 * IMAGE_TILE_SIZE + 1, 4 * IMAGE_TILE_SIZE + 1))

    def randomise_chit_cards(self, win):
        pass
        







