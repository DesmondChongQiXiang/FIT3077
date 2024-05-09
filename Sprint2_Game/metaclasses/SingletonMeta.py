class SingletonMeta(type):
    """Metaclass that allows for only one instance of each class user. Instantiating another instance of the same class,
    even with different parameters will always return the original singleton.

    Author: Shen
    """

    __singletons = {}  # static class variable keeping track of all the singletons of varying classes

    def __call__(cls, *args, **kwargs):
        """Instantiate the class defining their metaclass as this class.

        Args:
            cls: The class using the SingletonMeta
            *args, **kwargs: Arguments and key-word arguments passed in to instantiate class
        """
        if cls not in cls.__singletons:
            cls.__singletons[cls] = super().__call__(*args, **kwargs)  # create the class object
        return cls.__singletons[cls]

# ADAPTED FROM: https://refactoring.guru/design-patterns/singleton/python/example 