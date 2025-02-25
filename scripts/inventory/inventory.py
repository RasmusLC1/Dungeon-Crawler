from scripts.inventory.inventory_slot import Inventory_Slot
from copy import copy

class Inventory():
    def __init__(self, game):
        self.x_size = 9
        self.y_size = 1
        self.game = game
        self.available_pos = []
        self.size = (34, 34)
        self.active_item = None
        self.item_clicked = 0
        self.click_cooldown = 0
        self.clicked_inventory_slot = None
        self.inventory = []
        self.saved_data = {}
        self.item_inventory_dic = {}
        self.rune_inventory_dic = {}
        self.weapon_inventory_dic = {}
        self.Configure_Keyboard()
        self.lookup_dic = {
            'item': self.Append_Item_Inventory_Dic,
            'rune': self.Append_Rune_Inventory_Dic,
            'weapon': self.Append_Weapon_Inventory_Dic,
        }
        self.Setup()
    
    

    def Save_Inventory_Data(self):
        self.saved_data.clear()
        self.inventory_dic = {'item': {}, 'weapon': {}, 'rune': {}}  # Reinitialize after clearing

        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                continue
            inventory_slot.item.Save_Data()
            self.saved_data[inventory_slot.index] = inventory_slot.item.saved_data


    # Loads inventory data and updates inventory_dic
    def Load_Data(self, data):
                
        self.saved_data = data  # Store loaded data
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
            self.lookup_dic.get(inventory_slot.type)(inventory_slot)

        self.Configure_Inventory_Dic()

    def Configure_Inventory_Dic(self):

        self.inventory_dic = {'item': {}, 'weapon': {}, 'rune': {}}
        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                continue
            # Call the relevant functions
            self.lookup_dic.get(inventory_slot.type)(inventory_slot)
        

    
    def Append_Rune_Inventory_Dic(self, inventory_slot):
        if not inventory_slot.item:
            return
        # Ensure the type exists in the dictionary before appending
        if inventory_slot.item.type not in self.rune_inventory_dic:
            self.rune_inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
        
        self.rune_inventory_dic[inventory_slot.item.type].append(inventory_slot)
    
    def Append_Weapon_Inventory_Dic(self, inventory_slot):
        if not inventory_slot.item:
            return
        # Ensure the type exists in the dictionary before appending
        if inventory_slot.item.type not in self.weapon_inventory_dic:
            self.weapon_inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
        
        self.weapon_inventory_dic[inventory_slot.item.type].append(inventory_slot)
    
    def Append_Item_Inventory_Dic(self, inventory_slot):
        if not inventory_slot.item:
            return
        # Ensure the type exists in the dictionary before appending
        if inventory_slot.item.type not in self.item_inventory_dic:
            self.item_inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
        
        self.item_inventory_dic[inventory_slot.item.type].append(inventory_slot)

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
        self.Key_Board_Input()
        return
    
    

    def Update_Inventory_Slot_Pos(self):
        for index, inventory_slot in enumerate(self.inventory):
            pos = self.Set_Item_Inventory_Slot_Pos(index)
            inventory_slot.Update_Pos(pos)

    def Clear_Inventory(self):
        for inventory_slot in self.inventory:
            inventory_slot.Remove_Item()

    


    # Configure the inventory when Initialiased
    def Setup(self):
        self.Setup_Inventory_Dic()
        self.Setup_Item_Inventory()
        self.Setup_Weapon_Inventory()
        self.Setup_Rune_Inventory()

    def Setup_Inventory_Dic(self):
        self.inventory_dic = {
            'item': {},
            'weapon': {},
            'rune': {}
        }
        
    def Setup_Item_Inventory(self):
        for i in range(self.x_size):
            (x, y) = self.Set_Item_Inventory_Slot_Pos(i)
            inventory_slot = Inventory_Slot(self.game, (x, y), 'item', self.size, None, i, str(i + 1))
            inventory_slot.Set_White_List(['weapon', 'potion', 'loot'])
            self.inventory.append(inventory_slot)

    def Setup_Weapon_Inventory(self):
        y =  self.game.screen_height / self.game.render_scale - 40
        x = self.game.screen_width / 2 / self.game.render_scale - 220
        inventory_slot = Inventory_Slot(self.game, (x, y), 'weapon', self.size, None, 12, str(10))
        inventory_slot.Set_White_List(['weapon'])
        self.inventory.append(inventory_slot)

    # Configure the inventory when initialized
    def Setup_Rune_Inventory(self):
        symbols = ['z', 'x', 'c']
        for i in range(3):
            
            (x_pos, y_pos) = self.Set_Rune_Inventory_Slot_Pos(i)
            index = i + 9
            inventory_slot = Inventory_Slot(self.game, (x_pos, y_pos), 'rune', self.size, None, index, symbols[i])
            background = self.game.assets['rune_background'][0]
            inventory_slot.Add_Background(background)
            # inventory_slot.inventory_type = 'rune'
            inventory_slot.Set_White_List(['rune'])
            self.inventory.append(inventory_slot)  # Add to instance's inventory
            self.rune_inventory_dic[inventory_slot.index] = []
            self.rune_inventory_dic[inventory_slot.index].append(inventory_slot)


    def Set_Rune_Inventory_Slot_Pos(self, index):
        x_pos = index * self.size[0] + self.game.screen_width / self.game.render_scale - 160
        y_pos = self.game.screen_height / self.game.render_scale - 40
        return (x_pos, y_pos)
        

    def Set_Item_Inventory_Slot_Pos(self, index):
        x = index * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 130
        y = self.game.screen_height / self.game.render_scale - 40
        return (x, y)

    def Configure_Keyboard(self):
        return

    def Key_Board_Input(self):
        keyboard = self.game.keyboard_handler
        key_map = {
            keyboard._1_pressed: 0, keyboard._2_pressed: 1, keyboard._3_pressed: 2,
            keyboard._4_pressed: 3, keyboard._5_pressed: 4, keyboard._6_pressed: 5,
            keyboard._7_pressed: 6, keyboard._8_pressed: 7, keyboard._9_pressed: 8,
            keyboard.z_pressed: 10, keyboard.x_pressed: 11, keyboard.c_pressed: 12,
        }

        for key, index in key_map.items():
            if key:
                self.Activate_Inventory_Slot(index)
                break
    

    def Activate_Inventory_Slot(self, index):
        inventory_slot = self.inventory[index]
        if inventory_slot.item:
            inventory_slot.item.Activate()
            inventory_slot.Update()

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
    def Item_Double_Click(self):
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

    def Item_Double_Click(self):
        if not super().Item_Double_Click():
            return
        active_inventory = self.game.weapon_inventory.active_inventory
        weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
        self.clicked_inventory_slot.item.Handle_Double_Click(self, weapon_inventory)
        

    # Add item to the inventory
    def Add_Item(self, item):
        # Check if an item can have more than one charge, example health potion is 3
        if self.Add_Item_To_Inventory_Slot_Merge(item):
            return True
                    
        return self.Add_Item_To_Inventory_Slot(item)

    def Add_Rune(self, rune):
        for inventory_slot in sum(self.rune_inventory_dic.values(), []):  # Flatten the lists
            if not inventory_slot.item:
                inventory_slot.Add_Item(rune)
                return  # Stop after adding the rune
    
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
    
    # Finds an item in the inventory using inventory_dic for faster lookup
    def Find_Item_In_Inventory(self, item):
        if item.ID in self.item_inventory_dic:
            index = self.item_inventory_dic[item.type]
            return self.inventory[index]
        return None

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
        
        if type in self.item_inventory_dic:
            self.item_inventory_dic[type]  # Remove from dictionary
        elif type in self.rune_inventory_dic:
            self.item_inventory_dic[type]  # Remove from dictionary
        elif type in self.weapon_inventory_dic:
            self.item_inventory_dic[type]  # Remove from dictionary

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

    # Handle double clicking behaviour, return True if valid double click
    def Item_Double_Click(self):
        if self.game.mouse.double_click and self.clicked_inventory_slot.item:
            if self.clicked_inventory_slot.item.sub_category == 'weapon':
                self.clicked_inventory_slot.Set_Active(True)
                self.game.mouse.Reset_Double_Click()
                return True
            
        return False

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
            self.game.player.Set_Active_Weapon(item_holder, self.clicked_inventory_slot.inventory_type)

            self.clicked_inventory_slot = None  # Clear clicked slot

            # Move active item into the new slot
            inventory_slot.Add_Item(self.active_item)
            self.game.player.Set_Active_Weapon(self.active_item, inventory_slot.inventory_type)

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
