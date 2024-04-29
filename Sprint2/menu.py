import pygame
from game import Game
class Menu:
    """
    Menu Class

    Represents the menu interface for selecting the number of players.

    Methods:
        select_player_num_display: Displays the menu and allows the player to select the number of players.
        __game_title_display: Displays the game title.
        __draw_select_player_button: Draws a button for selecting the number of players.
        __check_button_is_clicked: Checks if a button is clicked.
    """
    def select_player_num_display(self):
        """
        Displays the menu and allows the player to select the number of players.

        Returns:
            int: Number of players selected.
        """
        while True: # Loop indefinitely until a valid player number is selected
            game = Game() # Create a Game instance to get the screen
            game.screen.fill((0,0,0)) # Fill the game screen with black
            self.__game_title_display() # Display the game title

            # Draw buttons for selecting the number of players
            two_player_button_rect = self.__draw_select_player_button("2 PLAYERS",(640,250))
            three_player_button_rect = self.__draw_select_player_button("3 PLAYERS",(640,375))
            four_player_button_rect = self.__draw_select_player_button("4 PLAYERS",(640,500))

            mouse_pos = pygame.mouse.get_pos() # Get the current mouse position

            for event in pygame.event.get(): # Check for events
                if event.type == pygame.QUIT: # If the user quits, exit the game
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN: # If a mouse button is clicked
                    # Check which button is clicked and return the corresponding number of players
                    if self.__check_button_is_clicked(two_player_button_rect,mouse_pos):
                        return 2
                    if self.__check_button_is_clicked(three_player_button_rect,mouse_pos):
                        return 3
                    if self.__check_button_is_clicked(four_player_button_rect,mouse_pos):
                        return 4
            pygame.display.update() # Update the display
        self.clock.tick(60) # Limit frame rate to 60 FPS

    def __game_title_display(self):
        """
        Displays the game title.
        """
        # Render the game title text
        start_game =  pygame.font.Font("assets/font.ttf", 100).render("FIERY DRAGON", True, "#b68f40")
        start_game_rect = start_game.get_rect(center=(640, 75)) # Get the rectangle for the title text
        game = Game() # Create a Game instance to use the screen
        game.screen.blit(start_game, start_game_rect) # Blit the title text onto the game screen

    def __draw_select_player_button(self,text,button_pos):
        """
        Draws a button for selecting the number of players.

        Args:
            text (str): Text to display on the button.
            button_pos (tuple): Position of the button.

        Returns:
            pygame.Rect: Rect object representing the button.
        """
        option_button = pygame.image.load("assets/Options Rect.png") # Load the button image
        option_button_rect = option_button.get_rect(center=(button_pos)) # Get the rectangle for the button
        game = Game() # Create a Game instance
        game.screen.blit(option_button,option_button_rect) # Blit the button image onto the game screen
        text = pygame.font.Font("assets/font.ttf", 50).render(text, True, "#d7fcd4") # Render the button text
        text_rect = text.get_rect(center=(button_pos)) # Get the rectangle for the button text
        game.screen.blit(text,text_rect) # Blit the button text onto the game screen
        return option_button_rect # Return the rectangle representing the button

    def __check_button_is_clicked(self,button_rect,mouse_pos):
        """
        Checks if a button is clicked.

        Args:
            button_rect (pygame.Rect): Rect object representing the button.
            mouse_pos (tuple): Current mouse position.

        Returns:
            bool: True if the button is clicked, False otherwise.
        """
        # Check if the mouse position is within the button rectangle boundaries
        if mouse_pos[0] in range(button_rect.left, button_rect.right) and mouse_pos[1] in range(button_rect.top,button_rect.bottom):
            return True # Return True if the button is clicked
        return False # Return False if the button is not clicked



