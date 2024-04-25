import pygame
class Button():
    def __init__(self, img, pos, font,text_input,base_color,hovering_color):
        self.img = img
        self.pos = pos
        self.font = font
        self.text_input = text_input
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.img_rect = self.img.get_rect(center=(self.pos))
        self.text_rect = self.text.get_rect(center=(self.pos))
    def update(self,screen):
        screen.blit(self.img, self.img_rect)
        screen.blit(self.text,self.text_rect)

    def check_forInput(self,pos):
        if pos[0] in range(self.img_rect.left,self.img_rect.right) and pos[1] in range(self.img_rect.top,self.img_rect.bottom):
            return True
        return False

    def change_color(self,pos):
        if pos[0] in range(self.img_rect.left,self.img_rect.right) and pos[1] in range(self.img_rect.top,self.img_rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)