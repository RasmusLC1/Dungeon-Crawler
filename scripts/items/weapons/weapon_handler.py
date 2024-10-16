from scripts.items.weapons.close_combat.sword import Sword
from scripts.items.weapons.close_combat.torch import Torch
from scripts.items.weapons.projectiles.spear import Spear
from scripts.items.weapons.ranged_weapons.bow import Bow
from scripts.items.weapons.projectiles.arrow import Arrow
from scripts.items.weapons.shields.shield import Shield


class Weapon_Handler():
    def __init__(self, game):
        self.game = game    

    def Weapon_Spawner(self, name, pos_x, pos_y, amount = 0):
        if 'sword' in name:
            self.Spawn_Sword(pos_x, pos_y)
            return True
        elif 'shield' in name:
            self.Spawn_Shield(pos_x, pos_y)
            return True
        elif 'spear' in name:
            self.Spawn_Spear(pos_x, pos_y)
            return True
        elif 'torch' in name:
            self.Spawn_Torch(pos_x, pos_y)
            return True
        elif 'bow' in name:
            self.Spawn_Bow(pos_x, pos_y)
            return True
        elif 'arrow' in name:
            self.Spawn_Arrow(pos_x, pos_y, amount)
            return True

        return False

    def Spawn_Sword(self, pos_x, pos_y):
        weapon = Sword(self.game, (pos_x, pos_y), (16,16))
        self.game.item_handler.Add_Item(weapon)
    
    def Spawn_Shield(self, pos_x, pos_y):
        weapon = Shield(self.game, (pos_x, pos_y), (16,16))
        self.game.item_handler.Add_Item(weapon)

    def Spawn_Spear(self, pos_x, pos_y):
        weapon = Spear(self.game, (pos_x, pos_y), (16,16))
        self.game.item_handler.Add_Item(weapon)

    def Spawn_Torch(self, pos_x, pos_y):
        weapon = Torch(self.game, (pos_x, pos_y), (16,16))
        self.game.item_handler.Add_Item(weapon)

    def Spawn_Bow(self, pos_x, pos_y):
        weapon = Bow(self.game, (pos_x, pos_y), (16,16))
        self.game.item_handler.Add_Item(weapon)

    def Spawn_Arrow(self, pos_x, pos_y, amount):
        for i in range(amount):
            arrow = Arrow(self.game, (pos_x, pos_y), (16,16))
            self.game.item_handler.Add_Item(arrow)
