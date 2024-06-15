import math
import random
import pygame

from scripts.particle import Particle
from scripts.traps.trap_handler import Trap_Handler
from scripts.entities.effects import Status_Effect_Handler


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0, 0, 0]
        self.friction = 2
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.health = 100
        self.max_health = self.health
        self.snared = 0
        self.nearby_traps = []
        
        self.action = ''
        self.anim_offset = (-3, -3)
        self.flip = [False, False]
        self.set_action('idle')
        self.frame_movement = (0.0, 0.0)
        self.last_frame_movement = (0.0, 0.0)

        # Status Effects
        self.is_on_fire = 0
        self.fire_cooldown = 0
        self.fire_animation = 0
        self.fire_animation_cooldown = 0

        self.poisoned = 0
        self.poisoned_cooldown = 0
        self.poison_animation = 0
        self.poison_animation_cooldown = 0

        self.is_on_ice = 0
        self.frozen = 0
        self.frozen_cooldown = 0
        self.frozen_animation = 0

        self.status_effects = Status_Effect_Handler(self)
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()
        
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        self.frame_movement = (movement[0]*4/self.friction + self.velocity[0], movement[1]*4/self.friction + self.velocity[1])
        self.Update_Status_Effects()
        self.Update_Traps()
  
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            
        self.animation.update()

        self.Movement(movement, tilemap)

    def Movement(self, movement, tilemap):
        self.pos[0] += self.frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if self.frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
        
        self.pos[1] += self.frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if self.frame_movement[1] < 0:
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
        self.last_frame_movement = self.frame_movement
         
            

    def Update_Traps(self):
        self.nearby_traps = Trap_Handler.find_nearby_traps(self.game, self.pos, 20)
        for trap in self.nearby_traps:
            trap.Update(self)

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

    def Push(self, x_direction, y_direction):
        self.pos[0] += x_direction
        self.pos[1] += y_direction

    def On_Ice(self):
        if not self.is_on_ice:
            self.is_on_ice = 10
        else:
            self.is_on_ice -= 1
            self.frame_movement = self.last_frame_movement 

    def Update_Status_Effects(self):
        self.friction = 2
        self.status_effects.OnFire()
        self.status_effects.Snare()
        self.status_effects.Poisoned()
        self.status_effects.Frozen()
    
    def Set_Snare(self, snare_time):
        self.snared = snare_time
    
    def Set_Poisoned(self, poisoned):
        self.poisoned = max(random.randint(poisoned, poisoned * 2), self.poisoned)
            
    def Set_Frozen(self, freeze):
        self.frozen = max(random.randint(freeze, freeze * 2), self.frozen)

    def Set_On_Fire(self, fire_time):
        self.is_on_fire = max(random.randint(fire_time, fire_time * 2), self.is_on_fire)

    def Slow_Down(self, effect):
        self.friction = max(2, effect)


            
    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip[0], self.flip[1]), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        self.status_effects.render_fire(self.game, surf, offset)
        self.status_effects.render_poison(self.game, surf, offset)

            
