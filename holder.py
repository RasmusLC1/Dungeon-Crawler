from scripts.engine.utility.helper_functions import Helper_Functions
import math
import pygame
import random


class Path_Finding():
    def __init__(self, game, entity) -> None:
        self.game = game
        self.entity = entity

        self.pos_holder = (0,0)

        self.path = [] # Path to destination
        self.pathfinding_cooldown = 0

        # self.pos in 16/16 tileformat
        self.src_x = 0
        self.src_y = 0

        # destination in 16/16 tileformat
        self.des_x = 0
        self.des_y = 0

        self.pos_holder_timer = 0
        self.stuck_timer = 0

        self.corner_handling_cooldown = 0

        self.player_found = False

    def Path_Finding(self, target, look_for_new_path = False):
        print("TEST")

        self.Set_Position_Holder()

        self.Update_Stuck_Timer()
        if self.Stuck_Check():
            return

        if self.Direct_Pathing():
            return
        else:
            if self.player_found:
                self.player_found = False
                target = self.game.player.pos
        
        # Only run this if we need a new path
        if look_for_new_path:
            self.Find_Shortest_Path(target)

        self.Navigate_Path()


    def Navigate_Path(self):
        # Pathfinding
        if len(self.path) > 1:
            # Calculate the updated position
            self.Calculate_Position()
            # Assign the target to be the next position
            target = self.path[1]
            # Move the entity away from walls
            self.Corner_Handling()

            if self.Path_Segment_Complete(target):
                return

            self.Calculate_Path_Segment(target)

            self.entity.direction =  Helper_Functions.Direction_Vector((self.entity.direction_x, self.entity.direction_y))
            return
        # If there is no path, move at random
        else:
            self.Moving_Random()

    def Calculate_Path_Segment(self, target):
        # Calculate Direction
        self.entity.direction_x = 0.1 
        self.entity.direction_y = 0.1 
        # Update the direction relative to the target
        if target[1] == self.src_x:
            self.entity.direction_x = 0
        elif target[1] < self.src_x:
            self.entity.direction_x *= -1
        if target[0] == self.src_y:
            self.entity.direction_y = 0
        elif target[0] < self.src_y:
            self.entity.direction_y *= -1

    # Check if enemy has reached target, pop the first element and set direction to 0
    def Path_Segment_Complete(self, target):
        if not (self.src_y, self.src_x) == target:
            return False
        
        self.entity.direction = (0,0)
        self.path.pop(0)
        self.corner_handling_cooldown = 0
        return True

    def Find_Shortest_Path(self, destination) -> None:
        if self.pathfinding_cooldown:
            self.pathfinding_cooldown -= 1
            return
            
        self.path.clear()
        self.Calculate_Position()
        self.Calculate_Destination_Position(destination)
        self.game.a_star.a_star_search(self.path, [self.src_y, self.src_x], [self.des_x, self.des_x])
        self.pathfinding_cooldown = 100
        return

    # Move the entity if they're to close to a wall
    def Corner_Handling(self):
        self.corner_handling_cooldown = 1

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
            pos_x = self.entity.pos[0] + math.cos(angle) * 16 * i
            pos_y = self.entity.pos[1] + math.sin(angle) * 16 * i
            if not self.game.ray_caster.Check_Tile((pos_x, pos_y)):
                    return False
        return True
    

    def Direct_Pathing(self):
        distance = Helper_Functions.Abs_Distance_Float(self.entity.pos, self.game.player.pos)

        # Player is close, so the enemy charge directly
        if distance < 60:
            dx = self.game.player.pos[0] - self.entity.pos[0]
            dy = self.game.player.pos[1] - self.entity.pos[1]
            # Check if the enemy has 
            if not self.Line_Of_Sight(distance, dx, dy):
                return False
            self.entity.direction = pygame.math.Vector2(dx, dy)
            self.entity.direction.normalize_ip()
            self.entity.direction[0] /= self.game.render_scale
            self.entity.direction[1] /= self.game.render_scale
            self.player_found = True
            return True
        
        return False

    # Save the entity's position every 200 ticks
    def Set_Position_Holder(self):
        if self.pos_holder_timer:
            self.pos_holder_timer -= 1
        else:
            self.pos_holder = self.entity.pos.copy()
            self.pos_holder_timer = 200

    def Update_Stuck_Timer(self) -> None:
        if self.pos_holder_timer < 160:
            dx, dy = Helper_Functions.Abs_Distance_Tuple(self.entity.pos, self.pos_holder)
            if dx < 2 and dy < 2:
                self.stuck_timer += 1
            else:
                self.stuck_timer = 0


    # Move the entity at random if stuck
    def Stuck_Check(self):
        if not self.stuck_timer > 20:
            return False
        
        self.entity.random_movement_cooldown = 200
        self.Moving_Random()
        return True
    
    def Moving_Random(self):
        self.entity.direction = (self.entity.direction_x, self.entity.direction_y)
        if self.entity.random_movement_cooldown:
            self.entity.random_movement_cooldown -= 1
            return
        self.entity.direction_x = random.randint(-1, 1) / 10
        self.entity.direction_y = random.randint(-1, 1) / 10
        
        self.entity.direction = (self.entity.direction_x, self.entity.direction_y)
        self.entity.random_movement_cooldown = 20
        self.entity.walking = max(0, self.entity.walking-1)

        self.entity.Trap_Collision_Handler()

    
    def Calculate_Position(self):
        self.src_x = round(self.entity.pos[0] / 16) - self.game.a_star.min_x 
        self.src_y = round(self.entity.pos[1] / 16) - self.game.a_star.min_y 
        
    def Calculate_Destination_Position(self, destination):
        self.des_x = round(destination[0] / 16) - self.game.a_star.min_x 
        self.des_x = round(destination[1] / 16) - self.game.a_star.min_y 
