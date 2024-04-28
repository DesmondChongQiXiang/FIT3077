from abc import ABC,abstractmethod

class ChitCard(ABC):

    def __init__(self,number_of_animal,animal,x,y) :
        self.number_of_animal = number_of_animal
        self.animal = animal
        self.is_flipped = False
        self.tile_coefficient = 1
        self.flipped_this_turn = False
        self.x = x
        self.y = y

    def set_is_flipped(self):
        if self.is_flipped == False:
            self.is_flipped = True
            self.flipped_this_turn = True
        elif self.is_flipped == True & self.flipped_this_turn == False:
            self.is_flipped = False

    @abstractmethod
    def carry_out_task(self,dragon):
        pass
        
        