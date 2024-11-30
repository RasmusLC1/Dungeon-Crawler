from scripts.items.weapons.close_combat.sword import Sword
from scripts.items.weapons.close_combat.halberd import Halberd
from scripts.items.weapons.close_combat.torch import Torch
from scripts.items.weapons.close_combat.battle_axe import Battle_Axe
from scripts.items.weapons.projectiles.spear import Spear
from scripts.items.weapons.projectiles.hatchet import Hatchet
from scripts.items.weapons.projectiles.hammer import Hammer
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

        elif 'halberd' in name:
            weapon = self.Spawn_Halberd(pos_x, pos_y)

        elif 'hatchet' in name:
            weapon = self.Spawn_Hatchet(pos_x, pos_y)

        elif 'hammer' in name:
            weapon = self.Spawn_Hammer(pos_x, pos_y)

        elif 'battle_axe' in name:
            weapon = self.Spawn_Battle_Axe(pos_x, pos_y)

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
            if weapon.equipped:
                weapon.entity = self.game.player
                weapon.Equip()
        
        if not weapon.in_inventory:
            self.game.item_handler.Add_Item(weapon)

        return True


    def Spawn_Sword(self, pos_x, pos_y):
        return Sword(self.game, (pos_x, pos_y))

    def Spawn_Halberd(self, pos_x, pos_y):
        return Halberd(self.game, (pos_x, pos_y))
    
    def Spawn_Hatchet(self, pos_x, pos_y):
        return Hatchet(self.game, (pos_x, pos_y))
    
    def Spawn_Hammer(self, pos_x, pos_y):
        return Hammer(self.game, (pos_x, pos_y))
    
    def Spawn_Battle_Axe(self, pos_x, pos_y):
        return Battle_Axe(self.game, (pos_x, pos_y))

    def Spawn_Shield(self, pos_x, pos_y):
        return Shield(self.game, (pos_x, pos_y))

    def Spawn_Spear(self, pos_x, pos_y):
        return Spear(self.game, (pos_x, pos_y))

    def Spawn_Torch(self, pos_x, pos_y):
        return Torch(self.game, (pos_x, pos_y))


    def Spawn_Bow(self, pos_x, pos_y):
        return Bow(self.game, (pos_x, pos_y))


    def Spawn_Arrow(self, pos_x, pos_y, amount):
        return Arrow(self.game, (pos_x, pos_y), amount)

