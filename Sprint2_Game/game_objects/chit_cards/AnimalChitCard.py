from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.animals.Animal import Animal
from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from typing import Optional


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
                        f"{asset_path}/chit_card_{self.__animal.value}_{self.get_symbol_count()}.png",
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
        if self._board_delegate is not None:
            tile_animal: Optional[Animal] = self._board_delegate.get_character_floor_tile(character).get_animal()
            if tile_animal is not None and tile_animal != self.__animal:
                character.set_should_continue_turn(False)
            else:
                self._board_delegate.move_character_by_steps(character, self.get_symbol_count())
                
            if not self.get_flipped():
                self.set_flipped(not self.get_flipped())
        else:
            raise Exception("Board delegate was not set when on_click() called.")
