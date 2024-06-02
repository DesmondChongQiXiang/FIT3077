from abc import ABC, abstractmethod


class SaveCodec(ABC):
    """Represents a codec that can encode/decode from a save file.

    Author: Shen
    """

    def __init__(self, save_path: str):
        """Constructor.

        Args:
            save_path: The directory path relative to the root of the project to save the json file to.
        """
        self._save_path: str = save_path

    @abstractmethod
    def load(self) -> None:
        """Load data from the configured save path, and do something with it."""
        ...

    @abstractmethod
    def save(self) -> None:
        """Save any stored data into the save path."""
        ...
