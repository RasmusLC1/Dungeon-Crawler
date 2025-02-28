import pygame

class Text_Box_handler():
    def __init__(self, game):
        self.game = game
        self.nearby_items = []
        self.nearby_item_cooldown = 0
        self.current_item = None

    def Update(self):
        self.current_item = None
        # self.Update_Nearby_Items()
        self.Check_Items()
        self.Check_Inventory_Slots()

    def Check_Items(self):
        for entity in self.game.entities_render.entities:
            self.current_item = entity.Update_Text_Box(entity.rect(), self.game.mouse.rect_pos())
            if self.current_item:
                return

    def Check_Inventory_Slots(self):
        if self.current_item:
            return
        for inventory_slot in self.game.inventory.inventory:

            if not inventory_slot.item:
                continue
            self.current_item = inventory_slot.item.Update_Text_Box(inventory_slot.rect(), self.game.mouse.rect_pos(self.game.render_scroll))
            
            if self.current_item:
                return


    def Render(self, surf, offset=(0, 0)):
        if not self.current_item:
            return
        self.current_item.text_box.Render(surf, offset)
