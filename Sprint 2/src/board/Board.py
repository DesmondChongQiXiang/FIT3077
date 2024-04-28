from .BoardConfig import *
import pygame
import os
import random


class Board:

    def __init__(self):
        self.tiles = []
        self.chit_cards = []
        self.dragons = []
        self.animal_tiles = []
        # Retrieve animal images from the assets directory
        self.images = self.load_images()

        # Randomise animal tiles
        self.randomize_animal_tiles()

    def randomize_animal_tiles(self):
        # Create a list of animal tile types with each animal appearing exactly six times
        animal_types = ['salamander', 'bat', 'spider', 'baby_dragon']
        tiles_per_animal = 6
        self.animal_tiles = animal_types * tiles_per_animal
        random.shuffle(self.animal_tiles)

    def draw_board(self, win):
        win.fill(BLACK)

        # Create a copy of animal_tiles for drawing tiles
        animal_tiles_copy = self.animal_tiles.copy()

        tile_index = 0

        for row in range(ROWS):
            for col in range(COLUMNS):
                # Drawing cave tiles
                if (row == 0 and col == CENTER_COL) or (row == ROWS - 1 and col == CENTER_COL) or \
                (row == CENTER_ROW and col == 0) or (row == CENTER_ROW and col == COLUMNS - 1):
                    pygame.draw.rect(win, YELLOW, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
                    pygame.draw.rect(win, BLACK, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

                if row == 0 and col == CENTER_COL:
                    win.blit(self.images['cave_salamander'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                elif row == ROWS - 1 and col == CENTER_COL:
                    win.blit(self.images['cave_bat'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                elif row == CENTER_ROW and col == 0:
                    win.blit(self.images['cave_spider'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                elif row == CENTER_ROW and col == COLUMNS - 1:
                    win.blit(self.images['cave_baby_dragon'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))

                # Drawing normal tiles
                elif 1 <= row <= ROWS - 2 and 1 <= col <= COLUMNS - 2:
                    pygame.draw.rect(win, WHITE, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
                    pygame.draw.rect(win, BLACK, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

                    if (row == 1 and 1 <= col <= COLUMNS - 2) or (row == ROWS - 2 and 1 <= col <= COLUMNS - 2) or (col == COLUMNS - 2 and 1 <= row <= ROWS - 2) or (col == 1 and 1 <= row <= ROWS - 2):
                        # Get the next animal tile image
                        animal_tile = self.animal_tiles[tile_index % len(self.animal_tiles)]
                        tile_index += 1

                        # Load and draw the image on the tile
                        image = self.images[animal_tile]
                        win.blit(image, (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))

        
        # Drawing chit card section
        rect_size = 5
        rect_width = rect_size * IMAGE_TILE_SIZE
        pygame.draw.rect(win, YELLOW, ((CENTER_COL - 2) * IMAGE_TILE_SIZE + 1, (CENTER_ROW - 2) * IMAGE_TILE_SIZE + 1, rect_width - 2, rect_width - 2))

    def load_images(self):
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

        return images

    def randomise_chit_cards(self, win):
        pass
        







