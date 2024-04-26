from screen.ModularClickableSprite import ModularClickableSprite

class ChitCard(ModularClickableSprite):
    """Represents a chit card.

    Author: Shen
    """
    def __init__(self, symbol_count: int, coordinates: tuple[int, int]) -> None:
        """
        Args:
            symbol_count: The symbol count for the chit card
            coordinates: The coordinates (x,y) to draw the chit cards at
        """
        self.__symbol_count = symbol_count
        self.__flipped: bool = False
        self.__coordinates = coordinates

    def set_flipped(self, state: bool) -> None:
        """Set the flipped state of the chit card."""
        self.__flipped = state

    def get_flipped(self) -> bool:
        """Gets whether the chit card is flipped."""
        return self.__flipped
    
    def get_symbol_count(self) -> int:
        """Gets the number of symbols the chit card should have."""
        return self.__symbol_count

    def get_coordinates(self) -> tuple[int, int]:
        """Gets the coordinates in (x,y) at which the chit card should be drawn"""
        return self.__coordinates