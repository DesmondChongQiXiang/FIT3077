from .GameBoard import GameBoard
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.tiles.Tile import Tile
from game_objects.tiles.NormalTile import NormalTile
from game_objects.tiles.TileDrawData import TileDrawData
from game_objects.chit_cards.ChitCard import ChitCard
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawAssetInstruction import DrawAssetInstruction
from core.singletons import PygameScreenController_instance


class DefaultGameBoard(GameBoard, DrawableByAsset):
    """Represents the default fiery dragons game board. Cells are drawn in a square, using the width of the screen
    as reference.

    Author: Shen
    """

    ### CONFIG
    DIMENSION_CELL_COUNT: int = 7  # Cell count for each dimension

    def __init__(self, main_tile_sequence: list[Tile], starting_tiles: list[tuple[Tile, Tile]]):
        """
        Args:
            main_tile_sequence: The main tile sequence (excluding starting tiles) to use for the game board. Must have (DIMENSION_CELL_COUNT * 4) - 4 tiles.
            starting_tiles: The starting tiles. In form: (starting tile, next tile)
        """
        self.__main_tile_sequence: list[Tile] = []
        self.__starting_tiles: list[Tile] = []
        self.__starting_tiles_set: set[Tile] = set()
        self.__chit_cards: list[ChitCard] = []

        # Set the starting tiles
        dest_to_start_tile: dict[Tile, Tile] = dict()
        for tile_pair in starting_tiles:
            starting_tile, dest = tile_pair[0], tile_pair[1]
            self.__starting_tiles_set.add(starting_tile)
            self.__starting_tiles.append(starting_tile)
            dest_to_start_tile[dest] = starting_tile

        # Create main tile sequence, taking in account starting tiles
        for tile in main_tile_sequence:
            if tile in dest_to_start_tile:
                self.__main_tile_sequence.append(dest_to_start_tile[tile])
            self.__main_tile_sequence.append(tile)

        # Check enough tiles
        self.__check_enough_main_tiles()

    def __check_enough_main_tiles(self) -> None:
        """Checks that there is the correct number of main tiles. If incorrect, throws an exception

        Throws:
            Exception if the number of starting tiles is incorect (DIMENSION_CELL_COUNT * 4) - 4
        """
        main_tiles_only_len = len(self.__main_tile_sequence) - len(self.__starting_tiles)
        if main_tiles_only_len != DefaultGameBoard.get_tiles_required():
            raise Exception(
                f"There must be {DefaultGameBoard.get_tiles_required()} tiles in the main tile sequence (len={main_tiles_only_len}). DIMENSION_CELL_COUNT = {DefaultGameBoard.DIMENSION_CELL_COUNT}."
            )

    #### GameBoard interface
    def move_character_by_steps(self, character: PlayableCharacter, steps: int) -> None:
        pass

    def get_character_floor_tile(self, character: PlayableCharacter) -> Tile:
        # TODO: Do not call. Will crash if no starting tiles
        return self.__starting_tiles[0]

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
        width, height = PygameScreenController_instance().get_screen_size()
        square_size: int = width // DefaultGameBoard.DIMENSION_CELL_COUNT
        draw_instructions: list[DrawAssetInstruction] = []

        # setting draw data in clockwise pattern, starting at top left
        i_top, i_right, i_bottom = DefaultGameBoard.DIMENSION_CELL_COUNT, DefaultGameBoard.DIMENSION_CELL_COUNT * 2 - 1, DefaultGameBoard.DIMENSION_CELL_COUNT * 3 - 2
        i_offset = 0

        for i, tile in enumerate(self.__main_tile_sequence):
            i = i - i_offset

            if tile in self.__starting_tiles_set:   # don't draw starting tiles
                i_offset += 1
                continue

            if i < i_top:  # draw top row
                tile.set_draw_data(TileDrawData((square_size * i, 0), (square_size, square_size)))
            elif i < i_right:  # draw right column
                factor: int = i - i_top + 1
                tile.set_draw_data(TileDrawData((width - square_size, square_size * factor), (square_size, square_size)))
            elif i < i_bottom:  # draw bottom column
                factor: int = i - i_right + 1
                tile.set_draw_data(TileDrawData((width - square_size * (factor + 1), height - square_size), (square_size, square_size)))
            else:  # draw left column
                factor: int = i - i_bottom + 1
                tile.set_draw_data(TileDrawData((0, height - square_size * (factor+1)), (square_size, square_size)))

        # getting draw instructions after setting draw data
        for tile in self.__main_tile_sequence:
            for instruction in tile.get_draw_assets_instructions():
                draw_instructions.append(instruction)

        return draw_instructions

    ### Static methods
    @staticmethod
    def get_chit_card_safe_area() -> tuple[tuple[int, int], tuple[int, int]]:
        """Get the square safe area for the chit cards.

        Returns:
            ((x0, y0), (x1, y1)), where the first & second pair corresponds to the top left & bottom right corner of the square
            shaped safe area.
        """
        width, height = PygameScreenController_instance().get_screen_size()
        square_size: int = width // DefaultGameBoard.DIMENSION_CELL_COUNT
        return ((square_size, square_size), (width - square_size, height - square_size))

    ### Static methods
    @staticmethod
    def get_tiles_required() -> int:
        """Get the number of tiles required to construct the default game board.

        Returns:
            The number of tiles required
        """
        return DefaultGameBoard.DIMENSION_CELL_COUNT * 4 - 4
