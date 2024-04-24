import pygame
from core.GameConfig import *
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.game_board.GameBoard import GameBoard



class GameWorld:
    """Initialises and manages a game instance. Provides the interface between it and the players."""

    def __init__(self, playable_characters: list[PlayableCharacter], chit_cards: list[ChitCard], game_board: GameBoard):
        self.playable_characters: list[PlayableCharacter] = playable_characters
        self.chit_cards: list[ChitCard] = chit_cards
        self.game_board: GameBoard = game_board

        self.__run()

    def __run(self) -> None:
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
