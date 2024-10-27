import pygame
from scripts.inventory.inventory_slot import Inventory_Slot
from scripts.inventory.inventory import Inventory
from copy import copy

class Rune_Inventory(Inventory):
    def __init__(self, game):
        super().__init__(game, 3, 1)
        self.Setup_Inventory()
        

    # Configure the inventory when initialized
    def Setup_Inventory(self):
        x_pos = self.game.screen_width / self.game.render_scale - 25
        y_pos = self.game.screen_height / self.game.render_scale - 20
        index = 0
        for i in range(self.x_size):
            x = i * self.size[0] + self.game.screen_width / self.game.render_scale - 55
            inventory_slot = Inventory_Slot(self.game, (x, y_pos), self.size, None, index)
            background = self.game.assets['rune_background'][0]
            inventory_slot.Add_Background(background)
            # inventory_slot.inventory_type = 'rune'
            inventory_slot.Set_White_List(['rune'])
            self.inventory.append(inventory_slot)  # Add to instance's inventory
            index +=1
        
    def Key_Board_Input(self):
        keyboard = self.game.keyboard_handler

        if keyboard.z_pressed:
            self.Activate_Inventory_Slot(0)
        elif keyboard.x_pressed:
            self.Activate_Inventory_Slot(1)
        elif keyboard.c_pressed:
            self.Activate_Inventory_Slot(2)
        
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

    
