from typing import Protocol
from abc import abstractmethod
from game_objects.characters.PlayableCharacter import PlayableCharacter


class WinEventListener(Protocol):
    """Conformers listen for win events that occur in the game.

    Author: Rohan
    """

    @abstractmethod
    def on_player_win(self, character: PlayableCharacter):
        """When a player wins, do something.

        Args:
            character: The character who won
        """
        ...
