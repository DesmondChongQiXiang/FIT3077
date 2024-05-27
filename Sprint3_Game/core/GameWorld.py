from __future__ import annotations
from typing import cast
from settings import FRAMES_PER_SECOND, SCREEN_BACKGROUND_COLOUR
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.game_board.GameBoard import GameBoard
from screen.ModularClickableSprite import ModularClickableSprite
from screen.PygameScreenController import PygameScreenController
from game_events.WinEventListener import WinEventListener
from game_events.WinEventPublisher import WinEventPublisher
from metaclasses.SingletonMeta import SingletonMeta
from threading import Timer

import pygame


class GameWorld(WinEventListener, metaclass=SingletonMeta):
    """A singleton. This class creates and manages a game instance. It provides the interface between it and the players.

    Author: Shen, Rohan
    """

    __GAME_END_CLOSE_DELAY: float = 5.0  # seconds after which to close the game after the game ends (i.e when a player wins)

    def __init__(self, playable_characters: list[PlayableCharacter], game_board: GameBoard):
        """Configures the game world, with the first character in the list of playable characters being the starting player.

        Args:
            playable_characters: The list of playable characters to initialise the world (game) with
            game_board: The game board

        Throws:
            Exception when the number of playable characters is less than 2.
        """
        if len(playable_characters) < 2:
            raise ValueError("Number of playable characters must be at least 2.")

        self.__playable_characters: list[PlayableCharacter] = playable_characters
        self.__game_board: GameBoard = game_board
        self.__current_player = playable_characters[0]
        self.__current_player_i = 0  # for turn processing purposes only
        self.__should_game_run: bool = True
        self.__mouse_click_enabled = True

        self.__current_player.set_is_currently_playing(True)
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
                            self.__fire_onclick_for_clicked_hitboxes(clickable_hitboxes, self.__current_player)

            # Handle Player Turns
            if self.__process_current_player_turn():
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

    def __process_current_player_turn(self) -> bool:
        """Ends the current player's turn and transitions turn to the next player if their turn should end. Otherwise does
        nothing.

        Returns:
            Whether the current player's turn ended.
        """
        if not self.__current_player.should_continue_turn():
            self.__current_player.set_is_currently_playing(False)
            self.__current_player.set_should_continue_turn(True)  # reset for the playable character's next turn

            if self.__current_player_i + 1 > len(self.__playable_characters) - 1:
                # if the current player was the last player, loop around to the starting player
                self.__current_player = self.__playable_characters[0]
                self.__current_player_i = 0
            else:
                # otherwise turn should go to next player
                self.__current_player = self.__playable_characters[self.__current_player_i + 1]
                self.__current_player_i += 1

            self.__current_player.set_is_currently_playing(True)
            return True

        return False

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
        for player_char in self.__playable_characters:
            if player_char == character:
                print(f"Player {player_char.name()} has won the game!")

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
