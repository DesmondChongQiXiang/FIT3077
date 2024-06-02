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
