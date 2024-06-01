from game_concepts.powers.Power import Power
from game_objects.game_board.GameBoard import GameBoard
from game_objects.characters.PlayableCharacter import PlayableCharacter
from typing import Optional


class SwapPower(Power):
    """Swap with the player that is closest to the user of the power. The user's turn automatically ends upon a successful
    swap, otherwise their turn does not end.

    Warning: Must set a game board to use before execution using use_game_board().

    Author: Shen, Rohan
    """

    def __init__(self, game_board: Optional[GameBoard]):
        """Constructor.

        Args:
            game_board (optional): The game board to use for calculating the nearest player to the user.
                If None, the game board to use must be set before execution using use_game_board().
        """
        self.__game_board: Optional[GameBoard] = game_board

    def _on_execute(self, user: PlayableCharacter) -> None:
        """Swap with the player that is closest to the user of the power if there is one and ends the users turn if
        a swap did occur.

        Args:
            user: The user of the power

        Raises:
            Exception if the game board to use was not set before execution.
        """
        if self.__game_board is None:
            raise Exception("The game board to use for the swap power was not set before execution.")

        closest_char: Optional[PlayableCharacter] = self.__game_board.get_closest_character(user)

        # if there was a closest character, swap and end turn. Otherwise dont swap and dont end turn.
        if closest_char is not None:
            self.__game_board.swap_characters(user, closest_char)
            user.set_should_continue_turn(False)

    def use_game_board(self, game_board: GameBoard) -> None:
        """Set the game board for the power to use to calculate the nearest player.

        Args:
            game_board: The game board to use.
        """
        self.__game_board = game_board
