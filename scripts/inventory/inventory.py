import pygame
from scripts.inventory.items.item import Item
from scripts.inventory.inventory_slot import Inventory_Slot
from copy import copy

class Inventory:
    def __init__(self, game):
        self.x_size = 7
        self.y_size = 2
        self.game = game
        self.available_pos = []
        self.size = (10, 10)
        self.active_item = None
        self.item_clicked = 0
        
        self.inventory = []
        self.Setup()

    def Setup(self):
        for j in range(self.y_size):
            for i in range(self.x_size):
                x = i * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 40
                y = j * self.size[0] + self.game.screen_height / self.game.render_scale - 25
                self.inventory.append(Inventory_Slot(self.game, (x, y), (10, 10), None))

    def Update(self, offset = (0,0)):
        Inventory.Active_Item(self, offset)
        for inventory_slot in self.inventory:
            if inventory_slot.item:
                inventory_slot.item.Update_Animation()
                if self.game.mouse.left_click:
                    # Check for collision with inventory slot
                    if inventory_slot.rect().colliderect(self.game.mouse.rect_click()):
                        inventory_slot.Set_Active(True)
                        self.item_clicked += 1
                        if self.game.mouse.hold_down_left > 10 and not inventory_slot.active:
                            self.active_item = copy(inventory_slot.item)
                            self.active_item.active = True
                
                
                inventory_slot.Update()
                if inventory_slot.active:
                    if not self.game.mouse.left_click:
                        inventory_slot.Set_Active(False)


                            
    def Return_Item(self):
        # Return the item to Inventory
        for inventory_slot in self.inventory:
            if inventory_slot.active:
                inventory_slot.Set_Active(False)
                self.active_item = None
                return  

    def Move_Item(self, offset):
        # Render legal item position and move it
        self.active_item.render(self.game.display, offset)  
        self.active_item.Move(self.game.mouse.mpos)
        # Add item back to item list when released in legal position
        if self.game.mouse.left_click == False:
            self.game.items.append(self.active_item)
            self.active_item = None
            for inventory_slot in self.inventory:
                if inventory_slot.active:
                    inventory_slot.Set_Active(False)
                    inventory_slot.item = None
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
        # Delete the item from the current inventory slot of we were able to move it
        if Move_item:
            for inventory_slot in self.inventory:
                if inventory_slot.active:
                    inventory_slot.Set_Active(False)
                    inventory_slot.item = None
                    return True
        return False

    # Active item is an item being dragged
    def Active_Item(self, offset = (0,0)):
        # Check if there is an active item
        if self.active_item:
            # Check for out of bounds
            item_out_of_bounds = self.active_item.Move_Legal(self.game.mouse.mpos, self.game.player.pos, self.game.tilemap)
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

        return

    def Overflow(self, item):
        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                inventory_slot.Add_Item(item)
                inventory_slot.item.Update()

                return True
        return False

    # Add item to the inventory
    def Add_Item(self, item):

        # Increment the amount in the inventory slot
        if item.max_amount > 1:
            for inventory_slot in self.inventory:
                if inventory_slot.item:
                    inventory_slot.item.Update()
                    if inventory_slot.item.type == item.type and inventory_slot.item.amount < inventory_slot.item.max_amount:
                        current_amount = inventory_slot.item.amount + item.amount
                        inventory_slot.item.Increase_Amount(item.amount)
                        # Handle overflow and send it to the new available position
                        if current_amount > inventory_slot.item.max_amount:
                            new_amount = current_amount - inventory_slot.item.max_amount
                            new_item = copy(item)
                            new_item.Set_Amount(new_amount)
                            # Add item to item list if there is no room
                            if not self.Overflow(new_item):
                                self.game.items.add(new_item)
                        self.game.items.remove(item)
                        inventory_slot.item.Update()
                        return
        # Assign new item
        i = 0
        j = 0
        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                inventory_slot.Add_Item(item)
                self.game.items.remove(item)
                inventory_slot.item.Update()

                return True
            # 2d array simulation for position
            i += 1
            if i >= self.x_size:
                i = 0
                j += 1

        return False
        


    def render(self, surf):
        for inventory_slot in self.inventory:
            inventory_slot.render(surf)

