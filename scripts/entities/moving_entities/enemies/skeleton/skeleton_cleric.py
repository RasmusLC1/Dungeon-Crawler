from scripts.entities.moving_entities.enemies.skeleton.skeleton import Skeleton
from scripts.entities.items.weapons.close_combat.sceptre import Sceptre

import random


class Skeleton_Cleric(Skeleton):
    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        type = str(random.randint(1, 1))
        super().__init__(game, pos, 'skeleton_cleric_' + type, health, strength, max_speed, agility, intelligence, stamina)
        self.Equip_Weapon(Sceptre(self.game, self.pos))
        self.max_weapon_charge = 70
        self.healing_cooldown = 0
        self.attack_strategy = 'medium_range'


    def Update(self, tilemap, movement=(0, 0)):
        self.Weapon_Cooldown()
        self.Update_Healing_Cooldown()
        self.Heal_Nearby_Enemies()
        super().Update(tilemap, movement)

    def Update_Healing_Cooldown(self):
        if not self.healing_cooldown:
            return
        
        self.healing_cooldown = max(0, self.healing_cooldown - 1)

    def Heal_Nearby_Enemies(self):
        if self.healing_cooldown:
            return
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self, 5)
        if not self.nearby_enemies:
            self.healing_cooldown = 500
            return
        for enemy in self.nearby_enemies:
            enemy.effects.Set_Effect('healing', 15)
        self.healing_cooldown = 1000

