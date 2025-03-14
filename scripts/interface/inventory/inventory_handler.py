from scripts.interface.inventory.keyboard_inventory import Keyboard_Inventory
from scripts.interface.inventory.weapon_inventory.weapon_inventory import Weapon_Inventory
from scripts.interface.inventory.rune_inventory.rune_inventory import Rune_Inventory
from scripts.interface.inventory.item_inventory.item_inventory import Item_Inventory



class Inventory_Handler():
    def __init__(self, game):
        self.game = game
        self.active_item = None
        self.item_clicked = 0
        self.click_cooldown = 0
        self.clicked_inventory_slot = None
        self.inventory = [] # General shared inventory
        self.inventory_dic = {}

        self.item_inventory = Item_Inventory(game, self.inventory, self.inventory_dic)
        self.weapon_inventory = Weapon_Inventory(game, self.inventory, self.inventory_dic)
        self.rune_inventory = Rune_Inventory(game, self.inventory, self.inventory_dic)
        self.keyboard_inventory = Keyboard_Inventory(game, self.inventory, self.inventory_dic)
        self.saved_data = {}
        
    

    def Save_Inventory_Data(self):
        self.saved_data.clear()

        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                continue
            inventory_slot.item.Save_Data()
            self.saved_data[inventory_slot.index] = inventory_slot.item.saved_data
            self.saved_data['active_inventory'] = self.weapon_inventory.active_inventory_slot.index


    # Loads inventory data and updates inventory_dic
    def Load_Data(self, data):
        active_inventory_slot = 12 # Default value
        self.saved_data = data  # Store loaded data
        lookup_dic = {
                'item': self.item_inventory,
                'weapon': self.weapon_inventory,
                'rune': self.rune_inventory,
                }
        for inventory_index, item_data in data.items():
            if not item_data:
                continue
            
            # Get the active_inventory_slot
            if isinstance(item_data, int):
                active_inventory_slot = item_data
                continue
            
            if "inventory_index" not in item_data:
                continue
            # Find correct slot
            inventory_slot = next((slot for slot in self.inventory if slot.index == item_data["inventory_index"]), None)
            if not inventory_slot:
                continue
            item = self.game.item_handler.Load_Item_From_Data(item_data)
            if not item:
                continue
            

            item.Remove_Tile()
            if not inventory_slot.Add_Item(item):
                print("FAILED TO LOAD ITEM: ", item.type, inventory_slot)
            
            # self.weapon_inventory.Set_Active_Inventory_Slot()
            lookup_dic.get(inventory_slot.type).Append_Inventory_Dic(inventory_slot)
        self.rune_inventory.Add_Active_Runes()

        self.weapon_inventory.Set_Active_Inventory_Slot(self.inventory_dic.get(active_inventory_slot))

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

    def Update_Runes(self):
        self.rune_inventory.Add_Active_Runes()

    # Needs to resize the UI correctly when screen is resized
    def Update_Inventory_Slot_Pos(self):
        return
        for index, inventory_slot in enumerate(self.inventory):
            pos = self.Set_Item_Inventory_Slot_Pos(index)
            inventory_slot.Update_Pos(pos)

    def Clear_Inventory(self):
        for inventory_slot in self.inventory:
            inventory_slot.Remove_Item()


    def Increment_Weapon_Inventory(self):
        self.weapon_inventory.Mouse_Scroll_Update_Active_Inventory()


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
                    if self.weapon_inventory.active_inventory_slot.item:
                        self.weapon_inventory.active_inventory_slot.item.Set_Position(self.weapon_inventory.active_inventory_slot.pos)
                    return
                if self.Item_Single_Click():
                    return
        return
    
    # Handle double clicking behaviour, return True if valid double click
    # TODO: fix with UPDATE
    def Item_Double_Click(self):
        if self.game.mouse.double_click and self.clicked_inventory_slot.item:
            if not self.clicked_inventory_slot.item.sub_category == 'weapon':
                return False
            active_inventory_slot = self.weapon_inventory.active_inventory_slot
            self.clicked_inventory_slot

            if self.Swap_Item(active_inventory_slot):
                self.clicked_inventory_slot = None
                return True

            if self.Move_Item(self.clicked_inventory_slot.item, active_inventory_slot):
                self.Reset_Inventory_Slot()
                for inventory_slot in self.inventory:
                    if not inventory_slot.item:
                        continue
                self.clicked_inventory_slot = None
                return True
            self.clicked_inventory_slot = None
            return True
        
        self.clicked_inventory_slot = None
        return False

    # Finds the first empty inventory slot
    def Find_Available_Inventory_Slot(self):
        for i, inventory_slot in enumerate(self.inventory):
            if inventory_slot is None:
                return i # return index
        return None  # No available slots

    # Add item to the inventory
    def Add_Item(self, item):
        return self.item_inventory.Add_Item(item)

    def Add_Rune(self, rune):
        self.rune_inventory.Add_Item(rune)

    def Replace_Rune(self, old_rune, new_rune):
        self.rune_inventory.Replace_Rune(old_rune, new_rune)

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
                self.item_inventory.inventory_dic[self.active_item.type] = self.clicked_inventory_slot.index  # Update inventory dictionary
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
            inventory_slots = self.item_inventory.inventory_dic.get(self.active_item.type)
            
            if inventory_slots:
                first_slot = next((slot for slot in inventory_slots if slot.item), None)
                if first_slot:
                    self.item_inventory.Remove_Item_From_Inventory(first_slot)
            
            self.game.item_handler.Add_Item(self.active_item)
            self.active_item.picked_up = False
            self.active_item.Set_Tile()
        
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

                if self.Swap_Item(inventory_slot):
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

        self.weapon_inventory.Equip_Weapon()
        
        return True


    def Swap_Item(self, inventory_slot):
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


    def Remove_Item(self, item):
        # Ensure item is in the inventory
        inventory_slot = self.inventory_dic.get(item.inventory_index)
    
        if not inventory_slot:  
            return False  # Item not found or slot is None

        

        self.inventory_dic.pop(inventory_slot.item.type, None)
        inventory_slot.Set_Active(False)  # Deactivate the slot
        inventory_slot.Remove_Item()

        return True

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

    def Find_Inventory_Slot(self, index):
        return self.inventory_dic.get(index)

    def Overflow(self, item):
        empty_slots = {i: slot for i, slot in enumerate(self.inventory) if not slot.item}
        
        for slot in empty_slots.values():
            if slot.Add_Item(item):
                slot.item.Update()
                return True

        return False

    def Find_Inventory_Slot(self, index):
        return self.inventory_dic.get(index)
    

    def Render(self, surf):
        for inventory_slot in self.inventory:
            inventory_slot.Render(surf)
