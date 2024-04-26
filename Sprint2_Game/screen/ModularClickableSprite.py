from __future__ import annotations
from abc import ABC, abstractmethod
from screen.DrawAssetInstruction import DrawAssetInstruction


class ModularClickableSprite(ABC):
    """Allows a class to be represented by assets (images) that can be clicked on.

    Author: Shen
    """

    @abstractmethod
    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Get the instructions to draw the clickable asset.

        Returns:
            A list containing tuples in the form of (drawing instructions, object to return on click)
        """
        ...

    @abstractmethod
    def on_click(self) -> None:
        """When the sprite is clicked on, do something."""
        ...
