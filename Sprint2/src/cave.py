import pygame
from constants import CELL_WIDTH,CELL_HEIGHT  # Import constants for cell width and height
from game import Game
from drawableinterface import DrawableInterface # Import the DrawableInterface class for drawing objects
CAVE_WIDTH = CELL_WIDTH - 5 # Define the width of the cave
CAVE_HEIGHT = CELL_HEIGHT - 5 # Define the height of the cave
class Cave(DrawableInterface): # implement DrawableInterface
    """
    Cave Class

    Represents a cave in the game.

    Attributes:
        id (int): Unique identifier for the cave.
        animal (Animal): Animal type present in the cave.
        x_pos (int): X-coordinate position of the cave on the game screen.
        y_pos (int): Y-coordinate position of the cave on the game screen.
        image (pygame.Surface): Surface representing the image of the cave.
    """
    def __init__(self,id,animal,pos):
        """
        Initializes the Cave instance.

        Args:
            id (int): Unique identifier for the cave.
            animal (Animal): Animal type present in the cave.
            pos (tuple): Position of the cave on the game screen (x, y).
        """
        self.id = id # Set the unique identifier for the cave
        self.animal = animal # Set the animal type present in the cave
        self.x_pos = pos[0] # Set the x-coordinate position of the cave
        self.y_pos = pos[1] # Set the y-coordinate position of the cave
        # Load the image of the cave and scale it to the specified width and height
        image = pygame.image.load("../assets/cave{}.png".format(self.id)).convert_alpha() # load with the id
        self.image = pygame.transform.scale(image, (CAVE_WIDTH, CAVE_HEIGHT))

    def draw(self):
        """
        Draws the cave on the game screen.
        """
        game = Game() # Create a Game instance to get the screen
        # Blit the image of the cave onto the game screen at the specified position
        game.screen.blit(self.image, (self.x_pos + 2, self.y_pos + 2))