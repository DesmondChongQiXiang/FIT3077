from constants import *
from GameBoard import GameBoard

FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fiery Dragon")
gameboard = GameBoard()
def main():
    running = True
    clock = pygame.time.Clock()
    gameboard.create_chit_card()
    gameboard.create_tile(screen)
    gameboard.create_caves(4)
    gameboard.create_dragon_token(4)
    while running:
        clock.tick(FPS)
        screen.fill((0,0,0))
        menu_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for chitcard in gameboard.chit_card_list:
                    chitcard.checkforInput(menu_mouse_pos)
        gameboard.draw_tiles(screen)
        gameboard.draw_chit_card(screen)
        gameboard.draw_caves(screen)
        gameboard.draw_dragon_token(screen)
        pygame.display.update()
    pygame.quit()


main()

