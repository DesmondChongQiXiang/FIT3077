from core.GameWorld import GameWorld
from core.GameConfig import *
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.Dragon import Dragon
from game_objects.animals.Animals import Animal
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.chit_cards.AnimalChitCard import AnimalChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.CaveTile import CaveTile
from game_objects.tiles.NormalTile import NormalTile
from game_objects.game_board.GameBoard import GameBoard
from game_objects.game_board.DefaultGameBoard import DefaultGameBoard

import pygame
import random


# METHODS FOR GAME CONFIG - Move into game config
def generate_chit_cards_for_default_game_board() -> list[ChitCard]:
    """Generate chit cards for the default game board in its safe area.

    Returns:
        A list of chit cards for the game board
    """
    ##### CONFIG
    RAND_FACTOR: int = 45                                   # random factor in pixels
    CHIT_CARD_DIMENSIONS: tuple[int, int] = (85, 85)        # chit card dimensions (width, height) in px

    ##### GENERATING 
    safe_area = DefaultGameBoard.get_chit_card_safe_area()
    x0, y0, x1, y1 = safe_area[0][0], safe_area[0][1], safe_area[1][0], safe_area[1][1]
    chit_card_w, chit_card_h = CHIT_CARD_DIMENSIONS
    next_x, next_y = 0, 0     # default coords = (0, 0) to draw at if can't generate
    chit_cards: list[ChitCard] = []

    # generate chit tiles randomly in manner that doesn't clip board tiles
    x_random_range, y_random_range = chit_card_w + RAND_FACTOR, chit_card_h + RAND_FACTOR

    for cur_y in range(y0, y1 - y_random_range, y_random_range):
        for cur_x in range(x0, x1 - x_random_range, x_random_range):
            next_x, next_y = random.randint(cur_x, cur_x + RAND_FACTOR), random.randint(cur_y, cur_y + RAND_FACTOR)
            chit_cards.append(AnimalChitCard(Animal.SPIDER, 3, (next_x, next_y), CHIT_CARD_DIMENSIONS))

    return chit_cards


# MAIN
if __name__ == "__main__":
    # ============= PYGAME INIT ==============
    # Initialise pygame, and pygame screen
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # ============= GAME CONFIG ==============
    playable_characters: list[PlayableCharacter] = [Dragon(), Dragon(), Dragon(), Dragon()]
    tiles: list[Tile] = [NormalTile(), NormalTile(), NormalTile(), NormalTile(), NormalTile(), NormalTile(), NormalTile(), NormalTile()]
    chit_cards: list[ChitCard] = generate_chit_cards_for_default_game_board()
    starting_tiles: list[Tile] = [CaveTile()]
    game_board: GameBoard = DefaultGameBoard(tiles, [(starting_tiles[0], tiles[0])])

    # ============ GAME INSTANCE =============
    world = GameWorld(playable_characters, chit_cards, game_board)
