from gameboard import GameBoard
from game import Game
from menu import Menu

if __name__ == "__main__":
    print("a")
    gameboard = GameBoard()
    menu = Menu()
    game = Game(gameboard,menu)
    game.run()