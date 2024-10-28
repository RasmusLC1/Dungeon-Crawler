from scripts.entities.enemies.enemy import Enemy
from scripts.items.weapons.projectiles.ice_particle import Ice_Particle


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

    def Update(self, tilemap, movement = (0, 0)):
        super().Update(tilemap, movement)


        if self.distance_to_player <= 100:
            self.Attack()

        if self.distance_to_player > 110 and self.charge:
            self.charge = 0

        

        
    
    def Attack(self):
        if not super().Attack():
            return
        
        self.charge += 1

        if self.charge >= 100:
            self.shooting_ice = True

        if self.shooting_ice:
            self.Ice_Particle_Creation()

        if self.charge <= 0:
            self.shooting_ice = False
    
    
    def Ice_Particle_Creation(self):
        self.Set_Target(self.game.player.pos)
        self.Set_Attack_Direction()
        # Handle cooldown for spacing between fire particles
        if self.ice_cooldown:
            self.ice_cooldown -= 1
            return
        else:
            self.ice_cooldown = 3
            self.charge = max(0, self.charge - 20)

        damage = 1
        speed = 1
        max_range = 140
       

        # Calculate the base angle using atan2(y, x)
        base_angle = math.atan2(self.attack_direction[1], self.attack_direction[0])

        pos_x = math.cos(base_angle) * speed
        pos_y = math.sin(base_angle) * speed
        direction = (pos_x, pos_y)
        ice_particle = Ice_Particle(
                self.game,
                self.rect(),
                (3, 3),
                'ice_particle',
                damage,
                speed,
                max_range,
                'particle',
                self.charge,
                direction,  # Pass the direction here
                self
            )
        
        self.game.item_handler.Add_Item(ice_particle)

    

    def Set_Idle(self):
        pass

    def Set_Action(self, movement):
        pass

    def Set_Frozen(self, freeze_time):
        if self.wet:
            freeze_time *= 2
            self.wet = 0
        self.Set_Effect('health', freeze_time)
        return False