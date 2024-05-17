from __future__ import annotations
from collections import defaultdict
from typing import Optional, cast
from definitions import ROOT_PATH
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from metaclasses.SingletonMeta import SingletonMeta

import pygame


class PygameScreenController(metaclass=SingletonMeta):
    """Singleton containing useful methods for interacting with pygame's screen.

    Throws:
        Will throw an Exception if the pygame screen does not yet exist.

    Author: Shen
    """

    __CACHE_RESIZED_MAX_SIZE = 5000  # max size the resized image cache can reach before purge

    def __init__(self) -> None:
        """Initialise screen controller.

        Throws:
            Exception if the pygame screen does not yet exist
        """
        self.__screen: pygame.Surface = pygame.display.get_surface()
        self.__image_cache: dict[str, pygame.Surface] = dict()  # K = Absolute image path, V = Loaded image in alpha form
        self.__image_cache_resized: dict[str, dict[tuple[int, int], pygame.Surface]] = defaultdict(
            dict
        )  # K = Absolute image path, V = dictionary with key->(width, height), value->cached resized image
        self.__image_cache_resized_size: int = 0  # current resized cache size

        if self.__screen is None:
            raise Exception("The pygame screen does not yet exist.")

    def fill_screen_with_colour(self, rgb: tuple[int, int, int]) -> None:
        """Fill the screen with a solid colour.

        Args:
            rgb: The colour in form (R, G, B)
        """
        self.__screen.fill(rgb)

    def draw_asset(self, image_path: str, x: int, y: int, size: Optional[tuple[int, int]] = None, rotate: float = 0) -> pygame.Surface:
        """Draw an asset on coordinates (x,y) on the screen.

        Args:
            asset_path: The path to the asset relative to root directory
            x: x-coordinate
            y: y-coordinate
            size (optional): Requested width and height for the image in form (width, height)
            rotate: Degrees to rotate anti-clockwise by (default 0)

        Returns:
            The image (surface) that was drawn

        Author: Shen
        """
        abs_image_path: str = f"{ROOT_PATH}/{image_path}"

        # Use image cache to load image if possible. HIT: Load cached image. MISS: Load then cache image
        if abs_image_path not in self.__image_cache:
            self.__image_cache[abs_image_path] = pygame.image.load(abs_image_path).convert_alpha()

        ### TRANSFORMING & DRAWING
        image: pygame.Surface = self.__image_cache[abs_image_path]

        # Resize image to requested width and height
        if size is not None:
            width, height = size[0], size[1]

            # purge cache on exceeding resized cache's max size
            if self.__image_cache_resized_size > PygameScreenController.__CACHE_RESIZED_MAX_SIZE:
                self.__image_cache_resized = defaultdict(dict)
                self.__image_cache_resized_size = 0

            # Resize image whilst using resized cache as much as possible
            requested_size: tuple[int, int] = (width, height)
            resized_cache_for_image: dict[tuple[int, int], pygame.Surface] = self.__image_cache_resized[abs_image_path]

            if requested_size not in resized_cache_for_image:
                resized_cache_for_image[requested_size] = pygame.transform.smoothscale(image, (width, height))
                self.__image_cache_resized_size += 1
            image = resized_cache_for_image[requested_size]

        # Rotate image
        before_rotate_rect = image.get_rect()
        before_rotate_width, before_rotate_height = before_rotate_rect.width, before_rotate_rect.height

        image = pygame.transform.rotate(image, rotate)

        # Draw rotated image, offsetting for padding of image size from rotation
        image_rect = image.get_rect()
        x_rotate_offset, y_rotate_offset = int((image_rect.width - before_rotate_width) / 2), int((image_rect.height - before_rotate_height) / 2)
        self.__screen.blit(image, (x - x_rotate_offset, y - y_rotate_offset))

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
                instruction.get_size(),
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
        instance = cast(Optional[PygameScreenController], SingletonMeta._get_existing_instance(PygameScreenController))
        if instance is not None:
            return instance
        return PygameScreenController()
