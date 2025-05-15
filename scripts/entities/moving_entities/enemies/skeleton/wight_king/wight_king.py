from scripts.entities.moving_entities.enemies.skeleton.skeleton import Skeleton
from scripts.entities.items.weapons.close_combat.sword import Sword
from scripts.entities.items.weapons.projectiles.spear import Spear
from scripts.entities.moving_entities.enemies.skeleton.wight_king.wight_king_intent import Wight_King_Intent_Manager
from scripts.engine.assets.keys import keys

import random


class Wight_King(Skeleton):

    intent_manager_class = Wight_King_Intent_Manager


    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, keys.wight_king, health, strength, max_speed, agility, intelligence, stamina, 40, (40, 40))

        self.animation_handler.Set_Animation_Num_Max(4)
        self.animation_handler.Set_Attack_Animation_Num_Max(4)
        self.animation_handler.Set_Attack_Animation_Num_Cooldown_Max(8)
        self.Select_Weapon()
        self.intent_manager.Set_Intent(['keep_position', 'direct', 'dash', 'attack', 'attack', 'medium_range',])
        self.intent_manager.Set_Intent_Cooldown_Max(120)

    def Update(self, tilemap, movement=(0, 0)):
        super().Update(tilemap, movement)
        self.animation_handler.Update_Animation()


    def Select_Weapon(self):
        weapon = None

        random_weapon = random.randint(0, 1)

        if random_weapon == 0:
            weapon = Sword(self.game, self.pos)

        elif random_weapon == 1:
            weapon = Spear(self.game, self.pos)


        if not weapon:
            return False
        
        self.Equip_Weapon(weapon)