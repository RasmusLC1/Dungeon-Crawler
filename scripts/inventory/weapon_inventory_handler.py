from scripts.inventory.weapon_inventory import Weapon_Inventory

MELEE_WEAPONS = {'one_handed_melee', 'two_handed_melee'}


class Weapon_Inventory_Handler():

    def __init__(self, game, player_class, proffeciency):
        self.game = game
        self.inventories = []
        self.active_inventory = 0
        self.max_inventories = 2
        self.player_class = player_class
        self.player_proffeciency = proffeciency
        self.weapon_one = None
        self.weapon_two = None
        self.saved_data = {}

        self.Add_Inventory_Slot()

    def Save_Inventory_Data(self):
        i = 0
        for inventory in self.inventories:
            inventory.Save_Inventory_Data()
            self.saved_data[inventory.index] = inventory.saved_data
            i += 1

    def Load_Data(self, data):
        for item_id, item_data in data.items():
            if not item_data:
                continue
            # Extract the key value
            key = next(iter(item_data))
            for inventory in self.inventories:
                if key != inventory.index:
                    continue
                
                inventory.Load_Data(item_data)

    def Clear_Inventory(self):
        for inventory in self.inventories:
            inventory.Clear_Inventory()

    def Add_Inventory_Slot(self):
        self.inventories.append(Weapon_Inventory(self.game, 'left_right', 0))
        self.inventories.append(Weapon_Inventory(self.game, 'bow_arrow', 1))


    def Update(self, offset=(0, 0)):
        self.inventories[self.active_inventory].Update(offset)


    def Increment_inventory(self):
        if self.active_inventory < self.max_inventories - 1:
            self.active_inventory += 1
        else:
            self.active_inventory -= 1

    def Render(self, surf):
        self.Render_Inventory(surf)
        # Render the current active inventory
        
    def Render_Inventory(self, surf):
        current_inventory = self.inventories[self.active_inventory]
        for inventory_slot in current_inventory:
            inventory_slot.Render(surf)
