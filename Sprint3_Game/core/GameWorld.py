from __future__ import annotations
from typing import cast
from settings import FRAMES_PER_SECOND, SCREEN_BACKGROUND_COLOUR
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.game_board.GameBoard import GameBoard
from screen.ModularClickableSprite import ModularClickableSprite
from screen.PygameScreenController import PygameScreenController
from game_concepts.events.WinEventListener import WinEventListener
from game_concepts.events.WinEventPublisher import WinEventPublisher
from game_concepts.turns.TurnManager import TurnManager
from metaclasses.SingletonMeta import SingletonMeta
from threading import Timer

import pygame


class GameWorld(WinEventListener, metaclass=SingletonMeta):
    """A singleton. This class creates and manages the running of the game instance. It also manages the interface between
    player interactions and the game.

    Author: Shen, Rohan
    """

    __GAME_END_CLOSE_DELAY: float = 5.0  # seconds after which to close the game after the game ends (i.e when a player wins)

    def __init__(self, game_board: GameBoard, turn_manager: TurnManager):
        """Creates the game world for running the game.

        Args:
            game_board: The game board
            turn_manager: The manager for managing turns
        """
        self.__game_board: GameBoard = game_board
        self.__turn_manager: TurnManager = turn_manager
        self.__should_game_run: bool = True
        self.__mouse_click_enabled = True

        WinEventPublisher.instance().subscribe(self)

    # ----------- Class methods ----------------------------------------------------------------------------------------------------------------
    def run(self) -> None:
        """Initialises the game on the active pygame screen and runs the main game loop.

        Warning: Pygame and its display must be initialised through pygame.init() and pygame.display.set_mode() before running.
        """
        clock = pygame.time.Clock()
        #### GAME LOOP
        while self.__should_game_run:
            # Handle Drawing
            PygameScreenController.instance().fill_screen_with_colour(SCREEN_BACKGROUND_COLOUR)

            PygameScreenController.instance().draw_drawable_by_assets([self.__game_board])
            clickable_hitboxes = PygameScreenController.instance().draw_modular_clickable_sprites(self.__game_board.get_all_clickable_sprites())

            # Handle Events
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:  # handle when X pressed on window
                        self.__should_game_run = False
                        break

                    case pygame.MOUSEBUTTONDOWN:  # handle mouse click
                        if self.__mouse_click_enabled:
                            self.__fire_onclick_for_clicked_hitboxes(clickable_hitboxes, self.__turn_manager.get_currently_playing_character())

            # Handle Player Turns
            if self.__turn_manager.tick():
                self.__game_board.on_player_turn_end()

            # Update screen & Set FPS
            pygame.display.flip()  # update screen
            clock.tick(FRAMES_PER_SECOND)

        # Quit game once game loop broken
        pygame.quit()

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

    def disable_mouse_clicks(self) -> None:
        """Disable user interaction with the game by mouse clicks."""
        self.__mouse_click_enabled = False

    def enable_mouse_clicks(self) -> None:
        """Enable user interaction with the game by mouse clicks."""
        self.__mouse_click_enabled = True

    def stop_game(self) -> None:
        """Stops the game and causes the game to exit."""
        self.__should_game_run = False

    # --------- WinEventListener interface -------------------------------------------------------------------------------------------------
    def on_player_win(self, character: PlayableCharacter) -> None:
        """On a player win, print to the console the name of the character who won the game, prevent further interaction and quit the
        game after a delay specified by GameWorld.__GAME_END_CLOSE_DELAY.

        Args:
            character: The character
        """
        # print who won the game
        print(f"Player {character.name()} has won the game!")

        self.disable_mouse_clicks()

        # stop game after delay
        end_game_timer: Timer = Timer(GameWorld.__GAME_END_CLOSE_DELAY, self.stop_game)
        end_game_timer.start()

    # -------- Static methods ---------------------------------------------------------------------------------------------------------------
    @staticmethod
    def instance() -> GameWorld:
        """Get the shared instance of this controller.

        Returns:
            The singleton instance

        Raises:
            Exception if the instance did not exist before access
        """
        existing_instance = cast(GameWorld, SingletonMeta._get_existing_instance(GameWorld))  # type guaranteed to be GameWorld
        if existing_instance is not None:
            return existing_instance
        raise Exception("GameWorld instance accessed before instantiation.")
