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


class ArcadeGameConfiguration(GameConfiguration):
    """The default fiery dragons game configuration but with a more arcade style due to the addition of extra powers.
    This configuration includes the the following extensions: swap chit cards, skip chit cards, universal tiles.

    Author: Shen
    """

    # STARTING_TILE_POSITIONS
    # The starting tile positions as indexes along the start of the main tile sequence to use for each starting tile in order.
    # Warning: Indexes must be within the bounds of the number of tiles - 1
    STARTING_TILE_POSITIONS: list[int] = [3, 9, 15, 21]

    # PLAYABLE_CHARACTERS
    # Defines the playable characters to use for the game
    PLAYABLE_CHARACTERS: list[PlayableCharacter] = [
        Dragon(PlayableCharacterVariant.BLUE, "Blue"),
        Dragon(PlayableCharacterVariant.GREEN, "Green"),
        Dragon(PlayableCharacterVariant.ORANGE, "Orange"),
        Dragon(PlayableCharacterVariant.PURPLE, "Purple"),
    ]

    def __init__(self, save_codec: JSONSaveCodec):
        """
        Constructor.

        Args:
            save_codec: The codec to use for saving.
        """
        self.__main_tiles: list[Tile] = randomised_volcano_card_sequence(8)
        self.__starting_tiles: list[Tile] = [
            CaveTile(Animal.BABY_DRAGON, CaveTileVariant.BLUE, character=self.PLAYABLE_CHARACTERS[0]),
            CaveTile(Animal.SALAMANDER, CaveTileVariant.GREEN, character=self.PLAYABLE_CHARACTERS[1]),
            CaveTile(Animal.SPIDER, CaveTileVariant.ORANGE, character=self.PLAYABLE_CHARACTERS[2]),
            CaveTile(Animal.BAT, CaveTileVariant.PURPLE, character=self.PLAYABLE_CHARACTERS[3]),
        ]
        self.__starting_tile_positions_set: set[int] = set(self.STARTING_TILE_POSITIONS)  # positions as indexes along main sequence tiles
        self.__chit_cards: list[ChitCard] = []
        self.__turn_manager: TurnManager = DefaultTurnManger(self.PLAYABLE_CHARACTERS, 0)
        self.__game_board: Optional[GameBoard] = None

        save_codec.register_saveable(self)

    def generate_game_world(self) -> GameWorld:
        """Generate the game world with the default fiery dragons game configuration.

        Returns:
            The generated game world
        """

        # chit cards
        swap_powers: list[SwapPower] = [SwapPower(None) for _ in range(len(Animal))]
        for i, animal in enumerate(Animal):
            for j in range(1, 3):
                self.__chit_cards.append(AnimalChitCard(animal, j))
            self.__chit_cards.append(PirateChitCard(1 if i % 2 == 0 else 2))
            self.__chit_cards.append(PowerChitCard(SkipTurnPower(self.__turn_manager, 2), "assets/chit_cards/chit_card_skip_2.png"))
            self.__chit_cards.append(PowerChitCard(swap_powers[i], "assets/chit_cards/chit_card_swap.png"))

        # game board
        self.__game_board = DefaultGameBoard(
            self.__main_tiles,
            [
                (self.__starting_tiles[0], self.__main_tiles[self.STARTING_TILE_POSITIONS[0]]),
                (self.__starting_tiles[1], self.__main_tiles[self.STARTING_TILE_POSITIONS[1]]),
                (self.__starting_tiles[2], self.__main_tiles[self.STARTING_TILE_POSITIONS[2]]),
                (self.__starting_tiles[3], self.__main_tiles[self.STARTING_TILE_POSITIONS[3]]),
            ],
            self.__chit_cards,
            self.PLAYABLE_CHARACTERS,
        )

        # configure all powers who need a game board
        for power in swap_powers:
            power.use_game_board(self.__game_board)

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
        to_write["volcano_card_sequence"] = []
        to_write["chit_card_sequence"] = []

        # add player data to the save dictionary
        players_save_dict: list[Any] = to_write["player_data"]["players"]
        for player in self.PLAYABLE_CHARACTERS:
            players_save_dict.append(player.on_save(to_write))

        player_data_save_dict: dict[str, Any] = to_write["player_data"]
        player_data_save_dict["currently_playing"] = self.__turn_manager.on_save(to_write)  # add currently playing character index

        # add volcano card sequence (including caves) data to the save dictionary
        volcano_card_seq_save_dict: list[Any] = to_write["volcano_card_sequence"]
        starting_tile_i: int = 0  # tracks starting tile to ask saving data from

        for i in range(0, len(self.__main_tiles), 3):  # volcano cards are in groups of 3
            current_volcano_card: list[Any] = []

            for j in range(i, i + 3):
                cur_tile: JSONSavable = self.__main_tiles[j]
                current_volcano_card.append(cur_tile.on_save(to_write))

                # write starting tile data if the starting tile is attached to this tile
                if j in self.__starting_tile_positions_set:
                    current_volcano_card.append(self.__starting_tiles[starting_tile_i].on_save(to_write))
                    starting_tile_i += 1

            volcano_card_seq_save_dict.append(current_volcano_card)

        # add chit card sequence to save dictionary
        chit_card_seq_save_dict: list[Any] = to_write["chit_card_sequence"]
        for chit_card in self.__chit_cards:
            chit_card_seq_save_dict.append(chit_card.on_save(to_write))

        # allow default game board to perform any configuration on existing data in save dictionary
        if self.__game_board is None:
            raise Exception("Game board not defined before save. Run generate_game_world() first.")
        self.__game_board.on_save(to_write)

    @staticmethod
    def create_game_world_from_json_save(save_data: dict[str, Any]) -> GameWorld:
        """Create a game world from JSON save data saved with an Arcade configuration.

        Args:
            save_data: The dictionary representing the JSON save data from an Arcade configuration

        Returns:
            A game world configured with

        Raises:
            Exception if the structure of the JSON dict was altered in an incompatible way
        """
        class_factory: JSONSaveClassFactory = JSONSaveClassFactory()
        playable_chars: list[PlayableCharacter] = []
        tiles: list[Tile] = []
        powers: list[Power] = []

        # initialise players
        try:
            players_save_dict: list[Any] = save_data["player_data"]["players"]
        except:
            raise Exception("player_data.players did not exist when trying to load from a JSON save data dictionary. From: ArcadeGameConfiguration.") 
        
        for player_data in players_save_dict:
            player_data: dict[str, Any] = player_data
            player: PlayableCharacter = class_factory.create_concrete_class(ClassTypeIdentifier(player_data["type"]), player_data)
            playable_chars.append(player)

        # initialise tiles + caves from volcano cards
        try:
            volcano_card_seq_save_dict: list[list[Any]] = save_data["volcano_card_sequence"]
        except:
            raise Exception("volcano_card_sequence did not exist when trying to load from a JSON save data dictionary. From: ArcadeGameConfiguration.")
        
        vc_counter: int = 0
        for volcano_card in volcano_card_seq_save_dict:
            for tile in volcano_card:
                ...

