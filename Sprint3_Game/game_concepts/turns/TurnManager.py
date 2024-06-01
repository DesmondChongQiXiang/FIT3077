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
        self._player_char_to_i: dict[PlayableCharacter, int] = dict()

        # initialise player character to index dictionary
        for i, character in enumerate(self._player_characters):
            self._player_char_to_i[character] = i

        self._current_player.set_is_currently_playing(True)

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
    def skip_to_player_on_turn_end(self, player_char: PlayableCharacter) -> None:
        """Skip to the playable character's turn once the current player's turn ends.

        Args:
            player_char: The player's character to skip to
        """
        ...

    @abstractmethod
    def get_player_character_n_turns_downstream(self, n: int, character: PlayableCharacter) -> PlayableCharacter:
        """Get the playable character that is n turns downstream from another playable character.

        Args:
            n: How many turns downstream
            character: The playable character to track downstream from

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
