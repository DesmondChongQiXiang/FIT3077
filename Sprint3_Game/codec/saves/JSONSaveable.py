from typing import Protocol, Any
from abc import abstractmethod


class JSONSaveable(Protocol):
    """Implementers can receive python like JSON dictionaries for loading/saving purposes.

    Author: Shen
    """

    @abstractmethod
    def on_save(self, to_write: dict[str, Any]) -> None:
        """Upon save, receive a json like python dictionary that can be edited. This json dictionary will be encoded,
        and as such must remain in a json encodable format.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to JSON.
        """
        ...

    @abstractmethod
    def on_load(self, loaded_data: dict[str, Any]) -> None:
        """Upon load, load from the loaded JSON data.

        Args:
            loaded_data: The dictionary representing the loaded JSON.
        """
        ...
