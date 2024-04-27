import pygame

class Menu:
    def select_player_num_display(self,screen):
        while True:
            screen.fill((0,0,0))
            self.__start_game_display(screen)
            two_player_button_rect = self.__draw_select_player_button(screen,"2 PLAYERS",(640,250))
            three_player_button_rect = self.__draw_select_player_button(screen, "3 PLAYERS",(640,375))
            four_player_button_rect = self.__draw_select_player_button(screen, "4 PLAYERS",(640,500))

            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__check_button_is_clicked(two_player_button_rect,mouse_pos):
                        return 2
                    if self.__check_button_is_clicked(three_player_button_rect,mouse_pos):
                        return 3
                    if self.__check_button_is_clicked(four_player_button_rect,mouse_pos):
                        return 4
            pygame.display.update()
        self.clock.tick(60)

    def __start_game_display(self,screen):
        start_game =  pygame.font.Font("../assets/font.ttf", 100).render("START GAME", True, "#b68f40")
        start_game_rect = start_game.get_rect(center=(640, 75))
        screen.blit(start_game, start_game_rect)

    def __draw_select_player_button(self,screen,text,button_pos):
        option_button = pygame.image.load("../assets/Options Rect.png")
        option_button_rect = option_button.get_rect(center=(button_pos))
        screen.blit(option_button,option_button_rect)
        text = pygame.font.Font("../assets/font.ttf", 50).render(text, True, "#d7fcd4")
        text_rect = text.get_rect(center=(button_pos))
        screen.blit(text,text_rect)
        return option_button_rect

    def __check_button_is_clicked(self,button_rect,mouse_pos):
        if mouse_pos[0] in range(button_rect.left, button_rect.right) and mouse_pos[1] in range(button_rect.top,button_rect.bottom):
            return True
        return False



