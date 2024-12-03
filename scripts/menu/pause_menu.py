import pygame
from scripts.menu.menu import Menu

class Pause_Menu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        

    def Init_Buttons(self):
        width = self.game.screen_width // self.game.render_scale // 2
        button_size_x = 200
        button_size_y = 40
        # Resume Button
        self.Generate_Button((width - button_size_x // 2, button_size_y * 2.5), (button_size_x, button_size_y), 'resume', 'run_game')
        self.Generate_Button((width - button_size_x // 2, button_size_y * 4.5), (button_size_x, button_size_y), 'Main Menu', 'main_menu', True)
        self.Generate_Button((width - button_size_x // 2, button_size_y * 6.5), (button_size_x, button_size_y), 'exit game', 'exit_game')


    def Check_Keyboard_Input(self):
         if self.game.keyboard_handler.escape_pressed:
            self.game.keyboard_handler.Set_Escape_Key(False)
            self.game.state_machine.Set_State('run_game')

