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

        # self.pos in 16/16 tileformat
        self.src_x = 0
        self.src_y = 0

        # destination in 16/16 tileformat
        self.des_x = 0
        self.des_y = 0

        self.pos_holder_timer = 0
        self.stuck_timer = 0

        self.player_found = False

        self.direct_pathing_cooldown = 0




    def Path_Finding(self, target, look_for_new_path = False):
        self.Calculate_Distance_To_Player()

        self.Set_Position_Holder()

        self.Corner_Handling()



        self.Update_Stuck_Timer()
        if self.Stuck_Check():
            return
        
        if self.Attack_Strategy():
            self.entity.Trap_Collision_Handler()

            return
        else:
            # If enemy looses sight of player he will try to go to the last known location
            if self.player_found:
                self.player_found = False
                self.entity.Set_Target(self.game.player.pos)
                look_for_new_path = True
        
   

        # Only run this if we need a new path
        if look_for_new_path:
            self.Find_Shortest_Path()
        
        if not self.Navigate_Path():
            self.Moving_Random()



    def Navigate_Path(self):
        # Pathfinding
        if len(self.path) < 2:
            return False
        
        # Calculate the updated position
        self.Calculate_Position()
        # Assign the target to be the next position
        target = self.path[1]

        # Move the entity away from walls
        # self.Corner_Handling()
        if self.Path_Segment_Complete(target):
            return
        self.Calculate_Path_Segment(target)

        
        return True

    

    def Calculate_Path_Segment(self, target):
        target_pos = (target[0] * 16, target[1] * 16)
        self.entity.direction = pygame.math.Vector2(target_pos[0] - self.entity.pos[0], target_pos[1] - self.entity.pos[1])
        if self.entity.direction.length() > 0:
            self.entity.direction.normalize_ip()

    # Check if enemy has reached target, pop the first element and set direction to 0
    def Path_Segment_Complete(self, target):

        # Use a threshold for reaching the target to avoid precision issues
        reach_threshold = 16
        if math.hypot(self.entity.pos[0] - target[0] * 16, self.entity.pos[1] - target[1] * 16) > reach_threshold:
            return False

        self.entity.direction = (0, 0)
        self.path.pop(0)
        return True

    def Find_Shortest_Path(self) -> None:
        # Check if the entity has recently received a new target
        if self.entity.locked_on_target:
            return
            
        self.path.clear()
        self.Calculate_Position()
        self.Calculate_Destination_Position(self.entity.target)
        for i in range(3):
            self.game.a_star.a_star_search(self.path, [self.src_x, self.src_y], [self.des_x, self.des_y], self.entity.path_finding_strategy)
            if self.path:
                break

        self.path = [(x + self.game.a_star.min_x, y + self.game.a_star.min_y) for (x, y) in self.path]

        self.entity.Set_Locked_On_Target(500)
        return
    

    # Move the entity if they're to close to a wall
    def Corner_Handling(self):        
        direction_x = 0
        direction_y = 0
        if self.entity.collisions['up']:
            direction_y = -2
        if self.entity.collisions['down']:
            direction_y = 2
        if self.entity.collisions['left']:
            direction_x = 2
        if self.entity.collisions['right']:
            direction_x = -2
        if direction_x or direction_y:
            self.entity.Set_Frame_movement((direction_x, direction_y))
            self.entity.Tile_Map_Collision_Detection(self.game.tilemap)



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
    
    def Calculate_Distance_To_Player(self):
        self.entity.distance_to_player = Helper_Functions.Abs_Distance_Float(self.entity.pos, self.game.player.pos)


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
        if self.stuck_timer < 20:
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

        self.entity.Trap_Collision_Handler()

    
    def Calculate_Position(self):
        self.src_x = round(self.entity.pos[0] // 16) - self.game.a_star.min_x 
        self.src_y = round(self.entity.pos[1] // 16) - self.game.a_star.min_y 
        
    def Calculate_Destination_Position(self, destination):
        self.des_x = round(destination[0] // 16) - self.game.a_star.min_x 
        self.des_y = round(destination[1] // 16) - self.game.a_star.min_y 


    # ATTACK STRATEGIES:
    #################################################
    # Return True if pathing updated else false
    def Attack_Strategy(self) -> bool:
        if self.game.player.status_effects.invisibility:
            return False
        if self.entity.attack_strategy == 'direct':
            return self.Direct_Pathing()
        elif self.entity.attack_strategy == 'long_range':
            return self.Keep_Distance(100, 80)
        elif self.entity.attack_strategy == 'medium_range':
            return self.Keep_Distance(60, 30)
        elif self.entity.attack_strategy == 'medium_range':
            return self.Keep_Distance(30, 20)
        elif self.entity.attack_strategy == 'keep_position':
            self.entity.direction = (0, 0)
            return True
        else:
            return self.Direct_Pathing()

    def Keep_Distance(self, max_range, closest_range):
        # Cooldown since the player's relative position does not need constant update
        if self.direct_pathing_cooldown:
            self.direct_pathing_cooldown = max(0, self.direct_pathing_cooldown - 1)
            return True       
        
        if self.entity.distance_to_player < max_range and self.entity.distance_to_player > closest_range:
            random_x = random.randint(1, 10) / 10
            random_y = random.randint(1, 10) / 10
            self.entity.direction = pygame.math.Vector2(random_x, random_y)
            self.entity.direction.normalize_ip()
            self.direct_pathing_cooldown = 20

            return True
        
        if self.entity.distance_to_player > max_range :
            return self.Charge_player(150)
        
        return self.Run_Away(60)

        

    def Direct_Pathing(self):
        # Cooldown since the player's relative position does not need constant update
        if self.direct_pathing_cooldown:
            self.direct_pathing_cooldown = max(0, self.direct_pathing_cooldown - 1)
            return True
        return self.Charge_player(200)  
        # Player is close, so the enemy charge directly
        
    def Run_Away(self, distance):
        if self.entity.distance_to_player < distance:
            dx = (self.game.player.pos[0] - self.entity.pos[0]) * -1
            dy = (self.game.player.pos[1] - self.entity.pos[1]) * -1
            # Check if the enemy has 
            if not self.Line_Of_Sight(self.entity.distance_to_player, dx, dy):
                return False
            self.entity.direction = pygame.math.Vector2(dx, dy)
            if self.entity.direction[0] == 0 and self.entity.direction[1] == 0:
                return False
            
            self.entity.direction.normalize_ip()
            self.player_found = True
            if not self.entity.alert_cooldown:
                self.entity.Set_Alert_Cooldown(400)
                self.game.clatter.Generate_Clatter(self.entity.pos, 400) # Generate clatter to alert nearby enemies
            self.direct_pathing_cooldown = 10
            return True
        
        return False


    def Charge_player(self, distance):
        if self.entity.distance_to_player < distance:
            dx = self.game.player.pos[0] - self.entity.pos[0]
            dy = self.game.player.pos[1] - self.entity.pos[1]
            # Check if the enemy has 
            if not self.Line_Of_Sight(self.entity.distance_to_player, dx, dy):
                return False
            self.entity.direction = pygame.math.Vector2(dx, dy)
            if self.entity.direction[0] == 0 and self.entity.direction[1] == 0:
                return False
            self.entity.direction.normalize_ip()
            self.player_found = True
            # Only update every 1000 ticks since you don't want
            # the enemies to spam the ability and lag the game
            if not self.entity.alert_cooldown:
                self.entity.Set_Alert_Cooldown(1000)
                self.game.clatter.Generate_Clatter(self.entity.pos, 400) # Generate clatter to alert nearby enemies
            self.direct_pathing_cooldown = 10
            return True
        return False