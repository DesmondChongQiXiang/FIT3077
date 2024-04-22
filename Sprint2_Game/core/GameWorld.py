import pygame
from core.GameConfig import *


class GameWorld:
    """Initialises and manages a game instance. Provides the interface between it and the players."""

    def __init__(self):
        self.__run()

    def __run(self):
        """Creates the game instance, and runs the main game loop."""
        pygame.init()
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        # game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            pygame.display.flip()  # update screen
            clock.tick(FRAMES_PER_SECOND)
