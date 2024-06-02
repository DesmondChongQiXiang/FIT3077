from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.animals.Animal import Animal
from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from factories.ClassTypeIdentifier import ClassTypeIdentifier

from typing import Optional, Any


class AnimalChitCard(ChitCard):
    """Represents a chit card that when flipped lets characters move when the animal matches the character's tile.

    Author: Shen
    """

    def __init__(self, animal: Animal, symbol_count: int, draw_properties: Optional[DrawProperties] = None) -> None:
        """
        Args:
            animal: The animal associated with the chit card
            symbol_count: The symbol count for the chit card
            draw_properties (optional): Properties specifying how and where the chit card should be drawn
        """
        self.__animal = animal
        super().__init__(symbol_count, draw_properties)

    def _on_draw_request(self, draw_properties: DrawProperties) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """On draw request, returns instructions to draw a chit card that displays its back when its not flipped. When flipped,
        it draws the chit card's animal with an indication of the number of sybmbols.

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
                        f"{asset_path}/chit_card_{self.__animal.value}_{self._symbol_count}.png",
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
        clicking. Ends the player's turn if the animal on the chit card flipped does not match with the animal on its
        current tile it's standing on.

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
        tile_animal: Optional[Animal] = self._board_delegate.get_character_floor_tile(character).get_animal()
        if not self.get_flipped():
            if tile_animal is not None and tile_animal != self.__animal:
                # failed match ends turn
                character.set_should_continue_turn(False)
            else:
                self._board_delegate.move_character_by_steps(character, self._symbol_count)

            self.set_flipped(not self.get_flipped())

    def on_save(self, to_write: dict[str, Any]) -> None:
        """When requested on save, add the object describing the chit card to the chit card sequence list. 

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.

        Raises:
            Exception if player_data.players did not exist in the writing dictionary before the request
        """
        try:
            chit_card_sequence: list[Any] = to_write["chit_card_sequence"]
        except Exception:
            raise Exception(f"chit_card_sequence did not exist before issuing save request for this chit card. type=AnimalChitCard")

        chit_card_sequence.append(
            {"type": ClassTypeIdentifier.chit_card_animal, "animal": self.__animal.value, "symbol_count": self._symbol_count, "flipped": self.get_flipped()}
        )
