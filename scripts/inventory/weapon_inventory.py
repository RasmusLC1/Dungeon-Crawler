import pygame
from scripts.entities.player.items.item import Item
from scripts.inventory.inventory_slot import Inventory_Slot

class Weapon_Inventory():
    def __init__(self, game):
        self.x_size = 2
        self.game = game
        self.size = (17, 17)

    # Configure the inventory when Initialiased
    def Setup_Inventory(self, type):
        # Create a new inventory list for this setup
        inventory = []
        weapon_class = []
        if type == 'left_right':
            weapon_class.insert(0, 'left_hand')
            weapon_class.insert(1, 'right_hand')
        if type == 'bow_arrow':
            weapon_class.insert(0, 'bow')
            weapon_class.insert(1, 'arrow')
        else:
            print("WEAPON_CLASS NOT FOUND")

        for i in range(self.x_size):
            x = i * self.size[1] + 5
            inventory_slot = Inventory_Slot(self.game, (x, 5), self.size, None)
            background = self.game.assets[type][i]
            inventory_slot.Add_Background(background)
            inventory_slot.Inventory_type = weapon_class[i]
            inventory.append(inventory_slot)

        return inventory

    def Render(self, surf):
        for inventory_slot in self.inventory:
            inventory_slot.Render(surf)
