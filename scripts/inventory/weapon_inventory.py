import pygame
from scripts.inventory.inventory_slot import Inventory_Slot
from scripts.inventory.inventory import Inventory
from copy import copy

class Weapon_Inventory(Inventory):
    def __init__(self, game, type):
        super().__init__(game, 2, 1)
        self.Setup_Inventory(type)

    # Configure the inventory when initialized
    def Setup_Inventory(self, type):
        # Create a new inventory list for this setup
        weapon_class = []
        if type == 'left_right':
            weapon_class.insert(0, 'left_hand')
            weapon_class.insert(1, 'right_hand')
        elif type == 'bow_arrow':
            weapon_class.insert(0, 'bow')
            weapon_class.insert(1, 'arrow')
        else:
            print("WEAPON_CLASS NOT FOUND")
            return

        for i in range(self.x_size):
            x = i * self.size[1] + 5
            inventory_slot = Inventory_Slot(self.game, (x, 5), self.size, None)
            background = self.game.assets[type][i]
            inventory_slot.Add_Background(background)
            inventory_slot.inventory_type = weapon_class[i]
            self.inventory.append(inventory_slot)  # Add to instance's inventory

    def Update(self, offset=(0, 0)):
        super().Update(offset)
        # for inventory_slot in self.inventory:
            # print(inventory_slot.pos)
            # if inventory_slot.item:
            #     print(inventory_slot.item.picked_up)
            # print(inventory_slot.active)

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

    
