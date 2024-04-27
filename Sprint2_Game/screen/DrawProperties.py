class DrawProperties:
    """A data class for organising the data required for drawing any object.

    Author: Shen
    """

    def __init__(self, coordinates: tuple[int, int], size: tuple[int, int], rotation: float = 0):
        """
        Args:
            coordinates: The coordinates the tile should be drawn at in form (x, y)
            size: The size of the tile in pixels in form (width, height)
            rotation: The number of degrees anti-clockwise the tile should be drawn at. (default = 0)
        """
        self.__coordinates = coordinates
        self.__size = size
        self.__rotation = rotation

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

    def get_rotation(self) -> float:
        """Returns the degrees anticlockwise the tile should be drawn at (if specified).

        Returns:
            The degrees
        """
        return self.__rotation
