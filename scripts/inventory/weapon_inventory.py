import pygame
from scripts.entities.player.items.item import Item
from scripts.inventory.inventory_slot import Inventory_Slot
from copy import copy

class Weapon_Inventory():
    def __init__(self, game, type):
        self.x_size = 2
        self.game = game
        self.size = (17, 17)
        self.inventory = []  # Store the inventory here
        self.active_item = None
        self.item_clicked = 0
        self.click_cooldown = 0
        self.clicked_inventory_slot = None
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
            inventory_slot.Inventory_type = weapon_class[i]
            self.inventory.append(inventory_slot)  # Add to instance's inventory

    # Implement the __iter__ method to make the class iterable
    def __iter__(self):
        return iter(self.inventory)
    
    # General Update function
    def Update(self, offset=(0, 0)):
        self.Active_Item(offset)

        for inventory_slot in self.inventory:
            if inventory_slot.item:
                inventory_slot.item.Update_Animation()
                if self.game.mouse.left_click:
                    # Check for collision with inventory slot
                    if inventory_slot.rect().colliderect(self.game.mouse.rect_click()):
                        self.clicked_inventory_slot = inventory_slot
                        self.item_clicked += 1
                        # Activates when mouse has been held down for 10 ticks and the inventory slot is not active anymore 
                        if self.game.mouse.hold_down_left > 10 and not inventory_slot.active:
                            # Copy the item and pick it up
                            self.active_item = copy(inventory_slot.item)
                            self.active_item.picked_up = True
                            inventory_slot.Set_Active(True)
                            return
        self.Item_Click()
        return


    # Handle clicking items
    def Item_Click(self):
        if not self.game.mouse.left_click:
            if self.game.mouse.hold_down_left < 5 and self.game.mouse.hold_down_left > 0:
                if self.clicked_inventory_slot:
                    self.clicked_inventory_slot.item.Activate()
                    self.clicked_inventory_slot.Update()
                    self.clicked_inventory_slot = None
                    
        return

    # Return the item to its previous Inventory slot and deactivate
    # the item and inventory slot
    def Return_Item(self):
        if self.clicked_inventory_slot:
            self.clicked_inventory_slot.Set_Active(False)
            self.active_item = None
            self.clicked_inventory_slot = None
        return  

    # Move the item around
    def Move_Item(self, offset):
        # Render legal item position and move it
        self.active_item.Render(self.game.display, offset)  
        self.active_item.Move(self.game.mouse.mpos)
        # Add item back to item list when released in legal position
        if self.game.mouse.left_click == False:
            if not self.active_item.Place_Down():
                self.game.item_handler.Add_Item(self.active_item)
                self.game.entities_render.append(self.active_item)

            self.active_item = None
            # Set the inventory to be inactive again
            if self.clicked_inventory_slot:
                self.clicked_inventory_slot.Set_Active(False)
                self.clicked_inventory_slot.item = None
                self.clicked_inventory_slot = None
        return

    def Move_Item_To_New_Slot(self, offset):
        Move_item = False
        for inventory_slot in self.inventory:
            # Collision with other inventory slots
            if inventory_slot.rect().colliderect(self.game.mouse.rect_pos(offset)):
                # Check if it contains an item and add the item there if it's empty
                if not inventory_slot.item:
                    inventory_slot.Add_Item(self.active_item)
                    Move_item = True
        # Delete the item from the current inventory slot if we were able to move it
        if Move_item:
            for inventory_slot in self.inventory:
                if inventory_slot.active:
                    inventory_slot.Set_Active(False)
                    inventory_slot.item = None
                    return True
        return False

    # Active item is an item being dragged
    def Active_Item(self, offset=(0, 0)):
        # Check if there is an active item
        if self.active_item:
            # Check for out of bounds
            item_out_of_bounds = self.active_item.Move_Legal(self.game.mouse.mpos, self.game.player.pos, self.game.tilemap, offset)
            if item_out_of_bounds == False:
                if self.game.mouse.left_click == False:       
                    if self.Move_Item_To_New_Slot(offset):
                        return    
                    self.Return_Item()
                    return
                
                self.active_item.render_out_of_bounds(self.game.player.pos, self.game.mouse.mpos, self.game.display, offset)  
            else:
                self.Move_Item(offset)
                return

    def Render(self, surf):
        for inventory_slot in self.inventory:
            inventory_slot.Render(surf)
