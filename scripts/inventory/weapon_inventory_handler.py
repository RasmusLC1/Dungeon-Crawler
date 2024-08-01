from scripts.inventory.weapon_inventory import Weapon_Inventory

MELEE_WEAPONS = {'one_handed_melee', 'two_handed_melee'}


class Weapon_Inventory_Handler():

    def __init__(self, game, player_class, proffeciency):
        self.game = game
        self.weapon_inventory = Weapon_Inventory(game)
        self.inventories = []
        self.active_inventory = 0
        self.max_inventories = 2
        self.player_class = player_class
        self.player_proffeciency = proffeciency

        self.Add_Inventory_Slot()

    def Add_Inventory_Slot(self):
        self.inventories.insert(0, self.weapon_inventory.Setup_Inventory('left_right'))
        self.inventories.insert(1, self.weapon_inventory.Setup_Inventory('bow_arrow'))


    def Add_Weapon_To_Inventory(self, weapon):
        # If the player is unable to pick up the Weapon
        if not weapon.weapon_class in self.player_proffeciency:
            if self.game.inventory.Add_Item(self):
                self.picked_up = False
                self.game.entities_render.remove(self)
            return
        

        for inventory in self.inventories:
            for inventory_slot in inventory:
                if inventory_slot.Inventory_type == 'melee':
                    if weapon.weapon_class in MELEE_WEAPONS:
                        pass
                    
                        






    def Increment_inventory(self):
        if self.active_inventory < self.max_inventories - 1:
            self.active_inventory += 1
        else:
            self.active_inventory -= 1

    def Render(self, surf):
        # Render the current active inventory
        current_inventory = self.inventories[self.active_inventory]
        for inventory_slot in current_inventory:
            inventory_slot.Render(surf)
