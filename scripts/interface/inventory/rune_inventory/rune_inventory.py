from scripts.interface.inventory.base_inventory import Base_Inventory
from scripts.interface.inventory.inventory_slot import Inventory_Slot

class Rune_Inventory(Base_Inventory):

    def Append_Inventory_Dic(self, inventory_slot):
        if not inventory_slot.item:
            return
        # Ensure the type exists in the dictionary before appending
        if inventory_slot.item.type not in self.inventory_dic:
            self.inventory_dic[inventory_slot.index] = []  # Initialize if not present
        
        self.inventory_dic[inventory_slot.index].append(inventory_slot)
        

    def Setup(self):
        symbols = ['z', 'x', 'c']
        for i in range(3):
            
            (x_pos, y_pos) = self.Set_Inventory_Slot_Pos(i)
            index = i + 9
            inventory_slot = Inventory_Slot(self.game, (x_pos, y_pos), 'rune', self.size, None, index, symbols[i])
            background = self.game.assets['rune_background'][0]
            inventory_slot.Add_Background(background)
            # inventory_slot.inventory_type = 'rune'
            inventory_slot.Set_White_List(['rune'])
            self.Add_Inventory_Slot(inventory_slot)

    def Set_Inventory_Slot_Pos(self, index):
        x_pos = index * self.size[0] + self.game.screen_width / self.game.render_scale - 160
        y_pos = self.game.screen_height / self.game.render_scale - 40
        return (x_pos, y_pos)
    
    # Initialise the active runes
    def Add_Active_Runes(self):
        for rune in self.game.rune_handler.active_runes:
            self.shared_inventory_dic[rune.inventory_index].Add_Item(rune)

    def Replace_Rune(self, old_rune, new_rune):
        # Find the corresponding inventory slot
        for inventory_slot in self.shared_inventory:
            if not inventory_slot.item:
                continue

            if inventory_slot.item.type != old_rune.type:
                continue
            print(inventory_slot)

            # Replace with the new rune
            inventory_slot.item = new_rune

            # Ensure the new rune is added to the dictionary
            if new_rune.type not in self.inventory_dic:
                self.inventory_dic[new_rune.type] = []

            self.inventory_dic[new_rune.type].append(inventory_slot)

            # Optionally remove the old rune from the dictionary
            # self.inventory_dic[old_rune.type].remove(inventory_slot)
            # if not self.inventory_dic[old_rune.type]:
            #     del self.inventory_dic[old_rune.type]
            return True  # Successfully replaced the rune


    
    def Add_Item(self, item):
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
            item.Remove_Tile()
            return True
        return False  # No available slots