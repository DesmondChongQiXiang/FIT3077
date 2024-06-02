from typing import Any, Sequence
from presets import *
from settings import *
from core.GameWorld import GameWorld
from codec.saves.JSONSaveCodec import JSONSaveCodec
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
    """The default fiery dragons game configuration but with a more arcade style due to the addition of powers.
    This configuration includes the the following extensions: swap chit cards, skip chit cards, universal tiles.

    Author: Shen
    """

    def __init__(self, save_codec: JSONSaveCodec):
        """
        Constructor.

        Args:
            save_codec: The codec to use for saving.
        """
        save_codec.register_saveable(self)

        # variables for generating the game world
        self.__tiles: list[Tile] = randomised_volcano_card_sequence(8)

    def generate_game_world(self) -> GameWorld:
        """Generate the game world with the default fiery dragons game configuration.

        Returns:
            The generated game world
        """
        # playable characters
        playable_characters: list[PlayableCharacter] = [
            Dragon(PlayableCharacterVariant.BLUE, "Blue"),
            Dragon(PlayableCharacterVariant.GREEN, "Green"),
            Dragon(PlayableCharacterVariant.ORANGE, "Orange"),
            Dragon(PlayableCharacterVariant.PURPLE, "Purple"),
        ]

        # starting tiles
        starting_tiles: list[Tile] = [
            CaveTile(Animal.BABY_DRAGON, CaveTileVariant.BLUE, character=playable_characters[0]),
            CaveTile(Animal.SALAMANDER, CaveTileVariant.GREEN, character=playable_characters[1]),
            CaveTile(Animal.SPIDER, CaveTileVariant.ORANGE, character=playable_characters[2]),
            CaveTile(Animal.BAT, CaveTileVariant.PURPLE, character=playable_characters[3]),
        ]

        # turn manager
        turn_manager: TurnManager = DefaultTurnManger(playable_characters, 0)

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
            self.__tiles,
            [(starting_tiles[0], self.__tiles[3]), (starting_tiles[1], self.__tiles[9]), (starting_tiles[2], self.__tiles[15]), (starting_tiles[3], self.__tiles[21])],
            chit_cards,
            playable_characters,
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
