from typing import Optional
from .DrawAssetInstruction import DrawAssetInstruction
from .DrawableByAsset import DrawableByAsset

class DrawClickableAssetInstruction(DrawAssetInstruction):
    """A data class for organising the data required for drawing a clickable image using an asset.

    Author: Shen
    """

    def __init__(
        self,
        asset_path: str,
        associated_drawable: DrawableByAsset,
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
            associated_drawable: Drawable object associated with the asset
        """
        super().__init__(asset_path, x, y, size, rotate)
        self.__associated_drawable = associated_drawable

    def get_associated_drawable(self) -> DrawableByAsset:
        return self.__associated_drawable
