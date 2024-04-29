from constants import *
import threading
import pygame
"""
Fiery Dragon Game

This module defines the main game logic and functionality for the Fiery Dragon game.

Classes:
    Game: Represents the main game instance.

"""
class SingletonMeta(type):
    """
    Metaclass for implementing the Singleton design pattern.
    """
    _instances = {} # Dictionary to store instances of SingletonMeta
    _singleton_lock = threading.Lock() # Lock for thread safety

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._singleton_lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
class Game(metaclass=SingletonMeta):
    """
    Game Class

    Represents the main game instance.

    Attributes:
        chitcards (list): List of chit cards in the game.
        occupiables (list): List of occupiable item(tiles, caves).
        players (list): List of dragon token in the game.
        player_num (int): Number of players in the game.
        gameboard (GameBoard): Instance of the game board.
        menu (Menu): Instance of the game menu.
        FPS (int): Frames per second for the game.
        screen (pygame.Surface): Pygame surface representing the game screen.
    """

    def __init__(self,gameboard,menu):
        """
        Initializes the Game instance.

        Args:
            gameboard (GameBoard): Instance of the game board.
            menu (Menu): Instance of the game menu.
        """
        self.chitcards = []
        self.occupiables = []
        self.players = []
        self.player_num = -1
        self.gameboard = gameboard
        self.menu = menu
        self.FPS = 150
        pygame.init() # Initialize pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Create game screen
        pygame.display.set_caption("Fiery Dragon") # Set window caption

    def __select_player_num(self):
        """
        Private method to select the number of players for the game.
        """
        self.player_num = self.menu.select_player_num_display()

    def __initialise_game(self):
        """
        Private method to initialize the game components.
        """
        self.occupiables.extend(self.gameboard.create_tiles())  # Create game tiles
        self.chitcards.extend(self.gameboard.create_chit_cards()) # Create chit cards
        self.occupiables.extend(self.gameboard.create_caves(self.player_num)) # Create caves
        self.players.extend(self.gameboard.create_dragon_token(self.player_num)) # Create dragon tokens
    def __gameloop(self):
        """
        Private method representing the game loop.
        """
        running = True # Variable to control game loop
        clock = pygame.time.Clock() # Pygame clock for controlling FPS
        while running:
            clock.tick(self.FPS) # Limit the frame rate
            self.screen.fill((0,0,0))  # Fill the screen with black
            mouse_pos = pygame.mouse.get_pos() # Get mouse position
            for chitcard in self.chitcards:
                chitcard.change_backgroundcolor(mouse_pos) # Change background color of chit cards if player hovering over it
            for event in pygame.event.get(): # Event handling loop
                if event.type == pygame.QUIT: # Check for quit event
                    running = False # Exit game loop
                if event.type == pygame.MOUSEBUTTONDOWN: # Check for mouse button click
                    for chitcard in self.chitcards:
                        chitcard.flip(mouse_pos) # loop through each chit card to check the position is within the range of it
            self.gameboard.draw_gameboard() # Draw the game board
            pygame.display.update() # Update display
        pygame.quit() # Quit pygame

    def run(self):
        """
        Method to start and run the game.
        """
        self.__select_player_num()
        self.__initialise_game()
        self.__gameloop()







