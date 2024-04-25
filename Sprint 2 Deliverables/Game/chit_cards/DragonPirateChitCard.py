from .ChitCard import ChitCard

class DragonPirateChitCard(ChitCard):

    def __init__(self, chit_steps, chit_quantity):
        super().__init__(chit_steps)
        # The number of chit symbols on the chit card (1 or 2)
        self.chit_quantity = chit_quantity

    # Set the number of steps to move back based on its chit count
    def set_steps(self):
        self.chit_steps = -self.chit_quantity

    def perform_action(self, dragon):
        pass