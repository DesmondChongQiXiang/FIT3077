from game_concepts.turns.TurnManager import TurnManager
from game_objects.characters.PlayableCharacter import PlayableCharacter


class DefaultTurnManger(TurnManager):
    """Turn manager that executes and manages changes of turns as expected. It does not intervene or perform any special
    effects when a player's turn should end.

    Author: Shen
    """

    def __init__(self, player_characters: list[PlayableCharacter], starting_player_i: int) -> None:
        """
        Constructor.

        Args:
            player_characters: List containing the player's characters
            starting_player_i: The index for playable_characters of the starting character

        Raises:
            Exception if starting_player_i is invalid when playable_characters is indexed by it
        """
        super().__init__(player_characters, starting_player_i)

    def skip_to_player_on_turn_end(self, player_char: PlayableCharacter) -> None:
        """Skip to the playable character's turn once the current player's turn ends.

        Args:
            player_char: The player's character to skip to
        """
        for i in range(self._current_player_i + 1, self._current_player_i + len(self._player_characters)):
            current_char: PlayableCharacter = self._player_characters[i % len(self._player_characters)]
            if current_char == player_char:
                return
            current_char.set_should_continue_turn(False)

    def get_player_character_n_turns_downstream(self, n: int) -> PlayableCharacter:
        """Get the playable character that is n turns downstream from the currently playing character.

        Args:
            n: How many turns downstream

        Returns:
            The playable character n turns downstream
        """
        return self._player_characters[(self._current_player_i + n) % len(self._player_characters)]

    def tick(self) -> bool:
        """On game tick, ends the player's turn if it should end and transitions to the next player's turn.

        Returns:
            Whether the current player's turn ended.
        """
        if not self._current_player.should_continue_turn():
            self.__configure_current_player_for_turn_change()

            # roll to next player's turn
            self._current_player_i = (self._current_player_i + 1) % len(self._player_characters)
            self._current_player = self._player_characters[self._current_player_i]

            self._current_player.set_is_currently_playing(True)
            return True

        return False

    # ---------- Class methods ---------------------------------------------------------------------------------------------------
    def __configure_current_player_for_turn_change(self) -> None:
        """Perform any required configurations to the current player immediately before their turn ends."""
        self._current_player.set_is_currently_playing(False)
        self._current_player.set_should_continue_turn(True)  # reset for the playable character's next turn
