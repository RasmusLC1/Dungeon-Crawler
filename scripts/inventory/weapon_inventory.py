import pygame
from scripts.inventory.inventory_slot import Inventory_Slot
from scripts.inventory.inventory import Inventory
from copy import copy

class Weapon_Inventory(Inventory):
    def __init__(self, game, type, index):
        super().__init__(game, 2, 1)
        self.Setup_Inventory(type)
        self.index = index


    def Load_Data(self, data):
        for ID, item_data in data.items():
            if not item_data:
                continue
            for inventory_slot in self.inventory:

                if item_data['inventory_index'] != inventory_slot.index:
                    continue

                self.game.item_handler.Load_Item_From_Data(item_data)
                item = self.game.item_handler.Find_Item(item_data['ID'])
                if not item:
                    continue

                if item.category == 'weapon':
                    item.Set_Entity(self.game.player)


                inventory_slot.Add_Item(item)

        

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
        index = 0
        for i in range(self.x_size):
            x = i * self.size[1] + 5
            inventory_slot = Inventory_Slot(self.game, (x, 5), self.size, None, index)
            background = self.game.assets[type][i]
            inventory_slot.Add_Background(background)
            inventory_slot.inventory_type = weapon_class[i]
            inventory_slot.Set_White_List(['weapon'])
            self.inventory.append(inventory_slot)  # Add to instance's inventory
            index += 1
    
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

    
