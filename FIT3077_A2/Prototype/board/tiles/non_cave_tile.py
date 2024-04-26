from .tile import Tile

class NonCaveTile(Tile):

    def __init__(self,animal,dragon,x,y) :
        self.animal = animal
        self.dragon = dragon
        self.x = x
        self.y = y

    def set_player_on_tile(self, dragon) -> bool:
        if self.dragon == None:
            self.dragon = dragon
            return True
        else:
            return False
        
