from __future__ import annotations
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.chit_cards.ChitCard import ChitCard
from game_concepts.powers.Power import Power
from factories.ClassTypeIdentifier import ClassTypeIdentifier

from typing import Optional, Any


class PowerChitCard(ChitCard):
    """Represents a chit card that can execute a power when clicked on.

    Author: Desmond, Ian, Shen
    """

    def __init__(self, power: Power, image_path: str, draw_properties: Optional[DrawProperties] = None) -> None:
        """
        Args:
            power: The power for the chit card to execute when clicked
            image_path: The image path relative to the root of this project to use for the front of this chit card
            draw_properties (optional): Properties specifying how and where the chit card should be drawn
        """
        super().__init__(draw_properties=draw_properties)
        self.__image_path: str = image_path
        self.__power: Power = power

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
                        self.__image_path,
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

        # flip logic
        if not self.get_flipped():
            self.__power.set_user(character)
            self.__power.execute()
            self.set_flipped(not self.get_flipped())

    def on_save(self, to_write: dict[str, Any]) -> Optional[Any]:
        """When requested on save, add a JSON compatible object describing this power chit card.

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
                "type": ClassTypeIdentifier.chit_card_power.value,
                "deferred": True,
                "dependencies": [self.__power.on_save(to_write)],
                "asset_path": self.__image_path,
                "flipped": self.get_flipped(),
            }
        )

    @classmethod
    def create_from_json_save(cls, save_data: dict[str, Any], power: Power) -> PowerChitCard:
        """Create a power chit card based on a power chit card json save data object, and a power.

        Args:
            save_data: The dictionary representing the JSON save data object for a power chit card type
            power: The power for the power chit card

        Returns:
            A power chit card matching the save data, with the power passed in
        """
        try:
            instance: PowerChitCard = cls(power, save_data["asset_path"])
            instance.set_flipped(save_data["flipped"])
            return instance
        except:
            raise Exception(f"Save data must have attributes 'asset_path' and 'flipped'. Passed in={save_data}")
