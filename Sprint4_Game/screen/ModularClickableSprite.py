from __future__ import annotations
from abc import abstractmethod
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from typing import Protocol, Optional


class ModularClickableSprite(Protocol):
    """Allows an object to be represented by assets (images) that can be clicked on.

    Author: Shen
    """

    @abstractmethod
    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Get the instructions required to draw the clickable asset.

        Returns:
            A list containing tuples in the form of (drawing instruction, object to return when clicking on
            graphic represented by instruction)
        """
        ...

    @abstractmethod
    def on_click(self, character: Optional[PlayableCharacter]) -> None:
        """When the sprite is clicked on, do something.

        Args:
            character: The character who clicked the sprite if there was one.
        """
        ...
