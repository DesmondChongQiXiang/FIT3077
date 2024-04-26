import pygame
from core.GameConfig import *
from core.singletons import PygameScreenController_instance
from game_objects.characters.PlayableCharacter import PlayableCharacter
from game_objects.chit_cards.ChitCard import ChitCard
from game_objects.game_board.GameBoard import GameBoard
from screen.ModularClickableSprite import ModularClickableSprite


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
            pygame.display.get_surface().fill("white")

            PygameScreenController_instance().draw_assets_from_instructions(self.game_board.get_draw_assets_instructions())
            hitboxes = PygameScreenController_instance().draw_clickable_assets_from_instructions(self.chit_cards[0].get_draw_clickable_assets_instructions())

            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:  # Handle closing of game
                        pygame.quit()
                        return

                    case pygame.MOUSEBUTTONDOWN:  # handle mouse click
                        self.__handle_clickables_on_mouse_click(hitboxes)

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
