"""Entry point for the execution of the game."""

from settings import *
from definitions import *
from utils.os_utils import *
from game_configurations.GameConfiguration import GameConfiguration
from game_configurations.ArcadeGameConfiguration import ArcadeGameConfiguration
from core.GameWorld import GameWorld
from codec.saves.SaveCodec import SaveCodec
from codec.saves.JSONSaveCodec import JSONSaveCodec
from screen.ui.Menu import Menu
from screen.ui.buttons.ButtonType import ButtonType

import pygame
import os

if __name__ == "__main__":
    # ----- CONFIGURATION VARIABLES --------------------------------------------------------------------------------------
    # SAVE_DIRECTORY
    # The save directory relative to the root project to save a save file into
    SAVE_DIRECTORY: str = "saves"

    # SAVE_CODEC
    # The codec to use for encoding/decoding save files
    SAVE_CODEC: SaveCodec = JSONSaveCodec(SAVE_DIRECTORY)

    # GAME_CONFIGURATION
    # The game configuration the game is to use
    GAME_CONFIGURATION: GameConfiguration = ArcadeGameConfiguration(SAVE_CODEC)

    # ----- PYGAME INIT -------------------------------------------------------------------------------------------------
    # Initialise pygame
    pygame.init()
    pygame.display.set_caption("Fiery Dragons")

    # Initialise pygame screen
    if os.name == "nt":
        # For Windows: Automatically ensure screen size is within safe area for monitor
        user_screen_w, user_screen_h = nt_safe_size_for_program_window(ScreenDimension.WIDTH), nt_safe_size_for_program_window(ScreenDimension.HEIGHT)
        smallest_window_dimension: int = min(user_screen_h, user_screen_w)
        game_screen_size: int = smallest_window_dimension if REQUESTED_SCREEN_SIZE > smallest_window_dimension else REQUESTED_SCREEN_SIZE

        pygame.display.set_mode((game_screen_size, game_screen_size))
    else:
        # For all other OS: Use requested screen size
        pygame.display.set_mode((REQUESTED_SCREEN_SIZE, REQUESTED_SCREEN_SIZE))

    # ----- GAME INSTANCE ------------------------------------------------------------------------------------------
    # MENU
    save_file_exists: bool = os.path.isfile(f"{ROOT_PATH}/{SAVE_DIRECTORY}/{JSONSaveCodec.SAVE_FILE_NAME}.json")

    menu: Menu = Menu(save_file_exists, SAVE_CODEC if save_file_exists else None)
    buttonTypePressed: ButtonType = menu.run()

    # GAME WORLD
    # Generate game world based on whether the player chooses to continue or create a new game
    game_world: GameWorld

    match buttonTypePressed:
        case ButtonType.CONTINUE:
            load_data = SAVE_CODEC.load()
            game_world = GAME_CONFIGURATION.create_game_world_from_json_save(load_data)

        case _:
            game_world = GAME_CONFIGURATION.generate_game_world()

    game_world.run()
