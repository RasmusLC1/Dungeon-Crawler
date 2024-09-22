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
        self.attack_animation_num_cooldown_max = 200

        self.jumping_animation_num_max = 8 # Jumping attack
        self.jumping_animation_num = 0
        self.jumping_animation_num_cooldown_max = 5

        self.on_back_animation_num_max = 8 # To make spider friendly again
        self.on_back_animation_num_cooldown_max = 50

        self.shot_fired = 0
        self.attack_cooldown = 0

        self.spider_web = None

        self.attack_symbol_offset = 10


    def Update(self, tilemap, movement = (0, 0)):
        super().Update(tilemap, movement)
        self.Update_Shot_Fired()        
        self.Update_Attack_Cooldown()

        if self.distance_to_player > 50 and self.attack_strategy != 'medium_range':
            self.charge = 0
            self.attack_strategy = 'medium_range'

        if self.attack_cooldown:
            return
        
        self.Attack()

    def Attack(self):
        if not super().Attack():
            return

        if self.shot_fired:
            self.Jump_Attack()
            return

        if self.distance_to_player <= 50:
            self.Ranged_Attack()
            return
        

    def Jump_Attack(self):
        if self.shot_fired == 1:
            self.Set_Attack_Cooldown(60)
            return
        
        if self.shot_fired < 30 and self.shot_fired > 15:
            self.Set_Frame_movement((self.attack_direction[0], self.attack_direction[1]))
            self.Tile_Map_Collision_Detection(self.game.tilemap)
            self.attack_strategy =  'direct'
            if self.max_speed == self.max_speed_holder:
                self.max_speed *= 15
        elif self.shot_fired < 15:
            self.attack_strategy =  'long_range'
            if self.max_speed != self.max_speed_holder:
                self.max_speed = self.max_speed_holder
        else:
            self.attack_strategy = 'close_range'

        self.Bite_Attack()
    
    # Bite the player when the player is close
    def Bite_Attack(self):
        if self.Future_Rect(self.attack_direction).colliderect(self.game.player.rect()):
            self.attack_strategy =  'long_range'
            self.game.player.Damage_Taken(self.strength)
            self.game.player.Set_Effect('Poison', 4)
            self.Set_Attack_Cooldown(60)
        

    def Ranged_Attack(self):
        self.charge += 1
        
        if self.charge == 5:
            self.attack_strategy = 'keep_position'

        if self.charge >= 80:
            self.Initialise_Spider_Web()
            self.attack_strategy = 'medium_range'
            self.charge = 0
            self.Set_Shot_Fired(45)
    
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
        self.shot_fired = 45

    
    def Update_Shot_Fired(self):
        if self.shot_fired:
            self.shot_fired = max(0, self.shot_fired - 1)
        return
    
    def Update_Attack_Cooldown(self):
        if self.attack_cooldown:
            self.attack_cooldown = max(0, self.attack_cooldown - 1)
        return

    # Set new action for animation
    def Set_Action(self, movement):
        if self.shot_fired:
            self.Set_Animation('jumping')
            return

        if self.charge and self.distance_to_player <= 50:
            self.Set_Animation('attack')
            return

        # Check for movement
        if not movement[0] and not movement[1]:
            self.Set_Animation('idle')
            return
        if movement[1] or movement[0]:
            self.Set_Animation('running')

    
    def Update_Jumping_Animation(self) -> None:
        if not self.jumping_animation_num_cooldown:
            self.jumping_animation_num += 1
            if self.jumping_animation_num > self.jumping_animation_num_max:
                self.jumping_animation_num = 0
            self.jumping_animation_num_cooldown = self.jumping_animation_num_cooldown_max
        else:
            self.jumping_animation_num_cooldown = max(0, self.jumping_animation_num_cooldown - 1)


    def Set_Shot_Fired(self, amount):
        self.shot_fired = amount
        return
    
    def Set_Attack_Cooldown(self, amount):
        self.attack_cooldown = amount
        return
