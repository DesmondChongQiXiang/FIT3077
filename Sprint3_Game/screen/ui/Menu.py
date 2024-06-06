from __future__ import annotations
from screen.PygameScreenController import PygameScreenController
from settings import FRAMES_PER_SECOND
from screen.ui.buttons.Button import Button
from screen.DrawProperties import DrawProperties
from screen.ModularClickableSprite import ModularClickableSprite
from commands.saving.SaveCommand import SaveCommand
from codec.saves.SaveCodec import SaveCodec
from screen.ui.buttons.ButtonType import ButtonType
from typing import cast, Optional, Any
import pygame


class Menu:
    """A class represent menu that show before the game start

    Author: Desmond, Shen
    """

    def __init__(self, show_continue_button: bool, save_codec: Optional[SaveCodec[dict[str, Any]]]) -> None:
        """Constructor.

        Args:
            show_continue_button: Whether the continue button is shown
            save_codec: The save codec to use for a continue button. Not optional if continue show_continue_button is True.

        Raises:
            Exception if save codec was not set when the continue button should be shown.
        """
        self.__save_codec: Optional[SaveCodec[dict[str, Any]]] = save_codec
        self.__clickables: list[ModularClickableSprite] = []
        self.__new_game_button: Optional[ModularClickableSprite] = None
        self.__continue_button: Optional[ModularClickableSprite] = None
        self.__show_continue_button = show_continue_button

        if self.__show_continue_button and self.__save_codec is None:
            raise Exception("Save codec must be set when show continue button is shown.")

    def run(self) -> ButtonType:  # type: ignore
        """Display the menu of the game.

        Warning: Pygame and its display must be initialised through pygame.init() and pygame.display.set_mode() before running.

        Returns:
            The button type clicked
        """
        clock: pygame.time.Clock = pygame.time.Clock()
        self.__create_menu_button()

        #### GAME LOOP
        running = True
        while running:

            # Handle Drawing
            PygameScreenController.instance().fill_screen_with_colour((0, 0, 0))
            self.__display_title()
            clickable_hitboxes = PygameScreenController.instance().draw_modular_clickable_sprites(self.__clickables)

            # Handle Events
            for event in pygame.event.get():
                match event.type:
                    # handle when X pressed on window
                    case pygame.QUIT:
                        running = False
                        break

                    # handle mouse click
                    # >>>>> Kinda hacky (evidence: switch cases). If more time, would've created new FieryDragon class to manage GameWorld instances, menu, etc. And load, new game commands passed to buttons would act through the FieryDragon class. GameWorld would also no longer be singleton. - Shen
                    case pygame.MOUSEBUTTONDOWN:
                        clickedSprite: Optional[ModularClickableSprite] = self.__fire_onclick_for_clicked_hitboxes(clickable_hitboxes)

                        if clickedSprite is not None:
                            if clickedSprite == self.__new_game_button:
                                return ButtonType.NEW_GAME
                            return ButtonType.CONTINUE

            # Update screen & Set FPS
            pygame.display.flip()  # update screen
            clock.tick(FRAMES_PER_SECOND)

        # Quit game if quitting by pygame.QUIT
        pygame.quit()

    def __create_menu_button(self) -> None:
        """
        create buttons object of the menu
        """
        screen_size: tuple[int, int] = PygameScreenController.instance().get_screen_size()
        menu_button_size: tuple[int, int] = (screen_size[0] // 2, screen_size[1] // 5)

        # creating new game button
        new_game_button: Button = Button(
            "assets/menu/new_game.png",
            None,
            draw_properties=DrawProperties(
                (screen_size[0] // 2 - menu_button_size[0] // 2, screen_size[0] // 2 - menu_button_size[0] // 3), (menu_button_size[0], menu_button_size[1])
            ),
        )
        self.__new_game_button = new_game_button
        self.__clickables.append(new_game_button)

        # create continue button
        if self.__show_continue_button:
            if self.__save_codec is None:
                raise Exception("Save codec was none when trying to add continue button.")

            continue_button: Button = Button(
                "assets/menu/continue.png",
                None,
                DrawProperties(
                    (screen_size[0] // 2 - menu_button_size[0] // 2, screen_size[0] // 2 + menu_button_size[0] // 3), (menu_button_size[0], menu_button_size[1])
                ),
            )

            self.__continue_button = continue_button
            self.__clickables.append(continue_button)

    def __display_title(self) -> None:
        """
        display the title of the game
        """
        screen_size: tuple[int, int] = PygameScreenController.instance().get_screen_size()
        title_size: tuple[int, int] = (screen_size[0] // 2, screen_size[1] // 4)
        PygameScreenController.instance().draw_asset("assets/menu/title.png", screen_size[0] // 2 - title_size[0] // 2, 0, (title_size[0], title_size[1]))

    def __fire_onclick_for_clicked_hitboxes(self, hitboxes: list[tuple[pygame.Rect, ModularClickableSprite]]) -> Optional[ModularClickableSprite]:
        """Fires on_click() for any objects containing hitboxes under the user's current cursor position.

        Args:
            hitboxes: A list of tuples of form (rectangular hitbox, object associated with hitbox)

        Returns:
            The sprite clicked if any
        """
        for rect, clickable in hitboxes:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                clickable.on_click(None)
                return clickable
        return None
