import math
import pygame

class Ray_Caster():
    def __init__(self, game):
        self.tiles = []
        self.enemies = []
        self.traps = []
        self.chests = []
        self.decorations = []
        self.traps = []
        self.nearby_traps = []
        self.nearby_cooldown = 0
        self.inactive_distance = 300
        
        self.game = game
        self.default_activity = 700

    def Update(self, game):
        # Handle tile activity degradation
        for tile in self.tiles:
            if tile['active']:
                tile['active'] -= 1
            # Find distance from player and if it's greater than 300, delete it
            distance = math.sqrt((game.player.pos[0] - tile['pos'][0] * 16) ** 2 + (game.player.pos[1] - tile['pos'][1] * 16) ** 2)
            if abs(distance) > self.inactive_distance:
                tile['active'] = 0
                self.tiles.remove(tile)

        for enemy in self.enemies:
            if enemy.active:
                enemy.Reduce_Active()
            else:
                self.enemies.remove(enemy)
            distance = math.sqrt((game.player.pos[0] - enemy.pos[0]) ** 2 + (game.player.pos[1] - enemy.pos[1]) ** 2)
            if abs(distance) > self.inactive_distance:
                print(abs(distance))
                enemy.Set_Active(0)
                self.enemies.remove(enemy)


        for chest in self.chests:
            if chest.active:
                chest.Reduce_Active()
            else:
                self.chests.remove(chest)
                return
            distance = abs(math.sqrt((game.player.pos[0] - chest.pos[0]) ** 2 + (game.player.pos[1] - chest.pos[1]) ** 2))
            if abs(distance) > self.inactive_distance:
                chest.Set_Active(0)
                self.chests.remove(chest)
            if chest.empty:
                self.chests.remove(chest)
                return
            
        for trap in self.traps:
            if trap.active:
                trap.Reduce_Active()
            else:
                self.traps.remove(trap)
            distance = math.sqrt((game.player.pos[0] - trap.pos[0]) ** 2 + (game.player.pos[1] - trap.pos[0]) ** 2)
            if abs(distance) > self.inactive_distance:
                trap.Set_Active(0)
                self.traps.remove(trap)


    def Check_Trap(self, pos):
        for trap in self.game.trap_handler.nearby_traps:
            if self.rect(pos).colliderect(trap.rect()):
                if not trap.active:
                    trap.Set_Active(self.default_activity)
                    self.traps.append(trap)
                else:
                    trap.Set_Active(self.default_activity)   

    def Check_Enemy(self, pos):
        for enemy in self.game.player.nearby_enemies:
            # Check if enemy is already in the enemy list
            if self.rect(pos).colliderect(enemy.rect()):
                if not enemy.active:
                    enemy.Set_Active(300)
                    self.enemies.append(enemy)
                else:
                    enemy.Set_Active(300)

    def Check_Chest(self, pos):
        for chest in self.game.player.nearby_chests:
            if self.rect(pos).colliderect(chest.rect()):
                if not chest.active:
                    chest.Set_Active(self.default_activity)
                    self.chests.append(chest)
                else:
                    chest.Set_Active(self.default_activity)
    
    def Check_Decoration(self, pos):
        for decoration in self.game.decoration_handler.nearby_decoration:
            if self.rect(pos).colliderect(decoration.rect()):
                if not decoration.active:
                    decoration.Set_Active(self.default_activity)
                    self.decorations.append(decoration)
                else:
                    decoration.Set_Active(self.default_activity)

    def Check_Tile(self, pos):
        tile = self.game.tilemap.Current_Tile(pos)
        if tile:
            if not tile['active']:
                tile['active'] = self.default_activity
                if not 'trap' in tile['type']:
                    self.tiles.append(tile)
            else:
                tile['active'] = self.default_activity

            if 'Wall' in tile['type']:
                return False
            if tile['light'] <= 0:
                return False
            
        return True

    def Ray_Caster(self):
        # Basic raycasting attributes
        num_lines = 20 # Define the number of lines and the spread angle (in degrees)
        spread_angle = 120  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1) # Calculate the angle increment between each line
        # Calculate the starting angle
        base_angle = math.atan2(self.game.player.direction_y_holder, self.game.player.direction_x_holder)
        start_angle = base_angle - math.radians(spread_angle / 2)
        
        # Check the tile the player is standing on
        self.Check_Tile(self.game.player.pos)
        self.Check_Trap(self.game.player.pos)
        self.Check_Enemy(self.game.player.pos)
        self.Check_Chest(self.game.player.pos)
        self.Check_Decoration(self.game.player.pos)

        # Find nearby Enemies
        if not self.nearby_cooldown:
            self.game.player.nearby_enemies.clear()
            self.game.player.Nearby_Enemies(200)
            self.game.player.Find_Nearby_Chests(200)
            self.nearby_cooldown = 20
        else:
            self.nearby_cooldown -= 1

        # Look for tiles that hit the rays
        for j in range(num_lines):
            for i in range(1, 13):
                angle = start_angle + j * math.radians(angle_increment)
                pos_x = self.game.player.pos[0] + math.cos(angle) * 16 * i
                pos_y = self.game.player.pos[1] + math.sin(angle) * 16 * i

        
                if not self.Check_Tile((pos_x, pos_y)):
                    break
                
                
                self.Check_Trap((pos_x, pos_y))
                self.Check_Enemy((pos_x, pos_y))
                self.Check_Chest((pos_x, pos_y))
                self.Check_Decoration((pos_x, pos_y))


                

                
                
                

                        
                # pygame.draw.line(surf, (255, 255, 255), (self.game.player.pos[0] - offset[0], self.game.player.pos[1] - offset[1]), (pos_x, pos_y), 1)
        
        # print(self.game.player.nearby_enemies)

    def rect(self, pos):
        return pygame.Rect(pos[0], pos[1], 10, 10)