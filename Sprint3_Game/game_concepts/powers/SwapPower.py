from game_concepts.powers.Power import Power
from game_objects.game_board.GameBoard import GameBoard
from game_objects.characters.PlayableCharacter import PlayableCharacter
from typing import Optional


class SwapPower(Power):
    """Swap the player that is closest to the user of the power.

    Author: Shen, Rohan
    """

    def __init__(self, game_board: GameBoard):
        """Constructor.

        Args:
            game_board: The game board which the user is on
        """
        self.__game_board: GameBoard = game_board

    def _on_execute(self, user: PlayableCharacter) -> None:
        """Swap with the player that is closest to the user of the power.

        Args:
            user: The user of the power

        Raises:
            Exception when the target was not set upon execution.
        """
        closest_char: Optional[PlayableCharacter] = self.__game_board.get_closest_character(user)

        # if there was a closest character, swap and end turn. Otherwise dont swap and dont end turn.
        if closest_char is not None:
            self.__game_board.swap_characters(user, closest_char)
            user.set_should_continue_turn(False)
