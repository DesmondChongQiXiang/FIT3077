from presets import *
from settings import *
from core.GameWorld import GameWorld
from game_events.turns.DefaultTurnManager import DefaultTurnManger
from game_events.turns.TurnManager import TurnManager
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.Dragon import Dragon
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.chit_cards.AnimalChitCard import AnimalChitCard
from game_objects.chit_cards.PirateChitCard import PirateChitCard
from game_objects.chit_cards.SwapChitCard import SwapChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.CaveTile import CaveTile
from game_objects.tiles.CaveTileVariant import CaveTileVariant
from game_objects.game_board.GameBoard import GameBoard
from game_objects.game_board.DefaultGameBoard import DefaultGameBoard
from game_objects.animals.Animal import Animal
from game_objects.characters.PlayableCharacterVariant import PlayableCharacterVariant
from utils.os_utils import *

import pygame
import random
import os

if __name__ == "__main__":
    # ----- PYGAME INIT -------------------------------------------------------------------------------------------------
    # initialise pygame
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
    tiles: list[Tile] = randomised_volcano_card_sequence(8)

    chit_cards: list[ChitCard] = []
    for i, animal in enumerate(Animal):
        for j in range(1, 3):
            chit_cards.append(AnimalChitCard(animal, j))
        chit_cards.append(PirateChitCard(1 if i % 2 == 0 else 2))
        chit_cards.append(PowerChitCard(1))
        chit_cards.append(SwapChitCard())

    playable_characters: list[PlayableCharacter] = [
        Dragon(PlayableCharacterVariant.BLUE, "Blue"),
        Dragon(PlayableCharacterVariant.GREEN, "Green"),
        Dragon(PlayableCharacterVariant.ORANGE, "Orange"),
        Dragon(PlayableCharacterVariant.PURPLE, "Purple"),
    ]
    starting_tiles: list[Tile] = [
        CaveTile(Animal.BABY_DRAGON, CaveTileVariant.BLUE, character=playable_characters[0]),
        CaveTile(Animal.SALAMANDER, CaveTileVariant.GREEN, character=playable_characters[1]),
        CaveTile(Animal.SPIDER, CaveTileVariant.ORANGE, character=playable_characters[2]),
        CaveTile(Animal.BAT, CaveTileVariant.PURPLE, character=playable_characters[3]),
    ]

    game_board: GameBoard = DefaultGameBoard(
        tiles,
        [(starting_tiles[0], tiles[3]), (starting_tiles[1], tiles[9]), (starting_tiles[2], tiles[15]), (starting_tiles[3], tiles[21])],
        chit_cards,
        playable_characters,
    )

    turn_manager: TurnManager = DefaultTurnManger(playable_characters, 0)

    # ----- GAME INSTANCE --------------------------------------------------------------------------------------------------
    world = GameWorld(playable_characters, game_board, turn_manager)
    world.run()
