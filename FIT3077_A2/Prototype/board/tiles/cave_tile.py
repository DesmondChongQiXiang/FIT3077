from .tile import Tile

class CaveTile(Tile):

    def __init__(self,animal,dragon,x,y) :
        self.animal = animal
        self.dragon = dragon
        self.x = x
        self.y = y

    def set_player_on_tile(self, dragon) -> bool:
        pass