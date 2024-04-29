from .ChitCard import ChitCard

class DragonPirateChitCard(ChitCard):

    def __init__(self, chit_steps, animal, x, y):
        super().__init__(chit_steps, x, y)
        self.animal = animal
        self.flipped = False

    def flip(self):
        if not self.flipped:
            self.flipped = True

    def perform_action(self, dragon):
        pass