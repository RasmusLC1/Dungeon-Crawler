from scripts.inventory.keyboard_inventory import Keyboard_Inventory
from scripts.inventory.weapon_inventory.weapon_inventory import Weapon_Inventory
from scripts.inventory.rune_inventory.rune_inventory import Rune_Inventory
from scripts.inventory.item_inventory.item_inventory import Item_Inventory



class Inventory_Handler():
    def __init__(self, game):
        self.game = game
        self.active_item = None
        self.item_clicked = 0
        self.click_cooldown = 0
        self.clicked_inventory_slot = None
        self.inventory = [] # General shared inventory

        self.item_inventory = Item_Inventory(game, self.inventory)
        self.weapon_inventory = Weapon_Inventory(game, self.inventory)
        self.rune_inventory = Rune_Inventory(game, self.inventory)
        self.keyboard_inventory = Keyboard_Inventory(game, self.inventory)
        self.saved_data = {}
        
    

    def Save_Inventory_Data(self):
        self.saved_data.clear()

        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                continue
            inventory_slot.item.Save_Data()
            self.saved_data[inventory_slot.index] = inventory_slot.item.saved_data


    # Loads inventory data and updates inventory_dic
    def Load_Data(self, data):
                
        self.saved_data = data  # Store loaded data
        lookup_dic = {
                'item': self.item_inventory,
                'rune': self.weapon_inventory,
                'weapon': self.rune_inventory,
                }
        for inventory_index, item_data in data.items():
            if not item_data:
                continue
            # Find correct slot
            inventory_slot = next((slot for slot in self.inventory if slot.index == item_data["inventory_index"]), None)
            if not inventory_slot:
                continue
            self.game.item_handler.Load_Item_From_Data(item_data)
            item = self.game.item_handler.Find_Item(item_data["ID"])
            if not item:
                continue

            inventory_slot.Add_Item(item)
            
            lookup_dic.get(inventory_slot.type).Append_Inventory_Dic(inventory_slot)


    # General Update function
    def Update(self, offset=(0, 0)):
        self.Active_Item(offset)
        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                continue
            inventory_slot.Update_Item()
            if not self.Update_Inventory_Slot_Item_Animation(inventory_slot):
                continue
            # Check if the mouse has been clicked, if no we skip that inventory
            # slot if no continue to next inventory slot
            if not self.game.mouse.left_click:
                continue
            if not self.Inventory_Slot_Collision_Click(inventory_slot):
                continue
            if self.Pickup_Item_To_Move(inventory_slot):
                return
            
            
        self.Item_Click()
        self.keyboard_inventory.Key_Board_Input()
        return
    
    
    def Equip_Weapon(self):
        for inventory_slot in self.weapon_inventory_dic.values():
            if not inventory_slot.item:
                continue
            inventory_slot.item.Equip()


    def Update_Inventory_Slot_Pos(self):
        for index, inventory_slot in enumerate(self.inventory):
            pos = self.Set_Item_Inventory_Slot_Pos(index)
            inventory_slot.Update_Pos(pos)

    def Clear_Inventory(self):
        for inventory_slot in self.inventory:
            inventory_slot.Remove_Item()


    def Increment_Weapon_Inventory(self):
        pass


    # Activates when mouse has been held down for 10 ticks and
    # the inventory slot is not active anymore 
    def Pickup_Item_To_Move(self, inventory_slot):
        if self.game.mouse.hold_down_left > 10 and not inventory_slot.active:
            # Move the item
            self.active_item = inventory_slot.item
            self.active_item.picked_up = False
            inventory_slot.item = None
            inventory_slot.Set_Active(True)
            return True
        return False

    # Check for collision with inventory slot, if no collision return False
    def Inventory_Slot_Collision_Click(self, inventory_slot):
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
    # TODO: fix with UPDATE
    def Item_Double_Click(self):
        return
        if self.game.mouse.double_click and self.clicked_inventory_slot.item:
            if self.clicked_inventory_slot.item.sub_category == 'weapon':
                self.clicked_inventory_slot.Set_Active(True)
                self.game.mouse.Reset_Double_Click()
                return True
            
        return False

    # Finds the first empty inventory slot
    def Find_Available_Inventory_Slot(self):
        for i, inventory_slot in enumerate(self.inventory):
            if inventory_slot is None:
                return i # return index
        return None  # No available slots

    # Add item to the inventory
    def Add_Item(self, item):
        self.item_inventory.Add_Item(item)

    def Add_Rune(self, rune):
        self.rune_inventory.Add_Item(rune)
    
    # Merges items into existing slots if possible
    def Add_Item_To_Inventory_Slot_Merge(self, item):
        if item.max_amount <= 1:
            return False  # Can't merge single-stack items
        # Check if this item type is already in the dictionary
        if not item.type in self.item_inventory_dic:
            return False

        for inventory_slot in self.item_inventory_dic[item.type]:  
            if not inventory_slot.item or inventory_slot.item.amount >= inventory_slot.item.max_amount:
                continue

            # Calculate how much can be merged
            available_space = inventory_slot.item.max_amount - inventory_slot.item.amount
            amount_to_merge = min(item.amount, available_space)

            # Merge items
            inventory_slot.item.Increase_Amount(amount_to_merge)
            item.Set_Amount(item.amount - amount_to_merge)

            # If the entire item was merged, remove it
            if item.amount == 0:
                self.game.item_handler.Remove_Item(item)
                inventory_slot.item.Update()
                return True
            
        # If there is still remaining amount, try placing it in an empty slot
        if item.amount > 0:
            return self.Add_Item_To_Inventory_Slot(item)

        return False  # No slot to merge into


    # Places an item in an empty slot if merging is not possible
    def Add_Item_To_Inventory_Slot(self, item):

        for inventory_slot in self.inventory:
            if inventory_slot.item:
                continue
            if not inventory_slot.Add_Item(item):
                continue
            
            self.game.item_handler.Remove_Item(item)
            
            try:
                # Update inventory dictionary
                if item.type not in self.item_inventory_dic or not isinstance(self.item_inventory_dic[item.type], list):
                    self.item_inventory_dic[item.type] = []


                self.item_inventory_dic[item.type].append(inventory_slot)
            except Exception as e:
                print("FAILED TO ADD ITEM", e, item, self.item_inventory_dic)
            inventory_slot.item.Update()
            return True
        return False  # No available slots

    # Handle single clicking behavior, return True if valid click
    def Item_Single_Click(self):
        if not self.clicked_inventory_slot or not self.clicked_inventory_slot.item:
            return False

        if self.game.mouse.single_click_delay and self.game.mouse.double_click:
            return False

        if not (0 < self.game.mouse.hold_down_left < 5):
            return False

        self.clicked_inventory_slot.item.Activate()
        self.clicked_inventory_slot.Update()
        self.clicked_inventory_slot = None
        self.game.mouse.Set_Inventory_Clicked(10)
        return True

    # Return the item to its previous Inventory slot and deactivate the item and slot
    def Return_Item(self):
        if self.clicked_inventory_slot:
            if not self.clicked_inventory_slot.item:  # Ensure slot is empty before returning item
                self.Move_Item(self.active_item, self.clicked_inventory_slot)
                self.item_inventory_dic[self.active_item.type] = self.clicked_inventory_slot.index  # Update inventory dictionary
                self.active_item = None
                self.clicked_inventory_slot = None
            else:
                print("Error: Slot already occupied when trying to return item.")
        return

    # Move the item around
    def Drag_Item(self, offset):
        self.active_item.Render(self.game.display, offset)
        self.active_item.Move(self.game.mouse.mpos)

        if not self.game.mouse.left_click:
            self.Place_Down_Item()
            self.Reset_Inventory_Slot()
            return False
        return True

    # Places an item down in the inventory
    def Place_Down_Item(self):
        if self.active_item.Place_Down():
            self.game.item_handler.Add_Item(self.active_item)
            self.active_item.picked_up = False
            self.active_item.Set_Tile()
            self.item_inventory_dic[self.active_item.type] = self.active_item.inventory_index  # Update dictionary
            # self.item_inventory_dic[self.active_item.type].clear()
        self.active_item = None

    def Reset_Inventory_Dic_Slot(self, inventory_slot):
        if not inventory_slot.item:
            return
        type = inventory_slot.item.type
        
        if self.item_inventory.Clear_Inventory_Dic_Slot(type):
            return
        elif self.rune_inventory.Clear_Inventory_Dic_Slot(type):
            return
        elif self.weapon_inventory.Clear_Inventory_Dic_Slot(type):
            return

    # Set the inventory to be inactive again
    def Reset_Inventory_Slot(self):
        if not self.clicked_inventory_slot:
            return
        
        self.clicked_inventory_slot.Set_Active(False)

        if self.clicked_inventory_slot.type == 'weapon':
            self.game.player.Remove_Active_Weapon()

        if self.clicked_inventory_slot.item:
            self.Reset_Inventory_Dic_Slot(self.clicked_inventory_slot)
            
        self.clicked_inventory_slot.item = None
        self.clicked_inventory_slot = None

 
 

    def Move_Item_To_New_Slot(self, offset):
        # Check if the item is being moved to another inventory
        if self.active_item.move_inventory_slot:
            self.active_item.move_inventory_slot = False
            self.active_item = None  # Clear active item
            return True

        for inventory_slot in self.inventory:
            if inventory_slot.rect().colliderect(self.game.mouse.rect_pos(offset)):
                if inventory_slot.active:
                    return False

                if self.Swap_Item(self.active_item, inventory_slot):
                    return True

                if self.Move_Item(self.active_item, inventory_slot):
                    self.Reset_Inventory_Slot()
                    for inventory_slot in self.inventory:
                        if not inventory_slot.item:
                            continue
                    self.active_item = None  # Clear active item
                    return True
        return False

    def Move_Item(self, item, inventory_slot):
        inventory_type_holder = item.inventory_type
        item.picked_up = True  # Ensure the item is marked as picked up

        # Try to place the item in the inventory slot
        if not inventory_slot.Add_Item(item):
            return False

        inventory_slot.Set_Active(False)  # Deactivate slot after placing item

        if inventory_type_holder:
            item.Update_Player_Hand(inventory_type_holder)

        self.Set_Player_Weapon(item, inventory_slot)
        
        return True

    def Set_Player_Weapon(self, item, inventory_slot):
        if inventory_slot.type == 'weapon':
            item.Equip()

    def Swap_Item(self, item, inventory_slot):
        if inventory_slot.item:
            item_holder = inventory_slot.item  # Store item to be swapped
            self.clicked_inventory_slot.Reset_Inventory_Slot()
            inventory_slot.Reset_Inventory_Slot()

            # Move original item to active inventory slot
            self.clicked_inventory_slot.Add_Item(item_holder)

            self.clicked_inventory_slot = None  # Clear clicked slot

            # Move active item into the new slot
            inventory_slot.Add_Item(self.active_item)

            self.weapon_inventory.Equip_Weapon()


            self.active_item = None  # Clear active item
            return True

        return False


    def Remove_Item(self, item, move_item):
        if not move_item:
            return False
        
        for inventory_slot in self.inventory:
            if not inventory_slot.item.ID == item.ID:
                continue
            inventory_slot.Set_Active(False)  # Deactivate the slot
            inventory_slot.item = None  # Remove the item
            return True
        
        return False

    def Active_Item(self, offset=(0, 0)):
        if not self.active_item:
            return

        item_out_of_bounds = self.active_item.Move_Legal(
            self.game.mouse.mpos, self.game.player.pos, self.game.tilemap, offset
        )

        if not item_out_of_bounds:
            if not self.game.mouse.left_click:
                if self.Move_Item_To_New_Slot(offset):
                    return  
                if not self.active_item:
                    return
                self.Return_Item()
                return
            self.active_item.Render_Out_Of_Bounds(
                self.game.player.pos, self.game.mouse.mpos, self.game.display, offset
            )
        else:
            if not self.Drag_Item(offset):
                return
            self.active_item.Render_In_Bounds(
                self.game.player.pos, self.game.mouse.mpos, self.game.display, offset
            )

    def Overflow(self, item):
        empty_slots = {i: slot for i, slot in enumerate(self.inventory) if not slot.item}
        
        for slot in empty_slots.values():
            if slot.Add_Item(item):
                slot.item.Update()
                return True

        return False

    def Render(self, surf):
        for inventory_slot in self.inventory:
            inventory_slot.Render(surf)
