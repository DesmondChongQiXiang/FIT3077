"""Entry point for the execution of the game."""

from settings import *
from utils.os_utils import *
from game_configurations.GameConfiguration import GameConfiguration
from game_configurations.DefaultGameConfiguration import DefaultGameConfiguration
from codec.saves.SaveCodec import SaveCodec
from codec.saves.JSONSaveCodec import JSONSaveCodec

import pygame
import os

if __name__ == "__main__":
    # ----- CONFIGURATION VARIABLES --------------------------------------------------------------------------------------
    # GAME_CONFIG
    # The game configuration the game is to use
    GAME_CONFIG: GameConfiguration = DefaultGameConfiguration()

    # SAVE_CODEC
    # The codec to use for encoding/decoding save files
    SAVE_CODEC: SaveCodec = JSONSaveCodec("saves")

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

    # ----- GAME CONFIG --------------------------------------------------------------------------------------------------
    SAVE_CODEC._JSONSaveCodec__json_dict["test"] = 5
    SAVE_CODEC.save()

    # ----- GAME INSTANCE ------------------------------------------------------------------------------------------
    GAME_CONFIG.generate_game_world().run()
