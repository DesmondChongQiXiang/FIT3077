from typing import Optional
from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.characters.PlayableCharacter import PlayableCharacter
from commands.Command import Command


class Button(ModularClickableSprite):
    """A class that represents the buttons other than game_objects.

    Author: Desmond
    """

    def __init__(self, asset_path: str, command: Command, draw_properties: Optional[DrawProperties] = None) -> None:
        """
        Args:
            asset_path: The asset relative to the root of the project to use for drawing the button
            command: The command for the button to execute on click
            draw_properties (optional): Properties specifying how and where the button should be drawn
        """
        self.__asset_path = asset_path
        self.__command: Command = command
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
        coord_x, coord_y = draw_properties.get_coordinates()

        return [
            (
                DrawAssetInstruction(
                    self.__asset_path,
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
        if self.__command is not None:  # TEMP: Placeholder for once loading is figured out
            self.__command.execute()
