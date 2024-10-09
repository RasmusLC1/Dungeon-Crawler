import pygame
from scripts.inventory.inventory_slot import Inventory_Slot
from scripts.inventory.inventory import Inventory
from copy import copy

class Spell_Inventory(Inventory):
    def __init__(self, game):
        super().__init__(game, 1, 3)
        self.Setup_Inventory()
        

    # Configure the inventory when initialized
    def Setup_Inventory(self):
        x_pos = self.game.screen_width / self.game.render_scale - 35
        for i in range(self.y_size):
            print("TEST")
            y = i * self.size[0] + self.game.screen_height / self.game.render_scale - 55
            inventory_slot = Inventory_Slot(self.game, (x_pos, y), self.size, None)
            background = self.game.assets['rune_background'][0]
            inventory_slot.Add_Background(background)
            inventory_slot.inventory_type = 'spell'
            inventory_slot.Set_White_List(['spell'])
            self.inventory.append(inventory_slot)  # Add to instance's inventory
        

        
    def Find_Inventory_Slot(self, searched_inventory_slot):
        for inventory_slot in self.inventory:
            if inventory_slot.inventory_type == searched_inventory_slot.inventory_type:
                continue
            if inventory_slot.item:
                return True
            
        return False
    
    def Item_Double_Click(self):
        if not super().Item_Double_Click():
            return
        self.clicked_inventory_slot.item.Handle_Double_Click(self, self.game.item_inventory)

    
