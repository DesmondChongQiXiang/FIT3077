from core.GameWorld import GameWorld
from core.GameConfig import *
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.Dragon import Dragon
from game_objects.chit_cards.ChitCard import ChitCard
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

    # ============= GAME CONFIG ==============
    playable_characters: list[PlayableCharacter] = [Dragon(), Dragon(), Dragon(), Dragon()]
    tiles: list[Tile] = []
    starting_tiles: list[Tile] = [CaveTile(Animal.BABY_DRAGON)]
    chit_cards: list[ChitCard] = generate_chit_cards_for_default_game_board()

    for _ in range(24):
        tiles.append(NormalTile(Animal.BABY_DRAGON))
    
    game_board: GameBoard = DefaultGameBoard(tiles, [(starting_tiles[0], tiles[0])])


    # ============ GAME INSTANCE =============
    world = GameWorld(playable_characters, chit_cards, game_board)
