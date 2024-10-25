import pygame
from scripts.menu.button import Button
from scripts.menu.rune_button import Rune_Button
from scripts.menu.menu import Menu

class Shrine_Menu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.runes = []
        self.upgrade_rune = None
        self.Init_Rune_Upgrade_Buttons()
    
    def Init_Rune_Upgrade_Buttons(self):
        self.rune_upgrade_buttons = []
        width = self.game.screen_width // self.game.render_scale // 2
        button_size_x = 100
        self.Generate_Rune_Button((width - button_size_x // 2 + 50, 100), (button_size_x, 20), 'soul', 'souls')
        self.Generate_Rune_Button((width - button_size_x // 2 + 50, 130), (button_size_x, 20), 'Strength', 'strength')

        

    def Init_Buttons(self):
        self.buttons = []
        width = self.game.screen_width // self.game.render_scale // 2
        button_size_x = 100
        self.Generate_Button((width - button_size_x // 2, 50), (button_size_x, 20), 'resume', 'run_game')
    
    def Generate_Rune_Button(self, pos, size, text, effect):
        rune_button = Rune_Button(self.game, pos, size, text, effect)
        self.rune_upgrade_buttons.append(rune_button)

    def Update(self):
        super().Update()
        self.Rune_Interactions()

        if not self.upgrade_rune:
            return
        
        for rune_button in self.rune_upgrade_buttons:
            rune_button.Update(self.upgrade_rune)



    def Rune_Interactions(self):
        for rune in self.runes:
            if rune.Menu_Rect().colliderect(self.game.mouse.rect_click()):
                self.game.mouse.Reset_Click_Pos()
                self.upgrade_rune = rune

    def Check_Keyboard_Input(self):
         if self.game.keyboard_handler.escape_pressed:
            self.game.keyboard_handler.Set_Escape_Key(False)
            self.game.state_machine.Set_State('run_game')

    # Get a random Rune
    def Randomise_Runes(self):
        print(len(self.game.rune_handler.runes))
        self.Set_Active_Runes_Menu_Pos()

    
    def Set_Active_Runes_Menu_Pos(self):
        self.runes = self.game.rune_handler.active_runes
        pos_x = 100
        pos_y = 100
        for rune in self.runes:
            rune.menu_pos = (pos_x, pos_y)
            pos_y += 20


    def Render(self, surf):
        super().Render(surf)
        for rune in self.runes:
            rune.Render_Menu(surf)

        if not self.upgrade_rune:
            return
        
        for rune_button in self.rune_upgrade_buttons:
            rune_button.Render(surf)