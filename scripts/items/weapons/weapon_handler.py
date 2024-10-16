from scripts.items.weapons.close_combat.sword import Sword
from scripts.items.weapons.close_combat.torch import Torch
from scripts.items.weapons.projectiles.spear import Spear
from scripts.items.weapons.ranged_weapons.bow import Bow
from scripts.items.weapons.projectiles.arrow import Arrow
from scripts.items.weapons.shields.shield import Shield


class Weapon_Handler():
    def __init__(self, game):
        self.game = game    

    def Weapon_Spawner(self, name, pos_x, pos_y, amount = 0, data = None):
        weapon = None
        if 'sword' in name:
            weapon = self.Spawn_Sword(pos_x, pos_y)

        elif 'shield' in name:
            weapon = self.Spawn_Shield(pos_x, pos_y)

        elif 'spear' in name:
            weapon = self.Spawn_Spear(pos_x, pos_y)

        elif 'torch' in name:
            weapon = self.Spawn_Torch(pos_x, pos_y)

        elif 'bow' in name:
            weapon = self.Spawn_Bow(pos_x, pos_y)

        elif 'arrow' in name:
            weapon = self.Spawn_Arrow(pos_x, pos_y, amount)

        if not weapon:
            return False
        
        if data:
            weapon.Load_Data(data)
        
        self.game.item_handler.Add_Item(weapon)

        return True


    def Spawn_Sword(self, pos_x, pos_y):
        return Sword(self.game, (pos_x, pos_y), (16,16))

    
    def Spawn_Shield(self, pos_x, pos_y):
        return Shield(self.game, (pos_x, pos_y), (16,16))

    def Spawn_Spear(self, pos_x, pos_y):
        return Spear(self.game, (pos_x, pos_y), (16,16))

    def Spawn_Torch(self, pos_x, pos_y):
        return Torch(self.game, (pos_x, pos_y), (16,16))


    def Spawn_Bow(self, pos_x, pos_y):
        return Bow(self.game, (pos_x, pos_y), (16,16))


    def Spawn_Arrow(self, pos_x, pos_y, amount):
        return Arrow(self.game, (pos_x, pos_y), (16,16), amount)

