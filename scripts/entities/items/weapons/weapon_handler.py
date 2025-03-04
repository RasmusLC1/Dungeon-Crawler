from scripts.entities.items.weapons.close_combat.sword import Sword
from scripts.entities.items.weapons.close_combat.halberd import Halberd
from scripts.entities.items.weapons.close_combat.torch import Torch
from scripts.entities.items.weapons.close_combat.warhammer import Warhammer
from scripts.entities.items.weapons.close_combat.battle_axe import Battle_Axe
from scripts.entities.items.weapons.close_combat.sceptre import Sceptre
from scripts.entities.items.weapons.close_combat.bell import Bell
from scripts.entities.items.weapons.close_combat.scythe import Scythe

from scripts.entities.items.weapons.projectiles.spear import Spear
from scripts.entities.items.weapons.projectiles.hatchet import Hatchet
from scripts.entities.items.weapons.projectiles.hammer import Hammer
from scripts.entities.items.weapons.projectiles.arrow import Arrow

from scripts.entities.items.weapons.ranged_weapons.bow import Bow
from scripts.entities.items.weapons.ranged_weapons.crossbow import Crossbow
from scripts.entities.items.weapons.shields.shield import Shield

import random

class Weapon_Handler():
    def __init__(self, game):
        self.game = game

        # Map weapon names to their classes
        self.weapon_map = {
            'sword': Sword,
            'halberd': Halberd,
            'hatchet': Hatchet,
            'hammer': Hammer,
            'warhammer': Warhammer,
            'battle_axe': Battle_Axe,
            'shield': Shield,
            'spear': Spear,
            'torch': Torch,
            'sceptre': Sceptre,
            'bell': Bell,
            'scythe': Scythe,
            'bow': Bow,
            'crossbow': Crossbow,
        }

        self.random_weapon_map = {
            0 : Sword,
            1 : Halberd,
            2 : Hatchet,
            3 : Hammer,
            4 : Warhammer,
            5 : Battle_Axe,
            6 : Spear,
            7 : Sceptre,
            8 : Bell,
            9 : Scythe,
            10 : Bow,
            11 : Crossbow,
            range(12, 17) : Arrow,
        }


    def Weapon_Spawner(self, name, pos_x, pos_y, amount=0, data=None):
        # Handle special cases first
        if 'particle' in name:
            return True  # or your specific logic for particles

        if 'arrow' in name:
            weapon = Arrow(self.game, (pos_x, pos_y), amount)
        else:
            # Lookup the class; return False if not found
            weapon_class = self.weapon_map.get(name)
            if not weapon_class:
                return None
            weapon = weapon_class(self.game, (pos_x, pos_y))

        # Load custom data if any
        if data:
            weapon.Load_Data(data)
            if weapon.equipped:
                weapon.entity = self.game.player
                weapon.Equip()

        # Finally, add to the item handler
        self.game.item_handler.Add_Item(weapon)
        return weapon

    def Spawn_Random_Weapon(self, pos):
        random_weapon_index = random.randint(0, 17)

        selected_weapon = self.random_weapon_map.get(random_weapon_index)

        # If the random weapon is an arrow
        if random_weapon_index >= 12:
            weapon = Arrow(self.game, pos, random.randint(0, 8))
        else:
            weapon = selected_weapon(self.game, pos)
        # Finally, add to the item handler
        self.game.item_handler.Add_Item(weapon)
        return True