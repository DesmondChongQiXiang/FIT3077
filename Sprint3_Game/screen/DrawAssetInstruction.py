from typing import Optional


class DrawAssetInstruction:
    """A data class for organising the data required for drawing an image using an asset.

    Author: Shen
    """

    def __init__(
        self,
        asset_path: str,
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
            size (optional): (width, height) of the image in px
            rotate: Degrees to rotate the image by anti-clockwise
        """
        self.__asset_path = asset_path
        self.__x = x
        self.__y = y
        self.__size = size
        self.__rotate = rotate

    def get_asset_path(self) -> str:
        """Get the asset path relative to the root of the project.

        Returns:
            The asset path
        """
        return self.__asset_path

    def get_x_coord(self) -> int:
        """Get the x coordinate to draw on.

        Returns:
            The x-coordinate
        """
        return self.__x

    def get_y_coord(self) -> int:
        """Get the y coordinate to draw on.

        Returns:
            The y-coordinate
        """
        return self.__y

    def get_size(self) -> Optional[tuple[int, int]]:
        """Get the size to draw the asset at if it exists.

        Returns:
            The size in form (width, height)px
        """
        return self.__size

    def get_rotation(self) -> float:
        """Get the degrees of anticlockwise rotation to draw the image at.

        Returns:
            The degrees
        """
        return self.__rotate
