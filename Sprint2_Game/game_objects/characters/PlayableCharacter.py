from abc import ABC, abstractmethod
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawProperties import DrawProperties
from game_objects.characters.PlayableCharacterVariant import PlayableCharacterVariant
from typing import Optional


class PlayableCharacter(ABC, DrawableByAsset):
    """Represents a playable character in the game. Actions in the game interact with this class to determine their
    behaviour.

    Author: Shen
    """

    def __init__(self, variant: PlayableCharacterVariant, draw_properties: Optional[DrawProperties] = None, max_action_count: int = 1):
        """
        Args:
            variant: The variant of the character
            draw_properties (optional): The drawing properties specifying how to draw the character
            max_action_count (default = 1): The max number of actions the character can take before its turn ends
        """
        self._variant = variant
        self.__draw_properties = draw_properties
        self.__max_action_count = max_action_count
        self.__action_count: int = 0
        self._is_currently_playing: bool = False

    def notify_action_taken(self) -> None:
        """Notifies the character that an action has been taken. Default implementation increments the character's internal
        counter for the number of actions taken so far for its turn.

        Note:
            Override to change default behaviour
        """
        self.__action_count += 1

    def should_continue_turn(self) -> bool:
        """Return whether the playable character should continue its turn for the next tick (i.e game loop). Default
        implementation returns false and resets the character's internal counter for the number of actions taken
        when the number of actions taken by the character exceeds the maximum number of actions it can take for its turn.

        Note:
            Override to change default behaviour

        Returns:
            Whether the character should continue its turn
        """
        should_continue = self.__action_count <= self.__max_action_count
        if not should_continue:
            self.__action_count = 0
        return should_continue

    def get_draw_properties(self) -> Optional[DrawProperties]:
        """Return the drawing properties for the character (if it exists).

        Returns:
            The drawing properties
        """
        return self.__draw_properties

    def set_draw_properties(self, draw_properties: DrawProperties) -> None:
        """Set the properties specifying how to draw the character.

        Args:
            draw_data: The draw data
        """
        self.__draw_properties = draw_properties

    def set_is_currently_playing(self, playing: bool) -> None:
        """Set whether the character is currently playing. Affects how a character is drawn.

        Args:
            playing: Whether the character is currently playing
        """
        self._is_currently_playing = playing
