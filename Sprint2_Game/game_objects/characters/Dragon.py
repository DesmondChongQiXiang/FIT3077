from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.DrawAssetInstruction import DrawAssetInstruction
from screen.DrawProperties import DrawProperties
from typing import Optional


class Dragon(PlayableCharacter):
    """Represents a dragon character in the game.

    Author: Shen
    """

    def __init__(self, draw_properties: Optional[DrawProperties] = None):
        """
        Args:
            draw_properties (optional): The drawing properties specifying how to draw the character
        """
        super().__init__(draw_properties)

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

        return [DrawAssetInstruction("assets/characters/dragon.png", x, y, draw_properties.get_size())]
