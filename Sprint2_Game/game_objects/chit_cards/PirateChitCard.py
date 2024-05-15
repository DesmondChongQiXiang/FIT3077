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

    
    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Chit card displays its back when it is not flipped. Otherwise display its front. Don't draw if drawing properties have not been set.

        Returns:
            Array containing (instruction to represent flipped state, this object)
        """
        draw_properties = self.get_draw_properties()
        if draw_properties is None:
            return []
        asset_path: str = "assets/chit_cards"
        coord_x, coord_y = draw_properties.get_coordinates()

        if self.get_flipped():
            return [
                (
                    DrawAssetInstruction(
                        f"{asset_path}/chit_card_{self.get_symbol_count()}.png",
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
                self._board_delegate.move_character_by_steps(character, self.get_symbol_count())
                self.set_flipped(not self.get_flipped())
        else:
            raise Exception("Board delegate was not set when on_click() called.")