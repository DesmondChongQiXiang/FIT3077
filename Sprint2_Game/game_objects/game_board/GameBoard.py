from abc import abstractmethod
from typing import Protocol
from game_objects.tiles.Tile import Tile
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.characters.PlayableCharacter import PlayableCharacter


class GameBoard(Protocol):
    """Represents a game board that can be played on"""

    @abstractmethod
    def move_character_by_steps(self, character: PlayableCharacter, steps: int) -> None:
        """Move a character by an integer number of steps on the game board.

        Args:
            character: The character
            steps: Number of steps to move
        """
        ...

    @abstractmethod
    def get_character_floor_tile(self, character: PlayableCharacter) -> Tile:
        """Get the floor tile the character is standing on.

        Args:
            character: The character
        """
        ...

    @abstractmethod
    def flip_chit_card(self, character: PlayableCharacter, chit_card: ChitCard) -> None:
        """Flip a chit card on the game board.

        Args:
            character: The character
            chit_chard: The chit card to flip
        """
        ...

    @abstractmethod
    def add_chit_card(self, chit_card: ChitCard) -> None:
        """Add a chit card to the game board.

        Args:
            chit_card: The chit card to add
        """
        ...


# References
# https://typing.readthedocs.io/en/latest/spec/protocol.html#explicitly-declaring-implementation
# https://stackoverflow.com/questions/71531417/defining-an-interface-in-python
# protocols are used for static-type checking only in python
