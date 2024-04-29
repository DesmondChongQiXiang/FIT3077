from gameboard import GameBoard
from game import Game
from menu import Menu

gameboard = GameBoard()
menu = Menu()
game = Game(gameboard,menu)
game.run()