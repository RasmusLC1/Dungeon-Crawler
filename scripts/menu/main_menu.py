import pygame
from scripts.menu.button import Button
from scripts.menu.menu import Menu


class Main_Menu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)

    def Init_Buttons(self):
        self.buttons = []
        width = self.game.screen_width // self.game.render_scale // 2
        button_size_x = 100
        print(width)
        # Resume Button
        self.Generate_Button((width - button_size_x // 2, 50), (button_size_x, 20), 'New Game', 'new_game')
        self.Generate_Button((width - button_size_x // 2, 90), (button_size_x, 20), 'Load Game', 'load_game')
        self.Generate_Button((width - button_size_x // 2, 130), (button_size_x, 20), 'Exit Game', 'exit_game')


   
