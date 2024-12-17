from scripts.entities.enemies.enemy import Enemy
from scripts.items.weapons.magic_attacks.ice.ice_particle import Ice_Particle
from scripts.items.weapons.magic_attacks.ice.ice_shooter import Ice_Shooter


import math
import random


class Ice_Spirit(Enemy):
    def __init__(self, game, pos, type, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, type, health, strength, max_speed, agility, intelligence, stamina)
        self.animation = 'ice_spirit'
        self.animation_num_max = 3
        self.path_finding_strategy = 'standard'
        self.attack_strategy = 'long_range'
        self.look_for_health_cooldown = 0
        self.ice_cooldown = 0
        self.shooting_ice = False
        self.attack_animation_num_cooldown_max = 30
        self.ice_shooter = Ice_Shooter(self.game)

    def Update(self, tilemap, movement = (0, 0)):
        super().Update(tilemap, movement)

        if self.effects.frozen.effect:
            self.Set_Effect('healing', self.effects.frozen.effect)
            self.Set_Effect('frozen_resistance', 2)
        

        if self.distance_to_player <= 200:
            self.Attack()

        if self.distance_to_player > 250 and self.charge:
            self.charge = 0

        

        
    
    def Attack(self):
        if not super().Attack():
            return
        
        self.charge += 1

        if self.charge >= 100:
            self.shooting_ice = True

        if self.shooting_ice:
            self.Shoot_Ice_Particle()

        if self.charge <= 0:
            self.shooting_ice = False
    
    
    def Shoot_Ice_Particle(self):
        self.Set_Target(self.game.player.pos)
        self.Set_Attack_Direction()
        self.charge = self.ice_shooter.Ice_Particle_Creation(self.charge, self)

    def Set_Idle(self):
        pass

    def Set_Action(self, movement):
        pass