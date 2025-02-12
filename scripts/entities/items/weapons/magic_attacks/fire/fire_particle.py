from scripts.entities.items.weapons.magic_attacks.base_attacks.particle import Particle
import pygame

class Fire_Particle(Particle):
    def __init__(self, game, pos, shoot_distance):
        super().__init__(game, pos, 'fire_particle_attack', 2, 1, 2, 100, 'fire', shoot_distance)
