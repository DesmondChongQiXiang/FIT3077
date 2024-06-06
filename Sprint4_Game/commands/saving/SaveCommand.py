from typing import TypeVar, Generic
from commands.Command import Command
from codec.saves.SaveCodec import SaveCodec

T = TypeVar("T")


class SaveCommand(Command, Generic[T]):
    """Command that when executes causes a save codec to perform a save.

    Author: Shen
    """

    def __init__(self, save_codec: SaveCodec[T]):
        """Constructor.

        Args:
            save_codec: The save codec that will perform the save
        """
        self.__save_codec: SaveCodec[T] = save_codec

    def execute(self) -> None:
        """Execute the save for the save codec."""
        return self.__save_codec.save()
