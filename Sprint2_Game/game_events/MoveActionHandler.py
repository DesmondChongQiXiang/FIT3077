from abc import abstractmethod
from typing import Protocol
from game_objects.characters.PlayableCharacter import PlayableCharacter


class MoveActionHandler(Protocol):
    """Represents a class that can handle a move action.

    Author: Shen
    """

    @abstractmethod
    def on_move_action_fired(self, character: PlayableCharacter, steps: int) -> None:
        """On move action, do something."""
        ...
