import math
import random

import pygame

from scripts.particle import Particle

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0, 0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.health = 100
        self.max_health = self.health
        self.snared = 0

        self.is_on_fire = 0
        self.fire_cooldown = 0
        self.fire_animation = 0
        self.fire_animation_cooldown = 0
        
        self.action = ''
        self.anim_offset = (-3, -3)
        self.flip = [False, False]
        self.set_action('idle')
        
        self.last_movement = [0, 0, 0, 0]
        
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()
        
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0]*2 + self.velocity[0], movement[1]*2 + self.velocity[1])

        if self.snared:
            self.snared -= 1
            frame_movement = (0, 0)
        
        self.Movement(frame_movement, movement, tilemap)
        
        self.OnFire()
            
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            
        self.animation.update()

    def Movement(self, frame_movement, movement, tilemap):
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
        
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        
                
        if movement[0] > 0:
            self.flip[0] = False
        if movement[0] < 0:
            self.flip[0] = True
        if movement[1] < 0:
            self.flip[1] = False
        if movement[1] > 0:
            self.flip[1] = True            
            
        self.last_movement = movement

    def Damage_Taken(self, damage):
        self.health -= damage
        print("DAMAGE")
        print(self.health)

    def Healing(self, healing):
        if self.health + healing < self.max_health:
            self.health += healing
            return True
        elif self.health == self.max_health:
            return False
        else:
            self.health = self.max_health
            return True
        
    def Set_On_Fire(self, fire_time):
        self.is_on_fire = random.randint(fire_time, fire_time * 2)

    def OnFire(self):
        

        if self.fire_cooldown:
            self.fire_cooldown -= 1
        else:
            if self.is_on_fire:
                damage = random.randint(1, 3)
                self.Damage_Taken(damage)
                self.is_on_fire -= 1
                self.fire_cooldown = random.randint(30, 50)

        if self.fire_animation_cooldown:
            self.fire_animation_cooldown -= 1
        else:
            self.fire_animation_cooldown = 15
            if self.fire_animation >= 7:
                self.fire_animation = 0
            else:
                self.fire_animation += 1
                

    def Snare(self, snare_time):
        self.snared = snare_time
        print("SNARED")

    def Push(self, x_direction, y_direction):
        self.pos[0] += x_direction
        self.pos[1] += y_direction
        print("PUSHED")
            
    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip[0], self.flip[1]), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        if self.is_on_fire:
            fire_image = self.game.assets['fire'][self.fire_animation].convert_alpha()

            # Set the opacity to 70%
            fire_image.set_alpha(179)
            if self.flip[0]:
                surf.blit(pygame.transform.flip(fire_image, True, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + 5))
            else:
                surf.blit(fire_image, (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + 5))
