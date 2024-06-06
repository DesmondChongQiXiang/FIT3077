from typing import Protocol
from abc import abstractmethod


class Command(Protocol):
    """Represents a command that has one method execute() which can be used to execute functionalities that do not depend 
    on or affect the state of any game objects.

    Author: Shen
    """

    @abstractmethod
    def execute(self) -> None:
        """Execute the functionality defined by this command."""
        ...
