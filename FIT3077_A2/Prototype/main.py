import pygame
from board.settings import WIDTH,HEIGHT
from board.game_board import GameBoard
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Fiery Dragons')
FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    board = GameBoard([],[],[])

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board(WINDOW)
        pygame.display.update()

    
    pygame.quit()



main()