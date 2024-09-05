from scripts.entities.entities import PhysicsEntity
from scripts.entities.moving_entity import Moving_Entity
from scripts.engine.utility.helper_functions import Helper_Functions
from scripts.entities.enemies.path_finding import Path_Finding
from scripts.items.weapons.close_combat.sword import Sword


import random
import pygame
import math
from scripts.engine.a_star import A_Star
from scripts.engine.ray_caster import Ray_Caster



class Enemy(Moving_Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, type, pos, size)
        self.subtype = 'enemy'
        self.animation = 'decrepit_bones'
        self.walking = 0
        self.health = 30
        self.random_movement_cooldown = 0
        self.max_speed = 1
        self.max_speed_holder = self.max_speed  
        self.alert_cooldown = 0
        self.active_weapon_left = None

        self.path_finding = Path_Finding(game, self)


        self.left_weapon_cooldown = 0
        self.weapon_cooldown = 0
        self.charge = 0
        self.distance_to_player = 9999




        self.Equip_Weapon()


    def Equip_Weapon(self):
        sword = Sword(self.game, self.pos, (16,16), 'sword')
        if not sword.Check_Inventory_Type('left_hand'):
            
            return False
        sword.Pickup_Reset_Weapon(self)
        sword.Set_Equip(True)
        self.Set_Active_Weapon(sword)
        self.active_weapon_left.render = False
        del(sword)
        return True

    def update(self, tilemap, movement=(0, 0)):
        self.path_finding.Path_Finding(self.game.player.pos)
        movement = self.direction
        
        super().update(tilemap, movement = movement)
        # self.animation = 'decrepit_bones'

        self.direction_x_holder = self.direction_x 
        self.direction_y_holder = self.direction_y

        self.Update_Alert_Cooldown()

        self.Update_Left_Weapon()
        self.Weapon_Cooldown()
        if self.distance_to_player < 20:
            self.Attack()

    def Set_Idle(self):
        pass

    def Set_Action(self,  movement):
        pass

    def Update_Left_Weapon(self, offset=(0, 0)):
        if not self.active_weapon_left:
            return

        self.active_weapon_left.Set_Active(self.active)
        self.active_weapon_left.Set_Light_Level(self.light_level)

        self.active_weapon_left.Set_Equipped_Position(self.direction_y_holder)
        self.active_weapon_left.Update(offset)
        if not self.active_weapon_left:
            return
        self.active_weapon_left.Update_Attack()

        self.active_weapon_left.Update_Attack_Animation()

        return
    
    def Attack(self):
        if self.weapon_cooldown:
            return
        
        self.Set_Target(self.game.player.pos)
        self.active_weapon_left.Set_Attack_Ready(True)
        self.active_weapon_left.Set_Attack()
        self.weapon_cooldown = 100



    def Set_Active_Weapon(self, weapon):
        self.active_weapon_left = weapon

    def Update_Alert_Cooldown(self):
        if self.alert_cooldown:
            self.alert_cooldown = max(0, self.alert_cooldown - 1)

    def Set_Alert_Cooldown(self, amount):
        self.alert_cooldown = amount

    def Find_New_Path(self, destination):
        self.path_finding.Path_Finding(destination, True)

    def Weapon_Cooldown(self):
        if self.weapon_cooldown:
            self.weapon_cooldown = max(0, self.weapon_cooldown - 1)

    def Set_Idle(self):
        pass
        
    def Damage_Taken(self, damage):
        super().Damage_Taken(damage)
        if self.health <= 0:
            self.Reset_Effects()
            self.game.enemy_handler.Delete_Enemy(self)   

        self.direction = pygame.math.Vector2(self.direction_x, self.direction_y)
        
    def Trap_Collision_Handler(self):
        for trap in self.nearby_traps:
            if self.rect().colliderect(trap.rect()):
                # Run away in in the same direction the enemy was moving previously
                # Use min and max to prevent it teleporting
                if self.direction_x_holder < 0:
                    self.direction_x = max(-0.4, self.direction_x_holder * 4)
                else:
                    self.direction_x = min(0.4, self.direction_x_holder * 4)

                if self.direction_y_holder < 0:
                    self.direction_y = max(-0.4, self.direction_y_holder * 4)
                else:
                    self.direction_y = min(0.4, self.direction_y_holder * 4)

                self.direction = (self.direction_x, self.direction_y)
            else:
                # Check if the enemy will collide soon, if yes redirect in the opposite direction
                if self.Future_Rect(self.direction).colliderect(trap.rect()):
                    self.direction_x *= -1
                    self.direction_y *= -1
                    self.direction = (self.direction_x, self.direction_y)
                    break

    def Future_Rect(self, direction):
             return pygame.Rect(self.pos[0] + direction[0]*16, self.pos[1] + direction[1]*16, self.size[0], self.size[1])

    
    def Render(self, surf, offset = (0,0)):
        super().Render(surf, offset)
        self.Render_Weapons(surf, offset)


    def Render_Weapons(self, surf, offset):
        if self.active_weapon_left:
            self.active_weapon_left.Render_Equipped_Enemy(surf, offset)
        