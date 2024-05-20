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

    def __init__(self, variant: PlayableCharacterVariant, name: str, draw_properties: Optional[DrawProperties] = None):
        """
        Args:
            variant: The variant of the character
            name: The name for the character
            draw_properties (optional): The drawing properties specifying how to draw the character
        """
        self._variant = variant
        self._draw_properties = draw_properties
        self.__should_continue_turn: bool = True
        self.__name = name
        self._is_currently_playing: bool = False

    def should_continue_turn(self) -> bool:
        """Return whether the playable character should continue its turn for the next tick (i.e game loop).

        Returns:
            Whether the character should continue its turn
        """
        return self.__should_continue_turn

    def set_should_continue_turn(self, status: bool) -> None:
        """Set whether the character should continue its turn.

        Args:
            status: Whether the character should continue its turn
        """
        self.__should_continue_turn = status

    def set_draw_properties(self, draw_properties: DrawProperties) -> None:
        """Set the properties specifying how to draw the character.

        Args:
            draw_data: The draw data
        """
        self._draw_properties = draw_properties

    def set_is_currently_playing(self, playing: bool) -> None:
        """Set whether the character is currently playing. Affects how a character is drawn.

        Args:
            playing: Whether the character is currently playing
        """
        self._is_currently_playing = playing

    def name(self) -> str:
        """Gets the name of the playable character.

        Returns:
            The character's name
        """
        return self.__name
