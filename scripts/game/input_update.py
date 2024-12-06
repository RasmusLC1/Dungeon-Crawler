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
                if event.type == pygame.VIDEORESIZE:



                    print("EVENT", (self.game.screen_width, self.game.screen_height), (event.w, event.h))


                    if abs(event.w - self.game.screen_width) > abs(event.h - self.game.screen_height):
                        self.game.render_scale += (event.w - self.game.screen_width) / 2000
                    else:
                        self.game.render_scale += (event.h - self.game.screen_height) / 2000 





                    self.game.screen_width = event.w
                    self.game.screen_height = event.h
                    
                    print(self.game.render_scale)
                    
                    self.game.screen = pygame.display.set_mode((self.game.screen_width, self.game.screen_height), pygame.FULLSCREEN)
                    self.game.display = pygame.Surface((self.game.screen_width/self.game.render_scale, self.game.screen_height/self.game.render_scale))
                    self.game.renderer.Update_Background_Image()

                    self.Update_Inventories()
                    self.game.menu_handler.Resize_Menus()

    


    
    def Update_Inventories(self):
        if self.game.state_machine.game_state == 'main_menu':
             return
        self.game.item_inventory.Update_Inventory_Slot_Pos()
        self.game.weapon_inventory.Update_Inventory_Slot_Pos()
        self.game.rune_inventory.Update_Inventory_Slot_Pos()
