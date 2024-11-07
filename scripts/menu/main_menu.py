import pygame
from scripts.menu.button import Button
from scripts.menu.menu import Menu


class Main_Menu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.rect_surface.set_alpha(250)

    def Init_Buttons(self):
        self.buttons = []
        width = self.game.screen_width // self.game.render_scale // 2
        button_size_x = 200
        button_size_y = 40
        # Resume Button
        self.Generate_Button((width - button_size_x // 2, button_size_y * 2.5), (button_size_x, button_size_y), 'New Game', 'new_game')
        self.Generate_Button((width - button_size_x // 2, button_size_y * 4.5), (button_size_x, button_size_y), 'Load Game', 'load_game')
        self.Generate_Button((width - button_size_x // 2, button_size_y * 6.5), (button_size_x, button_size_y), 'Exit Game', 'exit_game')

