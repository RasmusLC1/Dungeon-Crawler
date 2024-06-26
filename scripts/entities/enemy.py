from scripts.entities.entities import PhysicsEntity
from scripts.entities.moving_entity import Moving_Entity

import random
import pygame
from scripts.a_star import A_Star



class Enemy(Moving_Entity):
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
        self.pathfinding_cooldown = 0
        self.path = []
        self.src_x = 0
        self.src_y = 0
        self.des_x = 0
        self.des_y = 0
    
    def update(self, tilemap, movement=(0, 0)):
        
        self.Path_Finding()
        movement = self.direction
        
        super().update(tilemap, movement = movement)
        self.animation = 'decrepit_bones'

        if abs(self.game.player.dashing) >= 50:
            if self.rect().colliderect(self.game.player.rect()):
                self.game.player.Damage_Taken(5)
                return True
        
    def Path_Finding(self):
        # Player is close, so the enemy charge directly
        if (abs(self.pos[0]) - abs(self.game.player.pos[0]) < 40 and abs(self.pos[1]) - abs(self.game.player.pos[1]) < 40):
            self.direction = pygame.math.Vector2((self.game.player.pos[0] - self.pos[0]), (self.game.player.pos[1] - self.pos[1]))
            if not self.direction:
                return
            self.direction.normalize_ip()
            self.direction[0] /= 4
            self.direction[1] /= 4
            return
        # Calculate a new shortest path
        if not self.pathfinding_cooldown:
            self.path.clear()
            self.Calculate_Position()
            
            A_Star.a_star_search(self.game, self, [self.src_y, self.src_x], [self.des_y, self.des_x])
            
            self.pathfinding_cooldown = 100
        else:
            self.pathfinding_cooldown -= 1
        # Pathfinding
        if self.path:
            i = 0
            target = (self.src_y, self.src_x)
            for i in range(len(self.path) - 1):
                if (self.src_y, self.src_x) == self.path[i]:
                    target = self.path[i + 1]
                    break
            # Calculate Direction
            direction_x = 0.1 
            direction_y = 0.1 
            if (self.src_y, self.src_x) != (self.des_y, self.des_x):
                if target[1] == self.src_x:
                    direction_x = 0
                elif target[1] < self.src_x:
                    direction_x *= -1
                if target[0] == self.src_y:
                    direction_y = 0
                elif target[0] < self.src_y:
                    direction_y *= -1
            else:
                self.direction = (0,0)
            self.direction = pygame.math.Vector2(direction_x, direction_y)
            return
        
        if not self.path:
            self.Moving_Random()

            
    def Calculate_Position(self):
        self.src_x = round(self.pos[0] / 16) - self.game.min_x 
        self.src_y = round(self.pos[1] / 16) - self.game.min_y 
        self.des_x = round(self.game.player.pos[0] / 16) - self.game.min_x 
        self.des_y = round(self.game.player.pos[1] / 16) - self.game.min_y 

    def Moving_Random(self):
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

    def Future_Rect(self, direction):
             return pygame.Rect(self.pos[0] + direction[0]*16, self.pos[1] + direction[1]*16, self.size[0], self.size[1])

    