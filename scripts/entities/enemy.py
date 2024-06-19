from scripts.entities.entities import PhysicsEntity
import random
import pygame
from scripts.a_star import A_Star



class Enemy(PhysicsEntity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, type, pos, size)
        self.animation = 'decrepit_bones'
        self.walking = 0
        self.health = 30
        self.movement_cooldown = 0
        self.direction = (0,0,0,0)
        self.direction_x = 0
        self.direction_y = 0
        self.running = 0
        self.direction_x_holder = 0
        self.direction_y_holder = 0
    
    def update(self, tilemap, movement=(0, 0)):
        
        
        if self.running:
            self.running -= 1
        else:
            self.direction_x / 2
            self.direction_y / 2
            self.direction = (self.direction_x, self.direction_y)
        if self.movement_cooldown:
            self.movement_cooldown -= 1
        else:
            self.direction_x = random.randint(-1, 1) / 10
            self.direction_y = random.randint(-1, 1) / 10
            self.direction_x_holder = self.direction_x 
            self.direction_y_holder = self.direction_y
            self.direction = (self.direction_x, self.direction_y)
            self.movement_cooldown = 100
            self.walking = max(0, self.walking-1)


        for trap in self.nearby_traps:
            if self.rect().colliderect(trap.rect()):
                
                self.direction_x = self.direction_x_holder * 4
                self.direction_y = self.direction_y_holder * 4
                self.direction = (self.direction_x, self.direction_y)
                self.running = 3
            else:
                if self.Future_Rect(self.direction).colliderect(trap.rect()):
                    self.direction_x *= -1
                    self.direction_y *= -1
                    self.direction = (self.direction_x, self.direction_y)
                    break

        movement = self.direction

        
        super().update(tilemap, movement = movement)
        self.animation = 'decrepit_bones'
        
        

        if abs(self.game.player.dashing) >= 50:
            if self.rect().colliderect(self.game.player.rect()):
                self.game.player.Damage_Taken(5)
                return True
            
    def Future_Rect(self, direction):
             return pygame.Rect(self.pos[0] + direction[0]*10, self.pos[1] + direction[1]*10, self.size[0], self.size[1])

    