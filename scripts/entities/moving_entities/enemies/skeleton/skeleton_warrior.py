from scripts.entities.items.weapons.close_combat.sword import Sword
from scripts.entities.items.weapons.close_combat.torch import Torch
from scripts.entities.items.weapons.projectiles.spear import Spear

from scripts.entities.moving_entities.enemies.skeleton.skeleton import Skeleton

import random


class Skeleton_Warrior(Skeleton):
    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        type = str(random.randint(1, 3))
        super().__init__(game, pos, 'skeleton_warrior_' + type, health, strength, max_speed, agility, intelligence, stamina, 60)
        self.Select_Weapon()
        self.intent_manager.Set_Intent(['direct', 'attack', 'attack', 'attack', 'medium_range'])


    def Select_Weapon(self):
        weapon = None

        random_weapon = random.randint(0, 2)

        if random_weapon == 0:
            weapon = Sword(self.game, self.pos)

        elif random_weapon == 1:
            weapon = Spear(self.game, self.pos)

        elif random_weapon == 2:
            weapon = Torch(self.game, self.pos)

        if not weapon:
            return False
        
        self.Equip_Weapon(weapon)