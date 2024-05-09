from __future__ import annotations
from typing import cast
from core.GameConfig import FRAMES_PER_SECOND, SCREEN_BACKGROUND_COLOUR
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.game_board.GameBoard import GameBoard
from game_objects.tiles.Tile import Tile
from screen.ModularClickableSprite import ModularClickableSprite
from screen.PygameScreenController import PygameScreenController
from metaclasses.SingletonMeta import SingletonMeta

import pygame


class GameWorld(metaclass=SingletonMeta):
    """A singleton. This class creates and manages a game instance. It provides the interface between it and the players.

    Author: Shen
    """

    def __init__(self, playable_characters: list[PlayableCharacter], game_board: GameBoard):
        """Configures the game world, with the first character in the list of playable characters being the starting player.

        Args:
            playable_charcters: The list of playable characters to initialise the world (game) with
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
        self.__mouse_click_enabled = True

        self.__current_player.set_is_currently_playing(True)

    def run(self) -> None:
        """Initialises the game on the active pygame screen and runs the main game loop.

        Warning: Pygame and its display must be initialised through pygame.init() and pygame.display.set_mode() before running.
        """
        clock = pygame.time.Clock()

        # GAME LOOP
        while True:
            # Handle Drawing
            pygame.display.get_surface().fill(SCREEN_BACKGROUND_COLOUR)

            PygameScreenController.instance().draw_assets_from_instructions(self.__game_board.get_draw_assets_instructions())
            chit_card_hitboxes = PygameScreenController.instance().draw_clickable_assets_from_instructions(self.__game_board.get_draw_clickable_assets_instructions())

            # Handle Events
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:  # Handle closing of game
                        pygame.quit()
                        return

                    case pygame.MOUSEBUTTONDOWN:  # handle mouse click
                        if self.__mouse_click_enabled:
                            self.__fire_onclick_for_clicked_hitboxes(chit_card_hitboxes, self.__current_player)

            # Handle Player Turns
            if self.__process_current_player_turn():
                self.__game_board.on_player_turn_end()

            # Update screen & Set FPS
            pygame.display.flip()  # update screen
            clock.tick(FRAMES_PER_SECOND)

    def __fire_onclick_for_clicked_hitboxes(self, hitboxes: list[tuple[pygame.Rect, ModularClickableSprite]], player: PlayableCharacter) -> None:
        """Fires on_click() for any objects containing hitboxes under the user's current cursor position.

        Args:
            hitboxes: A list of tuples of form (rectangular hitbox, object associated with hitbox)
            player: The playable character of the current player
        """
        players_tile: Tile = self.__game_board.get_character_floor_tile(player)

        for rect, clickable in hitboxes:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                clickable.on_click(player, players_tile)

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

    @staticmethod
    def instance() -> GameWorld:
        """Get the shared instance of this controller.

        Returns:
            The singleton instance

        Raises:
            Exception if the instance did not exist before access
        """
        existing_instance = cast(GameWorld, GameWorld._get_existing_instance(GameWorld))  # type guranteed to be GameWorld
        if existing_instance is not None:
            return existing_instance
        raise Exception("GameWorld instance accessed before instantiation.")
