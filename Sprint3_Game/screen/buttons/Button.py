from typing import Optional
from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.buttons.ButtonType import ButtonType


class Button(ModularClickableSprite):
    """A class that represents the buttons other than gameo_bjects. 

    Author: Desmond
    """
    def __init__(self, button_type: ButtonType, draw_properties: Optional[DrawProperties] = None) -> None:
        """
        Args:
            button_type: the type of button
            draw_properties (optional): Properties specifying how and where the button should be drawn
        """
        self._button_type: ButtonType = button_type
        self._draw_properties: Optional[DrawProperties] = draw_properties

    def set_draw_properties(self, draw_properties: DrawProperties) -> None:
        """Set how the button should be drawn.

        Args:
            draw_properties: The draw properties
        """
        self._draw_properties = draw_properties

    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """Get the instructions required to draw the button

        Returns:
            A list containing tuples in the form of (drawing instruction, object to return when clicking on
            graphic represented by instruction)

        Raises:
            Exception if the draw properties were not set prior to a request to draw.
        """
        if self._draw_properties is None:
            raise Exception("Tried drawing, but the draw properties (properties required for drawing) weren't set.")
        return self._on_draw_request(self._draw_properties)

    def _on_draw_request(self, draw_properties: DrawProperties) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        """On draw request, returns instructions to draw a button that displays based on the type of button

        Args:
            draw_properties: The draw properties requesting how to draw this object

        Returns:
            A list containing tuples in the form of (drawing instruction, object to return when clicking on
            graphic represented by instruction)
        """
        asset_path: str = "assets/menu"
        coord_x, coord_y = draw_properties.get_coordinates()

        return [
            (
                DrawAssetInstruction(
                    f"{asset_path}/{self._button_type.value}.png",
                    x=coord_x,
                    y=coord_y,
                    size=draw_properties.get_size(),
                ),
                self,
            )
        ]

    def on_click(self, character: PlayableCharacter) -> None:
        """On click, perform different effect based on the type of the current button

        Args:
            character: The character who clicked the sprite
        """
        if self._button_type.value == "new_game":
            pass
        elif self._button_type.value == "continue":
            # todo: loading saved game
            pass
        elif self._button_type.value == "save":
            # todo: saving current state of game
            pass

