from game_concepts.powers.Power import Power
from game_concepts.turns.TurnManager import TurnManager
from game_objects.characters.PlayableCharacter import PlayableCharacter


class SkipTurnPower(Power):
    """Skip a number of turns past the user of the power once his/her turn ends.

    Author: Shen, Desmond, Ian
    """

    def __init__(self, turn_manager: TurnManager, players_to_skip: int):
        """Constructor.

        Args:
            turn_manager: A turn manager managing the player characters currently playing
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
