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
    # data.
    __MAPPING: dict[ClassTypeIdentifier, Callable[[dict[str, Any]], Any]] = {
        ClassTypeIdentifier.player_dragon: lambda data: Dragon.create_from_json_save(data)
    }
