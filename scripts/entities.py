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

        self.health = 3
        self.snared = 0
        
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
        
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            
        self.animation.update()
    def Damage_Taken(self, damage):
        self.health -= damage
        print("DAMAGE")
        print(self.health)

    def Snare(self, snare_time):
        self.snared = snare_time
        print("SNARED")
            
    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip[0], self.flip[1]), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))


