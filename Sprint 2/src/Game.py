from board.Board import Board
from board.BoardConfig import *
from Dragon import Dragon
import pygame


class Game:

    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Game, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, players=None, board=None):
        if players is None and board is None:
            self.default_init()
        else:
            self.players = players
            self.board = board

    def default_init(self):
        player_1 = Dragon("Rohan", 1)
        player_2 = Dragon("Ian", 2)
        player_3 = Dragon("Shen", 3)
        player_4 = Dragon("Desmond", 4)
        self.players = [player_1, player_2, player_3, player_4]
        self.board = Board()

    def start_game(self):
        pygame.init()
        window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fiery Dragons")
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.board.flip_chit_cards()
            
            self.board.draw_board(window)
            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    game = Game()

    game.start_game()
    


