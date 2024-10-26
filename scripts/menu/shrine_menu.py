import pygame
import math
from scripts.menu.button import Button
from scripts.menu.rune_button import Rune_Button
from scripts.menu.menu import Menu

class Shrine_Menu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.runes = []
        self.upgrade_rune = None
        self.Init_Rune_Upgrade_Buttons()
        self.rune_highlight = pygame.Surface((20, 20))
        self.rune_highlight.fill((120, 120, 120))

        self.rune_text_clear = pygame.Surface((140, 35))
        self.rune_text_clear.fill((20, 20, 20))
    
    def Init_Rune_Upgrade_Buttons(self):
        self.rune_upgrade_buttons = []
        width = self.game.screen_width // self.game.render_scale // 2
        button_size_x = 100
        self.Generate_Rune_Button((width - button_size_x // 2, 100), (button_size_x, 20), 'Souls', 'souls', (100, 100, 150))
        self.Generate_Rune_Button((width - button_size_x // 2, 130), (button_size_x, 20), 'Power', 'power', (140, 0, 0))

        

    def Init_Buttons(self):
        self.buttons = []
        width = self.game.screen_width // self.game.render_scale
        button_size_x = 100
        self.Generate_Button((width - button_size_x - 10, 10), (button_size_x, 20), 'resume', 'run_game', False, (100, 100, 100))
    
    def Generate_Rune_Button(self, pos, size, text, effect, color = (0, 0, 0)):
        rune_button = Rune_Button(self.game, pos, size, text, effect, color)
        self.rune_upgrade_buttons.append(rune_button)

    def Update(self):
        super().Update()
        self.Rune_Interactions()

        if not self.upgrade_rune:
            return
        
        for rune_button in self.rune_upgrade_buttons:
            if self.upgrade_rune.original_soul_cost == 0 and rune_button.effect == 'souls':
                continue

            if self.upgrade_rune.original_power == 0 and rune_button.effect == 'power':
                continue
            
            # Return True if successfully upgraded
            if rune_button.Update(self.upgrade_rune):
                self.game.display.blit(self.rune_text_clear, (20, 20))
                self.game.player.Decrease_Souls(self.upgrade_rune.upgrade_cost)
                new_upgrade_cost = math.ceil(self.upgrade_rune.upgrade_cost /  10)
                self.upgrade_rune.Modify_Upgrade_Cost(new_upgrade_cost)



    def Rune_Interactions(self):
        for rune in self.runes:
            if rune.Menu_Rect().colliderect(self.game.mouse.rect_click()):
                self.game.mouse.Reset_Click_Pos()
                self.upgrade_rune = rune
                # Clear the previous text
                self.game.display.blit(self.rune_text_clear, (20, 20))


    def Check_Keyboard_Input(self):
         if self.game.keyboard_handler.escape_pressed:
            self.game.keyboard_handler.Set_Escape_Key(False)
            self.game.state_machine.Set_State('run_game')

    # Get a random Rune
    def Randomise_Runes(self):
        self.Set_Active_Runes_Menu_Pos()

    
    def Set_Active_Runes_Menu_Pos(self):
        self.runes = self.game.rune_handler.active_runes
        pos_x = 20
        pos_y = 100
        for rune in self.runes:
            rune.menu_pos = (pos_x, pos_y)
            pos_y += 20


    def Render(self, surf):
        super().Render(surf)

        if self.upgrade_rune:
            surf.blit(self.rune_highlight, (self.upgrade_rune.menu_pos[0] - 2, self.upgrade_rune.menu_pos[1] - 2))
            self.game.default_font.Render_Word(surf, "Souls Cost:   " + str(self.upgrade_rune.current_soul_cost), (20, 20))        
            self.game.default_font.Render_Word(surf, "Power:        " + str(self.upgrade_rune.current_power), (20, 32))        
            self.game.default_font.Render_Word(surf, "Upgrade Cost: " + str(self.upgrade_rune.upgrade_cost), (20, 44))
            soul_symbol_x_pos = 120 + 8 * len(str(self.upgrade_rune.upgrade_cost))
            self.game.symbols.Render_Symbol(surf, 'soul',  (soul_symbol_x_pos, 44))

            
        for rune in self.runes:
            rune.Render_Menu(surf)

        if not self.upgrade_rune:
            return
        
        for rune_button in self.rune_upgrade_buttons:
            rune_button.Render(surf)