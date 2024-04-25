from Button import Button
import pygame
class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Fiery Dragons")
        self.clock = pygame.time.Clock()

    def get_font(self,size):
        return pygame.font.Font("../assets/font.ttf", size)

    def select_player_num_display(self):
        menu_background = pygame.image.load("../assets/menu background.jpg")
        menu_background = pygame.transform.scale(menu_background, (1280, 720))
        while True:
            self.screen.blit(menu_background, (0, 0))

            menu_mouse_pos = pygame.mouse.get_pos()

            start_game = self.get_font(100).render("START GAME", True, "#b68f40")
            start_game_rect = start_game.get_rect(center=(640, 75))

            option_button = pygame.image.load("../assets/Options Rect.png")

            two_players_button = Button(img=option_button, pos=(640, 250), font=self.get_font(50),
                                        text_input="2 PLAYERS", base_color="#d7fcd4", hovering_color="White")
            three_players_button = Button(img=option_button, pos=(640, 375), font=self.get_font(50),
                                          text_input="3 PLAYERS", base_color="#d7fcd4", hovering_color="White")
            four_players_button = Button(img=option_button, pos=(640, 500), font=self.get_font(50),
                                         text_input="4 PLAYERS", base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(start_game, start_game_rect)

            for button in [two_players_button, three_players_button, four_players_button]:
                button.change_color(menu_mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if two_players_button.check_forInput(menu_mouse_pos):
                        return 2
                    if three_players_button.check_forInput(menu_mouse_pos):
                        return 3
                    if four_players_button.check_forInput(menu_mouse_pos):
                        return 4
            pygame.display.update()
        self.clock.tick(60) #60fps








