import math
import pygame
import random


class Attack_Stategies():

    def __init__(self, game, entity) -> None:
        self.game = game
        self.entity = entity


        self.player_found = False

        self.direct_pathing_cooldown = 0

    # Return True if pathing updated else false
    def Attack_Strategy(self) -> bool:
        if self.game.player.effects.invisibility.effect:
            return False
        if self.entity.attack_strategy == 'direct': # charge the player
            return self.Direct_Pathing()
        elif self.entity.attack_strategy == 'long_range': # keep long distance
            return self.Keep_Distance(200, 160)
        elif self.entity.attack_strategy == 'medium_range': # keep medium distance
            return self.Keep_Distance(120, 80)
        elif self.entity.attack_strategy == 'short_range':
            return self.Keep_Distance(80, 40)
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

    # Check for line of sight with the player
    def Line_Of_Sight(self, distance, dx, dy):
        tile_size = self.game.tilemap.tile_size

        # Convert enemy’s pixel position to tile coordinates
        ex = int(self.entity.pos[0] // tile_size)
        ey = int(self.entity.pos[1] // tile_size)
        # Convert player’s pixel position to tile coordinates
        px = int(self.game.player.pos[0] // tile_size)
        py = int(self.game.player.pos[1] // tile_size)

        # Generate the list of tiles along the line
        line_tiles = self.bresenham_line((ex, ey), (px, py))

        # Check each tile. If any tile is not see-through, return False
        for (tx, ty) in line_tiles:
            tile_key = f"{tx};{ty}"
            # If your ray_caster.Check_Tile(tile_key) means "can see through" is True
            # or "walkable" is True, adapt accordingly.
            if not self.game.ray_caster.Check_Tile(tile_key):
                return False

        return True

    # Returns all the tile coordinates on a line between `start` and `end`.
    # start/end should be (x, y) tuples in tile coordinates (integer grid positions).    
    def bresenham_line(self, start, end):

        x1, y1 = start
        x2, y2 = end

        points = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            points.append((x1, y1))
            if x1 == x2 and y1 == y2:
                break

            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        return points

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