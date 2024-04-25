from abc import ABC, abstractmethod

class ChitCard(ABC):
    
    def __init__(self, chit_steps):
        self.flipped = False
        self.chit_steps = chit_steps

    def flip(self):
        # Player flipping a chit card
        if self.flipped == False:
            self.flipped = True
        # Player turn ends, unflip the chit card
        elif self.flipped == True:
            self.flipped = False

    @abstractmethod
    def perform_action(self, dragon):
        pass
