from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.animals.Animals import Animal
from screen.DrawClickableAssetInstruction import DrawClickableAssetInstruction
from game_objects.game_board.GameBoard import GameBoard


class AnimalChitCard(ChitCard):
    """Represents a chit card that when flipped lets characters move when the animal matches the character's tile.

    Author: Shen
    """

    def __init__(self, animal: Animal, game_board: GameBoard, symbol_count: int) -> None:
        """
        Args:
            animal: The animal associated with the chit card
            game_board: The gameboard the chit card should be on
            symbol_count: The symbol count for the chit card
        """
        self.__animal = animal
        super().__init__(game_board, symbol_count)

    def get_draw_clickable_assets_instructions(self) -> list[DrawClickableAssetInstruction]:
        """Draw the chit card."""
        # test instruction
        return [DrawClickableAssetInstruction("assets/chit_cards/chit_card_back.png", associated_sprite=self, x=250, y=250)]

    def on_click(self) -> None:
        """On click toggle its flipped state."""
        self.set_flipped(not self.get_flipped())
