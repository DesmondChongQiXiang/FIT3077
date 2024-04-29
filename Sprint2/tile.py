from animal import Animal # Import the Animal enum for representing types of animals
from constants import CELL_WIDTH,CELL_HEIGHT # Import constants for cell width and height
import pygame # Import the pygame module for game development
from game import Game # Import the Game class
from drawableinterface import DrawableInterface # Import the DrawableInterface class for drawing objects

TILE_WIDTH = CELL_WIDTH - 5 # Define the width of a tile
TILE_HEIGHT = CELL_HEIGHT - 5 # Define the height of a tile

class Tile(DrawableInterface):
    """
    Tile Class

    Represents a tile with a specific animal on it in the game.

    Attributes:
        animal (Animal): The type of animal represented by the tile.
        x_pos (int): X-coordinate position of the tile on the game screen.
        y_pos (int): Y-coordinate position of the tile on the game screen.
    """
    def __init__(self,animal:Animal,x_pos,y_pos):
        """
        Initializes the Tile instance.

        Args:
            animal (Animal): The type of animal represented by the tile.
            x_pos (int): X-coordinate position of the tile on the game screen.
            y_pos (int): Y-coordinate position of the tile on the game screen.
        """
        self.animal = animal # Set the type of animal represented by the tile
        self.x_pos = x_pos # Set the x-coordinate position of the tile
        self.y_pos = y_pos # Set the y-coordinate position of the tile

    def draw(self):
        # Load the image of the tile corresponding to the animal and scale it to the specified width and height
        image = pygame.image.load("assets/{}tile.png".format(self.animal.name)).convert_alpha() # find the tile image using animal name
        image = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))
        game = Game()# Create a Game instance
        # Blit the image of the tile onto the game screen at the specified position
        game.screen.blit(image, (self.x_pos + 2, self.y_pos + 2))