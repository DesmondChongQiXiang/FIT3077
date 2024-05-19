from __future__ import annotations
from abc import abstractmethod
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from typing import Protocol


class ModularClickableSprite(Protocol):
    """Allows an object to be represented by assets (images) that can be clicked on.

    Author: Shen
    """

    @abstractmethod
    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Get the instructions to draw the clickable assets.

        Returns:
            A list containing tuples in the form of (drawing instructions, object to return on click)
        """
        ...

    @abstractmethod
    def on_click(self, character: PlayableCharacter) -> None:
        """When the sprite is clicked on, do something.

        Args:
            character: The character who clicked the sprite
        """
        ...
