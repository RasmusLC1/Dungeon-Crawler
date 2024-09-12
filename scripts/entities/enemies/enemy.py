from scripts.entities.entities import PhysicsEntity
from scripts.entities.moving_entity import Moving_Entity
from scripts.engine.utility.helper_functions import Helper_Functions
from scripts.entities.enemies.path_finding import Path_Finding


import random
import pygame
import math



class Enemy(Moving_Entity):
    def __init__(self, game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, type, pos, size, health, strength, max_speed, agility, intelligence, stamina)
        self.subtype = 'enemy'     

        self.max_speed_holder = self.max_speed
        self.random_movement_cooldown = 0
        self.alert_cooldown = 0
        self.active_weapon = None
        self.weapon_cooldown = 0
        self.walking = 0
        self.target = self.game.player.pos

        self.path_finding = Path_Finding(game, self)
        self.distance_to_player = 9999
        self.charge = 0
        self.attack_strategy = 'direct'
        self.path_finding_strategy = 'standard'




    

    def Update(self, tilemap, movement=(0, 0)):
        self.path_finding.Path_Finding(self.target)
        movement = self.direction
        
        super().Update(tilemap, movement = movement)
        # self.animation = 'decrepit_bones'

        self.direction_x_holder = self.direction_x 
        self.direction_y_holder = self.direction_y

        self.Update_Alert_Cooldown()



    def Reset_Charge(self):
        self.charge = 0

    
    
    def Entity_Collision_Detection(self, tilemap):
        colliding_entity = super().Entity_Collision_Detection(tilemap)

        if colliding_entity:
            if colliding_entity.type == 'player':
                # Prevent further movement towards the player by stopping the enemy's movement
                self.direction = (0, 0)
                return colliding_entity

            # Collision logic for other entities
            collision_vector = pygame.math.Vector2(self.pos[0] - colliding_entity.pos[0],
                                                self.pos[1] - colliding_entity.pos[1])
            if collision_vector.length() > 0:
                collision_vector = collision_vector.normalize()
                direction_vector = pygame.math.Vector2(self.direction)
                reflected_direction = direction_vector.reflect(collision_vector)

                if self.Future_Rect(reflected_direction).colliderect(self.game.player.rect()):
                    self.direction = (0, 0)

                    return self.game.player

                self.direction = (reflected_direction.x, reflected_direction.y)

        return None
    
    def Attack(self):
        pass
        # print("Attack not implemented")

    def Update_Movement(self, movement):
        return super().Update_Movement(movement)

    
    def Set_Active_Weapon(self, weapon):
        self.active_weapon = weapon

    def Update_Alert_Cooldown(self):
        if self.alert_cooldown:
            self.alert_cooldown = max(0, self.alert_cooldown - 1)

    def Set_Alert_Cooldown(self, amount):
        self.alert_cooldown = amount

    def Find_New_Path(self, destination):
        self.Set_Target(destination)
        self.path_finding.Find_Shortest_Path()

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
        if self.active_weapon:
            self.active_weapon.Render_Equipped_Enemy(surf, offset)
        