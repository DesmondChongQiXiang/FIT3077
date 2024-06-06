from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic

T = TypeVar("T")


class SaveCodec(ABC, Generic[T]):
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
    def load(self) -> T:
        """Load data from the configured save path into a python readable format.
        
        Returns:
            The data in a python readable format.
        """
        ...

    @abstractmethod
    def save(self) -> None:
        """Save any stored data into the save path."""
        ...
