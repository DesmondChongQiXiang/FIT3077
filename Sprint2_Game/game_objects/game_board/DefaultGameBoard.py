from .GameBoard import GameBoard
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.tiles.Tile import Tile
from game_objects.chit_cards.ChitCard import ChitCard
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawAssetInstruction import DrawAssetInstruction
from core.singletons import PygameScreenController_instance


class DefaultGameBoard(GameBoard, DrawableByAsset):
    """Represents the default fiery dragons game board. Cells are drawn in a square, using the width of the screen
    as reference.

    Author: Shen
    """

    DIMENSION_CELL_COUNT: int = 7  # Cell count for each dimension

    def __init__(self, main_tile_sequence: list[Tile], starting_tiles: list[tuple[Tile, Tile]]):
        """
        Args:
            main_tile_sequence: The main tile sequence (excluding starting tiles) to use for the game board.
            starting_tiles: The starting tiles. In form: (starting tile, next tile)
        """
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

    #### GameBoard interface
    def move_character_by_steps(self, character: PlayableCharacter, steps: int) -> None:
        pass

    def get_character_floor_tile(self, character: PlayableCharacter) -> Tile:
        return Tile()

    def flip_chit_card(self, character: PlayableCharacter, chit_card: ChitCard) -> None:
        pass

    # TODO: should turn this to work on iterables
    def add_chit_card(self, chit_card: ChitCard) -> None:
        pass

    #### DrawableByAsset interface
    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """
        Instructions to draw the game board as a square of square cells, with the number of cells on each dimension equal to 
        DefaultGameBoard.DIMENSION_CELL_COUNT.

        Returns:
            The list of drawing instructions

        Author: Shen
        """
        cell_asset_path = "assets/game_board/game_board_tile.png"
        width, _ = PygameScreenController_instance().get_screen_size()
        square_size: int = width // DefaultGameBoard.DIMENSION_CELL_COUNT
        draw_instructions: list[DrawAssetInstruction] = []

        for row in range(DefaultGameBoard.DIMENSION_CELL_COUNT):
            if row == 0 or row == DefaultGameBoard.DIMENSION_CELL_COUNT - 1:
                for col in range(DefaultGameBoard.DIMENSION_CELL_COUNT):
                    draw_instructions.append(DrawAssetInstruction(cell_asset_path, x=square_size * col, y=square_size * row, size=(square_size, square_size)))
            else:
                draw_instructions.append(DrawAssetInstruction(cell_asset_path, x=0, y=square_size * row, size=(square_size, square_size)))
                draw_instructions.append(DrawAssetInstruction(cell_asset_path, x=width - square_size, y=square_size * row, size=(square_size, square_size)))

        return draw_instructions
