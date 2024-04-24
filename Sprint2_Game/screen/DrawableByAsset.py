from abc import abstractmethod
from typing import Protocol
from .DrawAssetInstruction import DrawAssetInstruction


class DrawableByAsset(Protocol):
    """Represents objects that can be drawn using assets on a pygame screen.

    Author: Shen
    """

    @abstractmethod
    def get_draw_assets_instructions(self) -> list[DrawAssetInstruction]:
        """Get the drawing instructions that draw the assets for the object."""
        ...


# References
# https://typing.readthedocs.io/en/latest/spec/protocol.html#explicitly-declaring-implementation
# https://stackoverflow.com/questions/71531417/defining-an-interface-in-python
# protocols are used for static-type checking only in python
