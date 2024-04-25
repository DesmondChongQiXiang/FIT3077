from Game import Game
from Display import Display
if __name__=="__main__":
    display = Display()
    game = Game(display)
    game.run()