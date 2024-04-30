import pygame
from core.GameConfig import FRAMES_PER_SECOND, SCREEN_BACKGROUND_COLOUR
from core.singletons import PygameScreenController_instance
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.game_board.GameBoard import GameBoard
from screen.ModularClickableSprite import ModularClickableSprite


class GameWorld:
    """Initialises and manages a game instance. Provides the interface between it and the players.

    Author: Shen
    """

    def __init__(self, playable_characters: list[PlayableCharacter], game_board: GameBoard):
        """
        Args:
            playable_charcters: The list of playable characters to initialise the world (game) with
            game_board: The game board
        """
        self.__playable_characters: list[PlayableCharacter] = playable_characters
        self.__game_board: GameBoard = game_board

        self.__run()

    def __run(self) -> None:
        """Initialises the game on the active pygame screen and runs the main game loop.

        Warning: Pygame and its display must be initialised through pygame.init() and pygame.display.set_mode() before running.
        """
        clock = pygame.time.Clock()

        # GAME LOOP
        while True:
            # Handle Drawing
            pygame.display.get_surface().fill(SCREEN_BACKGROUND_COLOUR)

            PygameScreenController_instance().draw_assets_from_instructions(self.__game_board.get_draw_assets_instructions())
            hitboxes = PygameScreenController_instance().draw_clickable_assets_from_instructions(self.__game_board.get_draw_clickable_assets_instructions())

            # Handle Events
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:  # Handle closing of game
                        pygame.quit()
                        return

                    case pygame.MOUSEBUTTONDOWN:  # handle mouse click
                        self.__handle_clickables_on_mouse_click(hitboxes)

            # Update screen & Set FPS
            pygame.display.flip()  # update screen
            clock.tick(FRAMES_PER_SECOND)

    def __handle_clickables_on_mouse_click(self, hitboxes: list[tuple[pygame.Rect, ModularClickableSprite]]) -> None:
        """Fires on_click() for any clickable that was clicked.

        Args:
            hitboxes: A list of tuples of form (rectangular hitbox, object associated with hitbox)
        """
        for rect, clickable in hitboxes:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                clickable.on_click()
