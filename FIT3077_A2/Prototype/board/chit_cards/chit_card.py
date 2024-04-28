from abc import ABC,abstractmethod

class ChitCard(ABC):
    """
    This is the initialiser for the abstract ChitCard class
    
    self.number_of_animal : This is the number of animals the chit card will have on it which determines how many steps on the game board we will move.

    self.animal : This is the animal icon the chit card will display

    self.is_flipped : We initially set is_flipped to be false as at the start of the game, all chit cards should be flipped face down.

    self.tile_coefficient : The tile_coefficient determines if we want to move positively or negatively. 

    self.x & self.y : The x and y coordinates determine the position of the chit cards on the game board
    """
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

    def set_flipped_this_turn(self):
        self.flipped_this_turn = False

    @abstractmethod
    def carry_out_task(self,dragon):
        pass
        
        