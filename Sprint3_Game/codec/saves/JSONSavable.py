from typing import Protocol, Any
from abc import abstractmethod


class JSONSavable(Protocol):
    """Implementers can receive python like JSON dictionaries for saving purposes.

    Author: Shen
    """

    @abstractmethod
    def on_save(self, to_write: dict[str, Any]) -> None:
        """Upon save, receive a json like python dictionary that can be edited. This json dictionary will be encoded
        into the save file, and as such must remain in a json encodable format.

        Warning: The dictionary must remain in json encodable format.

        Args:
            to_write: The dictionary that will be converted to the JSON save file.
        """
        ...
