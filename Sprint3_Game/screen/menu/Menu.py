from screen.PygameScreenController import PygameScreenController
from settings import FRAMES_PER_SECOND
from screen.menu.MenuButton import MenuButton
from screen.DrawProperties import DrawProperties
from screen.ModularClickableSprite import ModularClickableSprite
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawAssetInstruction import DrawAssetInstruction
from typing import Optional
import pygame

class Menu(ModularClickableSprite):
    def __init__(self, draw_properties: Optional[DrawProperties] = None):
        self.buttons = []

    def run(self,character):
        clock = pygame.time.Clock()
        running = True
        #### GAME LOOP
        while running:
            # Handle Drawing
            PygameScreenController.instance().fill_screen_with_colour((0,0,0))
            self.__create_menu_button()
            clickable_hitboxes = PygameScreenController.instance().draw_modular_clickable_sprites(self.buttons)
            # Handle Events
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:  # handle when X pressed on window
                        running = False
                        break

                    case pygame.MOUSEBUTTONDOWN:  # handle mouse click
                        self.__fire_onclick_for_clicked_hitboxes(clickable_hitboxes, character)
                        return

            # Update screen & Set FPS
            pygame.display.flip()  # update screen
            clock.tick(FRAMES_PER_SECOND)

        # Quit game once game loop broken
        pygame.quit()
    
    def __create_menu_button(self):
        start_button = MenuButton("start")
        start_button.set_draw_properties(DrawProperties((350,180),(200,100)))
        continue_button = MenuButton("continue")
        continue_button.set_draw_properties(DrawProperties((350,380),(200,100)))
        self.buttons.append(start_button)
        self.buttons.append(continue_button)

    def __fire_onclick_for_clicked_hitboxes(self, hitboxes: list[tuple[pygame.Rect, ModularClickableSprite]], player: PlayableCharacter) -> None:
        for rect, clickable in hitboxes:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                clickable.on_click(player)
    
    def set_draw_properties(self, draw_properties: DrawProperties) -> None:
        self._draw_properties = draw_properties

    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        if self._draw_properties is None:
            raise Exception("Tried drawing, but the draw properties (properties required for drawing) weren't set.")
        return self._on_draw_request(self._draw_properties)

    def _on_draw_request(self, draw_properties: DrawProperties) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        asset_path: str = "assets/menu"
        coord_x, coord_y = draw_properties.get_coordinates()

        return [
            (
                DrawAssetInstruction(
                    f"{asset_path}/menu_button.png",
                    x=coord_x,
                    y=coord_y,
                    size=draw_properties.get_size(),
                ),
                self,
            )
        ]

    def on_click(self, character: PlayableCharacter) -> None:
        # guard statements
        self.run(character)



