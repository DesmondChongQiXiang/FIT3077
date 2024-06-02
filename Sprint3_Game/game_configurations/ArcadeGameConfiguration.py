from typing import Any, Sequence
from presets import *
from settings import *
from core.GameWorld import GameWorld
from codec.saves.JSONSaveCodec import JSONSaveCodec
from codec.saves.JSONSavable import JSONSavable
from game_configurations.GameConfiguration import GameConfiguration
from game_concepts.turns.DefaultTurnManager import DefaultTurnManger
from game_concepts.turns.TurnManager import TurnManager
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
        # variables for generating the game world
        self.__main_tiles: list[Tile] = randomised_volcano_card_sequence(8)
        self.__starting_tiles: list[Tile] = [
            CaveTile(Animal.BABY_DRAGON, CaveTileVariant.BLUE, character=self.PLAYABLE_CHARACTERS[0]),
            CaveTile(Animal.SALAMANDER, CaveTileVariant.GREEN, character=self.PLAYABLE_CHARACTERS[1]),
            CaveTile(Animal.SPIDER, CaveTileVariant.ORANGE, character=self.PLAYABLE_CHARACTERS[2]),
            CaveTile(Animal.BAT, CaveTileVariant.PURPLE, character=self.PLAYABLE_CHARACTERS[3]),
        ]
        self.__starting_tile_positions_set: set[int] = set(self.STARTING_TILE_POSITIONS)  # positions as indexes along main sequence tiles

        save_codec.register_saveable(self)

    def generate_game_world(self) -> GameWorld:
        """Generate the game world with the default fiery dragons game configuration.

        Returns:
            The generated game world
        """

        # turn manager
        turn_manager: TurnManager = DefaultTurnManger(self.PLAYABLE_CHARACTERS, 0)

        # chit cards
        chit_cards: list[ChitCard] = []
        swap_powers: list[SwapPower] = [SwapPower(None) for _ in range(len(Animal))]
        for i, animal in enumerate(Animal):
            for j in range(1, 3):
                chit_cards.append(AnimalChitCard(animal, j))
            chit_cards.append(PirateChitCard(1 if i % 2 == 0 else 2))
            chit_cards.append(PowerChitCard(SkipTurnPower(turn_manager, 2), "assets/chit_cards/chit_card_skip_2.png"))
            chit_cards.append(PowerChitCard(swap_powers[i], "assets/chit_cards/chit_card_swap.png"))

        # game board
        game_board: GameBoard = DefaultGameBoard(
            self.__main_tiles,
            [
                (self.__starting_tiles[0], self.__main_tiles[self.STARTING_TILE_POSITIONS[0]]),
                (self.__starting_tiles[1], self.__main_tiles[self.STARTING_TILE_POSITIONS[1]]),
                (self.__starting_tiles[2], self.__main_tiles[self.STARTING_TILE_POSITIONS[2]]),
                (self.__starting_tiles[3], self.__main_tiles[self.STARTING_TILE_POSITIONS[3]]),
            ],
            chit_cards,
            self.PLAYABLE_CHARACTERS,
        )

        # configure all powers who need a game board
        for power in swap_powers:
            power.use_game_board(game_board)

        # GAME WORLD
        return GameWorld(game_board, turn_manager)

    def on_save(self, to_write: dict[str, Any]) -> None:
        """Upon save, add the key elements making up the game as placeholder properties to the save dictionary.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to JSON.
        """
        to_write["player_data"] = dict()
        to_write["volcano_card_sequence"] = []
        to_write["chit_card_sequence"] = []

        # add volcano card sequence (including caves) data to the saving dictionary
        starting_tile_i: int = 0  # tracks starting tile to ask saving data from
        volcano_card_sequence: list[Any] = to_write["volcano_card_sequence"]

        for i in range(0, len(self.__main_tiles), 3):  # volcano cards are in groups of 3
            volcano_card_sequence.append([])

            for j in range(i, i + 3):
                cur_tile: JSONSavable = self.__main_tiles[j]
                cur_tile.on_save(to_write)

                # write cave data if the cave is attached to this tile
                if j in self.__starting_tile_positions_set:
                    self.__starting_tiles[starting_tile_i].on_save(to_write)
                    starting_tile_i += 1
