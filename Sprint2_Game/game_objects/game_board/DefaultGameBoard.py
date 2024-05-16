from __future__ import annotations
from threading import Timer
from typing import Optional
from game_objects.game_board.GameBoard import GameBoard
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.tiles.Tile import Tile
from game_objects.chit_cards.ChitCard import ChitCard
from screen.DrawProperties import DrawProperties
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from screen.PygameScreenController import PygameScreenController
from core.GameWorld import GameWorld
from utils.pygame_utils import get_coords_for_center_drawing_in_rect

import random


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
    TURN_END_RESET_DELAY: float = 2.0  # Seconds to delay resetting game board on player turn end

    def __init__(self, main_tile_sequence: list[Tile], starting_tiles: list[tuple[Tile, Tile]], chit_cards: list[ChitCard], playable_characters: list[PlayableCharacter]):
        """
        Args:
            main_tile_sequence: The main tile sequence (excluding starting tiles) to use for the game board. Must have (DIMENSION_CELL_COUNT * 4) - 4 tiles.
            starting_tiles: The starting tiles. In form: (starting tile, next tile)
            chit_cards: The chit cards to use for the game board. Will be placed in order from left to right, top to bottom.
            playable_characters: The playable characters to play on the game board
        """
        self.__main_tile_sequence: list[Tile] = []
        self.__starting_tiles: list[Tile] = []
        self.__starting_tiles_set: set[Tile] = set()
        self.__starting_tiles_destinations_set: set[Tile] = set()  # stores the tiles that are the destinations for starting tiles
        self.__chit_cards: list[ChitCard] = chit_cards
        self.__character_tiles_visited: dict[PlayableCharacter, set[Tile]] = dict()  # K = character, V = set of tiles visited
        self.__character_location: dict[PlayableCharacter, int] = dict()  # K = character, V = index along main tile sequence
        self.__character_starting_tiles: dict[PlayableCharacter, Tile] = dict()  # K = character, V = their starting tile

        # ------ INITIALISATION ------------------------------------------------------------------------------------------------------------------------------------------------
        # initialise chit card position & size. Also set delegate
        self.__set_chit_card_draw_properties()

        for chit_card in self.__chit_cards:
            chit_card.set_game_board_delegate(self)

        # Populate starting tile stores, and create main tile sequence, taking in account starting tiles.
        dest_to_start_tile: dict[Tile, Tile] = dict()
        for tile_pair in starting_tiles:
            starting_tile, dest = tile_pair[0], tile_pair[1]
            self.__starting_tiles_destinations_set.add(dest)
            self.__starting_tiles_set.add(starting_tile)
            self.__starting_tiles.append(starting_tile)
            dest_to_start_tile[dest] = starting_tile

        for tile in main_tile_sequence:
            if tile in dest_to_start_tile:
                # starting tiles should be connected like so: tile -> starting tile -> tile
                self.__main_tile_sequence.append(tile)
                self.__main_tile_sequence.append(dest_to_start_tile[tile])
            self.__main_tile_sequence.append(tile)

        # Check enough tiles
        self.__check_enough_main_tiles()

        # Initialise character tiles visited, character starting location, character location dictionaries to initial game board state
        for character in playable_characters:
            self.__character_tiles_visited[character] = set()

        for tile in self.__starting_tiles:
            char_on_tile = tile.get_character_on_tile()
            if char_on_tile is not None:
                self.__character_starting_tiles[char_on_tile] = tile

        for i, tile in enumerate(self.__main_tile_sequence):
            potential_char: Optional[PlayableCharacter] = tile.get_character_on_tile()
            if potential_char is not None:
                self.__character_location[potential_char] = i

    def __check_enough_main_tiles(self) -> None:
        """Checks that there is the correct number of main tiles. If incorrect, throws an exception

        Throws:
            Exception if the number of main sequence tiles is incorrect (DIMENSION_CELL_COUNT * 4) - 4
        """
        main_tiles_only_len = (
            len(self.__main_tile_sequence) - len(self.__starting_tiles) * 2
        )  # *2 to account for starting tiles + duplicate tiles used in starting tile path
        if main_tiles_only_len != DefaultGameBoard.get_tiles_required():
            raise Exception(
                f"There must be {DefaultGameBoard.get_tiles_required()} tiles in the main tile sequence (len={main_tiles_only_len}). DIMENSION_CELL_COUNT = {DefaultGameBoard.DIMENSION_CELL_COUNT}."
            )

    def __set_chit_card_draw_properties(self) -> None:
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

    # ------ GameBoard abstract class --------------------------------------------------------------------------------------------
    def move_character_by_steps(self, character: PlayableCharacter, steps: int) -> None:
        """Move a character by a number of steps along the game board. Characters can only re-enter their starting tiles
        once they have visited all main tiles. If the character will overshoot their starting tile after visiting all tiles,
        then the character will not move and their turn will end.

        Args:
            character: The character to move
            steps: The number of steps to move (negative = anti-clockwise, positive = clockwise)
        """
        tile_intermediate_i: int = self.__character_location[character]
        steps_taken: int = 0

        while steps_taken < abs(steps):
            # If the character is going to move back into their cave, end the players turn
            if self.__character_starting_tiles[character] is self.__main_tile_sequence[tile_intermediate_i % len(self.__main_tile_sequence)] and steps < 0:
                    character.set_should_continue_turn(False)
                    return
            
            if steps < 0: # If a dragon pirate chit card has been flipped
                tile_intermediate_i -= 1

            else:
                tile_intermediate_i += 1  # check next tile
            steps_taken += 1

            current_tile_i = tile_intermediate_i % len(self.__main_tile_sequence)
            current_tile = self.__main_tile_sequence[current_tile_i]

            if current_tile in self.__starting_tiles_set:
                
                if self.__character_starting_tiles[character] is self.__main_tile_sequence[tile_intermediate_i % len(self.__main_tile_sequence)] and steps < 0:
                    character.set_should_continue_turn(False)
                    return

                # Allow character to only re-enter its own starting tile and only when they've visited all main sequence tiles
                if self.__character_starting_tiles[character] is current_tile and (
                    len(self.__character_tiles_visited[character]) == len(self.__main_tile_sequence) - len(self.__starting_tiles) * 2
                ):
                    if steps_taken < abs(steps):
                        # don't move character if starting tile will be overshot & end character's turn
                        character.set_should_continue_turn(False)
                        return

                    # go into its own starting tile
                    break
                
                
                tile_intermediate_i += 2 # otherwise skip the starting tile. +2 to account for its duplicate destination tile

            if steps > 0: # Only add the tile to the list of visited tiles if we're moving forward
                # add the currently considered tile to visited tiles for character accounting for any skipping of tiles
                self.__character_tiles_visited[character].add(self.__main_tile_sequence[tile_intermediate_i % len(self.__main_tile_sequence)])

        # place character on the calculated destination tile if not occupied and update character location. Otherwise end player's turn
        final_tile_i: int = tile_intermediate_i % len(self.__main_tile_sequence)
        final_tile: Tile = self.__main_tile_sequence[final_tile_i]

        if final_tile.get_character_on_tile() is not None:
            # if there is a character on the destination tile, end player's turn and do not move
            character.set_should_continue_turn(False)
            return

        self.__main_tile_sequence[final_tile_i].place_character_on_tile(character)
        self.__main_tile_sequence[self.__character_location[character]].set_character_on_tile(None)  # remove char from its current tile
        self.__character_location[character] = final_tile_i

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
        """When a player's turn ends, unflip all chit cards after a delay defined by DefaultGameBoard.TURN_END_RESET_DELAY.
        User interaction is disabled during the delay.
        """

        def unflip_chit_cards():
            for chit_card in self.__chit_cards:
                chit_card.set_flipped(False)
            GameWorld.instance().enable_mouse_clicks()

        unflip_timer = Timer(DefaultGameBoard.TURN_END_RESET_DELAY, unflip_chit_cards)
        unflip_timer.start()
        GameWorld.instance().disable_mouse_clicks()

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
        starting_tile_destinations_drawn: set[Tile] = set()

        # setting draw data in clockwise pattern (including starting tiles), starting at top left
        i_top, i_right, i_bottom = DefaultGameBoard.DIMENSION_CELL_COUNT, DefaultGameBoard.DIMENSION_CELL_COUNT * 2 - 1, DefaultGameBoard.DIMENSION_CELL_COUNT * 3 - 2
        i_offset = 0
        for i, tile in enumerate(self.__main_tile_sequence):
            i = i - i_offset

            # setting draw data for destinations of starting tiles whilst offsetting for duplicate
            if tile in self.__starting_tiles_destinations_set:
                i_offset += 1  # starting tile should be drawn on top of the destination tile
                if tile in starting_tile_destinations_drawn:
                    continue
                starting_tile_destinations_drawn.add(tile)

            # setting draw data for starting tiles
            if tile in self.__starting_tiles_set:
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

        # getting draw instructions for the entire board after setting draw data
        starting_tile_destinations_drawn: set[Tile] = set()

        for tile in self.__main_tile_sequence:
            tile_draw_instructions: Optional[list[DrawAssetInstruction]] = None

            if tile in self.__starting_tiles_destinations_set:
                # only get drawing instructions for one of the duplicate starting tile destination tiles [increase game performance]
                if tile not in starting_tile_destinations_drawn:
                    starting_tile_destinations_drawn.add(tile)
                    tile_draw_instructions = tile.get_draw_assets_instructions()
                else:
                    continue
            else:
                tile_draw_instructions = tile.get_draw_assets_instructions()

            for instruction in tile_draw_instructions:
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
        width, height = PygameScreenController.instance().get_screen_size()
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
