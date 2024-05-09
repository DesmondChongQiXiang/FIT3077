class SingletonMeta(type):
    """Meta class for creating a singleton. Instantiating another class, even with different parameters will
    always return the original singleton."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Instantiate the class defining their metaclass as this class.

        Args:
            cls: The class SingletonMeta (the class this function is defined in)
            *args, **kwargs: Arguments and key-word arguments passed in to instantiate class
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)  # create the class object
            cls._instances[cls] = instance
        return cls._instances[cls]


# ADAPTED FROM: https://refactoring.guru/design-patterns/singleton/python/example#example-0
