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
        self.randomise_animal_tiles()
        self.randomise_chit_cards()

    def randomise_animal_tiles(self):
        # Create a list of animal tile types with each animal appearing exactly six times
        animal_types = ['salamander', 'bat', 'spider', 'baby_dragon']
        tiles_per_animal = 6
        self.animal_tiles = animal_types * tiles_per_animal
        random.shuffle(self.animal_tiles)

    def randomise_chit_cards(self):
        chit_card_distribution = [
            'baby_dragon', 'baby_dragon_2', 'baby_dragon_3',
            'bat', 'bat_2', 'bat_3',
            'salamander', 'salamander_2', 'salamander_3',
            'spider', 'spider_2', 'spider_3',
            'pirate_dragon', 'pirate_dragon', 'pirate_dragon_2', 'pirate_dragon_2'
        ]
        random.shuffle(chit_card_distribution)
        self.chit_cards = chit_card_distribution

    def draw_chit_cards(self, win):
        # Drawing chit card section
        rect_size = 5
        rect_width = rect_size * IMAGE_TILE_SIZE
        pygame.draw.rect(win, YELLOW, ((CENTER_COL - 2) * IMAGE_TILE_SIZE + 1, (CENTER_ROW - 2) * IMAGE_TILE_SIZE + 1, rect_width - 2, rect_width - 2))

        positions = [
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
        (3, 2), (3, 6), (4, 2), (4, 6), (5, 2), (5, 6),
        (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
        ]   
        # Draw chit cards
        for i in range(len(self.chit_cards)):
            chit_card = self.chit_cards[i]
            image = self.images[chit_card]
            col, row = positions[i]
            x = col * IMAGE_TILE_SIZE
            y = row * IMAGE_TILE_SIZE
            
            # Create a circular mask
            mask_radius = IMAGE_TILE_SIZE // 2 - 4
            mask = pygame.Surface((IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(mask, (255, 255, 255, 255), (IMAGE_TILE_SIZE // 2, IMAGE_TILE_SIZE // 2), mask_radius)
            pygame.draw.circle(mask, (0, 0, 0, 255), (IMAGE_TILE_SIZE // 2, IMAGE_TILE_SIZE // 2), mask_radius, 2)  # Black border
            win.blit(mask, (x, y), special_flags=pygame.BLEND_RGBA_SUB)

            # Apply the mask to the chit card image
            masked_image = image.copy()
            masked_image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            win.blit(masked_image, (x, y))

    def draw_tiles(self, win):
        win.fill(BLACK)

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
                    if (row == 1 and 1 <= col <= COLUMNS - 2) or (row == ROWS - 2 and 1 <= col <= COLUMNS - 2) or (col == COLUMNS - 2 and 1 <= row <= ROWS - 2) or (col == 1 and 1 <= row <= ROWS - 2):
                        pygame.draw.rect(win, WHITE, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
                        pygame.draw.rect(win, BLACK, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

                        # Get the next animal tile image
                        animal_tile = self.animal_tiles[tile_index % len(self.animal_tiles)]
                        tile_index += 1

                        # Load and draw the image on the tile
                        image = self.images[animal_tile]
                        win.blit(image, (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))

    def load_images(self):
        # Getting reference to the assets directory
        current_dir = os.path.dirname(__file__)
        images_dir = os.path.join(current_dir, '..', 'assets')

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
            'cave_baby_dragon': 'cave_baby_dragon.png',
            'pirate_dragon': 'pirate_dragon.png',
            'pirate_dragon_2': 'pirate_dragon_2.png'
        }

        for tile_type, image_path in tile_types.items():
            image = pygame.image.load(os.path.join(images_dir, image_path))
            images[tile_type] = pygame.transform.scale(image, IMAGE_SIZE)

        return images
    
    def draw_board(self, win):
        self.draw_tiles(win)
        self.draw_chit_cards(win)

    
        







