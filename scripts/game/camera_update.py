import pygame

class Camera_Update():
    def __init__(self, game) -> None:
        self.game = game

    def Camera_Scroll(self):
        self.game.scroll[0] += (self.game.player.rect().centerx - self.game.display.get_width() / 2 - self.game.scroll[0]) / 25
        self.game.scroll[1] += (self.game.player.rect().centery - self.game.display.get_height() / 2 - self.game.scroll[1]) / 25
        self.game.render_scroll = (int(self.game.scroll[0]), int(self.game.scroll[1]))

    def Enable_Full_Screen(self, event):
        self.game.render_scale = max(event.w, event.h) / 1000

        self.game.screen_width = event.w
        self.game.screen_height = event.h
        
        
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