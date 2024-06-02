from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.game_board.GameBoard import GameBoard
from codec.saves.JSONSavable import JSONSavable

from typing import Optional
from abc import ABC, abstractmethod


class ChitCard(ModularClickableSprite, ABC, JSONSavable):
    """Represents a chit card. A chit card is a game element that can be flipped, and can be pressed on to perform
    an associated functionality.

    Author: Shen
    """

    def __init__(self, symbol_count: Optional[int] = None, draw_properties: Optional[DrawProperties] = None) -> None:
        """
        Args:
            symbol_count (optional): The symbol count for the chit card
            draw_properties (optional): Properties specifying how and where the chit card should be drawn
        """
        self._symbol_count: Optional[int] = symbol_count
        self.__flipped: bool = False
        self._draw_properties: Optional[DrawProperties] = draw_properties
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
        """Gets whether the chit card is flipped.

        Returns:
            Whether the chit card is flipped
        """
        return self.__flipped

    def set_draw_properties(self, draw_properties: DrawProperties) -> None:
        """Set how the chit card should be drawn.

        Args:
            draw_properties: The draw properties
        """
        self._draw_properties = draw_properties

    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Get the instructions required to draw the clickable chit cards.

        Returns:
            A list containing tuples in the form of (drawing instruction, object to return when clicking on
            graphic represented by instruction)

        Raises:
            Exception if the draw properties were not set prior to a request to draw.
        """
        if self._draw_properties is None:
            raise Exception("Tried drawing, but the draw properties (properties required for drawing) weren't set.")
        return self._on_draw_request(self._draw_properties)

    @abstractmethod
    def _on_draw_request(self, draw_properties: DrawProperties) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Called when a request is made to draw this object.

        The implementation must provide the instructions required to draw itself on the pygame screen, and the objects
        to return when clicking the graphic represented by each instruction.

        Args:
            draw_properties: The draw properties requesting how to draw this object

        Returns:
            A list containing tuples in the form of (drawing instruction, object to return when clicking on
            graphic represented by instruction)
        """
        ...
