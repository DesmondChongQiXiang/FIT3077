"""
Utilities for pygame.

Author: Shen
"""
from typing import Optional

import pygame

def scale_and_rotate_image(image: pygame.Surface, width: Optional[int] = None, height: Optional[int] = None, rotate: float = 0) -> pygame.Surface:
    """
    Scale an image to the specified width and height, whilst rotating it anticlockwise rotate degrees.

    Args:
        image: An image
        width: New width of the image
        height: New height of the image
        rotate: Degrees to rotate anti-clockwise
    """
    if width is not None and height is not None:
        image = pygame.transform.smoothscale(image.convert_alpha(), (width, height))
    return pygame.transform.rotozoom(image, rotate, 1.0)
