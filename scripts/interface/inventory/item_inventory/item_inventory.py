from scripts.interface.inventory.base_inventory import Base_Inventory
from scripts.interface.inventory.inventory_slot import Inventory_Slot

class Item_Inventory(Base_Inventory):

    def Append_Inventory_Dic(self, inventory_slot):
        if not inventory_slot.item:
            return
        # Ensure the type exists in the dictionary before appending
        if inventory_slot.item.type not in self.inventory_dic:
            self.inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
        
        self.inventory_dic[inventory_slot.item.type].append(inventory_slot)
        

    def Setup(self):
        for i in range(9):
            (x, y) = self.Set_Inventory_Slot_Pos(i)
            inventory_slot = Inventory_Slot(self.game, (x, y), 'item', self.size, None, i, str(i + 1))
            inventory_slot.Set_White_List(['weapon', 'potion', 'loot'])
            self.Add_Inventory_Slot(inventory_slot)

    def Set_Inventory_Slot_Pos(self, index):
        x = index * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 130
        y = self.game.screen_height / self.game.render_scale - 40
        return (x, y)
    

    
    # Add item to the inventory
    def Add_Item(self, item):
        # Check if an item can have more than one charge, example health potion is 3
        item.Remove_Tile()
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

        for inventory_slot in self.shared_inventory:
            if inventory_slot.item:
                continue
            if not inventory_slot.Add_Item(item):
                continue
            
            self.game.item_handler.Remove_Item(item)
            
            try:
                # Update inventory dictionary
                if item.type not in self.inventory_dic or not isinstance(self.inventory_dic[item.type], list):
                    self.inventory_dic[item.type] = []


                self.inventory_dic[item.type].append(inventory_slot)
            except Exception as e:
                print("FAILED TO ADD ITEM", e, item, self.inventory_dic)
            inventory_slot.item.Update()
            return True
        return False  # No available slots
