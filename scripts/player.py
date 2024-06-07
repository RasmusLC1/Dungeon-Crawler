from scripts.entities import PhysicsEntity
from scripts.particle import Particle
import random
import math
import pygame


class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.jumps = 1
        self.wall_slide = False
        self.dashing = 0
        self.stored_position = 0
    
    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

        
        self.Dashing_Update()

        if self.velocity[0] > 0:
            self.velocity[0] = max(self.velocity[0] - 0.1, 0)
        else:
            self.velocity[0] = min(self.velocity[0] + 0.1, 0)

        if self.velocity[1] > 0:
            self.velocity[1] = max(self.velocity[1] - 0.1, 0)
        else:
            self.velocity[1] = min(self.velocity[1] + 0.1, 0)

            
    def Dashing_Update(self):
        if abs(self.dashing) in {60, 50}:
            for i in range(20):
                angle = random.random() * math.pi * 2
                speed = random.random() * 0.5 + 0.5
                pvelocity = [math.cos(angle) * speed, math.sin(angle) * speed]
                self.game.particles.append(Particle(self.game, 'particle', self.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

        if self.dashing > 0:
            self.dashing = max(0, self.dashing - 1)


        if self.dashing > 50:
            direction = pygame.math.Vector2(self.mpos[0] - self.stored_position[0], self.mpos[1] - self.stored_position[1])
            if direction.length() > 0:  # Ensure the vector is not zero-length before normalizing
                direction.normalize_ip()

                dashing_speed = self.dashing / 5 

                self.velocity[0] = direction.x * dashing_speed
                self.velocity[1] = direction.y * dashing_speed
                
                if abs(self.dashing) == 51:
                    self.velocity[0] *= 0.1
                    self.velocity[1] *= 0.1
                pvelocity = [abs(self.dashing) / self.dashing * random.random() * 3, 0]
                self.game.particles.append(Particle(self.game, 'particle', self.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))   
    
    def Dash(self, offset=(0, 0)):
        if not self.dashing: 
            self.mpos = pygame.mouse.get_pos()
            self.mpos = (self.mpos[0] / 4, self.mpos[1] / 4)
            self.stored_position = self.pos.copy()
            self.stored_position[0] -= offset[0]
            self.stored_position[1] -= offset[1]
            self.dashing = 60



    def render(self, surf, offset=(0, 0)):
        if abs(self.dashing) <= 50:
            super().render(surf, offset=offset)
        
