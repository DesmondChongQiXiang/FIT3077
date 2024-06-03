from screen.PygameScreenController import PygameScreenController
from settings import FRAMES_PER_SECOND
from screen.buttons.Button import Button
from screen.buttons.Button import ButtonType
from screen.DrawProperties import DrawProperties
from screen.ModularClickableSprite import ModularClickableSprite
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawAssetInstruction import DrawAssetInstruction
from typing import Optional
import pygame

class Menu():
    """A class represent menu that show before the game start

    Author: Desmond
    """
    def __init__(self):
        self.buttons:list[Button] = []

    def run(self,character):
        """Display the menu of the game

        Warning: Pygame and its display must be initialised through pygame.init() and pygame.display.set_mode() before running.
        """
        clock = pygame.time.Clock()
        running = True
        #### GAME LOOP
        while running:
            # Handle Drawing
            PygameScreenController.instance().fill_screen_with_colour((0,0,0))
            self.__create_menu_button()
            self.__display_title()
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
        """
        create buttons object of the menu
        """
        # create new_game and continue button
        new_game_button = Button(ButtonType.NEW_GAME,DrawProperties((250,280),(200,100)))
        continue_button = Button(ButtonType.CONTINUE,DrawProperties((250,480),(200,100)))
        # storing the button object into buttons list
        self.buttons.append(new_game_button)
        self.buttons.append(continue_button)

    def __display_title(self):
        """
        display the title of the game
        """
        PygameScreenController.instance().draw_asset("assets/menu/title.png",200,100,(300,100))

    def __fire_onclick_for_clicked_hitboxes(self, hitboxes: list[tuple[pygame.Rect, ModularClickableSprite]], player: PlayableCharacter) -> None:
        """Fires on_click() for any objects containing hitboxes under the user's current cursor position.

        Args:
            hitboxes: A list of tuples of form (rectangular hitbox, object associated with hitbox)
            player: The playable character of the current player
        """
        for rect, clickable in hitboxes:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                clickable.on_click(player)



