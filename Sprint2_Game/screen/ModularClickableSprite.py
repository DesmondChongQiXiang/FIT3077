from __future__ import annotations
from abc import ABC, abstractmethod
from definitions import ROOT_PATH
from utils.pygame_utils import scale_and_rotate_image
from screen.DrawAssetInstruction import DrawAssetInstruction

import pygame


class ModularClickableSprite(ABC):
    """Allows a class to be represented by assets (images) that can be clicked on.

    Author: Shen
    """

    def __init__(self):
        self.__rect_to_objects: dict[pygame.rect.Rect, ModularClickableSprite] = {}  # stores click hitboxes for drawable objects

        self.update_click_hitboxes()

    @abstractmethod
    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Get the instructions to draw the clickable asset.

        Returns:
            A list containing tuples in the form of (drawing instructions, associated clickable object)
        """
        ...

    @abstractmethod
    def on_click(self) -> None:
        """When the sprite is clicked on, do something."""
        ...

    def update_click_hitboxes(self) -> None:
        """Update the click hitboxes for drawable objects based on the instructions from get_draw_clickable_assets_instructions()
        
        Author: Shen
        """
        for instruction, clickable in self.get_draw_clickable_assets_instructions():
            image = scale_and_rotate_image(
                pygame.image.load(f"{ROOT_PATH}/{instruction.get_asset_path()}"), instruction.get_width(), instruction.get_height(), instruction.get_rotation()
            )
            self.__rect_to_objects[image.get_rect()] = clickable
