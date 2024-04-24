from Constants import *
import os


class Board:

    def __init__(self):
        self.tiles = []
        self.selected_dragon = None

    def draw_tiles(self, win):
        # Calculate the center of the board
        center_row = ROWS // 2
        center_col = COLUMNS // 2

        # Calculate the top-left corner of the rectangle
        start_row = center_row - 2 
        start_col = center_col - 2 

        for row in range(ROWS):
            for col in range(COLUMNS):
                # Check if the current tile is on the outer row, column, or second outermost layer
                is_outer_row = row == 0 or row == ROWS - 1
                is_outer_col = col == 0 or col == COLUMNS - 1
                is_second_outer_row = row == 1 or row == ROWS - 2
                is_second_outer_col = col == 1 or col == COLUMNS - 2

                if is_outer_row or is_outer_col:
                    pygame.draw.rect(win, YELLOW, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
                elif is_second_outer_row or is_second_outer_col:
                    # Drawing the normal tiles of the board
                    pygame.draw.rect(win, WHITE, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
                    pygame.draw.rect(win, BLACK, (col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

        # Drawing the caves
        pygame.draw.rect(win, WHITE, (center_col * IMAGE_TILE_SIZE, (row - 8) * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
        pygame.draw.rect(win, BLACK, (center_col * IMAGE_TILE_SIZE, (row - 8) * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

        pygame.draw.rect(win, WHITE, (center_col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
        pygame.draw.rect(win, BLACK, (center_col * IMAGE_TILE_SIZE, row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

        pygame.draw.rect(win, WHITE, ((col - 8) * IMAGE_TILE_SIZE, center_row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
        pygame.draw.rect(win, BLACK, ((col - 8) * IMAGE_TILE_SIZE, center_row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

        pygame.draw.rect(win, WHITE, (col * IMAGE_TILE_SIZE, center_row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE))
        pygame.draw.rect(win, BLACK, (col * IMAGE_TILE_SIZE, center_row * IMAGE_TILE_SIZE, IMAGE_TILE_SIZE, IMAGE_TILE_SIZE), 1)

           
        # Drawing the chit cards section of the board
        rect_size = 5
        rect_width = rect_size * IMAGE_TILE_SIZE
        pygame.draw.rect(win, YELLOW, (start_col * IMAGE_TILE_SIZE + 1, start_row * IMAGE_TILE_SIZE + 1, rect_width - 2, rect_width - 2))

    def load_tile_images(self, win):
        # Getting reference to the images directory
        images_dir = os.path.join(os.path.dirname(__file__), 'images')

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
        







