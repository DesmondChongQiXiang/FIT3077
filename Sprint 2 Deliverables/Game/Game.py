from Board import *
from Player import Player


class Game:

    def __init__(self, players=None, board=None, active_player=None):
        if players is None and board is None and active_player is None:
            self.default_init()
        else:
            self.players = players
            self.board = board
            self.active_player = active_player

    def default_init(self):
        player_1 = Player("Rohan", 1)
        player_2 = Player("Ian", 2)
        player_3 = Player("Shen", 3)
        player_4 = Player("Desmond", 4)
        self.players = [player_1, player_2, player_3, player_4]
        self.board = Board()
        self.active_player = player_1

    def start_game(self):
        pygame.init()
        window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fiery Dragons")
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            self.board.draw_tiles(window)
            self.board.load_tile_images(window)
            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    game = Game()

    game.start_game()
    


