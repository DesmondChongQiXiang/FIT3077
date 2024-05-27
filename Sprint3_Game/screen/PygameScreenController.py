from __future__ import annotations
from collections import defaultdict
from collections.abc import Sequence
from typing import Optional, cast
from definitions import ROOT_PATH
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawableByAsset import DrawableByAsset
from screen.ModularClickableSprite import ModularClickableSprite
from metaclasses.SingletonMeta import SingletonMeta

import pygame


class PygameScreenController(metaclass=SingletonMeta):
    """Singleton containing useful methods for interacting with pygame's screen.

    Throws:
        Will throw an Exception if the pygame screen does not yet exist.

    Author: Shen
    """

    __CACHE_RESIZED_MAX_SIZE = 10000  # max size the resized image cache can reach before purge

    def __init__(self) -> None:
        """Initialise screen controller.

        Throws:
            Exception if the pygame screen does not yet exist
        """
        self.__screen: pygame.Surface = pygame.display.get_surface()

        self.__image_cache: dict[str, pygame.Surface] = dict()  # K = Relative image path, V = Loaded image in alpha form
        self.__image_cache_resized: dict[str, dict[tuple[int, int], pygame.Surface]] = defaultdict(
            dict
        )  # K = Relative image path, V = dictionary with key -> (width, height), value -> cached resized image
        self.__image_cache_resized_size: int = 0  # current resized cache size
        self.__rotate_cache: PygameScreenController.__ImageRotateCache = PygameScreenController.__ImageRotateCache()

        if self.__screen is None:
            raise Exception("The pygame screen does not yet exist.")

    def fill_screen_with_colour(self, rgb: tuple[int, int, int]) -> None:
        """Fill the screen with a solid colour.

        Args:
            rgb: The colour in form (R, G, B)
        """
        self.__screen.fill(rgb)

    def draw_asset(self, image_path: str, x: int, y: int, size: Optional[tuple[int, int]] = None, rotate: float = 0) -> pygame.Surface:
        """Draw an asset on coordinates (x,y) on the screen with the specified size and rotation.

        Has caching behaviour that attempts to cache as much as possible. If the respective caches get too large,
        the caches will be purged.

        Args:
            image_path: The path to the asset relative to root directory
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
        if image_path not in self.__image_cache:
            self.__image_cache[image_path] = pygame.image.load(abs_image_path).convert_alpha()

        ### TRANSFORMING & DRAWING
        image: pygame.Surface = self.__image_cache[image_path]

        # Resize image to requested width and height
        if size is not None:
            width, height = size[0], size[1]

            # purge cache on exceeding resized cache's max size
            if self.__image_cache_resized_size > PygameScreenController.__CACHE_RESIZED_MAX_SIZE:
                self.__image_cache_resized = defaultdict(dict)
                self.__image_cache_resized_size = 0

            # Resize image whilst using resized cache as much as possible
            requested_size: tuple[int, int] = (width, height)
            resized_cache_for_image: dict[tuple[int, int], pygame.Surface] = self.__image_cache_resized[image_path]

            if requested_size not in resized_cache_for_image:
                resized_cache_for_image[requested_size] = pygame.transform.smoothscale(image, (width, height))
                self.__image_cache_resized_size += 1
            image = resized_cache_for_image[requested_size]

        # Rotate image if rotation is value other than 0 degrees before drawing, whilst using cache as much as possible. Otherwise draw without rotation.
        if rotate != 0:
            cached_rotated_image: Optional[tuple[pygame.Surface, tuple[int, int]]] = self.__rotate_cache.get_cached_image(rotate, image_path)
            if cached_rotated_image is not None:
                image, (x_rotate_offset, y_rotate_offset) = cached_rotated_image
                self.__screen.blit(image, (x - x_rotate_offset, y - y_rotate_offset))
                return image
            else:
                # Cache miss, rotate the image and add to cache.

                before_rotate_rect = image.get_rect()
                before_rotate_width, before_rotate_height = before_rotate_rect.width, before_rotate_rect.height

                # Rotate image
                image = pygame.transform.rotate(image, rotate)

                # Draw rotated image, offsetting for padding of image size from rotation
                image_rect = image.get_rect()
                x_rotate_offset, y_rotate_offset = int((image_rect.width - before_rotate_width) / 2), int((image_rect.height - before_rotate_height) / 2)

                self.__rotate_cache.add_cached_image(rotate, image_path, (x_rotate_offset, y_rotate_offset), image)
                self.__screen.blit(image, (x - x_rotate_offset, y - y_rotate_offset))
        else:
            self.__screen.blit(image, (x, y))

        return image

    def draw_drawable_by_assets(self, drawables: Sequence[DrawableByAsset]) -> list[pygame.Surface]:
        """Draw assets according to the list of drawables's instructions.

        Args:
            drawables: The drawables that can be drawn using assets.

        Returns:
            The images that were drawn in order
        """
        images: list[pygame.Surface] = []

        for drawable in drawables:
            drawn_images = self.__draw_assets_from_instructions(drawable.get_draw_assets_instructions())
            for image in drawn_images:
                images.append(image)

        return images

    def draw_modular_clickable_sprites(self, clickables: Sequence[ModularClickableSprite]) -> list[tuple[pygame.Rect, ModularClickableSprite]]:
        """Draw sprites according to the list of clickable's drawing instructions, and return their hitboxes mapped
        to the associated object.

        Args:
            clickables: The clickables

        Returns:
            A list of tuples of form (rectangular hitbox, object associated with hitbox)
        """
        hitboxes_map: list[tuple[pygame.Rect, ModularClickableSprite]] = []
        for clickable in clickables:
            for instruction, clickable in clickable.get_draw_clickable_assets_instructions():
                drawn_img = self.__draw_assets_from_instructions([instruction])
                rect = drawn_img[0].get_rect()
                rect.x, rect.y = instruction.get_x_coord(), instruction.get_y_coord()
                hitboxes_map.append((rect, clickable))

        return hitboxes_map

    def __draw_assets_from_instructions(self, instructions: list[DrawAssetInstruction]) -> list[pygame.Surface]:
        """Draw assets in order based on instructions.

        Args:
            instructions: List containing drawing instructions

        Returns:
            The images that were drawn in order of instruction input
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

    # -------- CACHE CLASSES ----------------------------------------------------------------------------------------------------------
    class __ImageRotateCache:
        """Cache for storing rotated images.

        Author: Shen
        """

        __MAX_ASSET_PATH_CACHE_SIZE = 400  # Max number of entries for one asset path before purge

        def __init__(self, max_size: int = 10000):
            """
            Args:
                max_size: The max size the cache can reach before it is purged.
            """
            self.__max_size: int = max_size
            self.__size: int = 0
            self.__cache: dict[str, dict[float, tuple[pygame.Surface, tuple[int, int]]]] = defaultdict(
                dict
            )  # K = Relative image path, V = dict [rotation, (cached image, offsets for drawing rotated image)]

        def add_cached_image(self, rotation: float, asset_path: str, offset: tuple[int, int], rotated_image: pygame.Surface) -> None:
            """Add the cached image for the cache only if the image at the specified rotation has not been cached.
            Otherwise does nothing.

            Args:
                rotation: The rotation value for the image
                asset_path: The relative asset path for the image
                offset: The offset for coordinates (x, y) used to correct the rotation of the image
                rotated_image: The rotated image
            """
            rot_modded: float = round(rotation, 1) % 360
            cache_for_asset_path = self.__cache[asset_path]

            if rot_modded not in cache_for_asset_path:
                if len(cache_for_asset_path) > self.__MAX_ASSET_PATH_CACHE_SIZE:
                    # purge cache for asset path if size limit for asset path cache is exceeded
                    self.__cache[asset_path] = dict()
                if self.__size + 1 > self.__max_size:
                    # purge entire cache if max size exceeded
                    self.__cache = defaultdict(dict)
                    self.__size = 0

                self.__cache[asset_path][rot_modded] = (rotated_image, offset)
                self.__size += 1

        def get_cached_image(self, rotation: float, asset_path: str) -> Optional[tuple[pygame.Surface, tuple[int, int]]]:
            """Returns the cached image for the specified rotation and asset path if it exists.

            Args:
                rotation: The rotation value
                asset_path: The relative asset path for the image

            Returns
                Tuple in form (The cached image, The offset for coordinates (x, y) used to correct the rotation of the image) if it exists.
            """
            rot_modded: float = round(rotation, 1) % 360

            if asset_path in self.__cache:
                cache_for_asset_path: dict[float, tuple[pygame.Surface, tuple[int, int]]] = self.__cache[asset_path]
                if rot_modded in cache_for_asset_path:
                    image, offset = cache_for_asset_path[rot_modded]
                    return (image, offset)
            return None


# NOTES
# SEQUENCE Type
# What is Sequence type: Sequence means you cannot add to the list (it is read only). Equivalent to OOP <? extends Parent>
# https://stackoverflow.com/questions/53275080/mypy-creating-a-type-that-accepts-list-of-instances-of-subclasses
# https://stackoverflow.com/questions/5763750/why-we-cant-do-listparent-mylist-arraylistchild
