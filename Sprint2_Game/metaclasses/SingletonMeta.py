class SingletonMeta(type):
    """Metaclass that allows for only one instance of each class user. Instantiating another instance of the same class,
    even with different parameters will always return the original singleton."""

    _instances = {}  # static class variable keeping track of all the singletons of varying classes

    def __call__(cls, *args, **kwargs):
        """Instantiate the class defining their metaclass as this class.

        Args:
            cls: The class using SingletonMeta
            *args, **kwargs: Arguments and key-word arguments passed in to instantiate class
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)  # create the class object
            cls._instances[cls] = instance
        return cls._instances[cls]


# ADAPTED FROM: https://refactoring.guru/design-patterns/singleton/python/example#example-0
