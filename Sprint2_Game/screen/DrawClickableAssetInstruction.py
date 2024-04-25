from typing import Optional
from .DrawAssetInstruction import DrawAssetInstruction
from .ModularClickableSprite import ModularClickableSprite

class DrawClickableAssetInstruction(DrawAssetInstruction):
    """A data class for organising the data required for drawing a clickable image using an asset.

    Author: Shen
    """

    def __init__(
        self,
        asset_path: str,
        associate_sprite: ModularClickableSprite,
        x: int,
        y: int,
        size: Optional[tuple[int, int]] = None,
        rotate: float = 0,
    ) -> None:
        """
        Args:
            asset_path: The path to the asset relative to the root of the project
            x: The x-coordinate where the image is to be drawn
            y: The y-coordinate where the image is to be drawn
            size: (width, height) of the image in px
            rotate: Degrees to rotate the image by anti-clockwise
            associate_sprite: Clickable object associated with the asset
        """
        super().__init__(asset_path, x, y, size, rotate)
        self.__associated_drawable = associate_sprite

    def get_associated_drawable(self) -> ModularClickableSprite:
        return self.__associated_drawable
