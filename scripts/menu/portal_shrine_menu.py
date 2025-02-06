import pygame
import math
from scripts.menu.portal_button import Portal_Button
from scripts.menu.menu import Menu

class Portal_Shrine_Menu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.button_size_x *= 1.5
        self.button_size_y *= 1.5
        self.rect_surface.set_alpha(255)
        self.shrine = None
        self.portal_button = None
        self.Generate_Button((self.width - self.button_size_x // 2, self.button_size_y * 4.5), (self.button_size_x, self.button_size_y), 'resume Game', 'run_game')




    def Update(self):
        super().Update()
        self.game.souls_interface.Update()
        if self.portal_button:
            if self.shrine.is_open:
                return
            # If not purchased simply return
            if not self.portal_button.Update():
                return
            # Activate shrine
            self.shrine.Activate()


    def Initialise_Shrine(self, shrine):
        self.shrine = shrine
        self.portal_button = Portal_Button(self.game, (self.width - self.button_size_x // 2, self.button_size_y * 2.5), (self.button_size_x, self.button_size_y), 'Unlock Portal', (100, 100, 100))

    def Check_Keyboard_Input(self):
         if self.game.keyboard_handler.escape_pressed:
            self.game.keyboard_handler.Set_Escape_Key(False)
            self.game.state_machine.Set_State('run_game')


    def Render(self, surf):
        super().Render(surf)
        self.game.souls_interface.Render(self.game.display)
        if not self.shrine:
            return
        if self.shrine.is_open:
                return
        if self.portal_button:
            self.portal_button.Render(surf)

        