import pygame
from board.settings import WIDTH,HEIGHT,SQUARE_SIZE
from board.game_board import GameBoard
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Fiery Dragons')
FPS = 60

def get_row_col_from_mouse(pos):
    x,y = pos
    row = x // SQUARE_SIZE
    col = y // SQUARE_SIZE
    return (row,col)

def main():
    run = True
    clock = pygame.time.Clock()
    board = GameBoard([],[],[])
    board.shuffle_chit_cards()
    #chit_card = board.get_piece(2,6)
    #print(chit_card.x,chit_card.y)
    #board.flip_chit_card(chit_card)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(position)
                chit_card = board.get_piece(row,col)
                board.flip_chit_card(chit_card)
        board.draw_game(WINDOW)
        pygame.display.update()

    
    pygame.quit()



main()