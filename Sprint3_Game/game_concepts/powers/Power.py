from abc import abstractmethod, ABC
from typing import Optional
from game_objects.characters.PlayableCharacter import PlayableCharacter


class Power(ABC):
    """
    Represents a power that can cause effects to playable characters when executed. 

    Warning: The user of the power must be set, otherwise execution will fail.

    Author: Shen, Ian, Desmond
    """

    def __init__(self, user: Optional[PlayableCharacter] = None):
        """Constructor.

        Args:
            user (optional): The character using the power
        """
        self._user: Optional[PlayableCharacter] = user

    def set_user(self, user: PlayableCharacter) -> None:
        """Sets the user of the power.

        Args:
            user: The character using the power
        """
        self._user = user

    def execute(self) -> None:
        """Executes the action specified by the power.

        Raises:
            Exception if the user of the power is not set.
        """
        if self._user is not None:
            self._on_execute(self._user)
            return
        raise Exception("The user of the power was not set before execution.")

    @abstractmethod
    def _on_execute(self, user: PlayableCharacter) -> None:
        """On execution of the power, perform an effect.

        Args:
            user: The character that initiated the power
        """
        ...
