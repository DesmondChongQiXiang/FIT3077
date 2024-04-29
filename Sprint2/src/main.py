from game.gameboard import GameBoard
from game.game import Game
from game.menu import Menu

if __name__ == "__main__":
    gameboard = GameBoard()
    menu = Menu()
    game = Game(gameboard,menu)
    game.run()