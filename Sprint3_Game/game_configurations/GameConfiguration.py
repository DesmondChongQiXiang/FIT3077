from typing import Protocol
from abc import abstractmethod
from core.GameWorld import GameWorld
from codec.saves.JSONSaveable import JSONSaveable


class GameConfiguration(JSONSaveable, Protocol):
    """Represents a pre-defined configuration that can be used to generate a game instance. Game configurations are
    saveable as JSONs.

    Author: Shen
    """

    @abstractmethod
    def generate_game_world(self) -> GameWorld:
        """Generate the game world with the configuration.

        Returns:
            The generated game world
        """
        ...
