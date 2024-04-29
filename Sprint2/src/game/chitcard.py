import pygame.image # Import pygame.image for loading images
from .constants import CELL_WIDTH,CELL_HEIGHT # Import constants for cell width and height
from .game import Game
from .drawableinterface import DrawableInterface # Import the DrawableInterface class for drawing objects
import os

CHITCARD_WIDTH = CELL_WIDTH - 5 # Define the width of a chit card
CHITCARD_HEIGHT = CELL_HEIGHT - 5 # Define the height of a chit card

class ChitCard(DrawableInterface):
    """
    ChitCard Class

    Represents a chit card in the game.

    Attributes:
        animal (Animal): Animal type represented by the chit card.
        x_pos (int): X-coordinate position of the chit card on the game screen.
        y_pos (int): Y-coordinate position of the chit card on the game screen.
        animal_quantity (int): Quantity of the animal on the chit card.
        is_flipped (bool): Flag indicating whether the chit card is flipped.
        image (pygame.Surface): Surface representing the flipped image of the chit card.
        unflipped_image (pygame.Surface): Surface representing the unflipped image of the chit card.
    """
    def __init__(self, animal,x_pos,y_pos,animal_quantity):
        """
        Initializes the ChitCard instance.

        Args:
            animal (Animal): Animal type represented by the chit card.
            x_pos (int): X-coordinate position of the chit card on the game screen.
            y_pos (int): Y-coordinate position of the chit card on the game screen.
            animal_quantity (int): Quantity of the animal on the chit card.
        """
        self.animal = animal # Set the animal type represented by the chit card
        self.x_pos = x_pos # Set the x-coordinate position of the chit card
        self.y_pos = y_pos # Set the y-coordinate position of the chit card
        self.animal_quantity = animal_quantity  # Set the quantity of the animal on the chit card
        self.is_flipped = False # Initialize the chit card as not flipped
        # Load the flipped image of the chit card and scale it to the specified width and height
        ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
        image = pygame.image.load(f"{ROOT_PATH}/assets/{str(animal_quantity)}{animal.name}chitcard.png").convert_alpha() # load with animal quantity and animal name
        self.image = pygame.transform.scale(image, (CHITCARD_WIDTH, CHITCARD_HEIGHT))
        # Load the unflipped image of the chit card and scale it to the specified width and height
        unflipped_image =pygame.image.load(f"{ROOT_PATH}/assets/unflippedchitcard.png")
        self.unflipped_image = pygame.transform.scale(unflipped_image, (CHITCARD_WIDTH, CHITCARD_HEIGHT))


    def draw(self):
        """
        Draws the chit card on the game screen.
        """
        if self.is_flipped: # If the chit card is flipped, blit its flipped image
            Game.screen.blit(self.image, (self.x_pos + 2, self.y_pos + 2))
        else: # Otherwise, blit its unflipped image
            Game.screen.blit(self.unflipped_image, (self.x_pos + 2, self.y_pos + 2))

    def change_backgroundcolor(self,pos):
        """
        Changes the background color of the chit card when hovered over by the mouse.

        Args:
            pos (tuple): Current mouse position.
        """
        if pos[0] in range(self.x_pos,self.x_pos+CHITCARD_WIDTH) and pos[1] in range(self.y_pos,self.y_pos+CHITCARD_HEIGHT):
            # Draw a red rectangle to indicate the hover effect
            pygame.draw.rect(Game.screen, (255, 0, 0), pygame.Rect(self.x_pos,self.y_pos, CHITCARD_WIDTH, CHITCARD_HEIGHT))

    def flip(self,pos):
        """
        check the clicked mouse position is within the range
        if it is clicked, flips the chit card

        Args:
            pos (tuple): Current mouse position.
        """
        if pos[0] in range(self.x_pos,self.x_pos+CHITCARD_WIDTH) and pos[1] in range(self.y_pos,self.y_pos+CHITCARD_HEIGHT):
            self.is_flipped = not self.is_flipped # Toggle the flipped state of the chit card

class BackwardChitCard(ChitCard):
    """
    BackwardChitCard Class

    Represents a backward-moving chit card in the game, which typically moves the dragon token backward.

    Inherits from:
        ChitCard
    """

    def __init__(self, animal, x_pos, y_pos, animal_quantity):
        """
        Initializes the BackwardChitCard instance.

        Args:
            animal (Animal): Animal type represented by the chit card.
            x_pos (int): X-coordinate position of the chit card on the game screen.
            y_pos (int): Y-coordinate position of the chit card on the game screen.
            animal_quantity (int): Quantity of the animal on the chit card.
        """
        super().__init__(animal, x_pos, y_pos, animal_quantity)  # Call the superclass constructor

class ForwardChitCard(ChitCard):
    """
    ForwardChitCard Class

    Represents a forward-moving chit card in the game, which typically advances the dragon token.

    Inherits from:
        ChitCard
    """

    def __init__(self, animal, x_pos, y_pos, animal_quantity):
        """
        Initializes the ForwardChitCard instance.

        Args:
            animal (Animal): Animal type represented by the chit card.
            x_pos (int): X-coordinate position of the chit card on the game screen.
            y_pos (int): Y-coordinate position of the chit card on the game screen.
            animal_quantity (int): Quantity of the animal on the chit card.
        """
        super().__init__(animal, x_pos, y_pos, animal_quantity)  # Call the superclass constructor



