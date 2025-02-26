from scripts.inventory.base_inventory import Base_Inventory
from scripts.inventory.inventory_slot import Inventory_Slot



class Weapon_Inventory(Base_Inventory):
    def __init__(self, game, shared_inventory):
        super().__init__(game, shared_inventory)
        self.inventory_dic = {}

    def Append_Inventory_Dic(self, inventory_slot):
        if not inventory_slot.item:
            return
        # Ensure the type exists in the dictionary before appending
        if inventory_slot.item.type not in self.inventory_dic:
            self.inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
        
        self.inventory_dic[inventory_slot.item.type].append(inventory_slot)

    def Setup(self):
        for i in range(2):
            (x, y) = self.Set_Inventory_Slot_Pos(i)
            inventory_slot = Inventory_Slot(self.game, (x, y), 'weapon', self.size, None, 12, str(10))
            inventory_slot.Set_White_List(['weapon'])
            self.inventory.append(inventory_slot)

    def Set_Inventory_Slot_Pos(self, index):
        x = index * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 240
        y = self.game.screen_height / self.game.render_scale - 40
        return (x, y)

    def Equip_Weapon(self):
        for inventory in self.inventory_dic.values():
            for inventory_slot in inventory:
                if inventory_slot.item:
                    self.game.player.Set_Active_Weapon(inventory_slot.item)
                    break