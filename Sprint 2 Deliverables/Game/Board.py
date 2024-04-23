from Constants import *


class Board:

    def __init__(self):
        self.tiles = []
        self.selected_dragon = None

    def draw_tiles(self, win):
        for row in range(ROWS):
            for col in range(COLUMNS):
                # Check if the current tile is on the outer row, column, or second outermost layer
                is_outer_row = row == 0 or row == ROWS - 1
                is_outer_col = col == 0 or col == COLUMNS - 1
                is_second_outer_row = row == 1 or row == ROWS - 2
                is_second_outer_col = col == 1 or col == COLUMNS - 2
                if is_outer_row or is_outer_col:
                    pygame.draw.rect(win, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif is_second_outer_row or is_second_outer_col:
                    pygame.draw.rect(win, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(win, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
                else:
                    pygame.draw.rect(win, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def load_tile_images(self, win):
        # Getting the images from the images directory
        salamander_img = pygame.image.load('images/salamander.png')
        bat_img = pygame.image.load('images/bat.png')
        spider_img = pygame.image.load('images/spider.png')
        baby_dragon_img = pygame.image.load('images/baby_dragon.png')

        # Scaling the images
        scaled_baby_dragon = pygame.transform.scale(baby_dragon_img, IMAGE_SIZE)
        scaled_bat = pygame.transform.scale(bat_img, IMAGE_SIZE)
        scaled_spider = pygame.transform.scale(spider_img, IMAGE_SIZE)
        scaled_salamander = pygame.transform.scale(salamander_img, IMAGE_SIZE)

        win.blit(scaled_baby_dragon, (TILE_SIZE + 1, TILE_SIZE + 1))







