from scripts.entities.moving_entities.enemies.skeleton.skeleton import Skeleton
from scripts.entities.items.weapons.ranged_weapons.bow import Bow


import pygame
import random


class Skeleton_Ranger(Skeleton):
    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        type = str(random.randint(1, 3))
        super().__init__(game, pos, 'skeleton_ranger_' + type, health, strength, max_speed, agility, intelligence, stamina)
        self.animation_num_max = 3
        self.attack_animation_num_max = 3
        self.attack_animation_num_cooldown_max = 100
        self.animation_num_cooldown_max = 150
        self.attack_distance  = 200
        self.disengage_distance = 250
        self.attack_strategy = 'long_range'
        
        self.shooting_distance = False
        self.Equip_Weapon(Bow(self.game, self.pos))
        


    def Attack(self):
        if self.game.player.effects.invisibility.effect:
            return False
        
        if not self.active_weapon:
            return False

        if self.weapon_cooldown:
            return False
        
        self.Set_Target(self.game.player.pos)
        if self.active_weapon.type == 'bow':
            self.charge += 1
            self.active_weapon.Set_Charging_Enemy()
            if self.active_weapon.Enemy_Shooting():
                self.Reset_Charge()

                self.weapon_cooldown = 100
        
        return True
