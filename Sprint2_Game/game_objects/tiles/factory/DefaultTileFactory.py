from game_objects.animals.Animal import Animal
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.tiles.NormalTile import NormalTile
from game_objects.tiles.CaveTile import CaveTile
from game_objects.tiles.factory.TileFactory import TileFactory
from typing import Optional


class DefaultTileFactory(TileFactory):
    """Factory that creates the default forms of the Tiles.

    Author: Shen
    """

    def create_normal_tile(self, coordinates: tuple[int, int], size: tuple[int, int], animal: Animal, character: Optional[PlayableCharacter]) -> NormalTile:
        """Creates a NormalTile.

        Args:
            coordinates: Coordinates for the tile in form (x, y)
            size: Size of the tile in pixels in the form (width, height)
            animal: The animal to associate with the tile
            character (optional): The playable character to place on the tile

        Returns:
            A NormalTile instance
        """
        return NormalTile(coordinates, size, animal, character)

    def create_cave_tile(self, coordinates: tuple[int, int], size: tuple[int, int], character: Optional[PlayableCharacter]) -> CaveTile:
        """Creates a CaveTile.

        Args:
            coordinates: Coordinates for the tile in form (x, y)
            size: Size of the tile in pixels in the form (width, height)
            animal: The animal to associate with the tile
            character (optional): The playable character to place on the tile

        Returns:
            A CaveTile instance"""
        return CaveTile(coordinates, size, character)
