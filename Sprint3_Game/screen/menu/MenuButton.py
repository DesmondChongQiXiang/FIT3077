from typing import Optional
from screen.ModularClickableSprite import ModularClickableSprite
from screen.DrawProperties import DrawProperties
from screen.DrawAssetInstruction import DrawAssetInstruction
from game_objects.characters.PlayableCharacter import PlayableCharacter

class MenuButton(ModularClickableSprite):
    def __init__(self, display_word: str, draw_properties: Optional[DrawProperties] = None) -> None:
        self._display_word: str = display_word
        self._draw_properties: Optional[DrawProperties] = draw_properties

    def set_draw_properties(self, draw_properties: DrawProperties) -> None:
        self._draw_properties = draw_properties

    def get_draw_clickable_assets_instructions(self) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        if self._draw_properties is None:
            raise Exception("Tried drawing, but the draw properties (properties required for drawing) weren't set.")
        return self._on_draw_request(self._draw_properties)

    def _on_draw_request(self, draw_properties: DrawProperties) -> list[tuple[DrawAssetInstruction, ModularClickableSprite]]:
        asset_path: str = "assets/menu"
        coord_x, coord_y = draw_properties.get_coordinates()

        return [
            (
                DrawAssetInstruction(
                    f"{asset_path}/{self._display_word}.png",
                    x=coord_x,
                    y=coord_y,
                    size=draw_properties.get_size(),
                ),
                self,
            )
        ]

    def on_click(self, character: PlayableCharacter) -> None:
        pass

