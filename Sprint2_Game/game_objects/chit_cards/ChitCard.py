from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from typing import Optional


class ChitCard(ModularClickableSprite):
    """Represents a chit card.

    Author: Shen
    """

    def __init__(self, symbol_count: int, draw_properties: Optional[DrawProperties] = None) -> None:
        """
        Args:
            symbol_count: The symbol count for the chit card
            draw_properties (optional): Properties specifying how and where the chit card should be drawn
        """
        self.__symbol_count = symbol_count
        self.__flipped: bool = False
        self.__draw_properties = draw_properties

    def set_flipped(self, state: bool) -> None:
        """Set the flipped state of the chit card."""
        self.__flipped = state

    def get_flipped(self) -> bool:
        """Gets whether the chit card is flipped."""
        return self.__flipped

    def get_symbol_count(self) -> int:
        """Gets the number of symbols the chit card should have."""
        return self.__symbol_count

    def set_draw_properties(self, draw_properties: DrawProperties) -> None:
        """Set how the chit card should be drawn."""
        self.__draw_properties = draw_properties

    def get_draw_properties(self) -> Optional[DrawProperties]:
        """Returns how the chit card should be drawn if the data exists.

        Returns:
            How the chit card should be drawn (i.e its properties)
        """
        return self.__draw_properties
