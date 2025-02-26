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
        if inventory_slot.item.type not in self.weapon_inventory_dic:
            self.weapon_inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
        
        self.weapon_inventory_dic[inventory_slot.item.type].append(inventory_slot)

    def Setup(self):
        for i in range(2):
            (x, y) = self.Set_Weapon_Inventory_Slot_Pos(i)
            inventory_slot = Inventory_Slot(self.game, (x, y), 'weapon', self.size, None, 12, str(10))
            inventory_slot.Set_White_List(['weapon'])
            self.inventory.append(inventory_slot)

    def Set_Inventory_Slot_Pos(self, index):
        x = index * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 240
        y = self.game.screen_height / self.game.render_scale - 40
        return (x, y)
    
    def Reset_Inventory_Slot(self):
        if self.clicked_inventory_slot.type == 'weapon':
            self.game.player.Remove_Active_Weapon()

        return super().Reset_Inventory_Slot()
    
    def Move_Item(self, item, inventory_slot):
        inventory_type_holder = item.inventory_type

        if not super().Move_Item(item, inventory_slot):
            return False
        
        if inventory_type_holder:
            item.Update_Player_Hand(inventory_type_holder)

        self.Set_Player_Weapon(item, inventory_slot)
        return True
    
    def Set_Player_Weapon(self, item, inventory_slot):
        if inventory_slot.type == 'weapon':
            item.Equip()

    def Equip_Weapon(self):
        for inventory_slot in self.weapon_inventory_dic.values():
            if not inventory_slot.item:
                continue
            inventory_slot.item.Equip()

    def Swap_Item(self, item, inventory_slot):
        if not super().Swap_Item(item, inventory_slot):
            return False
        
        for inventory in self.weapon_inventory_dic.values():
            for inventory_slot in inventory:
                if inventory_slot.item:
                    self.game.player.Set_Active_Weapon(inventory_slot.item)
                    break

        return True