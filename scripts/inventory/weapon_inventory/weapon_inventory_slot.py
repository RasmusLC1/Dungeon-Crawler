from scripts.inventory.inventory_slot import Inventory_Slot

class Weapon_Inventory_Slot(Inventory_Slot):
    def __init__(self, game, pos, type, size, item, index, key = None):
        super().__init__(game, pos, type, size, item, index, key)
        self.active_inventory = False

    def Set_Active_Inventory(self, state):
        self.active_inventory = True
        if self.item:
            self.item.Equip()

    def Render(self, surf):
        
        return super().Render(surf)

    # Render the keyboard shortcut
    def Render_Key(self, surf):
        pass