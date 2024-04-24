from .tile import Tile

class NonCaveTile(Tile):

    def __init__(self,animal,dragon) :
        super().__init__

    def set_player_on_tile(self, dragon) -> bool:
        if self.dragon == None:
            self.dragon = dragon
            return True
        else:
            return False
        
