from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.animals.Animals import Animal
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite


class AnimalChitCard(ChitCard):
    """Represents a chit card that when flipped lets characters move when the animal matches the character's tile.

    Author: Shen
    """

    def __init__(self, animal: Animal, symbol_count: int) -> None:
        """
        Args:
            animal: The animal associated with the chit card
            symbol_count: The symbol count for the chit card
        """
        self.__animal = animal
        super().__init__(symbol_count)

    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Instructions to draw the animal chit card."""
        # test instruction
        return [(DrawAssetInstruction("assets/chit_cards/chit_card_back.png", x=250, y=250), self)]

    def on_click(self) -> None:
        """On click toggle its flipped state."""
        self.set_flipped(not self.get_flipped())
