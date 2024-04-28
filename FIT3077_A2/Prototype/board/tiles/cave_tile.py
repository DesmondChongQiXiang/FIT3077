from .tile import Tile
"""
This is the class CaveTile. This class is the child class of the abstract class Tile. It represents the caves that the players start the game and have to return 
to to win the game.
"""
class CaveTile(Tile):
    """
    This is the init for a Cave Tile the tiles that represent the dragons starting and end points

    self.animal : This the animal which the tile displays

    self.dragon : This is which dragon is on the tile at any given point, if it is not occupied, it is None

    self.x & self.y : These are the coordinates of the tile
    """
    def __init__(self,animal,dragon,x,y) :
        self.animal = animal
        self.dragon = dragon
        self.x = x
        self.y = y

    def set_player_on_tile(self, dragon) -> bool:
        pass