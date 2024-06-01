from .ChitCard import ChitCard
from typing import Optional
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from game_objects.characters.PlayableCharacter import PlayableCharacter


class SwapChitCard(ChitCard):
    """
    Represents a chit card that when flipped switches the position of the player who flips it with the player closest to them

    Author: Rohan
    """

    def __init__(self, draw_properties: Optional[DrawProperties] = None) -> None:
        """
        Args:
            draw_properties (optional): Properties specifying how and where the chit card should be drawn
        """
        super().__init__(draw_properties=draw_properties)

    def _on_draw_request(self, draw_properties: DrawProperties) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """On draw request, returns instructions to draw a chit card that displays its back when its not flipped. When flipped,
        it draws the swap chit card.

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
                        f"{asset_path}/chit_card_swap.png",
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
        clicking. Swap the player with the player closest to them if there is one.
        Args:
            character: The character who clicked the sprite

        Raises:
            Exception if the game board delegate was not set before calling
        """
        if self._board_delegate is not None:
            if not self.get_flipped():
                closest_char: Optional[PlayableCharacter] = self._board_delegate.get_closest_character(character)

                # if there was a closest character, swap and end turn. Otherwise dont swap and dont end turn.
                if closest_char is not None:
                    self._board_delegate.swap_characters(character, closest_char)
                    character.set_should_continue_turn(False)

                self.set_flipped(not self.get_flipped())
        else:
            raise Exception("Board delegate was not set when on_click() called.")
