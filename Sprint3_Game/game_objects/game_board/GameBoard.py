from abc import abstractmethod, ABC
from typing import Optional
from collections.abc import Sequence
from game_objects.tiles.Tile import Tile
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite


class GameBoard(ABC, DrawableByAsset):
    """Represents a game board that can be played on. Players can be placed on the board, and chit cards are used to
    interact with the game board.

    Author: Shen
    """

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
    def on_player_turn_end(self) -> None:
        """Perform any configuration to the game board a player's turn ends. Called when a player's turn ends."""
        ...

    @abstractmethod
    def get_all_clickable_sprites(self) -> Sequence[ModularClickableSprite]:
        """Get a read-only list all the clickable sprites for the game board.

        Returns:
            A read-only list containing all the clickable sprites.
        """
        ...

    
    @abstractmethod
    def get_closest_player(self, character:PlayableCharacter) -> Optional[int]:
        """
        Get's the player closest to the player passed into the function

        Returns:
            The tile the player occupied by the player closest to the player that is not in a cave
        """

    @abstractmethod
    def swap_with_closest_player(self,character:PlayableCharacter) -> None:
        """
        Swaps a player with the player closest to them
        """
