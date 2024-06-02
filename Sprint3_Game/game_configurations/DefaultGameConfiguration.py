from typing import Any
from presets import *
from settings import *
from core.GameWorld import GameWorld
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


class DefaultGameConfiguration(GameConfiguration):
    """The default fiery dragons game configuration.

    Author: Shen
    """

    def generate_game_world(self) -> GameWorld:
        """Generate the game world with the configuration.

        Returns:
            The generated game world
        """
        # tiles
        tiles: list[Tile] = randomised_volcano_card_sequence(8)

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
            tiles,
            [(starting_tiles[0], tiles[3]), (starting_tiles[1], tiles[9]), (starting_tiles[2], tiles[15]), (starting_tiles[3], tiles[21])],
            chit_cards,
            playable_characters,
        )

        # configure all powers who need a game board
        for power in swap_powers:
            power.use_game_board(game_board)

        # GAME WORLD
        return GameWorld(game_board, turn_manager)

    def on_save(self, to_write: dict[str, Any]) -> None:
        """Upon save, receive a json like python dictionary that can be edited. This json dictionary will be encoded,
        and as such must remain in a json encodable format.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to JSON.
        """
        ...

    def on_load(self, loaded_data: dict[str, Any]) -> None:
        """Upon load, load from the loaded JSON data.

        Args:
            loaded_data: The dictionary representing the loaded JSON.
        """
        ...
