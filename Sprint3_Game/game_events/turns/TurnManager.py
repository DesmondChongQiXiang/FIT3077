from abc import ABC, abstractmethod
from game_objects.characters.PlayableCharacter import PlayableCharacter


class TurnManager(ABC):
    """Manages turns within the game. Inheritors can modify how turns are handled.

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
        self._current_player: PlayableCharacter = player_characters[starting_player_i]
        self._current_player_i: int = starting_player_i
        self._player_characters: list[PlayableCharacter] = player_characters

    def get_number_of_players(self) -> int:
        """Gets the number of players in the game.

        Returns:
            The number of players
        """
        return len(self._player_characters)

    def get_currently_playing_character(self) -> PlayableCharacter:
        """Gets the currently playing character.

        Returns:
            The currently playing character
        """
        return self._current_player

    @abstractmethod
    def skip_to_player(self, player_char: PlayableCharacter) -> None:
        """Skip to the playable character's turn.

        Args:
            player_char: The character for the player
        """
        ...

    @abstractmethod
    def get_player_character_n_turns_downstream(self, n: int) -> PlayableCharacter:
        """Get the playable character that is n turns downstream from the currently playing character.

        Args:
            n: How many turns downstream

        Returns:
            The playable character n turns downstream
        """
        ...

    @abstractmethod
    def tick(self) -> bool:
        """Called every tick of the game to process turns.

        Returns:
            Whether the current player's turn ended.
        """
        ...
