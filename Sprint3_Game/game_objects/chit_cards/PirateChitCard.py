from .ChitCard import ChitCard
from typing import Optional
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from game_objects.characters.PlayableCharacter import PlayableCharacter


class PirateChitCard(ChitCard):
    """Represents a chit card that when flipped lets characters move backwards based on number of dragon pirates on chit card.

    Author: Rohan
    """

    def __init__(self, symbol_count: int, draw_properties: Optional[DrawProperties] = None) -> None:
        """
        Args:
            symbol_count: The symbol count for the chit card
            draw_properties (optional): Properties specifying how and where the chit card should be drawn
        """
        super().__init__(symbol_count, draw_properties)

    def _on_draw_request(self, draw_properties: DrawProperties) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """On draw request, returns instructions to draw a chit card that displays its back when its not flipped. When flipped,
        it draws dragon pirate symbol with an indication of the number of sybmbols.

        Args:
            draw_properties: The draw properties requesting how to draw this object

        Returns:
            A list containing tuples in the form of (drawing instruction, object to return when clicking on
            graphic represented by instruction)
        """
        asset_path: str = "assets/chit_cards"
        coord_x, coord_y = draw_properties.get_coordinates()

        if self.get_flipped():
            return [
                (
                    DrawAssetInstruction(
                        f"{asset_path}/chit_card_dragon_pirate_{self.get_symbol_count()}.png",
                        x=coord_x,
                        y=coord_y,
                        size=draw_properties.get_size(),
                    ),
                    self,
                )
            ]
        return [
            (
                DrawAssetInstruction(f"{asset_path}/chit_card_back.png", x=coord_x, y=coord_y, size=draw_properties.get_size()),
                self,
            )
        ]

    def on_click(self, character: PlayableCharacter) -> None:
        """On click, reveal the chit card if its not flipped. Once revealed, the chit card cannot be flipped back by
        clicking. Move the player in the negative direction based on the symbol count

        Args:
            character: The character who clicked the sprite

        Raises:
            Exception if the game board delegate was not set before calling
        """
        if self._board_delegate is not None:
            if not self.get_flipped():
                self._board_delegate.move_character_by_steps(character, self.get_symbol_count() * (-1))
                self.set_flipped(not self.get_flipped())
        else:
            raise Exception("Board delegate was not set when on_click() called.")
