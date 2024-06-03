from typing import Any, Optional, Callable
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
from factories.ClassTypeIdentifier import ClassTypeIdentifier
from utils.os_utils import *


class JSONSaveFactory:
    """Represents a factory that can create concrete classes from passed in JSON dictionary save data.

    Author: Shen
    """

    # MAPPING
    # Defines the mapping from class type identifier to lambdas that create concrete classes using JSON dictionary save
    # data and other required data.
    MAPPING: dict[ClassTypeIdentifier, Callable[..., Any]] = {
        ClassTypeIdentifier.tile_cave: lambda data: CaveTile.create_from_json_save(data),
        ClassTypeIdentifier.tile_normal: lambda data: NormalTile.create_from_json_save(data),
        ClassTypeIdentifier.player_dragon: lambda data: Dragon.create_from_json_save(data),
        ClassTypeIdentifier.chit_card_animal: lambda data: AnimalChitCard.create_from_json_save(data),
        ClassTypeIdentifier.chit_card_pirate: lambda data: PirateChitCard.create_from_json_save(data),
        ClassTypeIdentifier.chit_card_power: lambda data, power: PowerChitCard.create_from_json_save(data, power),
        ClassTypeIdentifier.power_skip: lambda data, turn_manager: SkipTurnPower.create_from_json_save(data, turn_manager),
        ClassTypeIdentifier.power_swap: lambda data, game_board: SwapPower.create_from_json_save(data, game_board),
    }

    def create_concrete_class(self, identifier: ClassTypeIdentifier, save_data: dict[str, Any], *args: Any) -> Any:
        """Create a concrete class based on the class identifier, save data and any other required parameters as
        specified in the same order as each concrete class's create_from_json_save() method.

        Args;
            identifier: The identifier for the concrete class
            save_data: Save data to initialise the class using
            *args: Any other required arguments in the same order as the associated class's create_from_save() method

        Returns:
            Class of the type bound to the class type identifier as defined by JSONSaveFactory.MAPPING
        """
        return self.MAPPING[identifier](save_data, *args)
