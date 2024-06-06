from __future__ import annotations
from typing import Any, Optional
from presets import *
from settings import *
from core.GameWorld import GameWorld
from codec.saves.JSONSaveCodec import JSONSaveCodec
from codec.saves.JSONSavable import JSONSavable
from factories.saves.JSONSaveClassFactory import JSONSaveClassFactory
from factories.ClassTypeIdentifier import ClassTypeIdentifier
from game_configurations.GameConfiguration import GameConfiguration
from game_concepts.turns.DefaultTurnManager import DefaultTurnManger
from game_concepts.turns.TurnManager import TurnManager
from game_concepts.powers.Power import Power
from game_concepts.powers.SkipTurnPower import SkipTurnPower
from game_concepts.powers.SwapPower import SwapPower
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.Dragon import Dragon
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.chit_cards.AnimalChitCard import AnimalChitCard
from game_objects.chit_cards.PirateChitCard import PirateChitCard
from game_objects.tiles.Tile import Tile
from game_objects.tiles.CaveTile import CaveTile
from game_objects.tiles.CaveTileVariant import CaveTileVariant
from game_objects.game_board.GameBoard import GameBoard
from game_objects.game_board.DefaultGameBoard import DefaultGameBoard
from game_objects.animals.Animal import Animal
from game_objects.characters.PlayableCharacterVariant import PlayableCharacterVariant
from utils.os_utils import *

import random

# TODO: In the future, save and load need to be refactored into several helper functions to reduce cognitive load - Shen


class ArcadeGameConfiguration(GameConfiguration):
    """The default fiery dragons game configuration but with a more arcade style due to the addition of extra powers.
    This configuration includes the the following extensions: swap chit cards, skip chit cards, universal tiles.

    Author: Shen
    """

    # GEN_DEFAULT_STARTING_TILE_POSITIONS
    # The starting tile positions as indexes along the start of the main tile sequence to use for placing the starting tiles when
    # using generate_game_world() to generate a GameWorld.
    # Warning: Indexes must be within the bounds of the main number of tiles - 1
    __GEN_DEFAULT_STARTING_TILE_POSITIONS: list[int] = [3, 9, 15, 21]

    def __init__(self, save_codec: JSONSaveCodec):
        """
        Constructor.

        Args:
            save_codec: The codec to use for saving.
        """
        self.__main_tile_sequence: list[Tile] = randomised_volcano_card_sequence(8)
        self.__playable_characters: list[PlayableCharacter] = [
            Dragon(PlayableCharacterVariant.BLUE, "Blue"),
            Dragon(PlayableCharacterVariant.GREEN, "Green"),
            Dragon(PlayableCharacterVariant.ORANGE, "Orange"),
            Dragon(PlayableCharacterVariant.PURPLE, "Purple"),
        ]
        self.__starting_tiles: list[Tile] = [
            CaveTile(Animal.BABY_DRAGON, CaveTileVariant.BLUE, character=self.__playable_characters[0]),
            CaveTile(Animal.SALAMANDER, CaveTileVariant.GREEN, character=self.__playable_characters[1]),
            CaveTile(Animal.SPIDER, CaveTileVariant.ORANGE, character=self.__playable_characters[2]),
            CaveTile(Animal.BAT, CaveTileVariant.PURPLE, character=self.__playable_characters[3]),
        ]
        self.__starting_tile_positions_set: set[int] = set(self.__GEN_DEFAULT_STARTING_TILE_POSITIONS)  # positions as indexes along main sequence tiles
        self.__chit_cards: list[ChitCard] = []
        self.__turn_manager: TurnManager = DefaultTurnManger(self.__playable_characters, 0)
        self.__game_board: Optional[GameBoard] = None
        self.__save_codec: JSONSaveCodec = save_codec

        save_codec.register_saveable(self)

    def generate_game_world(self) -> GameWorld:
        """Generate the game world with the default arcade fiery dragons game configuration.

        Returns:
            The generated game world
        """

        # CHIT CARDS: Default
        # Generate 12 animal chit cards, 4 pirate chit cards
        for i, animal in enumerate(Animal):
            # don't generate any universal matching chit cards
            if animal == Animal.UNIVERSAL:
                continue

            for j in range(1, 4):
                self.__chit_cards.append(AnimalChitCard(animal, j))
            self.__chit_cards.append(PirateChitCard(1 if i % 2 == 0 else 2))

        random.shuffle(self.__chit_cards)

        # GAME BOARD
        self.__game_board = DefaultGameBoard(
            self.__main_tile_sequence,
            [
                (self.__starting_tiles[0], self.__main_tile_sequence[self.__GEN_DEFAULT_STARTING_TILE_POSITIONS[0]]),
                (self.__starting_tiles[1], self.__main_tile_sequence[self.__GEN_DEFAULT_STARTING_TILE_POSITIONS[1]]),
                (self.__starting_tiles[2], self.__main_tile_sequence[self.__GEN_DEFAULT_STARTING_TILE_POSITIONS[2]]),
                (self.__starting_tiles[3], self.__main_tile_sequence[self.__GEN_DEFAULT_STARTING_TILE_POSITIONS[3]]),
            ],
            self.__chit_cards,
            self.__playable_characters,
            self.__save_codec,
        )

        # CHIT CARDS: Powers
        # Add 2 skip and 2 swap power chit cards
        self.__game_board.add_chit_card(PowerChitCard(SkipTurnPower(self.__turn_manager, 1), "assets/chit_cards/chit_card_skip_1.png"), True)
        self.__game_board.add_chit_card(PowerChitCard(SkipTurnPower(self.__turn_manager, 2), "assets/chit_cards/chit_card_skip_2.png"), True)
        for _ in range(2):
            self.__game_board.add_chit_card(PowerChitCard(SwapPower(self.__game_board), "assets/chit_cards/chit_card_swap.png"), True)

        # GAME WORLD
        return GameWorld(self.__game_board, self.__turn_manager)

    def on_save(self, to_write: dict[str, Any]) -> None:
        """Upon save, configure the save dictionary to represent the state of the current arcade type game.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to JSON on save.
        """
        to_write["player_data"] = dict()
        to_write["player_data"]["players"] = []
        to_write["dependencies"] = dict()
        to_write["volcano_card_sequence"] = []
        to_write["chit_card_sequence"] = []

        # ================================================================
        # ---------------------- save player data ------------------------
        # ================================================================
        players_save_dict: list[Any] = to_write["player_data"]["players"]
        for player in self.__playable_characters:
            players_save_dict.append(player.on_save(to_write))

        player_data_save_dict: dict[str, Any] = to_write["player_data"]
        player_data_save_dict["currently_playing"] = self.__turn_manager.on_save(to_write)  # add currently playing character index

        # ================================================================
        # ---------- save volcano cards + starting tiles -----------------
        # ================================================================
        # variables
        volcano_card_seq_save_dict: list[Any] = to_write["volcano_card_sequence"]
        starting_tile_i: int = 0  # tracks starting tile to ask saving data from

        # saving
        for i in range(0, len(self.__main_tile_sequence), 3):  # volcano cards are in groups of 3
            current_volcano_card_sequence: list[Any] = []
            current_volcano_card_start_tiles: list[Any] = []

            for j in range(i, i + 3):
                cur_tile: JSONSavable = self.__main_tile_sequence[j]
                current_volcano_card_sequence.append(cur_tile.on_save(to_write))

                # write starting tile data if the starting tile is attached to this tile
                if j in self.__starting_tile_positions_set:
                    starting_tile_data: Optional[dict[str, Any]] = self.__starting_tiles[starting_tile_i].on_save(to_write)
                    if starting_tile_data is None:
                        raise Exception("Starting tile object was None.")

                    starting_tile_data["location"] = j - i
                    current_volcano_card_start_tiles.append(starting_tile_data)
                    starting_tile_i += 1

            volcano_card_seq_save_dict.append(
                {"sequence": current_volcano_card_sequence, "starting_tiles": current_volcano_card_start_tiles if len(current_volcano_card_start_tiles) > 0 else None}
            )

        # ================================================================
        # ---------------------- save chit cards -------------------------
        # ================================================================
        for chit_card in self.__chit_cards:
            chit_card.on_save(to_write)

        # ================================================================
        # -------------- game board dynamic save config ------------------
        # ================================================================
        # allow default game board to perform any configuration on existing data in save dictionary
        if self.__game_board is None:
            raise Exception("Game board not defined before save. Run generate_game_world() or create_game_world_from_json_save() first.")
        self.__game_board.on_save(to_write)

    def create_game_world_from_json_save(self, save_data: dict[str, Any]) -> GameWorld:
        """Create a game world from JSON save data saved with an Arcade configuration.

        Args:
            save_data: The dictionary representing the JSON save data from an Arcade configuration

        Returns:
            A game world configured with the passed in Arcade configuration JSON save data

        Raises:
            Exception if the structure of the JSON dict was altered in an incompatible way
        """
        class_factory: JSONSaveClassFactory = JSONSaveClassFactory()
        deferred_chit_card_object_data: list[tuple[dict[str, Any], int]] = (
            []
        )  # Deferred (initialised after GameBoard initialisation) chit card data. [(data, index position it should be at)]

        # ================================================================
        # --------------------- initialise players -----------------------
        # ================================================================
        # variables
        playable_characters: list[PlayableCharacter] = []
        playable_character_positions: list[int] = []  # positions as indexes
        players_save_dict: list[Any] = save_data["player_data"]["players"]

        # create players
        for player_data in players_save_dict:
            player: PlayableCharacter = class_factory.create_concrete_class(ClassTypeIdentifier(player_data["type"]), player_data)
            playable_characters.append(player)
            playable_character_positions.append(player_data["location"])

        self.__playable_characters = playable_characters

        # ================================================================
        # ------------------ initialise turn manager ---------------------
        # ================================================================
        current_player_i: int = save_data["player_data"]["currently_playing"]
        turn_manager: TurnManager = DefaultTurnManger(playable_characters, current_player_i)

        self.__turn_manager = turn_manager

        # ================================================================
        # ------- initialise starting tiles + volcano cards --------------
        # ================================================================
        # variables
        main_tiles: list[Tile] = []
        starting_tiles: list[tuple[Tile, Tile]] = []  # (starting tile, connected tile)
        volcano_card_seq_save_dict: list[dict[str, Any]] = save_data["volcano_card_sequence"]
        cur_tile_i: int = 0

        # create the tiles + caves
        for volcano_card in volcano_card_seq_save_dict:
            volcano_card_main_seq: list[dict[str, Any]] = volcano_card["sequence"]
            volcano_card_start_tiles: Optional[list[dict[str, Any]]] = volcano_card["starting_tiles"]

            # initialise main tile sequence tiles
            for tile_data in volcano_card_main_seq:
                tile: Tile = class_factory.create_concrete_class(ClassTypeIdentifier(tile_data["type"]), tile_data)
                main_tiles.append(tile)

            # initialising starting tiles
            if volcano_card_start_tiles is not None:
                for start_tile_data in volcano_card_start_tiles:
                    starting_tile: Tile = class_factory.create_concrete_class(ClassTypeIdentifier(start_tile_data["type"]), start_tile_data)
                    starting_tiles.append((starting_tile, main_tiles[start_tile_data["location"] + cur_tile_i]))

            cur_tile_i += len(volcano_card_main_seq)

        self.__main_tile_sequence = main_tiles

        # ===============================================================
        # ------------------ initialise chit cards ----------------------
        # ===============================================================
        # variables
        chit_cards: list[ChitCard] = []
        chit_card_seq_save_dict: list[dict[str, Any]] = save_data["chit_card_sequence"]

        # creating non deferred chit cards. Saving deferred chit card data for later initialisation
        for i, chit_card_data in enumerate(chit_card_seq_save_dict):
            if not chit_card_data["deferred"]:
                chit_card: ChitCard = class_factory.create_concrete_class(ClassTypeIdentifier(chit_card_data["type"]), chit_card_data)
                chit_cards.append(chit_card)
            else:
                deferred_chit_card_object_data.append((chit_card_data, i))

        self.__chit_cards = chit_cards

        # ================================================================
        # ------------------ initialise game board -----------------------
        # ================================================================
        # initially place all playable characters on the board
        for i, character in enumerate(playable_characters):
            starting_tile: Tile = starting_tiles[i][0]
            starting_tile.set_character_on_tile(character)

        # initialise game board and move character to correct positions
        game_board: DefaultGameBoard = DefaultGameBoard(main_tiles, starting_tiles, chit_cards, playable_characters, self.__save_codec)
        game_board.move_characters_to_position_indexes(playable_character_positions, False)

        self.__game_board = game_board

        # ================================================================
        # ------------- perform deferred initialisations -----------------
        # ================================================================
        # variables
        dependency_map: dict[ClassTypeIdentifier, Any] = {
            ClassTypeIdentifier.turn_manager: turn_manager,
            ClassTypeIdentifier.game_board: game_board,
        }
        dependency_instances: dict[str, Any] = {}  # contains dependency id mapped to dependency class concrete instance
        dependencies_save_dict: dict[str, dict[str, Any]] = save_data["dependencies"]

        # initialise dependencies
        for dependency_id, dependency_data in dependencies_save_dict.items():
            dependency_type: str = dependency_data["type"]
            dependency_arg_identifiers: list[str] = dependency_data["required"]
            dependency_arg_list: list[Any] = [dependency_map[ClassTypeIdentifier(required_type)] for required_type in dependency_arg_identifiers]

            dependency_instances[dependency_id] = class_factory.create_concrete_class(ClassTypeIdentifier(dependency_type), dependency_data, *dependency_arg_list)

        # ============ DEFERRED: Chit cards ================================
        # getting deferred chit card instances and adding to game board
        for chit_card_data, pos in deferred_chit_card_object_data:
            chit_card_type: str = chit_card_data["type"]
            chit_card_dependency_ids: list[str] = chit_card_data["dependencies"]
            chit_card_dependency_instances: list[Any] = [dependency_instances[id] for id in chit_card_dependency_ids]

            game_board.add_chit_card(
                class_factory.create_concrete_class(ClassTypeIdentifier(chit_card_type), chit_card_data, *chit_card_dependency_instances), False, pos
            )

        # ================================================================
        # ----------------------- GAME WORLD -----------------------------
        # ================================================================
        return GameWorld(game_board, turn_manager)
