import random
import math
from scripts.engine.particles.particle import Particle

# TODO: FIX ATTACK DIRECTION

class Dash():
    def __init__(self, game, entity):
        self.game = game
        self.entity = entity
        self.dashing = 0

    def Dashing_Update(self):
        if not self.dashing:
            return
            


        if abs(self.dashing) in {60, 50}:
            for i in range(20):
                angle = random.random() * math.pi * 2
                speed = random.random() * 0.5 + 0.5
                pvelocity = [math.cos(angle) * speed, math.sin(angle) * speed]
                self.game.particles.append(Particle(self.game, 'particle', self.entity.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

        if self.dashing > 0:
            self.dashing = max(0, self.dashing - 1)


        if self.dashing > 50:
            
            # Temporarily set friction to zero to avoid deceleration during dash
            self.entity.friction = 0
            self.entity.max_speed = 40  # Adjust max speed speed for dashing distance


            # Set the velocity directly based on dash without friction interference
            self.entity.velocity[0] = self.entity.attack_direction[0] * self.dashing
            self.entity.velocity[1] = self.entity.attack_direction[1] * self.dashing

            if abs(self.dashing) == 51:
                self.entity.velocity[0] *= 0.1
                self.entity.velocity[1] *= 0.1

            pvelocity = [abs(self.dashing) / self.dashing * random.random() * 3, 0]
            self.game.particles.append(Particle(self.game, 'particle', self.entity.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

    def Dash(self):
        if self.dashing:
            return False
        
        self.entity.Set_Attack_Direction()
        self.dashing = 60
        return True