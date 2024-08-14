from scripts.entities.entities import PhysicsEntity
from scripts.entities.moving_entity import Moving_Entity

import random
import pygame
import math
from scripts.engine.a_star import A_Star
from scripts.engine.ray_caster import Ray_Caster



class Enemy(Moving_Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, type, pos, size)
        self.animation = 'decrepit_bones'
        self.walking = 0
        self.health = 30
        self.random_movement_cooldown = 0
        self.max_speed = 1
        self.max_speed_holder = self.max_speed  
        
        self.pos_holder = (0,0)
        self.pathfinding_cooldown = 0
        self.path = []
        self.src_x = 0
        self.src_y = 0
        self.des_x = 0
        self.des_y = 0
        self.pos_holder_timer = 0
        self.stuck_timer = 0
        self.stuck = False

        self.corner_handling_cooldown = 0


    def update(self, tilemap, movement=(0, 0)):
        
        self.Path_Finding()
        movement = self.direction
        
        super().update(tilemap, movement = movement)
        self.animation = 'decrepit_bones'

        if abs(self.game.player.dashing) >= 50:
            if self.rect().colliderect(self.game.player.rect()):
                self.game.player.Damage_Taken(5)
                return True
            
        self.direction_x_holder = self.direction_x 
        self.direction_y_holder = self.direction_y
    
    # TODO: Refactor
    def Path_Finding(self):
        self.Position_Holder()

        if self.Stuck_Check():
            return

        if self.Charging():
            return

        
        # Calculate a new shortest path
        if not self.pathfinding_cooldown:
            self.path.clear()
            self.Calculate_Position()
            self.Calculate_Player_Position()
            self.game.a_star.a_star_search(self, [self.src_y, self.src_x], [self.des_y, self.des_x])
            self.pathfinding_cooldown = 100
        else:
            self.pathfinding_cooldown -= 1
        # Pathfinding
        if len(self.path) > 1:
            # Calculate the updated position
            self.Calculate_Position()
            # Assign the target to be the next position
            target = self.path[1]
            # Move the entity away from walls
            self.Corner_Handling()

            # Check if enemy has reached target, pop the first element and set direction to 0
            if (self.src_y, self.src_x) == target:
                self.direction = (0,0)
                self.path.pop(0)
                self.corner_handling_cooldown = 0

            else:   
                # Calculate Direction
                self.direction_x = 0.1 
                self.direction_y = 0.1 
                # Update the direction relative to the target
                if target[1] == self.src_x:
                    self.direction_x = 0
                elif target[1] < self.src_x:
                    self.direction_x *= -1
                if target[0] == self.src_y:
                    self.direction_y = 0
                elif target[0] < self.src_y:
                    self.direction_y *= -1
                
                
                self.direction = pygame.math.Vector2(self.direction_x, self.direction_y)

                if self.pos_holder_timer < 160:
                    if abs(self.pos_holder[0] - self.pos[0]) < 1 and abs(self.pos_holder[1] - self.pos[1]) < 1:
                        self.stuck_timer += 1
                    else:
                        self.stuck_timer = 0
                self.corner_handling_cooldown = 1

                return
        # If there is no path, move at random
        else:
            self.Moving_Random()



    # Move the entity if they're to close to a wall
    def Corner_Handling(self):
        # Timer for how often cornerhandling should be done
        if self.corner_handling_cooldown:
            return

        
        target_x_pos = (self.src_x + self.game.a_star.min_x) * 16
        target_y_pos = (self.src_y + self.game.a_star.min_y) * 16
        if not self.game.tilemap.Current_Tile_Type((target_x_pos, target_y_pos + 16)) == 'Floor':
            # Change the path to be a list, so it can be modified and
            # set the path goal up to avoid clash with wall
            path_list = list(self.path[1])
            path_list[1] += 1
            self.path[1] = tuple(path_list)

        elif not self.game.tilemap.Current_Tile_Type((target_x_pos, target_y_pos - 16)) == 'Floor':
            path_list = list(self.path[1])
            path_list[1] -= 1
            self.path[1] = tuple(path_list)

        if not self.game.tilemap.Current_Tile_Type((target_x_pos + 16, target_y_pos)) == 'Floor':
            path_list = list(self.path[1])
            path_list[0] -= 1
            self.path[1] = tuple(path_list)
        elif not self.game.tilemap.Current_Tile_Type((target_x_pos - 16, target_y_pos)) == 'Floor':
            path_list = list(self.path[1])
            path_list[0] += 1
            self.path[1] = tuple(path_list)

    # Check for line of sight with the player
    def Line_Of_Sight(self, distance, dx, dy):
        

        # Calculate the angle in radians
        angle_radians = math.atan2(dy, dx)

        for i in range(1, int(distance/16)):
            angle = i * math.radians(angle_radians)
            pos_x = self.pos[0] + math.cos(angle) * 16 * i
            pos_y = self.pos[1] + math.sin(angle) * 16 * i
            if not self.game.ray_caster.Check_Tile((pos_x, pos_y)):
                    return False
        return True
    

    def Charging(self):
        distance = math.sqrt((self.game.player.pos[0] - self.pos[0]) ** 2 + (self.game.player.pos[1] - self.pos[1]) ** 2)

        # Player is close, so the enemy charge directly
        if distance < 60:
            dx = self.game.player.pos[0] - self.pos[0]
            dy = self.game.player.pos[1] - self.pos[1]
            # Check if the enemy has 
            if not self.Line_Of_Sight(distance, dx, dy):
                return False
            self.direction = pygame.math.Vector2(dx, dy)
            self.direction.normalize_ip()
            self.direction[0] /= self.game.render_scale
            self.direction[1] /= self.game.render_scale
            return True
        
        return False

    # Save the entity's position every 200 ticks
    def Position_Holder(self):
        if self.pos_holder_timer:
            self.pos_holder_timer -= 1
        else:
            self.pos_holder = self.pos.copy()
            self.pos_holder_timer = 200


    def Stuck_Check(self):
        # Check if the entity is stuck for 20 ticks
        if self.stuck_timer > 20:
            self.stuck = True
            self.random_movement_cooldown = 0
            self.stuck_timer = 0

        if self.stuck:
            self.Moving_Random()
            if self.random_movement_cooldown <= 0:
                self.stuck = False
            return True
        
        return False
        

    def Calculate_Position(self):
        self.src_x = round(self.pos[0] / 16) - self.game.a_star.min_x 
        self.src_y = round(self.pos[1] / 16) - self.game.a_star.min_y 
        
    def Calculate_Player_Position(self):
        self.des_x = round(self.game.player.pos[0] / 16) - self.game.a_star.min_x 
        self.des_y = round(self.game.player.pos[1] / 16) - self.game.a_star.min_y 

    
    def Moving_Random(self):
        self.direction = (self.direction_x, self.direction_y)
        if self.random_movement_cooldown:
            self.random_movement_cooldown -= 1
        else:
            self.direction_x = random.randint(-1, 1) / 10
            self.direction_y = random.randint(-1, 1) / 10
            
            self.direction = (self.direction_x, self.direction_y)
            self.random_movement_cooldown = 20
            self.walking = max(0, self.walking-1)
    
            self.Trap_Collision_Handler()
            

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

    
