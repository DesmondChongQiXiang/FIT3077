from typing import Protocol
from abc import abstractmethod

class PowerChitCardListener(Protocol):
    """
    Conforms listen for power chit card events that occur in the game.

    Author: Ian & Desmond
    """

    @abstractmethod
    def on_action_performed(self,  symbol_count:int):
        """
        When an action is performed (i.e. flipped a power chit card), do something.

        Args:
            character: The character who performed the action
        """
        ...
