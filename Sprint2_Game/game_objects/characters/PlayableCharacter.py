from abc import ABC, abstractmethod
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawProperties import DrawProperties
from typing import Optional


class PlayableCharacter(ABC, DrawableByAsset):
    """Represents a playable character in the game.

    Author: Shen
    """

    def __init__(self, draw_properties: Optional[DrawProperties] = None):
        """
        Args:
            draw_properties (optional): The drawing properties specifying how to draw the character
        """
        self.__draw_properties = draw_properties

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

    @abstractmethod
    def take_turn(self) -> None:
        """Perform turn functionalities for the character."""
