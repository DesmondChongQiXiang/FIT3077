from definitions import ROOT_PATH
from typing import Optional
from screen.DrawAssetInstruction import DrawAssetInstruction

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

    def draw_asset(self, image_path: str, x: int, y: int, width: Optional[int] = None, height: Optional[int] = None, rotate: float = 0) -> None:
        """Draw an asset on coordinates (x,y) on the screen.

        Args:
            asset_path: The path to the asset relative to root directory
            x: x-coordinate
            y: y-coordinate
            width (optional): Width for the image
            height (optional): Height for the image
            rotate: Degrees to rotate anti-clockwise by (default 0)

        Author: Shen
        """
        image = pygame.image.load(f"{ROOT_PATH}/{image_path}")
        if width is not None and height is not None:
            image = pygame.transform.smoothscale(image.convert_alpha(), (width, height))  # convert to 24/32 bit surface as required by pygame, and smoothly scale
        image = pygame.transform.rotozoom(image, rotate, 1.0)
        self.__screen.blit(image, (x, y))

    def draw_assets_from_instructions(self, instructions: list[DrawAssetInstruction]) -> None:
        """Draw assets based on instructions.

        Args:
            instructions: list containing drawing instructions

        Author: Shen
        """
        for instruction in instructions:
            self.draw_asset(
                instruction.get_asset_path(),
                instruction.get_x_coord(),
                instruction.get_y_coord(),
                instruction.get_width(),
                instruction.get_height(),
                instruction.get_rotation(),
            )

    def get_screen_size(self) -> tuple[int, int]:
        """Get the screen size.

        Returns:
            (width, height) of screen size

        Author: Shen
        """
        return self.__screen.get_size()


# References
# https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
