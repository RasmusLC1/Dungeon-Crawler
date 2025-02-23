from scripts.inventory.inventory import Inventory
from scripts.inventory.inventory_slot import Inventory_Slot
from copy import copy

class Item_Inventory(Inventory):
    def __init__(self, game):
        super().__init__(game, 9, 1)
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
        self.Setup()
        self.inventory_dic = {}
    
    # Saves inventory data to both self.saved_data and self.inventory_dic
    def Save_Inventory_Data(self):
        self.saved_data.clear()
        self.inventory_dic.clear()

        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                continue
            
            inventory_slot.item.Save_Data()
            self.saved_data[inventory_slot.index] = inventory_slot.item.saved_data
            self.inventory_dic[inventory_slot.index] = inventory_slot.item.ID  # Store item ID for quick lookup

    # Loads inventory data and updates inventory_dic
    def Load_Data(self, data):
        self.saved_data = data  # Store loaded data
        self.inventory_dic.clear()

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

            if "weapon" in item.sub_category:
                item.Set_Entity(self.game.player)

            inventory_slot.Add_Item(item)

        
        self.Configure_Inventory_Dic()

    def Configure_Inventory_Dic(self):
        for inventory_slot in self.inventory:
            if not inventory_slot.item:
                continue
            
            # Ensure the type exists in the dictionary before appending
            if inventory_slot.item.type not in self.inventory_dic:
                self.inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
            
            self.inventory_dic[inventory_slot.item.type].append(inventory_slot)


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
        

    # Add item to the inventory
    def Add_Item(self, item):
        # Check if an item can have more than one charge, example health potion is 3
        if self.Add_Item_To_Inventory_Slot_Merge(item):
            return True
                    
        return self.Add_Item_To_Inventory_Slot(item)

    
    # Merges items into existing slots if possible
    def Add_Item_To_Inventory_Slot_Merge(self, item):
        if item.max_amount <= 1:
            return False  # Can't merge single-stack items
        # Check if this item type is already in the dictionary
        if not item.type in self.inventory_dic:
            return False

        for inventory_slot in self.inventory_dic[item.type]:  
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
            if not inventory_slot.item:
                if inventory_slot.Add_Item(item):
                    self.game.item_handler.Remove_Item(item)
                    
                    # Update inventory dictionary
                    if item.type not in self.inventory_dic:
                        self.inventory_dic[item.type] = []
                    self.inventory_dic[item.type].append(inventory_slot)

                    inventory_slot.item.Update()
                    return True
        return False  # No available slots
    
    # Finds an item in the inventory using inventory_dic for faster lookup
    def Find_Item_In_Inventory(self, item):
        if item.ID in self.inventory_dic:
            index = self.inventory_dic[item.ID]
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
                self.inventory_dic[self.active_item.ID] = self.clicked_inventory_slot.index  # Update inventory dictionary
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
            self.inventory_dic[self.active_item.ID] = self.active_item.inventory_index  # Update dictionary
        self.active_item = None

    # Set the inventory to be inactive again
    def Reset_Inventory_Slot(self):
        if self.clicked_inventory_slot:
            self.clicked_inventory_slot.Set_Active(False)
            if self.clicked_inventory_slot.item:
                del self.inventory_dic[self.clicked_inventory_slot.item.ID]  # Remove from dictionary
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
                    self.clicked_inventory_slot.Reset_Inventory_Slot()  # Clear original slot
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

        return True

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
            if inventory_slot.item and inventory_slot.item.ID == item.ID:
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
