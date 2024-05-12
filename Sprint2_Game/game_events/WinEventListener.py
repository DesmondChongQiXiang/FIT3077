from typing import Protocol
from abc import abstractmethod
from game_objects.characters.PlayableCharacter import PlayableCharacter

class WinEventListener(Protocol):
    pass

    @abstractmethod
    def on_player_win(self, character: PlayableCharacter):
        ...
