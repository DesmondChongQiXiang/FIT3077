from Player import Player
class Game:

    def __init__(self,display):
        self.players = []
        self.game_board = None
        self.playerWinning = False
        self.display = display

    def run(self):
        self.create_player()



    def create_player(self):
        player_num = self.display.select_player_num_display()
        for id in range(1, player_num+1):
            player = Player(id)
            self.players.append(player)
        for player in self.players:
            print(player)



