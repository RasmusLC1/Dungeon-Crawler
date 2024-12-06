import pygame
from scripts.inventory.inventory_slot import Inventory_Slot
from scripts.inventory.inventory import Inventory

class Weapon_Inventory(Inventory):
    def __init__(self, game, type, index):
        super().__init__(game, 2, 1)
        self.Setup_Inventory(type)
        self.index = index


    def Update(self, offset = (0,0)):
        super().Update(offset)
        self.Render_Weapon(self.game.display)

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
            (x, y) = self.Set_Inventory_Slot_Pos(i)
            inventory_slot = Inventory_Slot(self.game, (x, y), self.size, None, index)
            background = self.game.assets[type][i]
            inventory_slot.Add_Background(background)
            inventory_slot.inventory_type = weapon_class[i]
            inventory_slot.Set_White_List(['weapon'])
            self.inventory.append(inventory_slot)  # Add to instance's inventory
            index += 1
    
    def Set_Inventory_Slot_Pos(self, index):
        x = index * self.size[1] + 10
        y = 5
        return (x, y)


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

    
    # Custom render function for equipped slots to render the weapon in hand and inventory
    def Render_Weapon(self, surf):
        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                continue
            weapon_image = self.game.assets[inventory_slot.item.type][0]
            surf.blit(weapon_image, inventory_slot.pos)
