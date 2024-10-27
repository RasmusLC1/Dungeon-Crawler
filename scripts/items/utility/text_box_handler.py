import pygame

class Text_Box_handler():
    def __init__(self, game):
        self.game = game
        self.nearby_items = []
        self.nearby_item_cooldown = 0
        self.current_item = None

    def Update(self):
        self.current_item = None
        self.Update_Nearby_Items()
        self.Check_Items()
        self.Check_Inventory_Slots()

    def Check_Items(self):
        for item in self.nearby_items:
            self.current_item = item.Update_Text_Box(item.rect(), self.game.mouse.rect_pos())
            if self.current_item:
                return

    def Check_Inventory_Slots(self):
        if self.current_item:
            return
        for inventory_slot in self.game.item_inventory.inventory:
            if not inventory_slot.item:
                continue
            self.current_item = inventory_slot.item.Update_Text_Box(inventory_slot.item.rect(), self.game.mouse.rect_pos(self.game.render_scroll))
            if self.current_item:
                return
        
        for inventory_slot in self.game.rune_inventory.inventory:
            if not inventory_slot.item:
                continue
            self.current_item = inventory_slot.item.Update_Text_Box(inventory_slot.item.rect(), self.game.mouse.rect_pos(self.game.render_scroll))
            if self.current_item:
                return

    def Update_Nearby_Items(self):
        if self.nearby_item_cooldown:
            self.nearby_item_cooldown = max(0, self.nearby_item_cooldown - 1)
            return False

        self.nearby_item_cooldown = 30
        self.nearby_items.clear()

        self.nearby_items = self.game.item_handler.Find_Nearby_Item(self.game.mouse.player_mouse, 100)
        # nearby_runes = self.game.rune_handler.Find_Nearby_Runes(self.game.mouse.player_mouse, 100)
        # if not nearby_runes:
        #     return True
        # self.nearby_items.extend(nearby_runes)
        return True
    

    def Render(self, surf, offset=(0, 0)):
        if not self.current_item:
            return
        self.current_item.text_box.Render(surf, offset)
