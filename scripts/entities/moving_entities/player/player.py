from scripts.entities.entities import PhysicsEntity
from scripts.entities.moving_entities.moving_entity import Moving_Entity
from scripts.engine.particles.particle import Particle
from scripts.entities.moving_entities.player.player_effects import Player_Status_Effect_Handler
from scripts.entities.moving_entities.player.player_weapon import Player_Weapon_Handler
from scripts.entities.moving_entities.player.player_movement import Player_Movement


import random
import math
import pygame


class Player(Moving_Entity):
    def __init__(self, game, pos, size, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, 'player', 'player', pos, size, health, strength, max_speed, agility, intelligence, stamina, 'player')
        
        self.animation_num_max = 3
        
        self.bow_cooldown = 0
        self.Set_Animation('idle_down')
        self.souls = 500
        self.nearby_chests = []
        self.view_direction = (0,0)

        self.light_cooldown = 0
        self.default_light_level = 6
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.default_light_level, self.tile)
        self.game.light_handler.Initialise_Light_Level(self.tile)

        self.weapons = []
        self.effects = Player_Status_Effect_Handler(self)
        self.weapon_handler = Player_Weapon_Handler(self.game, self)
        self.movement_handler = Player_Movement(self.game, self)






    def Save_Data(self):
        super().Save_Data()
        self.saved_data['souls'] = self.souls
        self.saved_data['max_speed'] = self.max_speed


        # self.saved_data['weapon_handler'] = self.weapon_handler


    def Load_Data(self, data):

        super().Load_Data(data)
        self.souls = data['souls']
        self.max_speed = data['max_speed']

        



    def Update(self, tilemap, movement=(0, 0), offset=(0, 0)):

        super().Update(tilemap, movement=movement)
        self.Mouse_Handler()
        self.movement_handler.Update()

        
        self.Update_Light()

        self.View_Direction(offset)

        self.weapon_handler.Update(offset)

        
    def View_Direction(self, offset):
        self.view_direction = pygame.math.Vector2(self.target[0] - self.pos[0], self.target[1] - self.pos[1])
        if self.view_direction.length() > 0:
            self.view_direction.normalize_ip()
    
    def Increase_Souls(self, added_soul):
        if self.effects.hunger.effect:
            added_soul += self.effects.hunger.effect
        self.souls += added_soul

    def Decrease_Souls(self, subtract_soul):
        self.souls -= subtract_soul

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
        
    def Set_Souls(self, souls):
        self.souls = souls

    def Set_Health(self, health):
        self.health = health

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


    
    def Set_Inventory_Interaction(self, state):
        self.weapon_handler.Set_Inventory_Interaction(state)

    def Set_Active_Weapon(self, weapon, hand):  

        self.weapon_handler.Set_Active_Weapon(weapon, hand)
    
    def Set_Light_State(self, state):
        self.light_source.active = state


    def Update_Light_Source(self, light_level):
        self.light_source.Update_Light_Level(light_level)

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
                self.game.light_handler.Move_Light(self.pos, self.light_source, self.tile)
        
        
    def Mouse_Handler(self):
        self.Set_Target(self.game.mouse.player_mouse)


    def Find_Nearby_Chests(self, range):
        self.nearby_chests = self.game.chest_handler.Find_Nearby_Chests(self.pos, range)



    # Render player
    def Render(self, surf, offset=(0, 0)):
        if abs(self.movement_handler.dashing) >= 50:
            return
        
        # Load and scale the entity images, split to allow better animation
        entity_image= self.game.assets[self.animation][self.animation_num]

        
        entity_image.set_alpha(self.alpha_value)

        if not "up" in self.animation:
            surf.blit(pygame.transform.flip(entity_image, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))


        self.weapon_handler.Render_Weapons(surf, offset)
        

        if  "up" in self.animation:
            surf.blit(pygame.transform.flip(entity_image, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))

        # Render status effects
        self.effects.Render_Effects(surf, offset)

        if self.damage_cooldown:
            scroll_up_effect = 20 - self.damage_cooldown
            self.game.default_font.Render_Word(surf, self.damage_text, (self.pos[0] - offset[0], self.pos[1] - scroll_up_effect - offset[1]), scroll_up_effect * 10, 'player_damage')
