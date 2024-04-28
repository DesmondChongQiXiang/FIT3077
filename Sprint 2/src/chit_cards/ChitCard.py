from abc import ABC, abstractmethod

class ChitCard(ABC):
    
    def __init__(self, chit_steps, x, y):
        self.flipped = False
        self.chit_steps = chit_steps
        self.col = x
        self.row = y

    def flip(self):
        # Player flipping a chit card
        if self.flipped == False:
            self.flipped = True

    @abstractmethod
    def perform_action(self, dragon):
        pass
