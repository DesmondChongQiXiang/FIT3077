from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from game_objects.game_board.GameBoard import GameBoard
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
        self._board_delegate: Optional[GameBoard] = None

    def set_flipped(self, state: bool) -> None:
        """Set the flipped state of the chit card.

        Args:
            state: Whether the chit card is flipped
        """
        self.__flipped = state

    def set_game_board_delegate(self, game_board: GameBoard) -> None:
        """Set the game board delegate to inform about events occurring for the chit cards.

        Args:
            game_board: The game board
        """
        self._board_delegate = game_board

    def get_flipped(self) -> bool:
        """Gets whether the chit card is flipped."""
        return self.__flipped

    def get_symbol_count(self) -> int:
        """Gets the number of symbols the chit card should have."""
        return self.__symbol_count

    def set_draw_properties(self, draw_properties: DrawProperties) -> None:
        """Set how the chit card should be drawn.

        Args:
            draw_properties: The draw properties
        """
        self.__draw_properties = draw_properties

    def get_draw_properties(self) -> Optional[DrawProperties]:
        """Returns how the chit card should be drawn if the data exists.

        Returns:
            How the chit card should be drawn (i.e its properties)
        """
        return self.__draw_properties
