import pygame
from scripts.menu.button import Button

class Pause_Menu():
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
        self.test_button = Button(self.game, (100, 20), (100, 100), 'test123', 1)

    def Update(self):
        self.test_button.Update()

    def Render(self, surf):

        surf.blit(self.rect_surface, (self.pos_x, self.pos_y))
        self.test_button.Render(surf)

        self.Check_Keyboard_Input()


    def Check_Keyboard_Input(self):
         if self.game.keyboard_handler.escape_pressed:
            self.game.keyboard_handler.Set_Escape_Key(False)
            self.game.state_machine.Set_State(1)

