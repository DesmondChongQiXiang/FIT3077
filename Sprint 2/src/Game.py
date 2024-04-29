from board.Board import Board
from board.BoardConfig import *
from board.Dragon import Dragon
from chit_cards.Animal import Animal
from chit_cards.AnimalChitCard import AnimalChitCard
from chit_cards.DragonPirateChitCard import DragonPirateChitCard
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
        self.players = [Dragon("Rohan", 1), Dragon("Ian", 2), Dragon("Shen", 3), Dragon("Desmond", 4)]
        self.board = Board()
        self.board.chit_cards = [AnimalChitCard(chit_steps=1, animal='bat', x=2, y=2),
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

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = x // IMAGE_TILE_SIZE
        col = y // IMAGE_TILE_SIZE
        return row, col

    def start_game(self):
        pygame.init()
        window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fiery Dragons")
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos() # gets the position of the mouse when the mouse is clicked
                    row, col = self.get_row_col_from_mouse(position)
                    # Check if a chit card was clicked
                    for chit_card in self.board.chit_cards:
                        if chit_card.col == row and chit_card.row == col:
                            chit_card.flip()  # Flip the chit card

            
            self.board.draw_board(window)
            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.start_game()
    


