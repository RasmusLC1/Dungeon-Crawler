from scripts.entities.entities import PhysicsEntity
from scripts.entities.moving_entity import Moving_Entity
from scripts.particle import Particle
from scripts.spark import Spark
from scripts.projectile.projectile import Projectile
from scripts.weapon_generator import Weapon_Generator, Weapon

import random
import math
import pygame


class Player(Moving_Entity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.jumps = 1
        self.wall_slide = False
        self.dashing = 0
        self.stored_position = 0
        
        self.max_ammo = 30
        self.ammo = 10
        self.active_weapon = 'gun'
        self.set_action('up')
        self.mana = 5


        self.coins = 0
        self.shootin_cooldown = 0
        
        self.weapons = []
    
    def update(self, tilemap, movement=(0, 0), offset=(0, 0)):
        super().update(tilemap, movement=movement)
        self.Dashing_Update(offset)
            

        if self.velocity[0] > 0:
            self.velocity[0] = max(self.velocity[0] - 0.1, 0)
        else:
            self.velocity[0] = min(self.velocity[0] + 0.1, 0)

        if self.velocity[1] > 0:
            self.velocity[1] = max(self.velocity[1] - 0.1, 0)
        else:
            self.velocity[1] = min(self.velocity[1] + 0.1, 0)

        if self.shootin_cooldown:
            self.shootin_cooldown -= 1

        self.Set_Direction_Holder()

    
    
            
    def Dashing_Update(self, offset=(0, 0)):
        if abs(self.dashing) in {60, 50}:
            for i in range(20):
                angle = random.random() * math.pi * 2
                speed = random.random() * 0.5 + 0.5
                pvelocity = [math.cos(angle) * speed, math.sin(angle) * speed]
                self.game.particles.append(Particle(self.game, 'particle', self.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

        if self.dashing > 0:
            self.dashing = max(0, self.dashing - 1)


        if self.dashing > 50:
            self.stored_position = self.pos.copy()
            self.stored_position[0] -= offset[0]
            self.stored_position[1] -= offset[1]
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

    def Ammo_Change(self, ammo):
        if self.ammo + ammo < self.max_ammo:
            self.ammo += ammo
            return True
        elif self.ammo == self.max_ammo:
            return False
        else:
            self.ammo = self.max_ammo
            return True
        
    def Coin_Change(self, coins):
        self.coins += coins
        
        

    def Shooting(self, offset=(0, 0)):
        
        if not self.ammo or self.shootin_cooldown:
            return
        
        self.shootin_cooldown = 20
        self.Mouse_Handler()
        self.stored_position = self.pos.copy()
        self.stored_position[0] -= offset[0]
        self.stored_position[1] -= offset[1]
        direction = pygame.math.Vector2(self.mpos[0] - self.stored_position[0], self.mpos[1] - self.stored_position[1])

        if direction.length() > 0:  # Ensure the vector is not zero-length before normalizing
            direction.normalize_ip()
            position = [self.rect().centerx - 7, self.rect().centery]
            velocity = [direction.x * 3, direction.y * 3]
            self.game.projectiles.append(Projectile(self.game, 'bullet', position, velocity, 0))
        self.ammo -= 1

    def Dash(self, offset=(0, 0)):
        print(self.game.inventory.Get_Inventory_Length())
        for weapon in self.weapons:
            print(weapon)
        if not self.dashing:
            self.Mouse_Handler()
            self.stored_position = self.pos.copy()
            self.stored_position[0] -= offset[0]
            self.stored_position[1] -= offset[1]
            self.dashing = 60

    def Mouse_Handler(self):
        self.mpos = pygame.mouse.get_pos()
        self.mpos = (self.mpos[0] / 4, self.mpos[1] / 4)

    def Set_Direction_Holder(self):
        if self.direction_x or self.direction_y:
            self.direction_x_holder = self.direction_x
            self.direction_y_holder = self.direction_y
            

    def render(self, surf, offset=(0, 0)):
        
        if abs(self.dashing) <= 50:
            super().render(surf, offset=offset)
        

        
        # Render active weapon
        # if self.flip[0]:
        #     surf.blit(pygame.transform.flip(self.game.assets[self.active_weapon], True, False), (self.rect().centerx - self.game.assets[self.active_weapon].get_width() - offset[0], self.rect().centery - offset[1]))
        # else:
        #     surf.blit(self.game.assets[self.active_weapon], (self.rect().centerx - offset[0], self.rect().centery -offset[1]))

        
