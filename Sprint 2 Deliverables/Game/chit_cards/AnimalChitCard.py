from .ChitCard import ChitCard

class AnimalChitCard(ChitCard):

    def __init__(self, chit_steps, chit_quantity, animal):
        super().__init__(chit_steps)
        # The number of chit symbols on the chit card (1 - 3)
        self.chit_quantity = chit_quantity
        # The animal type of the chit card
        self.animal = animal

    # Set the number of steps to move forward based on its chit count
    def set_steps(self):
        self.chit_steps = self.chit_quantity

    def perform_action(self, dragon):
        pass