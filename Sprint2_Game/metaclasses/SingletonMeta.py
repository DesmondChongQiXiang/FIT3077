from __future__ import annotations
from typing import Any, Optional


class SingletonMeta(type):
    """Metaclass that allows for only one instance of each class user. Instantiating another instance of the same class,
    even with different parameters will always return the original singleton.

    Author: Shen
    """

    _singletons: dict[SingletonMeta, SingletonMeta] = {}  # static class variable keeping track of all the singletons of varying classes

    def __call__(cls, *args, **kwargs):
        """Instantiate the class defining their metaclass as this class.

        Args:
            cls: The class using the SingletonMeta
            *args, **kwargs: Arguments and key-word arguments passed in to instantiate class
        """
        if cls not in cls._singletons:
            cls._singletons[cls] = super().__call__(*args, **kwargs)  # create the class object
        return cls._singletons[cls]

    def _get_existing_instance(self, cls: SingletonMeta) -> Optional[SingletonMeta]:
        """Gets the existing singleton instance if it exists. Otherwise returns None.

        Args:
            cls: The class of the singleton

        Returns:
            The singleton for the class if it exists.
        """
        if cls in self._singletons:
            return self._singletons[cls]
        return None


# ADAPTED FROM: https://refactoring.guru/design-patterns/singleton/python/example
