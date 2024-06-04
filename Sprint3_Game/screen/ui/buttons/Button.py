from typing import Optional
from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.characters.PlayableCharacter import PlayableCharacter
from screen.ui.buttons.ButtonType import ButtonType

class Button(ModularClickableSprite):
    """A class that represents the buttons other than game_objects. 

    Author: Desmond
    """
    def __init__(self, button_type: ButtonType, draw_properties: Optional[DrawProperties] = None, enabled_click:bool = True) -> None:
        """
        Args:
            button_type: the type of button
            draw_properties (optional): Properties specifying how and where the button should be drawn
            enabled_click: 
        """
        self._button_type: ButtonType = button_type
        self.__enabled_click: bool = enabled_click
        self.__clicked: bool = False
        self._draw_properties: Optional[DrawProperties] = draw_properties

    def disable_clicks(self) -> None:
        """Disable user interaction with the button by mouse clicks."""
        self.__enabled = False

    def enable_mouse_clicks(self) -> None:
        """Enable user interaction with the button by mouse clicks."""
        self.__enabled = True

    def set_clicked(self, state: bool) -> None:
        """set the state of clicked"""
        self.__clicked = state
    
    def get_clicked(self) -> bool:
        """return the state of clicked"""
        return self.__clicked
    
    def get_enabled_clicked(self) -> bool:
        return self.__enabled_click

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

    def on_click(self, character: Optional[PlayableCharacter]) -> None:
        """On click, perform different effect based on the type of the current button

        Args:
            character: The character who clicked the sprite if any
        """
        self.__clicked = True
        if self._button_type.value == "new_game":
            pass
        elif self._button_type.value == "continue":
            # todo: loading saved game
            pass
        elif self._button_type.value == "save":
            # todo: saving current state of game
            pass
        

