
from typing import Optional

class DrawAssetInstruction():
    """A data class for organising the data required for drawing an image using an asset.
    
    Author: Shen
    """

    def __init__(self, asset_path: str, x: int, y: int, size: Optional[tuple[int, int]] = None, rotate: float = 0) -> None:
        """        
        Args:
            asset_path: The path to the asset relative to the root of the project
            x: The x-coordinate where the image is to be drawn
            y: The y-coordinate where the image is to be drawn
            size: (width, height) of the image in px
            rotate: Degrees to rotate the image by anti-clockwise
        """
        self.__asset_path = asset_path
        self.__x = x
        self.__y = y
        self.__size = size
        self.__rotate = rotate
    
    def get_asset_path(self) -> str:
        return self.__asset_path
    
    def get_x_coord(self) -> int:
        return self.__x
    
    def get_y_coord(self) -> int:
        return self.__y
    
    def get_width(self) -> Optional[int]:
        return self.__size[0] if self.__size is not None else None
    
    def get_height(self) -> Optional[int]:
        return self.__size[1] if self.__size is not None else None
    
    def get_rotation(self) -> float:
        return self.__rotate
    
