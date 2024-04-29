from abc import ABC, abstractmethod # Import ABC and abstractmethod for defining abstract methods

class DrawableInterface(ABC):
    """
    DrawableInterface Class

    Interface for objects that can be drawn on the screen in a game.

    Methods:
        draw(self): Method to be implemented by subclasses for drawing the object.
    """
    @abstractmethod
    def draw(self):
        """
        Method to be implemented by subclasses for drawing the object.
        """
        pass
