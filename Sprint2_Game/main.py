from presets import *
from core.GameWorld import GameWorld
from core.GameConfig import *
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.Dragon import Dragon
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.CaveTile import CaveTile
from game_objects.game_board.GameBoard import GameBoard
from game_objects.game_board.DefaultGameBoard import DefaultGameBoard
from game_objects.animals.Animal import Animal
from game_objects.characters.PlayableCharacterVariant import PlayableCharacterVariant

import pygame
import random

if __name__ == "__main__":
    # ============= PYGAME INIT ==============
    # Initialise pygame, and pygame screen
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fiery Dragons")

    # ============= GAME CONFIG ==============
    tiles: list[Tile] = normal_tiles_in_animal_sequence(24)
    chit_cards: list[ChitCard] = animal_chit_cards_in_animal_sequence(16)
    playable_characters: list[PlayableCharacter] = [
        Dragon(PlayableCharacterVariant.BLUE, "Ian"),
        Dragon(PlayableCharacterVariant.GREEN, "Rohan"),
        Dragon(PlayableCharacterVariant.ORANGE, "Shen"),
        Dragon(PlayableCharacterVariant.PURPLE, "Desmond"),
    ]
    starting_tiles: list[Tile] = [
        CaveTile(Animal.BABY_DRAGON, character=playable_characters[0]),
        CaveTile(Animal.SALAMANDER, character=playable_characters[1]),
        CaveTile(Animal.SPIDER, character=playable_characters[2]),
        CaveTile(Animal.BAT, character=playable_characters[3]),
    ]

    random.shuffle(chit_cards)
    random.shuffle(tiles)

    game_board: GameBoard = DefaultGameBoard(
        tiles,
        [(starting_tiles[0], tiles[3]), (starting_tiles[1], tiles[9]), (starting_tiles[2], tiles[15]), (starting_tiles[3], tiles[21])],
        chit_cards,
        playable_characters,
    )

    # ============ GAME INSTANCE =============
    world = GameWorld(playable_characters, game_board)
    world.run()
