from scripts.entities.entities import PhysicsEntity
from scripts.entities.moving_entity import Moving_Entity
from scripts.engine.particles.particle import Particle
from scripts.spark import Spark
from scripts.entities.player.player_effects import Player_Status_Effect_Handler
from scripts.entities.player.player_weapon import Player_Weapon_Handler
from scripts.entities.player.player_movement import Player_Movement


import random
import math
import pygame


class Player(Moving_Entity):
    def __init__(self, game, pos, size, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, 'player', pos, size, health, strength, max_speed, agility, intelligence, stamina)
        
        self.animation_num_max = 3
        
        self.max_ammo = 30
        self.ammo = 10
        self.bow_cooldown = 0
        self.Set_Animation('idle_down')
        self.souls = 5
        self.nearby_chests = []
        self.view_direction = (0,0)

        self.light_level = 4
        self.light_cooldown = 0
        # self.light_source = None
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)


        self.coins = 0
        self.shootin_cooldown = 0

        self.weapons = []
        self.status_effects = Player_Status_Effect_Handler(self)
        self.weapon_handler = Player_Weapon_Handler(self.game, self)
        self.movement_handler = Player_Movement(self.game, self)

    
    def Update(self, tilemap, movement=(0, 0), offset=(0, 0)):
        self.invincible = False
        super().Update(tilemap, movement=movement)
        self.Mouse_Handler()
        self.movement_handler.Update()

        if self.shootin_cooldown:
            self.shootin_cooldown -= 1
        
        self.Update_Light()

        self.View_Direction(offset)

        self.weapon_handler.Update(offset)
        
    def View_Direction(self, offset):
        self.view_direction = pygame.math.Vector2(self.target[0] - self.pos[0], self.target[1] - self.pos[1])
        if self.view_direction.length() > 0:
            self.view_direction.normalize_ip()
    
    def Increase_Souls(self, added_soul):
        self.souls += added_soul

    def Entity_Collision_Detection(self, tilemap):
        if self.movement_handler.dashing > 40:
            return None
        return super().Entity_Collision_Detection(tilemap)
    
    def Remove_Active_Weapon(self, hand):
        self.weapon_handler.Remove_Active_Weapon(hand)

    def Attack_Direction_Handler(self, offset = (0,0)):
        super().Attack_Direction_Handler(offset)

    def Set_Charge(self, charge_speed, offset=(0, 0)):
        super().Set_Charge(charge_speed, offset)

    def Attacking(self, weapon, offset=(0, 0)):
        if weapon.attacking and not self.attacking:
            self.Attack_Direction_Handler(offset)

            direction_x = 5 * self.attack_direction[0]
            direction_y = 5 * self.attack_direction[1]
            self.Set_Frame_movement((direction_x, direction_y))
            self.Tile_Map_Collision_Detection(self.game.tilemap)
            self.attacking = weapon.attacking


        if self.attacking == 1:
            direction_x = - 5 * self.attack_direction[0]
            direction_y = - 5 * self.attack_direction[1]
            self.Set_Frame_movement((direction_x, direction_y))
            self.Tile_Map_Collision_Detection(self.game.tilemap)

        if self.attacking:
            self.attacking -= 1


    def Set_Light_State(self, state):
        self.light_source.active = state
    
    def Set_Inventory_Interaction(self, state):
        self.weapon_handler.Set_Inventory_Interaction(state)

    def Set_Active_Weapon(self, weapon, hand):  
        self.weapon_handler.Set_Active_Weapon(weapon, hand)
        
    # Function to update the light around player
    def Update_Light(self):
        if self.light_source:
            # Update all the light's around the player
            # Do it only when the player light has been activated to prevent lag
            if not self.light_source.active:
                self.game.light_handler.Remove_Light(self.light_source)
                self.game.light_handler.Restore_Light(self.light_source)
                self.Set_Light_State(True)
            else:
                self.game.light_handler.Move_Light(self.pos, self.light_source)

    def Back_Step(self,  offset=(0, 0)):
        if not self.back_step:
            self.Attack_Direction_Handler(offset)
            # Inverse attack Direction
            self.attack_direction = pygame.math.Vector2(self.attack_direction[0] * -1, self.attack_direction[1] * -1)
            self.back_step = 20
            self.invincible = True

    def Back_Step_Update(self):
        if not self.back_step:
            self.invincible = False
            return
        self.back_step = max(0, self.back_step - 1)
        if self.back_step < 15:
            return
        
        if self.attack_direction.length() > 0:

            self.friction = 0
            self.max_speed = 40  # Adjust max speed speed for dashing distance


            # Set the velocity directly based on dash without friction interference
            self.velocity[0] = self.attack_direction[0] * 20
            self.velocity[1] = self.attack_direction[1] * 20

    def Roll_Forward(self,  offset=(0, 0)):
        if not self.roll_forward:
            self.Attack_Direction_Handler(offset)
            self.roll_forward = 30
            self.invincible = True

    def Roll_Forward_Update(self):
        if not self.roll_forward:
            self.invincible = False
            return
        self.roll_forward = max(0, self.roll_forward - 1)
        if self.roll_forward < 20:
            return
        
        if self.attack_direction.length() > 0:

            self.friction = 0
            self.max_speed = 40  # Adjust max speed speed for dashing distance


            # Set the velocity directly based on dash without friction interference
            self.velocity[0] = self.attack_direction[0] * 20
            self.velocity[1] = self.attack_direction[1] * 20

    def Dashing_Update(self, offset=(0, 0)):
        if not self.dashing:
            self.invincible = False
            return
            

        if abs(self.dashing) in {60, 50}:
            for i in range(20):
                angle = random.random() * math.pi * 2
                speed = random.random() * 0.5 + 0.5
                pvelocity = [math.cos(angle) * speed, math.sin(angle) * speed]
                self.game.particles.append(Particle(self.game, 'particle', self.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

        if self.dashing > 0:
            self.dashing = max(0, self.dashing - 1)


        if self.dashing > 50:
            
            if self.attack_direction.length() > 0:
                # Temporarily set friction to zero to avoid deceleration during dash
                self.friction = 0
                self.max_speed = 40  # Adjust max speed speed for dashing distance


                # Set the velocity directly based on dash without friction interference
                self.velocity[0] = self.attack_direction[0] * self.dashing
                self.velocity[1] = self.attack_direction[1] * self.dashing

                if abs(self.dashing) == 51:
                    self.velocity[0] *= 0.1
                    self.velocity[1] *= 0.1

                pvelocity = [abs(self.dashing) / self.dashing * random.random() * 3, 0]
                self.game.particles.append(Particle(self.game, 'particle', self.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

    def Dash(self, offset=(0, 0)):
        if not self.dashing:
            self.Attack_Direction_Handler(offset)
            self.dashing = 60
            self.invincible = True
        
        
    def Mouse_Handler(self):
        self.Set_Target(self.game.mouse.player_mouse)


    def Find_Nearby_Chests(self, range):
        self.nearby_chests = self.game.chest_handler.Find_Nearby_Chests(self.pos, range)

    
            

    # Render player
    def Render(self, surf, offset=(0, 0)):
        if abs(self.movement_handler.dashing) >= 50:
            return
        
        # Load and scale the entity images, split to allow better animation
        entity_image_head = self.game.assets[self.animation + '_head'][self.animation_num]
        entity_image_head = pygame.transform.scale(entity_image_head, (16, 12))

        entity_image_body = self.game.assets[self.animation + '_body'][self.animation_num]
        entity_image_body = pygame.transform.scale(entity_image_body, (16, 9))

        entity_image_legs = self.game.assets[self.animation + '_legs'][self.animation_num]
        entity_image_legs = pygame.transform.scale(entity_image_legs, (16, 3))

        if self.status_effects.invisibility:
            # Set the alpha value to make the entity fade out, the lower the more invisible
            alpha_value = max(0, min(255, self.active)) 
            entity_image_head.set_alpha(alpha_value)
            entity_image_body.set_alpha(alpha_value)
            entity_image_legs.set_alpha(alpha_value)

        if not "up" in self.animation:
            surf.blit(pygame.transform.flip(entity_image_legs, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] + 6))
            surf.blit(pygame.transform.flip(entity_image_body, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
            surf.blit(pygame.transform.flip(entity_image_head, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] - 8))


        self.weapon_handler.Render_Weapons(surf, offset)
        

        if  "up" in self.animation:
            surf.blit(pygame.transform.flip(entity_image_legs, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] + 6))
            surf.blit(pygame.transform.flip(entity_image_body, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
            surf.blit(pygame.transform.flip(entity_image_head, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] - 8))

        # Render status effects
        self.status_effects.Render_Effects(self.game, surf, offset)

        if self.damage_cooldown:
            scroll_up_effect = 20 - self.damage_cooldown
            self.game.default_font.Render_Word(surf, self.damage_text, (self.pos[0] - offset[0], self.pos[1] - scroll_up_effect - offset[1]), 'player_damage')