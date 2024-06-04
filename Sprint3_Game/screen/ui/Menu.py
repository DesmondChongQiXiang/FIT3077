from __future__ import annotations
from screen.PygameScreenController import PygameScreenController
from settings import FRAMES_PER_SECOND
from screen.ui.buttons.Button import Button
from screen.ui.buttons.Button import ButtonType
from screen.DrawProperties import DrawProperties
from screen.ModularClickableSprite import ModularClickableSprite
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawAssetInstruction import DrawAssetInstruction
from typing import Optional
from typing import cast
import pygame

class Menu():
    """A class represent menu that show before the game start

    Author: Desmond
    """
    def __init__(self, is_saving_file_exist:bool = False):
        self.__buttons:list[Button] = []
        self.__is_saving_file_exist = is_saving_file_exist

    def run(self):
        """Display the menu of the game

        Warning: Pygame and its display must be initialised through pygame.init() and pygame.display.set_mode() before running.
        """
        clock = pygame.time.Clock()
        self.__create_menu_button()
        #### GAME LOOP
        running = True
        while running:
            # Handle Drawing
            PygameScreenController.instance().fill_screen_with_colour((0,0,0))
            self.__display_title()
            clickable_hitboxes = PygameScreenController.instance().draw_modular_clickable_sprites(self.__buttons)
            # Handle Events
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:  # handle when X pressed on window
                        running = False
                        break

                    case pygame.MOUSEBUTTONDOWN:  # handle mouse click
                        self.__fire_onclick_for_clicked_hitboxes(clickable_hitboxes)
                        if not self.__is_player_click_disabled_button():
                            return
            
            self.__reinitialise_button()
                    

            # Update screen & Set FPS
            pygame.display.flip()  # update screen
            clock.tick(FRAMES_PER_SECOND)

        # Quit game once game loop broken
        pygame.quit()
    
    def __create_menu_button(self):
        """
        create buttons object of the menu
        """
        # create new_game button
        screen_size: tuple[int, int] = PygameScreenController.instance().get_screen_size()
        menu_button_size: tuple[int,int] = (screen_size[0]//2,screen_size[1]//5)
        new_game_button = Button(ButtonType.NEW_GAME,DrawProperties((screen_size[0]//2-menu_button_size[0]//2,screen_size[0]//2 - menu_button_size[0]//3),(menu_button_size[0],menu_button_size[1])))
        # create enabled continue button if the saving file exist. Otherwise, create a disabled continue button
        if self.__is_saving_file_exist:
            continue_button = Button(ButtonType.CONTINUE,DrawProperties((screen_size[0]//2-menu_button_size[0]//2,screen_size[0]//2 + menu_button_size[0]//3),(menu_button_size[0],menu_button_size[1])))
        else:
            continue_button = Button(ButtonType.CONTINUE,DrawProperties((screen_size[0]//2-menu_button_size[0]//2,screen_size[0]//2 + menu_button_size[0]//3),(menu_button_size[0],menu_button_size[1])),False)
        # storing the button object into buttons list
        self.__buttons.append(new_game_button)
        self.__buttons.append(continue_button)

    def __display_title(self):
        """
        display the title of the game
        """
        screen_size: tuple[int, int] = PygameScreenController.instance().get_screen_size()
        title_size: tuple[int,int] = (screen_size[0]//2,screen_size[1]//4)
        PygameScreenController.instance().draw_asset("assets/menu/title.png",screen_size[0]//2-title_size[0]//2,0,(title_size[0],title_size[1]))

    def __fire_onclick_for_clicked_hitboxes(self, hitboxes: list[tuple[pygame.Rect, ModularClickableSprite]]) -> None:
        """Fires on_click() for any objects containing hitboxes under the user's current cursor position.

        Args:
            hitboxes: A list of tuples of form (rectangular hitbox, object associated with hitbox)
        """
        for rect, clickable in hitboxes:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                clickable.on_click(None)
                return
    
    def __is_player_click_disabled_button(self):
        """
        check if the player's clicked button is a disabled button
        """
        for button in self.__buttons:
            if button.get_clicked() is True and button.get_enabled_clicked() is False:
                return True
        return False
    
    def __reinitialise_button(self):
        """
        revert back the state of the button after checking
        """
        for button in self.__buttons:
            button.set_clicked(False)