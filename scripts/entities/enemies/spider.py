from scripts.entities.enemies.enemy import Enemy
from scripts.items.weapons.projectiles.spider_web_projectile import Spider_Web_Projectile

import math
import random
import pygame

class Spider(Enemy):
    def __init__(self, game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina)

        self.animation = 'spider'

        self.path_finding_strategy = 'standard'
        self.attack_strategy = 'medium_range'

        self.animation_num_max = 3 # running and idle animation
        self.animation_num_cooldown_max = 100

        self.attack_animation_num_max = 3 # Standard attack and shoot spider web
        self.attack_animation_num_cooldown_max = 100

        self.jumping_animation_num_max = 8 # Jumping attack
        self.jumping_animation_num_cooldown_max = 50

        self.on_back_animation_num_max = 8 # To make spider friendly again
        self.on_back_animation_num_cooldown_max = 50

        self.spider_web = None

    def Update(self, tilemap, movement = (0, 0)):
        super().Update(tilemap, movement)            

        if self.game.player.snared:
            self.Jump_Attack()

        if self.distance_to_player <= 50:
            self.Ranged_Attack()
            return

    def Ranged_Attack(self):
        self.charge += 1

        if self.charge >= 80:
            self.Initialise_Spider_Web()
    
    def Initialise_Spider_Web(self):
        self.Set_Target(self.game.player.pos)
        self.Set_Attack_Direction()

        damage = 1
        speed = 1
        max_range = 140

        base_angle = math.atan2(self.attack_direction[1], self.attack_direction[0])

        pos_x = math.cos(base_angle) * speed
        pos_y = math.sin(base_angle) * speed
        direction = (pos_x, pos_y)

        spider_web = Spider_Web_Projectile(self.game,
                                    self.rect(),
                                    (5, 5),
                                    'spider_web',
                                    damage,
                                    speed,
                                    max_range,
                                    'particle',
                                    self.charge,
                                    direction,  # Pass the direction here
                                    self
                                )
        
        self.game.item_handler.Add_Item(spider_web)

        self.charge = 0

    def Jump_Attack(self):
        pass

    # Set new action for animation
    def Set_Action(self, movement):
        # Check for movement
        if not movement[0] and not movement[1]:
            self.Set_Animation('idle')
        self.idle_count = 0
        

        if movement[1] or movement[0]:
            self.Set_Animation('running')

