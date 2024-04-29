from abc import ABC, abstractmethod

class ChitCard(ABC):
    """
    Abstract base class representing a chit card in the game.
    """
    
    def __init__(self, chit_steps, x, y):
        """
        Initialize a ChitCard object.

        Args:
        - chit_steps (int): The number of steps indicated by the number of animals on the chit card.
        - x (int): The x-coordinate of the chit card on the game board.
        - y (int): The y-coordinate of the chit card on the game board.
        """
        self.flipped = False
        self.chit_steps = chit_steps
        self.col = x
        self.row = y

    def flip(self):
        """
        Flip the chit card over.
        """
        if self.flipped == False:
            self.flipped = True

    @abstractmethod
    def perform_action(self, dragon):
        pass
