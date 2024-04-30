from .BoardConfig import *
from chit_cards.AnimalChitCard import AnimalChitCard
from chit_cards.DragonPirateChitCard import DragonPirateChitCard
import pygame
import os
import random


class Board:
    """
    Class representing the game board.
    """

    def __init__(self):
        """
        Initialize the Board object.
        """
        self.tiles = []
        self.chit_cards = [AnimalChitCard(chit_steps=1, animal='bat', x=2, y=2),
                                 AnimalChitCard(chit_steps=2, animal='bat_2', x=2, y=3),
                                 AnimalChitCard(chit_steps=3, animal='bat_3', x=2, y=4),
                                 AnimalChitCard(chit_steps=1, animal='salamander', x=2, y=5),
                                 AnimalChitCard(chit_steps=2, animal='salamander_2', x=2, y=6),
                                 AnimalChitCard(chit_steps=3, animal='salamander_3', x=3, y=2),
                                 AnimalChitCard(chit_steps=1, animal='baby_dragon', x=3, y=6),
                                 AnimalChitCard(chit_steps=2, animal='baby_dragon_2', x=4, y=2),
                                 AnimalChitCard(chit_steps=3, animal='baby_dragon_3', x=4, y=6),
                                 AnimalChitCard(chit_steps=1, animal='spider', x=5, y=2),
                                 AnimalChitCard(chit_steps=2, animal='spider_2', x=5, y=6),
                                 AnimalChitCard(chit_steps=3, animal='spider_3', x=6, y=2),
                                 DragonPirateChitCard(chit_steps=-1, animal='pirate_dragon', x=6, y=3),
                                 DragonPirateChitCard(chit_steps=-2, animal='pirate_dragon_2', x=6, y=4),
                                 DragonPirateChitCard(chit_steps=-1, animal='pirate_dragon', x=6, y=5),
                                 DragonPirateChitCard(chit_steps=-2, animal='pirate_dragon_2', x=6, y=6)]
        self.dragons = []
        self.animal_tiles = []

        # Retrieve animal images from the assets directory
        self.images = self.load_images()

        # Randomising animal tiles and chit cards' position
        self.randomise_animal_tiles()

    def randomise_animal_tiles(self):
        """
        Randomise the positions of animal tiles on the board.
        """
        # Create a list of animal tile types with each animal appearing exactly six times
        animal_types = ['salamander', 'bat', 'spider', 'baby_dragon']
        tiles_per_animal = 6
        self.animal_tiles = animal_types * tiles_per_animal
        random.shuffle(self.animal_tiles)

    def randomise_chit_card_positions(self):
        """
        Randomise the positions of chit cards on the board.
        """
        # Shuffle the chit cards to ensure randomness
        random.shuffle(self.chit_cards)

        # Iterate over pairs of chit cards (starting from the first one)
        for i in range(0, len(self.chit_cards), 2):
            # Swap the x and y coordinates of the chit cards
            self.chit_cards[i].col, self.chit_cards[i + 1].col = self.chit_cards[i + 1].col, self.chit_cards[i].col
            self.chit_cards[i].row, self.chit_cards[i + 1].row = self.chit_cards[i + 1].row, self.chit_cards[i].row

    def draw_tiles(self, win):
        """
        Draw the tiles on the board.
        """
        win.fill(BLACK)

        tile_index = 0

        for row in range(ROWS):
            for col in range(COLUMNS):
                # Drawing cave tiles
                if (row == 0 and col == CENTER_COL) or (row == ROWS - 1 and col == CENTER_COL) or \
                (row == CENTER_ROW and col == 0) or (row == CENTER_ROW and col == COLUMNS - 1):
                    pygame.draw.rect(win, YELLOW, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
                    pygame.draw.rect(win, BLACK, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

                # 1st cave
                if row == 0 and col == CENTER_COL:
                    win.blit(self.images['cave_salamander'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                    win.blit(self.images['dragon_token_1'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                # 2nd cave
                elif row == ROWS - 1 and col == CENTER_COL:
                    win.blit(self.images['cave_bat'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                    win.blit(self.images['dragon_token_2'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                # 3rd cave
                elif row == CENTER_ROW and col == 0:
                    win.blit(self.images['cave_spider'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                    win.blit(self.images['dragon_token_3'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                # 4th cave
                elif row == CENTER_ROW and col == COLUMNS - 1:
                    win.blit(self.images['cave_baby_dragon'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))
                    win.blit(self.images['dragon_token_4'], (col * IMAGE_TILE_SIZE + 1, row * IMAGE_TILE_SIZE + 1))

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

    def draw_chit_cards(self, win):
        """
        Draw the chit cards on the board.
        """
        # Drawing the section where the chit cards will be placed
        rect_size = 5
        rect_width = rect_size * IMAGE_TILE_SIZE
        pygame.draw.rect(win, YELLOW, ((CENTER_COL - 2) * IMAGE_TILE_SIZE + 1, (CENTER_ROW - 2) * IMAGE_TILE_SIZE + 1, rect_width - 2, rect_width - 2))

        for chit_card in self.chit_cards:
            chit_card_image = self.images[chit_card.animal]

            x = chit_card.col * IMAGE_TILE_SIZE + 1
            y = chit_card.row * IMAGE_TILE_SIZE + 1

            # If the chit card has not been flipped, it will blit the image of the chit card
            if chit_card.flipped:
                # Create a circular mask
                mask_radius = IMAGE_TILE_SIZE // 2
                mask = pygame.Surface((IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), pygame.SRCALPHA)
                pygame.draw.circle(mask, (255, 255, 255, 255), (IMAGE_TILE_SIZE // 2, IMAGE_TILE_SIZE // 2), mask_radius)
                pygame.draw.circle(mask, (0, 0, 0, 255), (IMAGE_TILE_SIZE // 2, IMAGE_TILE_SIZE // 2), mask_radius, 2)  # Black border

                # Apply the mask to the chit card image
                masked_image = chit_card_image.copy()
                masked_image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                win.blit(masked_image, (x, y))
            else:
            # Else, the chit card will remain covered (black)
                pygame.draw.circle(win, BLACK, (x + IMAGE_TILE_SIZE // 2, y + IMAGE_TILE_SIZE // 2), IMAGE_TILE_SIZE // 2)

    def load_images(self):
        """
        Load images for the game.
        """
        # Getting reference to the assets directory
        current_dir = os.path.dirname(__file__)
        images_dir = os.path.join(current_dir, 'assets')

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
            'pirate_dragon_2': 'pirate_dragon_2.png',
            'dragon_token_1': 'dragon_1.png',
            'dragon_token_2': 'dragon_2.png',
            'dragon_token_3': 'dragon_3.png',
            'dragon_token_4': 'dragon_4.png',
        }

        # Retrieving all the images within the assets directory and scaling them according to IMAGE_SIZE
        for tile_type, image_path in tile_types.items():
            image = pygame.image.load(os.path.join(images_dir, image_path))
            images[tile_type] = pygame.transform.scale(image, IMAGE_SIZE)

        return images
    
    def draw_board(self, win):
        """
        Draw the entire board.
        """
        self.draw_tiles(win)
        self.draw_chit_cards(win)


        







