from .GameBoard import GameBoard
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.tiles.Tile import Tile
from game_objects.chit_cards.ChitCard import ChitCard


class DefaultGameBoard(GameBoard):
    """Represents the default fiery dragons game board.

    Args:
        main_tile_sequence: The main tile sequence (excluding starting tiles) to use for the game board.
        starting_tiles: The starting tiles. In form: (starting tile, next tile)
    """
    def __init__(self, main_tile_sequence: list[Tile], starting_tiles: list[tuple[Tile, Tile]]):
        self.main_tile_sequence: list[Tile] = []
        self.starting_tiles: list[Tile] = []
        self.chit_cards: list[ChitCard] = []

        # Set the starting tiles
        dest_to_start_tile: dict[Tile, Tile] = dict()
        for tile_pair in starting_tiles:
            starting_tile, dest = tile_pair[0], tile_pair[1]
            self.starting_tiles.append(starting_tile)
            dest_to_start_tile[dest] = starting_tile

        # Create main tile sequence, taking in account starting tiles
        for tile in main_tile_sequence:
            if tile in dest_to_start_tile:
                self.main_tile_sequence.append(dest_to_start_tile[tile])
            self.main_tile_sequence.append(tile)
            
    def move_character_by_steps(self, character: PlayableCharacter, steps: int) -> None:
        pass

    def get_character_floor_tile(self, character: PlayableCharacter) -> Tile:
        return Tile()
    
    def flip_chit_card(self, character: PlayableCharacter, chit_card: ChitCard) -> None:
        pass

    # TODO: should turn this to work on iterables
    def add_chit_card(self, chit_card: ChitCard) -> None: 
        pass


