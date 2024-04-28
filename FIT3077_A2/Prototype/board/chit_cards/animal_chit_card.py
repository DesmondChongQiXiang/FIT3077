from .chit_card import ChitCard
"""
This is the class for the Animal Chit Card, it is a child class of the abstract class Chit Card
"""
class AnimalChitCard(ChitCard):
    """
    In the initialiser we create the Animal chit card with the number of the animal icons we want to display, 
    what animal and the x and y coordinates the chit card will be placed at. 
    
    self.number_of_animal : This is the number of animals the chit card will have on it which determines how many steps on the game board we will move.

    self.animal : This is the animal icon the chit card will display

    self.is_flipped : We initially set is_flipped to be false as at the start of the game, all chit cards should be flipped face down.

    self.tile_coefficient : The tile_coefficient determines if we want to move positively or negatively. As for the Animal Chit Cards,
    we want to be able to move positively in the direction we are supposed to be going. 

    self.x & self.y : The x and y coordinates determine the position of the chit cards on the game board
    """
    def __init__(self, number_of_animal,animal,x,y):
        self.number_of_animal = number_of_animal
        self.animal = animal
        self.is_flipped = False
        self.tile_coefficient = 1
        self.flipped_this_turn = False
        self.x = x
        self.y = y


    """
    This is a function that is used to flip the chit cards over. If the chit card is_flipped is false then we can flip it so we set is_flipped to be true
    At the end of a turn, we want to be able to flip all the chit cards back to un-flipped. So, i have an alternate if that checks if the chit_cards flipped
    this turn is true. Ths will be reset to false at the end of a players turn so that they can be flipped back to false
    """
    def set_is_flipped(self):
        if self.is_flipped == False:
            self.is_flipped = True
            self.flipped_this_turn = True
        elif self.is_flipped == True & self.flipped_this_turn == False:
            self.is_flipped = False


    """
    This is a function that sets the chit cards flipped this turn to false. This is used so that chit cards can all be flipped back at the end of a players turn.
    """
    def set_flipped_this_turn(self):
        self.flipped_this_turn = False

    def carry_out_task(self, dragon):
        pass