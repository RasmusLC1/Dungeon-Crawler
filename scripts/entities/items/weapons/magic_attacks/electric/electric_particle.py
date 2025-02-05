from scripts.entities.items.weapons.magic_attacks.base_attacks.particle import Particle
import pygame
import random

class Electric_Particle(Particle):
    def __init__(self, game, pos, shoot_distance):
        super().__init__(game, pos, 'electric_particle', 2, 2, 1, 100, 'electric', shoot_distance)
        # self.attack_animation_time = shoot_distance // self.attack_animation_max
    
 
    

