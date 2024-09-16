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

        self.spider_web = None

    def Update(self, tilemap, movement = (0, 0)):
        
        super().Update(tilemap, movement)
        self.Update_Shot_Fired()        

        if self.shot_fired < 30 and self.shot_fired > 15:
            self.Jump_Attack()
            return

        if self.distance_to_player <= 50 and not self.shot_fired:
            self.Ranged_Attack()
            return
        

        

    def Ranged_Attack(self):
        self.charge += 1

        if self.distance_to_player > 50:
            self.attack_strategy = 'medium_range'
            return
        
        if self.charge == 5:
            self.attack_strategy = 'keep_position'

        if self.charge >= 80:
            self.Initialise_Spider_Web()
            self.attack_strategy = 'medium_range'
            self.charge = 0



    
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

    def Jump_Attack(self):
        pass
    
    def Update_Shot_Fired(self):
        if self.shot_fired:
            self.shot_fired = max(0, self.shot_fired - 1)
        
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
        
        if not self.animation_num_cooldown:
            self.animation_num += 1
            if self.animation_num >= self.animation_num_max:
                self.animation_num = 0
            self.animation_num_cooldown = self.animation_num_cooldown_max
        else:
            self.animation_num_cooldown = max(0, self.animation_num_cooldown - 1)


    # Render entity
    def Render(self, surf, offset=(0, 0)):
        # Don't Render the enemy if their light level is very low
        # Simulates low visibility
        if not self.Update_Light_Level():
            return
        animation_num = self.animation_num

        if 'attack' in self.animation:
            animation_num = self.attack_animation_num

        if 'jumping' in self.animation:
            animation_num = self.jumping_animation_num

        # Load and scale the entity images, split to allow better animation
        entity_image_head = self.game.assets[self.animation + '_head'][animation_num]
        entity_image_head = pygame.transform.scale(entity_image_head, (16, 12))

        entity_image_body = self.game.assets[self.animation + '_body'][animation_num]
        entity_image_body = pygame.transform.scale(entity_image_body, (16, 9))

        entity_image_legs = self.game.assets[self.animation + '_legs'][animation_num]
        entity_image_legs = pygame.transform.scale(entity_image_legs, (16, 3))
        
        # Set the alpha value to make the entity fade out
        alpha_value = max(0, min(255, self.active)) 
        entity_image_head.set_alpha(alpha_value)
        entity_image_body.set_alpha(alpha_value)
        entity_image_legs.set_alpha(alpha_value)

         # Create a darkening surface that is affected by darkness
        dark_surface_head = pygame.Surface(entity_image_head.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))  

        dark_surface_body = pygame.Surface(entity_image_body.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_body.fill((self.light_level, self.light_level, self.light_level, 255))

        dark_surface_legs = pygame.Surface(entity_image_legs.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_legs.fill((self.light_level, self.light_level, self.light_level, 255))


        # Apply darkening effect using BLEND_RGBA_MULT
        entity_image_head.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        entity_image_body.blit(dark_surface_body, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        entity_image_legs.blit(dark_surface_legs, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        surf.blit(pygame.transform.flip(entity_image_legs, self.flip[0], False), 
                (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] + 9))
        surf.blit(pygame.transform.flip(entity_image_body, self.flip[0], False), 
                (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        surf.blit(pygame.transform.flip(entity_image_head, self.flip[0], False), 
                (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] - 12))

        # Render status effects
        self.status_effects.render_fire(self.game, surf, offset)
        self.status_effects.render_poison(self.game, surf, offset)
        self.status_effects.render_frozen(self.game, surf, offset)
        self.status_effects.render_wet(self.game, surf, offset)
