from __future__ import annotations
from threading import Timer
from typing import Optional
from collections.abc import Sequence
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
from utils.math_utils import *

import random


class DefaultGameBoard(GameBoard, DrawableByAsset):
    """Initialises and represents the default fiery dragons game board. Cells are drawn in a circle.
    Caves jut out from the main sequence of tiles. Chit cards are randomly placed within the inner ring.

    Author: Shen
    """

    ### CONFIG
    TURN_END_RESET_DELAY: float = 2.0  # Seconds to delay resetting game board on player turn end

    def __init__(self, main_tile_sequence: list[Tile], starting_tiles: list[tuple[Tile, Tile]], chit_cards: list[ChitCard], playable_characters: list[PlayableCharacter]):
        """
        Args:
            main_tile_sequence: The main tile sequence (excluding starting tiles) to use for the game board.
            starting_tiles: The starting tiles. In form: (starting tile, next tile)
            chit_cards: The chit cards to use for the game board. Will be placed in order from left to right, top to bottom.
            playable_characters: The playable characters to play on the game board
        """
        self.__tile_sequence: list[Tile] = []
        self.__main_tile_sequence_length: int = len(main_tile_sequence)  # length of just the main sequence (excluding starting tiles)
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
                self.__tile_sequence.append(tile)
                self.__tile_sequence.append(dest_to_start_tile[tile])
            self.__tile_sequence.append(tile)

        # Initialise character tiles visited, character starting location, character location dictionaries to initial game board state
        for character in playable_characters:
            self.__character_tiles_visited[character] = set()

        for tile in self.__starting_tiles:
            char_on_tile = tile.get_character_on_tile()
            if char_on_tile is not None:
                self.__character_starting_tiles[char_on_tile] = tile

        for i, tile in enumerate(self.__tile_sequence):
            potential_char: Optional[PlayableCharacter] = tile.get_character_on_tile()
            if potential_char is not None:
                self.__character_location[potential_char] = i

    def __set_chit_card_draw_properties(self) -> None:
        """Initialise the clickable chit cards to draw randomly within the inner zone (square) of the game board.

        DefaultGameBoard.CHIT_CARD_RAND_FACTOR and DefaultGameBoard.CHIT_CARD_DIMENSIONS determine the randomness
        and size of the chit cards.

        Warning:
            Will not set all chit card positions if random factor / chit card size is too large
        """
        # chit card generation factors
        screen_width: int = PygameScreenController.instance().get_screen_size()[0]

        #### Generating chit cards
        safe_area = self.__get_chit_card_safe_area()
        safe_area_width: int = safe_area[1][0] - safe_area[0][0]
        chit_card_rand_factor: int = int(safe_area_width * (105 / 1500))  # random factor for chit card generation in pixels.
        chit_card_size: tuple[int, int] = (int(0.18 * safe_area_width), int(0.18 * safe_area_width))  # chit card dimensions (width, height) in px

        x0, y0, x1, y1 = safe_area[0][0], safe_area[0][1], safe_area[1][0], safe_area[1][1]
        chit_card_w, chit_card_h = chit_card_size

        # generate chit tiles randomly in manner that doesn't clip board tiles
        chit_card_i = 0
        x_random_range, y_random_range = chit_card_w + chit_card_rand_factor, chit_card_h + chit_card_rand_factor

        for cur_y in range(y0, y1 - y_random_range, y_random_range):
            for cur_x in range(x0, x1 - x_random_range, x_random_range):
                if chit_card_i == len(self.__chit_cards):  # exit if no more chit cards to generate
                    break
                next_x, next_y = random.randint(cur_x, cur_x + chit_card_rand_factor), random.randint(cur_y, cur_y + chit_card_rand_factor)
                self.__chit_cards[chit_card_i].set_draw_properties(DrawProperties((next_x, next_y), chit_card_size))
                chit_card_i += 1

    # ------ GameBoard abstract class --------------------------------------------------------------------------------------------
    def move_character_by_steps(self, character: PlayableCharacter, steps: int) -> None:
        """Move a character by a number of steps along the game board. Characters can only re-enter their starting tiles
        once they have visited all main tiles. If the character will overshoot their starting tile after visiting all tiles
        or will overshoot their cave moving backwards, or will land on a tile occupied by another character, then the
        character will not move and their turn will end.

        Args:
            character: The character to move
            steps: The number of steps to move (negative = anti-clockwise, positive = clockwise)
        """
        tile_intermediate_i: int = self.__character_location[character]
        steps_taken: int = 0
        current_tile_i = tile_intermediate_i % len(self.__tile_sequence)
        current_tile = self.__tile_sequence[current_tile_i]

        while steps_taken < abs(steps):
            # If the character is already in a starting tile and is going to move further back, end their turn
            if self.__character_starting_tiles[character] is current_tile and steps < 0:
                character.set_should_continue_turn(False)
                return

            tile_intermediate_i = tile_intermediate_i - 1 if steps < 0 else tile_intermediate_i + 1  # consider next tile
            steps_taken += 1

            current_tile_i = tile_intermediate_i % len(self.__tile_sequence)
            current_tile = self.__tile_sequence[current_tile_i]

            if current_tile in self.__starting_tiles_set:
                # If the player is going to re-enter/pass their own starting tile by moving backwards, end their turn.
                if self.__character_starting_tiles[character] is current_tile and steps < 0:
                    character.set_should_continue_turn(False)
                    return

                # Allow character to only re-enter its own starting tile and only when they've visited all main sequence tiles
                if self.__character_starting_tiles[character] is current_tile and (
                    len(self.__character_tiles_visited[character]) == len(self.__tile_sequence) - len(self.__starting_tiles) * 2
                ):
                    if steps_taken < abs(steps):
                        # don't move character if starting tile will be overshot & end character's turn
                        character.set_should_continue_turn(False)
                        return

                    # go into its own starting tile
                    break

                tile_intermediate_i = tile_intermediate_i - 2 if steps < 0 else tile_intermediate_i + 2  # 2 to account for duplicate starting destination tile

            # add the currently considered tile to visited tiles for character accounting for any skipping of tiles
            self.__character_tiles_visited[character].add(self.__tile_sequence[tile_intermediate_i % len(self.__tile_sequence)])

        # place character on the calculated destination tile if not occupied and update character location. Otherwise end player's turn
        final_tile_i: int = tile_intermediate_i % len(self.__tile_sequence)
        final_tile: Tile = self.__tile_sequence[final_tile_i]

        if final_tile.get_character_on_tile() is not None:
            # if there is a character on the destination tile, end player's turn and do not move
            character.set_should_continue_turn(False)
            return

        self.__tile_sequence[final_tile_i].place_character_on_tile(character)
        self.__tile_sequence[self.__character_location[character]].set_character_on_tile(None)  # remove char from its current tile
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
        for tile in self.__tile_sequence:
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
        main_properties = self.__calculated_main_tile_sequence_properties()
        square_size = main_properties.square_size

        draw_instructions: list[DrawAssetInstruction] = []
        starting_tile_destinations_drawn: set[Tile] = set()
        main_circle_draw_properties: list[DrawProperties] = self.__circular_draw_properties_for_squares(
            self.__main_tile_sequence_length, square_size, (int(main_properties.circle_center_x), int(main_properties.circle_center_y))
        )
        main_circle_draw_properties_i: int = 0

        # setting draw data in clockwise pattern (including starting tiles) for tiles, starting at right tile
        for tile in self.__tile_sequence:
            did_draw_start_destination: bool = False

            # offsetting for drawing of duplicate starting tile destinations; allow drawing of destination tile only if it has not been drawn
            if tile in self.__starting_tiles_destinations_set:
                did_draw_start_destination = True  # starting tile should be drawn on top of the destination tile
                if tile in starting_tile_destinations_drawn:
                    continue
                starting_tile_destinations_drawn.add(tile)

            # setting draw data for starting tiles
            if tile in self.__starting_tiles_set:
                tile.set_draw_data(
                    self.__linearly_extrapolate_circlular_draw_properties(
                        square_size,
                        self.__main_tile_sequence_length,
                        main_circle_draw_properties[main_circle_draw_properties_i],
                    )
                )
                main_circle_draw_properties_i += 1
                continue

            # setting draw data for main tile sequence
            tile.set_draw_data(main_circle_draw_properties[main_circle_draw_properties_i])
            if not did_draw_start_destination:
                main_circle_draw_properties_i += 1

        # getting draw instructions for the entire board after setting draw data
        starting_tile_destinations_drawn: set[Tile] = set()

        for tile in self.__tile_sequence:
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

    def __circular_draw_properties_for_squares(self, n: int, square_size: float, central_coordinate: tuple[int, int]) -> list[DrawProperties]:
        """Gets the drawing properties (coordinates, rotation and size) that correspond to drawing squares such that their bottom corners
        touch in a circle around a specified coordinate.

        Args:
            n: The number of squares making up the circle
            square_size: The square size in pixels.
            central_coordinate: The coordinate (x,y) at which the circle should be centered

        Returns:
            The draw properties to draw the circle
        """
        draw_properties: list[DrawProperties] = []
        center_x: int = int(central_coordinate[0] - 0.5 * square_size)  # 0.5 * square size to offset for square overhang into circle
        center_y: int = int(central_coordinate[1] - 0.5 * square_size)
        circle_radius: float = polygon_radius_given_side_length(square_size, n)

        # Going anti-clockwise for each vertex of the circle, get the coordinates and rotation to draw the square at
        for i in range(n):
            internal_deg: float = polygon_internal_deg(n)
            central_deg: float = polygon_central_deg(n)
            rot_from_normal: float = (180 - internal_deg) / 2

            x: int = int(center_x + circle_radius * cos_deg(central_deg * i))
            y: int = int(center_y - circle_radius * sin_deg(central_deg * i))  # sign flipped because pygame y coordinate system is reversed
            rot: float = (((n - 1) + i) % n) * central_deg + rot_from_normal

            draw_properties.append(DrawProperties((x, y), (int(square_size), int(square_size)), rot))

        return draw_properties

    def __linearly_extrapolate_circlular_draw_properties(self, length: float, circle_sides: int, draw_properties: DrawProperties) -> DrawProperties:
        """Linearly extrapolate the drawing coordinates of the drawing property along its axis within the unit circle (as determined
        by its degrees of rotation) for a particular circle.

        Args:
            length: The size in px along its unit circle axis to extrapolate by
            circle_sides: The number of sides/squares making up the circle to extrapolate in
            draw_properties: The draw properties to extrapolate

        Returns:
            The linearly extrapolated draw properties.
        """
        x, y = draw_properties.get_coordinates()
        rot: float = draw_properties.get_rotation()
        internal_deg: float = polygon_internal_deg(circle_sides)
        central_deg: float = polygon_central_deg(circle_sides)
        rot_from_normal: float = (180 - internal_deg) / 2

        pos_in_circle: int = round(
            (((rot - rot_from_normal) + central_deg) / central_deg) % circle_sides
        )  # reverse calculation from rot formula for drawing in circle. 0 = square at 0 deg in unit circle (i.e first square)

        return DrawProperties(
            (int(x + length * cos_deg(pos_in_circle * central_deg)), int(y - length * sin_deg(pos_in_circle * central_deg))),
            draw_properties.get_size(),
            rot,
        )

    def get_all_clickable_sprites(self) -> Sequence[ModularClickableSprite]:
        """Get a read-only list of all the clickable sprites for the game board.

        Returns:
            A read-only list containing all the clickable sprites.
        """
        return self.__chit_cards

    # ------- Board properties -----------------------------------------------------------------------------------------
    def __get_chit_card_safe_area(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """Get the square safe area for the chit cards.

        Returns:
            ((x0, y0), (x1, y1)), where the first & second pair corresponds to the top left & bottom right corner of the square
            shaped safe area.
        """
        main_properties = self.__calculated_main_tile_sequence_properties()
        center_x, center_y = main_properties.circle_center_x, main_properties.circle_center_y
        safe_radius: float = (
            main_properties.circle_x1 - center_x - main_properties.square_size / 2
        )  # square_size / 2 because outline lies in middle of squares on circle outline

        square_distance_from_center: float = square_in_circle_apothem(safe_radius)
        x0, y0 = center_x - square_distance_from_center, center_y - square_distance_from_center
        x1, y1 = center_x + square_distance_from_center, center_y + square_distance_from_center

        return ((int(x0), int(y0)), (int(x1), int(y1)))

    def __calculated_main_tile_sequence_properties(self) -> __MainTileSequenceProperties:
        """Calculate and return the properties of the circular main tile sequence for drawing.

        The properties correspond to a circle within the bounds of the screen

        Returns:
            The properties of the main tile sequence
        """
        width, height = PygameScreenController.instance().get_screen_size()
        screen_center_x, screen_center_y = width / 2, height / 2

        # getting optimal side length and radius to ensure the drawn board's circle fits within the user's screen
        # optimal_side_length -> solving formula for side length given the radius of a polygon for side (length), letting r => solved for r, r + side/2 + side = screen_width/2 - 10
        optimal_side_length: float = (width * sin_deg(180 / self.__main_tile_sequence_length) - 30 * sin_deg(180 / self.__main_tile_sequence_length)) / (
            1 + 3 * sin_deg(180 / self.__main_tile_sequence_length)
        )
        optimal_radius: float = polygon_radius_given_side_length(optimal_side_length, self.__main_tile_sequence_length)

        # calculating rect bounds of circle
        circle_x0, circle_y0 = screen_center_x - optimal_radius, screen_center_y - optimal_radius
        circle_x1, circle_y1 = circle_x0 + optimal_radius * 2, circle_y0 + optimal_radius * 2

        return DefaultGameBoard.__MainTileSequenceProperties(
            optimal_radius,
            circle_x0,
            circle_x1,
            circle_y0,
            circle_y1,
            screen_center_x,
            screen_center_y,
            optimal_side_length,
        )

    class __MainTileSequenceProperties:
        """Private data class for organising the circular main tile sequence data for the default game board.

        Author: Shen
        """

        def __init__(
            self,
            circle_radius: float,
            circle_x0: float,
            circle_x1: float,
            circle_y0: float,
            circle_y1: float,
            circle_center_x: float,
            circle_center_y: float,
            square_size: float,
        ):
            """
            Args:
                circle_radius: The radius of the bounding outline for the circular main tile sequence
                circle_x0: The left x coordinate where the circular outline is to lie on
                circle_x1: The right x coordinate where the circular outline is to lie on
                circle_y0: The top y coordinate where the circular outline is to lie on
                circle_y1: The bottom y coordinate where the circular outline is to lie on
                circle_center_x: The x coordinate for the center of the circle
                circle_center_y: The y coordinate for the center of the circle
                square_size: The size of each dimension of the square tile

            Discussion:
                The circle_ coordinates represent coordinates of the circle outline that the center of the drawn objects will be located on.
                The circle_radius represents the distance from the middle of the circle to the outline that the center of drawn objects will be located on.
            """
            self.circle_radius = circle_radius
            self.circle_x0 = circle_x0
            self.circle_x1 = circle_x1
            self.circle_y0 = circle_y0
            self.circle_y1 = circle_y1
            self.circle_center_x: float = circle_center_x
            self.circle_center_y: float = circle_center_y
            self.square_size = square_size
