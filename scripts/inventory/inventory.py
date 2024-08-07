import pygame
from scripts.entities.player.items.item import Item
from scripts.inventory.inventory_slot import Inventory_Slot
from copy import copy

class Inventory:
    def __init__(self, game, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.game = game
        self.available_pos = []
        self.size = (17, 17)
        self.active_item = None
        self.item_clicked = 0
        self.click_cooldown = 0
        self.clicked_inventory_slot = None
        self.inventory = []


    # General Update function
    def Update(self, offset=(0, 0)):
        self.Active_Item(offset)

        for inventory_slot in self.inventory:
            if not self.Update_Inventory_Slot_Item_Animation(inventory_slot):
                continue
            # Check if the mouse has been clicked, if no we skip that inventory
            # slot if no continue to next inventory slot
            if not self.game.mouse.left_click:
                continue
            if not self.Inventory_Slot_Collision(inventory_slot):
                continue
            if self.Pickup_Item_To_Move(inventory_slot):
                return
            
        self.Item_Click()
        return

    # Activates when mouse has been held down for 10 ticks and
    # the inventory slot is not active anymore 
    def Pickup_Item_To_Move(self, inventory_slot):
        if self.game.mouse.hold_down_left > 10 and not inventory_slot.active:
            # Move the item
            self.active_item = inventory_slot.item
            self.active_item.picked_up = True
            inventory_slot.item = None
            inventory_slot.Set_Active(True)
            return True
        return False

    # Check for collision with inventory slot, if no collision return False
    def Inventory_Slot_Collision(self, inventory_slot):
        if inventory_slot.rect().colliderect(self.game.mouse.rect_click()):
            self.clicked_inventory_slot = inventory_slot
            self.item_clicked += 1
            return True
        
        return False

    # Update the animation of the item, return False if no item
    def Update_Inventory_Slot_Item_Animation(self, inventory_slot):
        if inventory_slot.item:
            inventory_slot.item.Update_Animation()
            return True
        return False

     # Handle clicking items
    def Item_Click(self):
        if not self.game.mouse.left_click:
            if self.clicked_inventory_slot:
                if self.Item_Double_Click():
                    return
                if self.Item_Single_Click():
                    return
        return
    
    # Handle double clicking behaviour, return True if valid double click
    def Item_Double_Click(self):
        if self.game.mouse.double_click and self.clicked_inventory_slot.item:
            if self.clicked_inventory_slot.item.category == 'weapon':
                self.clicked_inventory_slot.Set_Active(True)
                self.game.mouse.Reset_Double_Click()
                return True
            
        return False


    def Find_Available_Inventory_Slot(self):
        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                return inventory_slot
        else:
            return None
    
    # Handle single clicking behaviour, return True if valid click
    def Item_Single_Click(self):
        if not self.clicked_inventory_slot.item:
            return
        if not self.game.mouse.single_click_delay and not self.game.mouse.double_click:
            if self.game.mouse.hold_down_left < 5 and self.game.mouse.hold_down_left > 0:
                # if not self.game.mouse.single_click_delay:
                self.clicked_inventory_slot.item.Activate()
                self.clicked_inventory_slot.Update()
                self.clicked_inventory_slot = None
                return True
        
        return False


    # Return the item to its previous Inventory slot and deactivate
    # the item and inventory slot
    def Return_Item(self):
        if self.clicked_inventory_slot:
            # Ensure the slot is not active when returning the item
            if not self.clicked_inventory_slot.item:  # Ensure slot is empty before returning item
                self.Move_Item(self.active_item, self.clicked_inventory_slot)                
                self.active_item = None
                self.clicked_inventory_slot = None
            else:
                # Handle the case where the slot is occupied (e.g., deny return or swap)
                print("Error: Slot already occupied when trying to return item.")
        return

    # Move the item around
    def Drag_Item(self, offset):
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
        if self.active_item.move_inventory:
            self.active_item.move_inventory = False
            self.active_item = None  # Clear active item
            return True
        for inventory_slot in self.inventory:
            # Collision with other inventory slots
            if inventory_slot.rect().colliderect(self.game.mouse.rect_pos(offset)):
                if self.Move_Item(self.active_item, inventory_slot):
                    self.clicked_inventory_slot.item = None  # Clear the original slot
                    self.clicked_inventory_slot.Set_Active(False)  # Deactivate original slot
                    self.active_item = None  # Clear active item
                    return True
        return False
    
    # Method to move an item into a slot
    def Move_Item(self, item, inventory_slot):
        if not inventory_slot.item:
            item.picked_up = False  # Ensure the item is marked as not picked up
            inventory_slot.Add_Item(item)  # Place the item in the inventory slot
            inventory_slot.Set_Active(False)  # Deactivate the slot after placing the item
            return True
        return False

    # Method to remove an item from the inventory
    def Remove_Item(self, item, move_item):
        if not move_item:
            return False

        for sending_slot in self.inventory:
            if sending_slot.item == item:
                sending_slot.Set_Active(False)  # Deactivate the slot
                sending_slot.item = None  # Remove the item from the slot
                return True

        return False
    
    
    # Active item is an item being dragged
    def Active_Item(self, offset=(0, 0)):
        # Check if there is an active item
        if not self.active_item:
            return
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
            self.Drag_Item(offset)
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
        # Check if an item can have more than one charge, example health potion is 3
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
                                new_item.Update()
                                self.game.item_handler.Add_Item(new_item)
                        self.game.item_handler.Remove_Item(item)
                        inventory_slot.item.Update()
                        return True
                    
        i = 0
        j = 0
        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                inventory_slot.Add_Item(item)
                self.game.item_handler.Remove_Item(item)
                inventory_slot.item.Update()
                return True
            # 2d array simulation for position
            i += 1
            if i >= self.x_size:
                i = 0
                j += 1

        return False


    # Implement the __iter__ method to make the class iterable
    def __iter__(self):
        return iter(self.inventory)
    
    def Render(self, surf):
        for inventory_slot in self.inventory:
            inventory_slot.Render(surf)
