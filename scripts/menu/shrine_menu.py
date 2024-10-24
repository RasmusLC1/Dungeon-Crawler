import pygame
from scripts.menu.button import Button
from scripts.menu.menu import Menu

class Shrine_Menu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)

    def Init_Buttons(self):
        self.buttons = []
        width = self.game.screen_width // self.game.render_scale // 2
        button_size_x = 100
        # Resume Button
        self.Generate_Button((width - button_size_x // 2, 50), (button_size_x, 20), 'resume', 'run_game')
    
    def Check_Keyboard_Input(self):
         if self.game.keyboard_handler.escape_pressed:
            self.game.keyboard_handler.Set_Escape_Key(False)
            self.game.state_machine.Set_State('run_game')

    # Get a random Rune
    def Randomise_Runes(self):
        print(len(self.game.rune_handler.runes))
