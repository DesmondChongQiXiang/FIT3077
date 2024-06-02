from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.PlayableCharacterVariant import PlayableCharacterVariant
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.DrawProperties import DrawProperties
from factories.ClassTypeIdentifier import ClassTypeIdentifier
from typing import Optional, Any


class Dragon(PlayableCharacter):
    """Represents a dragon character in the game.

    Author: Shen
    """

    __TURN_ROTATE_SPEED: float = 1.5  # speed at which the sprite should rotate anti-clockwise during the dragon's turn

    def __init__(self, variant: PlayableCharacterVariant, name: str, draw_properties: Optional[DrawProperties] = None):
        """
        Args:
            variant: The variant of the dragon
            name: The name of the character
            draw_properties (optional): The drawing properties specifying how to draw the dragon
        """
        self.__draw_rotation: float = 0

        super().__init__(variant, name, draw_properties)

    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """Draw the dragon if the drawing properties have been specified. Otherwise draws nothing. A dragon who is currently
        taking its turn will rotate slowly anticlockwise, otherwise, it will use it standard appearance (not rotated).

        Returns:
            The drawing instructions
        """
        draw_properties = self._draw_properties
        if draw_properties is None:
            return []
        x, y = draw_properties.get_coordinates()

        # Turn sprite anticlockwise whilst playing. Otherwise draw at normal rotation (none).
        if self._is_currently_playing:
            self.__draw_rotation += Dragon.__TURN_ROTATE_SPEED
        else:
            self.__draw_rotation = 0

        return [DrawAssetInstruction(f"assets/characters/dragon/dragon_{self._variant.value}.png", x, y, draw_properties.get_size(), self.__draw_rotation)]

    def on_save(self, to_write: dict[str, Any]) -> Optional[Any]:
        """When requested on save, add the object describing the dragon to the respective player list. Location of the player is left
        None for later modification.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.

        Returns:
            None
            
        Raises:
            Exception if player_data.players did not exist in the writing dictionary before the request
        """
        try:
            players_list: list[Any] = to_write["player_data"]["players"]
        except Exception:
            raise Exception(f"player_data.players did not exist before issuing save request for this dragon. name={self.name()}")

        players_list.append({"type": ClassTypeIdentifier.player_dragon.value, "variant": self._variant.value, "name": self.name(), "location": None})
