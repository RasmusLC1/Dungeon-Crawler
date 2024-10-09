import pygame
from scripts.items.item import Item
from scripts.inventory.inventory import Inventory
from scripts.inventory.inventory_slot import Inventory_Slot
from copy import copy

class Item_Inventory(Inventory):
    def __init__(self, game):
        super().__init__(game, 9, 1)
        self.Setup()
        

    # Configure the inventory when Initialiased
    def Setup(self):
        for j in range(self.y_size):
            for i in range(self.x_size):
                x = i * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 65
                y = j * self.size[0] + self.game.screen_height / self.game.render_scale - 20
                inventory_slot = Inventory_Slot(self.game, (x, y), self.size, None)
                inventory_slot.Set_White_List(['weapon', 'potion', 'loot'])
                self.inventory.append(inventory_slot)



    def Item_Double_Click(self):
        if not super().Item_Double_Click():
            return
        active_inventory = self.game.weapon_inventory.active_inventory
        weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
        self.clicked_inventory_slot.item.Handle_Double_Click(self, weapon_inventory)
        

