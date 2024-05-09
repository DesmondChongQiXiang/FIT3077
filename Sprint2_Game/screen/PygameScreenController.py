from __future__ import annotations
from definitions import ROOT_PATH
from typing import Optional
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from metaclasses.SingletonMeta import SingletonMeta

import pygame


class PygameScreenController(metaclass=SingletonMeta):
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
        self.__image_cache: dict[str, pygame.Surface] = dict()  # K = Absolute image path, V = Loaded image in alpha form

        if self.__screen is None:
            raise Exception("The pygame screen does not yet exist.")

    def draw_asset(self, image_path: str, x: int, y: int, width: Optional[int] = None, height: Optional[int] = None, rotate: float = 0) -> pygame.Surface:
        """Draw an asset on coordinates (x,y) on the screen.

        Args:
            asset_path: The path to the asset relative to root directory
            x: x-coordinate
            y: y-coordinate
            width (optional): Width for the image
            height (optional): Height for the image
            rotate: Degrees to rotate anti-clockwise by (default 0)

        Returns:
            The image (surface) that was drawn

        Author: Shen
        """
        abs_image_path: str = f"{ROOT_PATH}/{image_path}"

        # Use image cache if possible. HIT: Load cached image. MISS: Load then cache image
        if abs_image_path not in self.__image_cache:
            self.__image_cache[abs_image_path] = pygame.image.load(abs_image_path).convert_alpha()

        image: pygame.Surface = self.__image_cache[abs_image_path]
        image = pygame.transform.rotozoom(image, rotate, 1.0)
        if width is not None and height is not None:
            image = pygame.transform.smoothscale(image, (width, height))  # convert to 24/32 bit surface as required by pygame, and smoothly scale
        self.__screen.blit(image, (x, y))

        return image

    def draw_assets_from_instructions(self, instructions: list[DrawAssetInstruction]) -> list[pygame.Surface]:
        """Draw assets in order based on instructions.

        Args:
            instructions: List containing drawing instructions

        Returns:
            The images that were drawn in order of instruction input

        Author: Shen
        """
        images: list[pygame.Surface] = []
        for instruction in instructions:
            image = self.draw_asset(
                instruction.get_asset_path(),
                instruction.get_x_coord(),
                instruction.get_y_coord(),
                instruction.get_width(),
                instruction.get_height(),
                instruction.get_rotation(),
            )
            images.append(image)

        return images

    def draw_clickable_assets_from_instructions(
        self, instructions: list[tuple[DrawAssetInstruction, ModularClickableSprite]]
    ) -> list[tuple[pygame.Rect, ModularClickableSprite]]:
        """Draws clickable assets from instructions in order and return their hitboxes mapped to an object.

        Args:
            instructions: List containing tuple of form (drawing instruction, object to return with click)

        Returns:
            A list of tuples of form (rectangular hitbox, object associated with hitbox)
        """
        hitboxes_map: list[tuple[pygame.Rect, ModularClickableSprite]] = []
        for instruction, clickable in instructions:
            drawn_img = self.draw_assets_from_instructions([instruction])
            rect = drawn_img[0].get_rect()
            rect.x, rect.y = instruction.get_x_coord(), instruction.get_y_coord()
            hitboxes_map.append((rect, clickable))

        return hitboxes_map

    def get_screen_size(self) -> tuple[int, int]:
        """Get the screen size.

        Returns:
            (width, height) of screen size

        Author: Shen
        """
        return self.__screen.get_size()
    
    @staticmethod
    def instance() -> PygameScreenController:
        """Get the shared instance of this controller.
        
        Returns:
            The singleton instance
        """
        return PygameScreenController()
