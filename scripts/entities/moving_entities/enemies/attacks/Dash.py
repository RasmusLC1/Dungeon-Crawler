import random
import math
import pygame
from scripts.engine.particles.particle import Particle

class Dash():
    def __init__(self, game, entity):
        self.game = game
        self.entity = entity
        self.dashing = 0
        self.dash_direction = (0,0)
        self.dash_start = 60
        self.dash_mid = 50

    def Dashing_Update(self):
        if not self.dashing:
            return
            


        if abs(self.dashing) in {self.dash_start, self.dash_mid}:
            for i in range(20):
                angle = random.random() * math.pi * 2
                speed = random.random() * 0.5 + 0.5
                pvelocity = [math.cos(angle) * speed, math.sin(angle) * speed]
                self.game.particles.append(Particle(self.game, 'particle', self.entity.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

        if self.dashing > 0:
            self.dashing = max(0, self.dashing - 1)


        if self.dashing > self.dash_mid:
            
            # Temporarily set friction to zero to avoid deceleration during dash
            self.entity.friction = 0
            self.entity.max_speed = 40  # Adjust max speed speed for dashing distance


            # Set the velocity directly based on dash without friction interference
            self.entity.velocity[0] = self.dash_direction[0] * self.dashing 
            self.entity.velocity[1] = self.dash_direction[1] * self.dashing 

            if abs(self.dashing) == self.dash_mid+1:
                self.entity.velocity[0] *= 0.1
                self.entity.velocity[1] *= 0.1

            pvelocity = [abs(self.dashing) / self.dashing * random.random() * 3, 0]
            self.game.particles.append(Particle(self.game, 'particle', self.entity.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

    def Dash(self):
        if self.dashing:
            return False
        self.Set_Dash_Direction()
        self.dashing = 60
        return True
    
    def Set_Dash_Direction(self):
        self.dash_direction = pygame.math.Vector2(self.entity.target[0] - self.entity.pos[0], self.entity.target[1] - self.entity.pos[1])
        if not self.dash_direction:
            return
        self.dash_direction.normalize_ip()