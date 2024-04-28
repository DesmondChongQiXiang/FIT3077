from .tile import Tile
"""
This is the class NonCaveTile. This class is the child class of the abstract class Tile. It represents the tiles that make up the game board that players move along.
"""
class NonCaveTile(Tile):

    """
    This is the init for a NonCave Tile aka the regular tiles that make up the volcano cards of the game board

    self.animal : This the animal which the tile displays

    self.dragon : This is which dragon is on the tile at any given point, if it is not occupied, it is None

    self.x & self.y : These are the coordinates of the tile
    """
    def __init__(self,animal,dragon,x,y) :
        self.animal = animal
        self.dragon = dragon
        self.x = x
        self.y = y


    """
    This method to be implemented will allow the dragon to be added to the tile's attribute so we can see if the tile is occupied or not. We use a bool so we can see
    to end the turn if the tile is occupied
    """
    def set_player_on_tile(self, dragon) -> bool:
        if self.dragon == None:
            self.dragon = dragon
            return True
        else:
            return False
        
