from core.GameWorld import GameWorld
from core.GameConfig import *
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.Dragon import Dragon
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.chit_cards.AnimalChitCard import AnimalChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.CaveTile import CaveTile
from game_objects.tiles.NormalTile import NormalTile
from game_objects.game_board.GameBoard import GameBoard
from game_objects.game_board.DefaultGameBoard import DefaultGameBoard
from game_objects.animals.Animal import Animal

import pygame

if __name__ == "__main__":
    # ============= PYGAME INIT ==============
    # Initialise pygame, and pygame screen
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fiery Dragons: Shen Jiang")

    # ============= GAME CONFIG ==============
    playable_characters: list[PlayableCharacter] = [Dragon(), Dragon(), Dragon(), Dragon()]
    tiles: list[Tile] = []
    chit_cards: list[ChitCard] = []
    starting_tiles: list[Tile] = [
        CaveTile(Animal.BABY_DRAGON, character=playable_characters[0]),
        CaveTile(Animal.SALAMANDER, character=playable_characters[1]),
        CaveTile(Animal.SPIDER, character=playable_characters[2]),
        CaveTile(Animal.BAT, character=playable_characters[3]),
    ]

    for _ in range(24):
        tiles.append(NormalTile(Animal.BAT))
    for _ in range(16):
        chit_cards.append(AnimalChitCard(Animal.SPIDER, 3))

    game_board: GameBoard = DefaultGameBoard(
        tiles, [(starting_tiles[0], tiles[3]), (starting_tiles[1], tiles[9]), (starting_tiles[2], tiles[15]), (starting_tiles[3], tiles[21])], chit_cards
    )

    # ============ GAME INSTANCE =============
    world = GameWorld(playable_characters, chit_cards, game_board)
