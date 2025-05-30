import pygame
import math
from scripts.menu.rune_button import Rune_Button
from scripts.menu.menu import Menu
from scripts.menu.rune_shrine_menu import Rune_Shrine_Menu
from scripts.engine.assets.keys import keys


class Rune_Bookshelf_Menu(Rune_Shrine_Menu):

    
    def Init_Rune_Upgrade_Buttons(self):
        self.rune_upgrade_buttons = []
        width = self.game.screen_width // self.game.render_scale // 2
        button_size_x = 200
        button_size_y = 40
        self.Generate_Rune_Button((width - button_size_x // 2, 230), (button_size_x, button_size_y), 'Purchase', 'purchase', (140, 0, 0))

    