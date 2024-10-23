import pygame
import sys


class Input_Update():
    def __init__(self, game) -> None:
        self.game = game


    def Input_Handler(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.state_machine.Set_State('exit_game')
                self.game.mouse.Mouse_Input(event, self.game.render_scroll)

                self.game.keyboard_handler.keyboard_Input(event, self.game.render_scroll)