from typing import Protocol
from abc import abstractmethod
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite

class DrawableByClickables(Protocol):
    """Represents objects that can draw clickables.
    
    Author: Shen
    """

    @abstractmethod
    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Get the instructions to draw the clickable asset.

        Returns:
            A list containing tuples in the form of (drawing instructions, object to return on click)
        """
        ...