from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.chit_cards.ChitCard import ChitCard
from factories.ClassTypeIdentifier import ClassTypeIdentifier

from typing import Optional, Any


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
        it draws dragon pirate symbol with an indication of the number of symbols.

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
                        f"{asset_path}/chit_card_dragon_pirate_{self._symbol_count}.png",
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
        # guard statements
        if self._board_delegate is None:
            raise Exception("Board delegate was not set when on_click() called.")
        if self._symbol_count is None:
            raise Exception("There was no symbol count set.")

        # flip logic
        if not self.get_flipped():
            self._board_delegate.move_character_by_steps(character, self._symbol_count * (-1))
            self.set_flipped(not self.get_flipped())

    def on_save(self, to_write: dict[str, Any]) -> Optional[Any]:
        """When requested on save, return a JSON compatible object describing this pirate chit card.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.

        Returns:
            A JSON compatible object describing the pirate chit card.
        """
        return {"type": ClassTypeIdentifier.chit_card_pirate.value, "symbol_count": self._symbol_count, "flipped": self.get_flipped()}
