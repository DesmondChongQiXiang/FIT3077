from __future__ import annotations
from game_concepts.powers.Power import Power
from game_concepts.turns.TurnManager import TurnManager
from game_objects.characters.PlayableCharacter import PlayableCharacter
from factories.ClassTypeIdentifier import ClassTypeIdentifier

from typing import Any, Optional


class SkipTurnPower(Power):
    """Skip a number of player turns once the user's his/her turn ends.

    Author: Shen, Desmond, Ian
    """

    def __init__(self, turn_manager: TurnManager, players_to_skip: int):
        """Constructor.

        Args:
            turn_manager: A turn manager managing the turns of players that are currently playing in the game
            players_to_skip: The number of players to skip ahead of the current player on execution
        """
        self.__turn_manager: TurnManager = turn_manager
        self.__players_to_skip: int = players_to_skip

    def _on_execute(self, user: PlayableCharacter) -> None:
        """Skip the number of turns as configured once the user's turn ends.

        Args:
            user: The user of the power

        Raises:
            Exception when the target was not set upon execution.
        """
        self.__turn_manager.skip_to_player_on_turn_end(self.__turn_manager.get_player_character_n_turns_downstream(self.__players_to_skip + 1, user))

    def on_save(self, to_write: dict[str, Any]) -> Optional[Any]:
        """When requested on save, return data describing the skip power.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.

        Returns:
            A JSON compatible object describing the skip turn power

        """
        return {"type": ClassTypeIdentifier.power_skip.value, "skip_value": self.__players_to_skip}

    @classmethod
    def create_from_json_save(cls, save_data: dict[str, Any]) -> SkipTurnPower:
        """Create a skip power based on a skip power type json save data object.

        Warning: The save data object must have been modified to include the turn manager object in the attribute "turn_manager".

        Args:
            save_data: The dictionary representing the JSON save data object for a skip power
            turn_manager: The turn manager for the game

        Returns:
            A skip turn power

        Raises:
            Exception if the structure of the json save data object was not as expected.
        """
        try:
            return cls(save_data["turn_manager"], save_data["skip_value"])
        except Exception as e:
            raise Exception(f"Save data must have attributes 'skip_value', 'turn_manager'. Passed in={save_data}. Error={e}")
