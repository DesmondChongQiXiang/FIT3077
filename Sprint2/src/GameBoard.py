import pygame
import random
from constants import ROWS, COLS, CELL_WIDTH,CELL_HEIGHT, BLACK
TILE_WIDTH = CELL_WIDTH - 5
TILE_HEIGHT = CELL_HEIGHT - 5
class GameBoard:
    def __init__(self):
        self.board = []
        self.turn = 0

    def draw_square_tile(self,screen):
        # top_row
        top_row = ["babydragon","spider","babydragon","bat","spider","spider"]
        self.traverse_cells(screen,1,1,1,6,top_row,1)

        right_column = ["bat","salamander", "salamander", "spider", "bat", "babydragon"]
        self.traverse_cells(screen, 1, 7, 7, 7, right_column, 2,False)

        bottom_row = ["bat","babydragon","salamander","spider","bat","salamander"]
        self.traverse_cells(screen, 7, 7, 1, 6, bottom_row, 2)

        left_column = ["salamander", "babydragon", "spider","bat","salamander", "babydragon"]
        self.traverse_cells(screen,1,7,1,1,left_column,2, False)

    def draw_chit_card(self,screen,chit_card_list,index_list):
        for i in range(len(chit_card_list)):
            row,col = index_list[i]
            image = pygame.image.load("../assets/{}".format(chit_card_list[i])).convert_alpha()
            image = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))
            screen.blit(image, (col * CELL_WIDTH + 2, row * CELL_HEIGHT + 2))

    def create_chit_card(self):
        animal_list = ["babydragon", "salamander", "spider", "bat"]
        quantity_list = ["1", "2", "3"]
        chit_card_list = []
        for animal in animal_list:
            for quantity in quantity_list:
                chit_card_list.append("{}{}chitcard.png".format(quantity, animal))
        for i in range(2):
            chit_card_list.append("1piratedragonchitcard.png")
            chit_card_list.append("2piratedragonchitcard.png")
            random.shuffle(chit_card_list)
        range_list = []
        for i in range(2,7):
            for j in range(2,7):
                range_list.append((i,j))
        random.shuffle(range_list)
        index_list = []
        for i in range(len(chit_card_list)):
            index_list.append(range_list.pop())
        return chit_card_list,index_list






    def draw_animal(self,animal, x, y, size, color):
        # Replace following with the actual drawing code for each animal
        if animal == "BAT":
            # Draw a bat on the tile
            pass
        elif animal == "SPIDER":
            # Draw a spider on the tile
            pass
    def create_board(self):
        pass

    def traverse_cells(self,screen, row_start, row_end, col_start, col_end, img_name_list,i, select_col = True):
        for row in range(row_start, row_end + 1):
            for col in range(col_start, col_end + 1):
                pygame.draw.rect(screen, BLACK, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 2)
                if select_col:
                    image = pygame.image.load("../assets/{}tile.jpg".format(img_name_list[col - i])).convert_alpha()
                else:
                    image = pygame.image.load("../assets/{}tile.jpg".format(img_name_list[row - i])).convert_alpha()
                image = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))
                screen.blit(image, (col * CELL_WIDTH + 2, row * CELL_HEIGHT + 2))
