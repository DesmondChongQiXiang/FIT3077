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

    def on_click(self, character: PlayableCharacter, characters_tile: Tile) -> None:
        """On click toggle its flipped state.
        
        Args:
            character: The character who clicked the sprite
            characters_tile: The tile the character was on
        """
        self.set_flipped(not self.get_flipped())
