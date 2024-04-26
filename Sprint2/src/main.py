from Game import Game
from constants import *
from GameBoard import GameBoard
# if __name__=="__main__":
#     display = Display()
#     game = Game(display)
#     game.run()

FPS = 60
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fiery Dragon")
gameboard = GameBoard()
def main():
    running = True
    clock = pygame.time.Clock()
    chit_card_list,index_list = gameboard.create_chit_card()
    print(index_list)
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        tile_size = 100
        gameboard.draw_square_tile(screen)
        gameboard.draw_chit_card(screen,chit_card_list,index_list)
        pygame.display.update()
    pygame.quit()


main()

