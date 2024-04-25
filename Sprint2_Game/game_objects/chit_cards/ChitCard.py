from screen.ModularClickableSprite import ModularClickableSprite

class ChitCard(ModularClickableSprite):
    """Represents a chit card.

    Author: Shen
    """
    def __init__(self, symbol_count: int) -> None:
        """
        Args:
            symbol_count: The symbol count for the chit card
        """
        self.__symbol_count = symbol_count
        self.__flipped: bool = False

    def set_flipped(self, state: bool) -> None:
        """Set the flipped state of the chit card."""
        self.__flipped = state

    def get_flipped(self) -> bool:
        """Gets whether the chit card is flipped."""
        return self.__flipped
