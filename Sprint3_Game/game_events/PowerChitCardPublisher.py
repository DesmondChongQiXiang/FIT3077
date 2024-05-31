from __future__ import annotations

from metaclasses.SingletonMeta import SingletonMeta
from game_events.PowerChitCardListener import PowerChitCardListener
from game_objects.characters.PlayableCharacter import PlayableCharacter
from typing import Optional, cast


class PowerChitCardPublisher(metaclass=SingletonMeta):
    """A publisher that allows subscribers to be notified of a character has flipped a Power Chit Card.

    Author: Desmond & Ian
    """

    def __init__(self) -> None:
        """Constructor."""
        self.__subscribers: list[PowerChitCardListener] = []

    def subscribe(self, listener: PowerChitCardListener) -> None:
        """Subscribe to listen to power type events.

        Args:
            listener: The listener
        """
        self.__subscribers.append(listener)

    def unsubscribe(self, listener: PowerChitCardListener) -> None:
        """Unsubscribe to listen to power type events.

        Args:
            listener: The listener
        """
        if listener in self.__subscribers:
            self.__subscribers.remove(listener)

    def notify_subscribers(self, symbol_count: int) -> None:
        """Notify all subscribed objects a player flipped a power chit card and the number of symbol on power chit card.

        Args:
            listener: The listener
        """
        for subscriber in self.__subscribers:
            subscriber.on_action_performed(symbol_count)

    @staticmethod
    def instance() -> PowerChitCardPublisher:
        """Get the shared instance of this controller.

        Returns:
            The singleton instance
        """
        instance = cast(Optional[PowerChitCardPublisher], SingletonMeta._get_existing_instance(PowerChitCardPublisher))
        if instance is not None:
            return instance
        return PowerChitCardPublisher()
