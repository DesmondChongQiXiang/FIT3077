from __future__ import annotations
from metaclasses.SingletonMeta import SingletonMeta
from game_events.WinEventListener import WinEventListener
from game_objects.characters.PlayableCharacter import PlayableCharacter
from typing import Optional, cast

class WinEventPublisher(metaclass = SingletonMeta):
    def __init__(self) -> None:
        self.subscribers = []

    def subscribe(self,subscriber: WinEventListener):
        self.subscribers.append(subscriber)

    def unsubscribe(self,subscriber: WinEventListener):
        if WinEventListener in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_subscribers(self,character: PlayableCharacter) -> PlayableCharacter:
        for subscriber in self.subscribers:
            subscriber.on_player_win(character)
        return character
            


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

