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
        index = 0
        for i in range(self.x_size):
            (x, y) = self.Set_Inventory_Slot_Pos(i)
            inventory_slot = Inventory_Slot(self.game, (x, y), self.size, None, index, str(i + 1))
            inventory_slot.Set_White_List(['weapon', 'potion', 'loot'])
            self.inventory.append(inventory_slot)
            index += 1

    def Set_Inventory_Slot_Pos(self, index):
        x = index * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 130
        y = self.game.screen_height / self.game.render_scale - 40
        return (x, y)

    def Key_Board_Input(self):
        keyboard = self.game.keyboard_handler

        if keyboard._1_pressed:
            self.Activate_Inventory_Slot(0)
        elif keyboard._2_pressed:
            self.Activate_Inventory_Slot(1)
        elif keyboard._3_pressed:
            self.Activate_Inventory_Slot(2)
        elif keyboard._4_pressed:
            self.Activate_Inventory_Slot(3)
        elif keyboard._5_pressed:
            self.Activate_Inventory_Slot(4)
        elif keyboard._6_pressed:
            self.Activate_Inventory_Slot(5)
        elif keyboard._7_pressed:
            self.Activate_Inventory_Slot(6)
        elif keyboard._8_pressed:
            self.Activate_Inventory_Slot(7)
        elif keyboard._9_pressed:
            self.Activate_Inventory_Slot(8)
    

    def Item_Double_Click(self):
        if not super().Item_Double_Click():
            return
        active_inventory = self.game.weapon_inventory.active_inventory
        weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
        self.clicked_inventory_slot.item.Handle_Double_Click(self, weapon_inventory)
        

