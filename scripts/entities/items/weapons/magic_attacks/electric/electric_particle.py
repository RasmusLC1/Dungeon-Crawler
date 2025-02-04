from scripts.entities.items.weapons.magic_attacks.base_attacks.particle import Particle
import pygame
import random

class Electric_Particle(Particle):
    def __init__(self, game, pos, shoot_distance):
        super().__init__(game, pos, 'electric_particle', 2, 2, 1, 100, 'electric', shoot_distance)
        # self.attack_animation_time = shoot_distance // self.attack_animation_max
    
 
    def Initialise_Shooting(self, speed):
        return_value = super().Initialise_Shooting(speed)
        if self.nearby_enemies:
            entity = random.choice(self.nearby_enemies)
            self.direction = pygame.math.Vector2(entity.pos[0] - self.pos[0], entity.pos[1] - self.pos[1]).normalize()
        return return_value

