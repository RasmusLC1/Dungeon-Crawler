from scripts.traps.trap import Trap

import random
import math
import pygame

class Lava(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.animation = random.randint(0, 2)
        self.light_level = 10
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level, self.tile)
        self.fire_particle_cooldown = 0
        

    def Update(self, entity):
        if entity.category == 'item':
            return
        if self.rect().colliderect(entity.rect()):
            self.Cooldown = 20
            entity.Set_Effect('slow_down', 4)
            if entity.effects.invulnerable.effect:
                return
            if entity.effects.wet.effect:
                entity.effects.wet.Decrease_Effect()
            if not entity.Set_Effect('fire', 5):
                return
            entity.Damage_Taken(5)

    def Animation_Update(self):
        self.Spawn_Fire_Particle()

        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 2:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(20, 30)

    def Spawn_Fire_Particle(self):
        if not self.fire_particle_cooldown:
            self.fire_particle_cooldown = random.randint(70, 150)
            self.game.particle_handler.Activate_Particles(random.randint(1, 2), 'fire', self.rect().center, frame=random.randint(50, 100))

            return
        
        self.fire_particle_cooldown -= 1
        return