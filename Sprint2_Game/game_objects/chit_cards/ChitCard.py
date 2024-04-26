from screen.ModularClickableSprite import ModularClickableSprite

class ChitCard(ModularClickableSprite):
    """Represents a chit card.

    Author: Shen
    """
    def __init__(self, symbol_count: int, coordinates: tuple[int, int], size: tuple[int, int]) -> None:
        """
        Args:
            symbol_count: The symbol count for the chit card
            coordinates: The coordinates (x,y) to draw the chit cards at
            size: (width, height) of the chit card in pixels
        """
        self.__symbol_count = symbol_count
        self.__flipped: bool = False
        self.__coordinates = coordinates
        self.__size = size

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
    
    def get_size(self) -> tuple[int, int]:
        """Gets the size of the chit card in pixels.
        
        Returns:
            Size of the chit card in form (width, height) 
        """
        return self.__size