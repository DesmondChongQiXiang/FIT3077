class TileDrawData:
    """A data class for organising the data required for drawing any tile.

    Author: Shen
    """

    def __init__(self, coordinates: tuple[int, int], size: tuple[int, int]):
        """
        Args:
            coordinates: The coordinates the tile should be drawn at in form (x, y)
            size: The size of the tile in pixels in form (width, height)
        """
        self.__coordinates = coordinates
        self.__size = size

    def get_coordinates(self) -> tuple[int, int]:
        """Returns the coordinates the tile should be drawn at.

        Returns:
            The coordinates in form (x, y)
        """
        return self.__coordinates

    def get_size(self) -> tuple[int, int]:
        """Returns the dimensions that the tile should be drawn at.

        Returns:
            The size in form (width, height)
        """
        return self.__size
