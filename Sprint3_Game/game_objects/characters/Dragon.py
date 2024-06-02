from __future__ import annotations
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
        """When requested on save, return a JSON compatible object describing this dragon. Location of the player is left
        None for later modification.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.

        Returns:
            A JSON compatible object describing the dragon
        """
        return {"type": ClassTypeIdentifier.player_dragon.value, "variant": self._variant.value, "name": self.name(), "location": None}

    @classmethod
    def create_from_json_save(cls, save_data: dict[str, Any]) -> Dragon:
        """Create a dragon based on player json save data.

        Args:
            save_data: The dictionary representing the JSON save data object for a player

        Returns:
            A dragon matching the save data
        """
        try:
            return cls(PlayableCharacterVariant(save_data["variant"]), save_data["name"])
        except:
            raise Exception(f"Save data must have attributes 'variant' and 'name'. Passed in={save_data}")
