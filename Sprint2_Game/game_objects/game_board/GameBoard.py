from abc import abstractmethod, ABC
from game_objects.tiles.Tile import Tile
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawableByAsset import DrawableByAsset
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.ModularClickableSprite import ModularClickableSprite
from game_events.MoveActionHandler import MoveActionHandler


class GameBoard(ABC, DrawableByAsset, MoveActionHandler):
    """Represents a game board that can be played on

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

    def on_move_action_fired(self, character: PlayableCharacter, steps: int) -> None:
        """Move the character by a number of steps.

        Args:
            character: The character which fired the move action
            steps: The steps the character should move
        """
        self.move_character_by_steps(character, steps)

    @abstractmethod
    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Get the instructions to draw the clickable assets of the game board.

        Returns:
            A list containing tuples in the form of (drawing instructions, object to return on click)
        """
        ...
