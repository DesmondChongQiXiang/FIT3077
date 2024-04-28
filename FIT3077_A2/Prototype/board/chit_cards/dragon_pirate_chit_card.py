from .chit_card import ChitCard
from ..animal import Animal

class DragonPirateChitCard(ChitCard):

    def __init__(self,animal,number_of_animal,x,y):
        self.number_of_animal = number_of_animal
        self.animal = animal
        self.is_flipped = False
        self.tile_coefficient = -1
        self.flipped_this_turn = False
        self.x = x
        self.y = y

    def carry_out_task(self, dragon):
        pass