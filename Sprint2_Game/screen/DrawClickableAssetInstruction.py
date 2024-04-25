from typing import Optional
from screen.DrawAssetInstruction import DrawAssetInstruction

import screen.ModularClickableSprite as mcs

class DrawClickableAssetInstruction(DrawAssetInstruction):
    """A data class for organising the data required for drawing a clickable image using an asset.

    Author: Shen
    """

    def __init__(
        self,
        asset_path: str,
        associated_sprite: mcs.ModularClickableSprite,
        x: int,
        y: int,
        size: Optional[tuple[int, int]] = None,
        rotate: float = 0,
    ) -> None:
        """
        Args:
            asset_path: The path to the asset relative to the root of the project
            associated_sprite: Clickable object associated with the asset
            x: The x-coordinate where the image is to be drawn
            y: The y-coordinate where the image is to be drawn
            size (Optional): (width, height) of the image in px.
            rotate (Optional): Degrees to rotate the image by anti-clockwise
        """
        super().__init__(asset_path, x, y, size, rotate)
        self.__associated_drawable = associated_sprite

    def get_associated_drawable(self) -> mcs.ModularClickableSprite:
        return self.__associated_drawable
