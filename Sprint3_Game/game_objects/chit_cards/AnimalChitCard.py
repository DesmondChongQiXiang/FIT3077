from __future__ import annotations
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

    def on_click(self, character: Optional[PlayableCharacter]) -> None:
        """On click, reveal the chit card if its not flipped. Once revealed, the chit card cannot be flipped back by
        clicking. Ends the player's turn if the animal on the chit card flipped does not match with the animal on its
        current tile it's standing on.

        Args:
            character: The character who clicked the sprite

        Raises:
            Exception if the game board delegate was not set before calling
            Exception if there was no playable character clicking this sprite
        """
        # guard statements
        if character is None:
            raise Exception("No playable character clicked this chit card. cls=AnimalChitCard")
        if self._board_delegate is None:
            raise Exception("Board delegate was not set when on_click() called.")
        if self._symbol_count is None:
            raise Exception("There was no symbol count set.")

        # flip logic
        tile_animal: Optional[Animal] = self._board_delegate.get_character_floor_tile(character).get_animal()
        if not self.get_flipped():
            self.set_flipped(not self.get_flipped())

            if tile_animal is None:
                return None

            # End character's turn and don't move if no match with tile animal / universal animal. Otherwise move character
            if tile_animal != Animal.UNIVERSAL and tile_animal != self.__animal:
                character.set_should_continue_turn(False)
            else:
                self._board_delegate.move_character_by_steps(character, self._symbol_count)

    def on_save(self, to_write: dict[str, Any]) -> Optional[Any]:
        """When requested on save, add the JSON compatible object describing this animal chit card to the save dictionary.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.

        Returns:
            None

        Raises:
            Exception if chit_card_sequence did not exist
        """
        to_write["chit_card_sequence"].append(
            {
                "type": ClassTypeIdentifier.chit_card_animal.value,
                "deferred": False,
                "animal": self.__animal.value,
                "symbol_count": self._symbol_count,
                "flipped": self.get_flipped(),
            }
        )

    @classmethod
    def create_from_json_save(cls, save_data: dict[str, Any]) -> AnimalChitCard:
        """Create an animal chit card based on a animal chit card type json save data object.

        Args:
            save_data: The dictionary representing the JSON save data object for an animal chit card type

        Returns:
            An animal chit card matching the save data
        """
        try:
            instance: AnimalChitCard = cls(Animal(save_data["animal"]), save_data["symbol_count"])
            instance.set_flipped(save_data["flipped"])
            return instance
        except:
            raise Exception(f"Save data must have attributes 'animal', 'symbol_count' and 'flipped'. Passed in={save_data}")
