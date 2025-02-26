from scripts.inventory.base_inventory import Base_Inventory
from scripts.inventory.inventory_slot import Inventory_Slot



class Rune_Inventory(Base_Inventory):
    def __init__(self, game, shared_inventory):
        super().__init__(game, shared_inventory)
        self.inventory_dic = {}

    def Append_Inventory_Dic(self, inventory_slot):
        if not inventory_slot.item:
            return
        # Ensure the type exists in the dictionary before appending
        if inventory_slot.item.type not in self.weapon_inventory_dic:
            self.weapon_inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
        
        self.weapon_inventory_dic[inventory_slot.item.type].append(inventory_slot)

    def Setup(self):
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

    def Set_Inventory_Slot_Pos(self, index):
        x_pos = index * self.size[0] + self.game.screen_width / self.game.render_scale - 160
        y_pos = self.game.screen_height / self.game.render_scale - 40
        return (x_pos, y_pos)
    
    def Reset_Inventory_Slot(self):
        if self.clicked_inventory_slot.type == 'weapon':
            self.game.player.Remove_Active_Weapon()

        return super().Reset_Inventory_Slot()
    
    def Add_Item(self, item):
        for inventory_slot in sum(self.rune_inventory_dic.values(), []):  # Flatten the lists
            if not inventory_slot.item:
                inventory_slot.Add_Item(item)
                return  # Stop after adding the rune