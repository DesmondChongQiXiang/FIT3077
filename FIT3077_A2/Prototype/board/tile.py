from abc import ABC,abstractmethod

class Tile(ABC):
    """
    This is the initialiser for the class Tile
    """
    def __init__(self,animal,dragon,x,y) :
        self.animal = animal
        self.dragon = None
        self.x = x
        self.y = y

    """
    This method returns the animal enum assigned to the tile
    """
    def get_tiles_animal(self):
        return self.animal
    
    """
    This return's the dragon object currently on the tile
    """
    def get_player_on_tile(self):
        return self.dragon

    """
    This sets the dragon on the tile to none as we want to remove the dragon when it moves spaces
    """
    def remove_player_from_tile(self):
        self.dragon = None

    """
    This is an abstract method that allows the player to move to the tile, if it is a cave will have a different behavior from if it is a non-cave tile
    """
    @abstractmethod
    def set_player_on_tile(self,dragon) -> bool:
        pass
