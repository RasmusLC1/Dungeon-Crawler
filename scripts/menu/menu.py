import pygame
from scripts.menu.button import Button

class Menu():
    def __init__(self, game) -> None:
        self.game = game
        self.background_color = (20, 20, 20)
        self.size_x = self.game.screen_width // self.game.render_scale
        self.size_y = self.game.screen_height // self.game.render_scale

        self.pos_x = 0
        self.pos_y = 0
        alpha = 2
        self.rect_surface = pygame.Surface((self.size_x, self.size_y))
        self.rect_surface.set_alpha(alpha)
        self.rect_surface.fill(self.background_color)
        self.Init_Buttons()


    def Init_Buttons(self):
        pass


    def Generate_Button(self, pos, size, text, menu_state, save_game = False, color = (0, 0, 0)):
        button = Button(self.game, pos, size, text, menu_state, save_game, color)
        self.buttons.append(button)



    def Update(self):
        self.Check_Keyboard_Input()
        
        for button in self.buttons:
            button.Update()

    def Render(self, surf):

        surf.blit(self.rect_surface, (self.pos_x, self.pos_y))

        for button in self.buttons:
            button.Render(surf)



    def Check_Keyboard_Input(self):
        pass

