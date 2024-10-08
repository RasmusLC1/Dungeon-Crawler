from scripts.entities.entities import PhysicsEntity
from scripts.entities.moving_entity import Moving_Entity
from scripts.engine.particles.particle import Particle
from scripts.spark import Spark
from scripts.entities.player.player_effects import Player_Status_Effect_Handler
from copy import copy

import random
import math
import pygame


class Player(Moving_Entity):
    def __init__(self, game, pos, size, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, 'player', pos, size, health, strength, max_speed, agility, intelligence, stamina)
        self.dashing = 0
        self.animation_num_max = 3
        
        self.max_ammo = 30
        self.ammo = 10
        self.active_weapon_left = None
        self.left_weapon_cooldown = 0
        self.active_weapon_right = None
        self.right_weapon_cooldown = 0
        self.active_bow = None
        self.bow_cooldown = 0
        self.Set_Animation('idle_down')
        self.souls = 5
        self.nearby_chests = []

        self.light_level = 5
        self.light_cooldown = 0
        # self.light_source = None
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)

        self.inventory_interaction = 0

        self.coins = 0
        self.shootin_cooldown = 0

        self.weapons = []
        self.status_effects = Player_Status_Effect_Handler(self)


    
    def Update(self, tilemap, movement=(0, 0), offset=(0, 0)):
        super().Update(tilemap, movement=movement)
        self.Mouse_Handler()
        if self.dashing:
            self.Dashing_Update(offset)

        if self.shootin_cooldown:
            self.shootin_cooldown -= 1
        
        self.Update_Light()

        self.Set_Direction_Holder()

        
        
        if self.game.weapon_inventory.active_inventory == 0:
            self.Update_Left_Weapon(offset)
            self.Update_Right_Weapon(offset)
        elif self.game.weapon_inventory.active_inventory == 1:
            self.Update_Bow(offset)
        else:
            print("INVENTORY MISSING")
    
    def Increase_Souls(self, added_soul):
        self.souls += added_soul

    def Entity_Collision_Detection(self, tilemap):
        if self.dashing > 40:
            return None
        return super().Entity_Collision_Detection(tilemap)

    def Attack_Direction_Handler(self, offset = (0,0)):
        super().Attack_Direction_Handler(offset)

    def Set_Charge(self, charge_speed, offset=(0, 0)):
        super().Set_Charge(charge_speed, offset)

    # Function to update the player's weapons
    # Each weapon needs it own method to handle it's cooldown
    def Update_Left_Weapon(self, offset=(0, 0)):

        if not self.active_weapon_left:
            return
        
        if self.inventory_interaction:
            self.Set_Inventory_Interaction(self.inventory_interaction - 1)
            self.active_weapon_left.Reset_Charge()
            return
        
        self.active_weapon_left.Set_Equipped_Position(self.direction_y_holder)

        self.active_weapon_left.Update(offset)
        if not self.active_weapon_left:
            return
        self.active_weapon_left.Update_Attack()
        self.Attacking(self.active_weapon_left, offset)

        
        if self.left_weapon_cooldown:
            self.left_weapon_cooldown -= 1
            return

        if not self.game.mouse.left_click:
            return
        
        cooldown = self.Weapon_Attack(self.active_weapon_left)
        
        self.left_weapon_cooldown = max(self.left_weapon_cooldown, cooldown)

        return
    
    def Update_Right_Weapon(self, offset=(0, 0)):
        # Return if there's no weapon
        if not self.active_weapon_right:
            return
        # Update the weapon position and logic

        if self.inventory_interaction:
            self.Set_Inventory_Interaction(self.inventory_interaction - 1)
            self.active_weapon_right.Reset_Charge()
            return

        self.active_weapon_right.Set_Equipped_Position(self.direction_y_holder)
        
        self.active_weapon_right.Update(offset)
        if not self.active_weapon_right:
            return
        self.active_weapon_right.Update_Attack()
        self.Attacking(self.active_weapon_right, offset)
        
        # Handle weapon cooldown
        if self.right_weapon_cooldown:
            self.right_weapon_cooldown -= 1
            return
        
        # Return if mouse has not been clicked
        if not self.game.mouse.right_click:
            return
        # Attack with weapon
        cooldown = self.Weapon_Attack(self.active_weapon_right)
        
        self.right_weapon_cooldown = max(self.right_weapon_cooldown, cooldown)

    
    def Update_Bow(self, offset=(0, 0)):
        # Return if there's no weapon
        if not self.active_bow:
            return
        # Update the weapon position and logic

        if self.inventory_interaction:
            self.Set_Inventory_Interaction(self.inventory_interaction - 1)
            self.active_bow.Reset_Charge()
            return

        self.active_bow.Set_Equipped_Position(self.direction_y_holder)
        
        self.active_bow.Update(offset)
        if not self.active_bow:
            return
        
        self.active_bow.Update_Attack()
        self.Attacking(self.active_bow, offset)
        
        # Handle weapon cooldown
        if self.bow_cooldown:
            self.bow_cooldown -= 1
            return
        
        # Return if mouse has not been clicked
        if not self.game.mouse.right_click:
            return
        # Attack with weapon
        cooldown = self.Weapon_Attack(self.active_bow)
        
        self.bow_cooldown = max(self.bow_cooldown, cooldown)

    
    # Activate weapon attack, return cooldown time
    def Weapon_Attack(self, weapon):
        # Return if inventory has not been clicked
        if self.game.mouse.inventory_clicked:
            return 0
        # weapon.Set_Attack()
        if weapon.attacking:
            cooldown = max(5 + weapon.attacking, 100/self.agility + weapon.attacking)
            return cooldown
        return 0
    
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

    def Set_Active_Weapon(self, weapon, hand):  
        if not weapon or not hand:
            return False    
        equipped_weapon = copy(weapon)
        equipped_weapon.Set_In_Inventory(False)
        if hand == 'left_hand':
            equipped_weapon.Move(self.pos)
            self.active_weapon_left = equipped_weapon
            return
        if hand == 'right_hand':
            equipped_weapon.Move(self.pos)
            self.active_weapon_right = equipped_weapon
            return
        if 'bow' in hand:
            equipped_weapon.Move(self.pos)
            self.active_bow = equipped_weapon

    def Remove_Active_Weapon(self, hand):
        if hand == 'left_hand' and self.active_weapon_left:
            self.active_weapon_left = None
        if hand == 'right_hand' and self.active_weapon_right:
            self.active_weapon_right = None

    def Set_Light_State(self, state):
        self.light_source.active = state
    
    
        
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

    def Back_Step(self):
        pass

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
        
        
    def Mouse_Handler(self):
        self.Set_Target(self.game.mouse.player_mouse)

    def Set_Direction_Holder(self):
        if self.direction_x or self.direction_y:
            self.direction_x_holder = self.direction_x
            self.direction_y_holder = self.direction_y

    def Find_Nearby_Chests(self, range):
        self.nearby_chests = self.game.chest_handler.Find_Nearby_Chests(self.pos, range)

    def Set_Inventory_Interaction(self, state):
        self.inventory_interaction = state
            

    # Render player
    def Render(self, surf, offset=(0, 0)):
        if abs(self.dashing) >= 50:
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


        self.Render_Weapons(surf, offset)
        

        if  "up" in self.animation:
            surf.blit(pygame.transform.flip(entity_image_legs, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] + 6))
            surf.blit(pygame.transform.flip(entity_image_body, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
            surf.blit(pygame.transform.flip(entity_image_head, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] - 8))

        # Render status effects
        self.status_effects.Render_Effects(self.game, surf, offset)

        
    def Render_Weapons(self, surf, offset):
        if self.game.weapon_inventory.active_inventory == 0:
            if self.active_weapon_left:
                self.active_weapon_left.Render_Equipped(surf, offset)
            if self.active_weapon_right:
                self.active_weapon_right.Render_Equipped(surf, offset)
        elif self.game.weapon_inventory.active_inventory == 1:
            if self.active_bow:
                self.active_bow.Render_Equipped(surf, offset)
        else:
            print("INVENTORY MISSING")

