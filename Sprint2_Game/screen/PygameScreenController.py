from __future__ import annotations
from definitions import ROOT_PATH
from typing import Optional

import pygame


class PygameScreenController:
    """Contains useful methods for interacting with pygame's screen.
    
    Warning: Should be used as a singleton

    Throws:
        Will throw an Exception if the pygame screen does not yet exist.

    Author: Shen
    """

    def __init__(self) -> None:
        """Initialise screen controller.

        Throws:
            Exception if the pygame screen does not yet exist
        """
        self.__screen = pygame.display.get_surface()

        if self.__screen is None:
            raise Exception("The pygame screen does not yet exist.")

    def draw_image(self, image_path: str, x: int, y: int, width: Optional[int] = None, height: Optional[int] = None, rotate: float = 0) -> None:
        """Draw an image on coordinates (x,y) on the screen.

        Args:
            image_filename: The path relative to root directory
            x: x-coordinate
            y: y-coordinate
            width (optional): Width for the image
            height (optional): Height for the image
            rotate: Degrees to rotate anti-clockwise by (default 0)

        Author: Shen
        """
        image = pygame.image.load(f"{ROOT_PATH}/{image_path}")
        if width is not None and height is not None:
            image = pygame.transform.scale(image, (width, height))
        image = pygame.transform.rotozoom(image, rotate, 1.0)
        self.__screen.blit(image, (x, y))


# References
# https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
