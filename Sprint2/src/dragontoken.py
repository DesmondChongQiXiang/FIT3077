import pygame
from constants import CELL_WIDTH,CELL_HEIGHT # Import constants for cell width and height
from game import Game # Import the Game class
from drawableinterface import DrawableInterface # Import the DrawableInterface class for drawing objects
import os

DRAGONTOKEN_WIDTH = CELL_WIDTH - 5 # Define the width of a dragon token
DRAGONTOKEN_HEIGHT = CELL_HEIGHT - 5 # Define the height of a dragon token
class DragonToken(DrawableInterface):
    """
    DragonToken Class

    Represents a dragon token/player in the game.

    Attributes:
        id (int): Unique identifier for the dragon token.
        x_pos (int): X-coordinate position of the dragon token on the game screen.
        y_pos (int): Y-coordinate position of the dragon token on the game screen.
        image (pygame.Surface): Surface representing the image of the dragon token.
    """
    def __init__(self,id,pos):
        """
        Initializes the DragonToken instance.

        Args:
            id (int): Unique identifier for the dragon token.
            pos (tuple): Position of the dragon token on the game screen (x, y).
        """
        self.id = id # Set the unique identifier for the dragon token
        self.x_pos = pos[0] # Set the x-coordinate position of the dragon token
        self.y_pos = pos[1] # Set the y-coordinate position of the dragon token
        # Load the image of the dragon token and scale it to the specified width and height
        ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
        image = pygame.image.load(f"{ROOT_PATH}/assets/dragontoken{str(self.id)}.png").convert_alpha()
        self.image = pygame.transform.scale(image, (DRAGONTOKEN_WIDTH, DRAGONTOKEN_HEIGHT))

    def draw(self):
        # Blit the image of the dragon token onto the game screen at the specified position
        Game.screen.blit(self.image, (self.x_pos +2, self.y_pos+2))