from __future__ import annotations
from metaclasses.SingletonMeta import SingletonMeta
from game_concepts.events.WinEventListener import WinEventListener
from game_objects.characters.PlayableCharacter import PlayableCharacter
from typing import Optional, cast


class WinEventPublisher(metaclass=SingletonMeta):
    """A publisher that allows subscribers to be notified of a character who has won the game.

    Author: Rohan
    """

    def __init__(self) -> None:
        """Constructor."""
        self.__subscribers: list[WinEventListener] = []

    def subscribe(self, listener: WinEventListener) -> None:
        """Subscribe to listen to win events.

        Args:
            listener: The listener
        """
        self.__subscribers.append(listener)

    def unsubscribe(self, listener: WinEventListener) -> None:
        """Subscribe an object to listen to win events.

        Args:
            listener: The listener
        """
        if listener in self.__subscribers:
            self.__subscribers.remove(listener)

    def notify_subscribers(self, character: PlayableCharacter) -> None:
        """Notify all subscribed objects about a character who won.

        Args:
            character: The character who won
        """
        for subscriber in self.__subscribers:
            subscriber.on_player_win(character)

    @staticmethod
    def instance() -> WinEventPublisher:
        """Get the shared instance of this controller.

        Returns:
            The singleton instance
        """
        instance = cast(Optional[WinEventPublisher], SingletonMeta._get_existing_instance(WinEventPublisher))
        if instance is not None:
            return instance
        return WinEventPublisher()
