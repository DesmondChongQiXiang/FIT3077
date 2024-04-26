from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.animals.Animal import Animal
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite


class AnimalChitCard(ChitCard):
    """Represents a chit card that when flipped lets characters move when the animal matches the character's tile.

    Author: Shen
    """

    def __init__(self, animal: Animal, symbol_count: int, coordinates: tuple[int, int], size: tuple[int, int]) -> None:
        """
        Args:
            animal: The animal associated with the chit card
            symbol_count: The symbol count for the chit card
            coordinates: The coordinates to draw the chit cards at
            size: (width, height) of the chit card in pixels
        """
        self.__animal = animal
        super().__init__(symbol_count, coordinates, size)

    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Chit card displays back when it is not flipped. Otherwise display its front.

        Returns:
            Array containing (instruction to represent flipped state, this object)
        """
        asset_path: str = "assets/chit_cards"
        coord_x, coord_y = self.get_coordinates()

        if self.get_flipped():
            return [
                (
                    DrawAssetInstruction(
                        f"{asset_path}/chit_card_{self.__animal.value}_{self.get_symbol_count()}.png",
                        x=coord_x,
                        y=coord_y,
                        size=self.get_size(),
                    ),
                    self,
                )
            ]
        return [
            (
                DrawAssetInstruction(f"{asset_path}/chit_card_back.png", x=coord_x, y=coord_y, size=self.get_size()),
                self,
            )
        ]

    def on_click(self) -> None:
        """On click toggle its flipped state."""
        self.set_flipped(not self.get_flipped())
