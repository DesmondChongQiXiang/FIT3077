from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.characters.PlayableCharacterVariant import PlayableCharacterVariant
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.DrawProperties import DrawProperties
from typing import Optional


class Dragon(PlayableCharacter):
    """Represents a dragon character in the game.

    Author: Shen
    """

    def __init__(self, variant: PlayableCharacterVariant, draw_properties: Optional[DrawProperties] = None):
        """
        Args:
            variant: The variant of the dragon
            draw_properties (optional): The drawing properties specifying how to draw the dragon
        """
        super().__init__(variant, draw_properties)

    # TODO: Implement turn taking functionality
    def take_turn(self) -> None:
        pass

    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """Draw the dragon if the drawing properties have been specified. Otherwise draws nothing.

        Returns:
            The drawing instructions
        """
        draw_properties = self.get_draw_properties()
        if draw_properties is None:
            return []
        x, y = draw_properties.get_coordinates()

        return [DrawAssetInstruction(f"assets/characters/dragon/dragon_{self._variant.value}.png", x, y, draw_properties.get_size())]
