from __future__ import annotations
from game_objects.game_board.GameBoard import GameBoard
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.tiles.Tile import Tile
from game_objects.chit_cards.ChitCard import ChitCard
from screen.DrawProperties import DrawProperties
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from core.singletons import PygameScreenController_instance
from utils.pygame_utils import get_coords_for_center_drawing_in_rect

import random
from threading import Timer


class DefaultGameBoard(GameBoard, DrawableByAsset):
    """Initialises and represents the default fiery dragons game board. Cells are drawn in a square, using the
    width of the screen as reference. Caves jut out from the main sequence of tiles. Chit cards are randomly
    placed within the inner ring.

    Author: Shen
    """

    ### CONFIG
    DIMENSION_CELL_COUNT: int = 7  # Cell count for each dimension
    CHIT_CARD_RAND_FACTOR: int = 40  # random factor in pixels
    CHIT_CARD_DIMENSIONS: tuple[int, int] = (75, 75)  # chit card dimensions (width, height) in px
    TURN_END_RESET_DELAY: float = 1.3  # Seconds to delay resetting game board on player turn end

    def __init__(self, main_tile_sequence: list[Tile], starting_tiles: list[tuple[Tile, Tile]], chit_cards: list[ChitCard]):
        """
        Args:
            main_tile_sequence: The main tile sequence (excluding starting tiles) to use for the game board. Must have (DIMENSION_CELL_COUNT * 4) - 4 tiles.
            starting_tiles: The starting tiles. In form: (starting tile, next tile)
            chit_cards: The chit cards to use for the game board. Will be placed in order from left to right, top to bottom.
        """
        self.__main_tile_sequence: list[Tile] = []
        self.__starting_tiles: list[Tile] = []
        self.__starting_tiles_set: set[Tile] = set()
        self.__chit_cards: list[ChitCard] = chit_cards

        # initialise chit card position & size
        self.__initialise_chit_card_draw_properties()

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
            Exception if the number of main sequence tiles is incorect (DIMENSION_CELL_COUNT * 4) - 4
        """
        main_tiles_only_len = len(self.__main_tile_sequence) - len(self.__starting_tiles)
        if main_tiles_only_len != DefaultGameBoard.get_tiles_required():
            raise Exception(
                f"There must be {DefaultGameBoard.get_tiles_required()} tiles in the main tile sequence (len={main_tiles_only_len}). DIMENSION_CELL_COUNT = {DefaultGameBoard.DIMENSION_CELL_COUNT}."
            )

    def __initialise_chit_card_draw_properties(self) -> None:
        """Initialise the clickable chit cards to draw randomly within the inner zone (square) of the game board.

        DefaultGameBoard.CHIT_CARD_RAND_FACTOR and DefaultGameBoard.CHIT_CARD_DIMENSIONS determine the randomness
        and size of the chit cards.

        Warning:
            Will not set all chit card positions if random factor / chit card size is too large
        """
        safe_area = DefaultGameBoard.__get_chit_card_safe_area()
        x0, y0, x1, y1 = safe_area[0][0], safe_area[0][1], safe_area[1][0], safe_area[1][1]
        chit_card_w, chit_card_h = DefaultGameBoard.CHIT_CARD_DIMENSIONS
        next_x, next_y = 0, 0  # default coords = (0, 0) to draw at if can't generate

        # generate chit tiles randomly in manner that doesn't clip board tiles
        chit_card_i = 0
        x_random_range, y_random_range = chit_card_w + DefaultGameBoard.CHIT_CARD_RAND_FACTOR, chit_card_h + DefaultGameBoard.CHIT_CARD_RAND_FACTOR

        for cur_y in range(y0, y1 - y_random_range, y_random_range):
            for cur_x in range(x0, x1 - x_random_range, x_random_range):
                if chit_card_i == len(self.__chit_cards):  # exit if no more chit cards to generate
                    break
                next_x, next_y = random.randint(cur_x, cur_x + DefaultGameBoard.CHIT_CARD_RAND_FACTOR), random.randint(
                    cur_y, cur_y + DefaultGameBoard.CHIT_CARD_RAND_FACTOR
                )
                self.__chit_cards[chit_card_i].set_draw_properties(DrawProperties((next_x, next_y), DefaultGameBoard.CHIT_CARD_DIMENSIONS))
                chit_card_i += 1

    # ------ GameBoard abstract class -----------------------------------------------------------------------------------------
    def move_character_by_steps(self, character: PlayableCharacter, steps: int) -> None:
        pass

    def get_character_floor_tile(self, character: PlayableCharacter) -> Tile:
        """Get the tile a character is on.

        Args:
            character: The character

        Returns:
            The tile the character is on

        Raises:
            Exception if the character could not be found on any tile
        """
        for tile in self.__main_tile_sequence:
            if tile.get_character_on_tile() == character:
                return tile
        raise Exception("Character could not be found on any tile.")

    def on_player_turn_end(self) -> None:
        """When a player's turn ends, unflip all chit cards."""

        def unflip_chit_cards():
            for chit_card in self.__chit_cards:
                chit_card.set_flipped(False)

        unflip_timer = Timer(DefaultGameBoard.TURN_END_RESET_DELAY, unflip_chit_cards)
        unflip_timer.start()

    # ------ DrawableByAsset interface & Drawing --------------------------------------------------------------------------------------
    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """
        Instructions to draw the game board as a square of square cells, with the number of cells on each dimension equal to
        DefaultGameBoard.DIMENSION_CELL_COUNT.

        Returns:
            The list of drawing instructions

        Author: Shen
        """
        main_properties = self.__get_main_tile_sequence_properties()
        main_x0, main_x1, main_y0, main_y1 = main_properties.main_x0, main_properties.main_x1, main_properties.main_y0, main_properties.main_y1
        square_size = main_properties.square_size

        draw_instructions: list[DrawAssetInstruction] = []

        # setting draw data in clockwise pattern (including starting tiles), starting at top left
        i_top, i_right, i_bottom = DefaultGameBoard.DIMENSION_CELL_COUNT, DefaultGameBoard.DIMENSION_CELL_COUNT * 2 - 1, DefaultGameBoard.DIMENSION_CELL_COUNT * 3 - 2
        i_offset = 0
        for i, tile in enumerate(self.__main_tile_sequence):
            i = i - i_offset

            # setting draw data for starting tiles
            if tile in self.__starting_tiles_set:
                i_offset += 1
                if i < i_top:  # draw for top row
                    tile.set_draw_data(DrawProperties((int(main_x0 + square_size * i), int(main_y0 - square_size)), (int(square_size), int(square_size))))
                elif i < i_right:  # draw for right column
                    factor: int = i - i_top + 1
                    tile.set_draw_data(DrawProperties((int(main_x1), int(main_y0 + square_size * factor)), (int(square_size), int(square_size)), 270))
                elif i < i_bottom:  # draw for bottom column
                    factor: int = i - i_right + 1
                    tile.set_draw_data(DrawProperties((int(main_x1 - square_size * (factor + 1)), int(main_y1)), (int(square_size), int(square_size)), 180))
                else:  # draw for left column
                    factor: int = i - i_bottom + 1
                    tile.set_draw_data(DrawProperties((int(main_x0 - square_size), int(main_y1 - square_size * (factor + 1))), (int(square_size), int(square_size)), 90))
                continue

            # setting draw data for main tile sequence
            if i < i_top:  # draw top row
                tile.set_draw_data(DrawProperties((int(main_x0 + square_size * i), int(main_y0)), (int(square_size), int(square_size))))
            elif i < i_right:  # draw right column
                factor: int = i - i_top + 1
                tile.set_draw_data(DrawProperties((int(main_x1 - square_size), int(main_y0 + square_size * factor)), (int(square_size), int(square_size))))
            elif i < i_bottom:  # draw bottom column
                factor: int = i - i_right + 1
                tile.set_draw_data(DrawProperties((int(main_x1 - square_size * (factor + 1)), int(main_y1 - square_size)), (int(square_size), int(square_size))))
            else:  # draw left column
                factor: int = i - i_bottom + 1
                tile.set_draw_data(DrawProperties((int(main_x0), int(main_y1 - square_size * (factor + 1))), (int(square_size), int(square_size))))

        # getting draw instructions after setting draw data
        for tile in self.__main_tile_sequence:
            for instruction in tile.get_draw_assets_instructions():
                draw_instructions.append(instruction)

        return draw_instructions

    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Draw the clickable chit cards for the default game board.

        Returns:
            The drawing instructions for the chit cards in form (instruction, chit card object)
        """
        ##### Getting instructions
        instructions: list[tuple[DrawAssetInstruction, ModularClickableSprite]] = []
        for chit_card in self.__chit_cards:
            for click_inst in chit_card.get_draw_clickable_assets_instructions():
                instructions.append(click_inst)

        return instructions

    # ------- Static methods -----------------------------------------------------------------------------------------
    @staticmethod
    def get_tiles_required() -> int:
        """Get the number of tiles required to construct the default game board.

        Returns:
            The number of tiles required
        """
        return DefaultGameBoard.DIMENSION_CELL_COUNT * 4 - 4

    @staticmethod
    def __get_chit_card_safe_area() -> tuple[tuple[int, int], tuple[int, int]]:
        """Get the square safe area for the chit cards.

        Returns:
            ((x0, y0), (x1, y1)), where the first & second pair corresponds to the top left & bottom right corner of the square
            shaped safe area.
        """
        main_properties = DefaultGameBoard.__get_main_tile_sequence_properties()
        main_x0, main_x1, main_y0, main_y1 = main_properties.main_x0, main_properties.main_x1, main_properties.main_y0, main_properties.main_y1
        square_size = main_properties.square_size
        return ((int(main_x0 + square_size), int(main_y0 + square_size)), (int(main_x1 - square_size), int(main_y1 - square_size)))

    @staticmethod
    def __get_main_tile_sequence_properties() -> _MainTileSequenceProperties:
        """Get the properties (bounds, size, square size) of the main tile sequence.

        Returns:
            The properties of the main tile sequence
        """
        width, height = PygameScreenController_instance().get_screen_size()
        main_width, main_height = width - 2 * (width // (DefaultGameBoard.DIMENSION_CELL_COUNT + 2)), height - 2 * (height // (DefaultGameBoard.DIMENSION_CELL_COUNT + 2))
        square_size: float = main_width / DefaultGameBoard.DIMENSION_CELL_COUNT
        main_x, main_y = get_coords_for_center_drawing_in_rect((0, 0), (width, height), (main_width, main_height))
        main_x0, main_x1, main_y0, main_y1 = (
            main_x,
            main_x + DefaultGameBoard.DIMENSION_CELL_COUNT * square_size,
            main_y,
            main_y + DefaultGameBoard.DIMENSION_CELL_COUNT * square_size,
        )
        return _MainTileSequenceProperties(width, height, main_x0, main_x1, main_y0, main_y1, square_size)


class _MainTileSequenceProperties:
    """Private data class for organising main tile sequence data for the default game board.

    Author: Shen
    """

    def __init__(self, width: int, height: int, x0: float, x1: float, y0: float, y1: float, square_size: float):
        """
        Args:
            width: The width of the main tile sequence
            height: The height of the main tile sequence
            x0: The left bound x coordinate for the main tile sequence
            x1: The right bound x coordinate for the main tile sequence
            y0: The top bound y coordinate for the main tile sequence
            y1: The bottom bound y coordinate for the main tile sequence
            square_size: The size of each dimension of the square tile
        """
        self.main_width = width
        self.main_height = height
        self.main_x0 = x0
        self.main_x1 = x1
        self.main_y0 = y0
        self.main_y1 = y1
        self.square_size = square_size
