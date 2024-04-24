from core.GameWorld import GameWorld
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.Dragon import Dragon
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.chit_cards.PirateChitCard import PirateChitCard
from game_objects.chit_cards.AnimalChitCard import AnimalChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.CaveTile import CaveTile
from game_objects.tiles.NormalTile import NormalTile
from game_objects.game_board.GameBoard import GameBoard
from game_objects.game_board.DefaultGameBoard import DefaultGameBoard


if __name__ == "__main__":
    # ============= GAME CONFIG ==============
    playable_characters: list[PlayableCharacter] = [Dragon(), Dragon(), Dragon(), Dragon()]
    chit_cards: list[ChitCard] = [PirateChitCard(), AnimalChitCard()]
    tiles: list[Tile] = [
        NormalTile(), NormalTile(), NormalTile(), NormalTile(), NormalTile(), NormalTile(), NormalTile(), NormalTile()
    ]
    starting_tiles: list[Tile] = [CaveTile()]

    game_board: GameBoard = DefaultGameBoard(tiles, [(starting_tiles[0], tiles[0])])

    # ============ GAME INSTANCE =============
    world = GameWorld(playable_characters, chit_cards, game_board)
