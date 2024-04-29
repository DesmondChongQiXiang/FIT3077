from .ChitCard import ChitCard

class AnimalChitCard(ChitCard):
    """
    Class representing an animal chit card in the game.
    """

    def __init__(self, chit_steps, animal, x, y):
        """
        Initialize an AnimalChitCard object.

        Args:
        - chit_steps (int): The number of steps indicated by the number of animals on the chit card.
        - animal (str): The type of animal associated with the chit card.
        - x (int): The x-coordinate of the chit card on the game board.
        - y (int): The y-coordinate of the chit card on the game board.
        """
        super().__init__(chit_steps, x, y)
        self.animal = animal
        self.flipped = False

    def flip(self):
        """
        Flip the chit card over.
        """
        if not self.flipped:
            self.flipped = True

    def perform_action(self, dragon):
        pass