import math
import pygame

class Ray_Caster():
    def __init__(self, game):
        self.tiles = []
        self.enemies = []
        self.traps = []
        self.chests = []
        self.doors = []
        self.items = []
        self.decorations = []
        self.torhces = []

        self.nearby_enemies = []
        self.nearby_traps = []
        self.nearby_torches = []
        # self.nearby_chest = []
        # self.nearby_doors = []
        self.nearby_decorations = []
        self.nearby_items = []
        
        self.nearby_cooldown = 0
        self.inactive_distance = 300
        
        self.game = game
        self.default_activity = 700

    def Update(self, game):
        
        self.Check_Tile_Active(game)

        self.Check_Enemy_Active(game)

        self.Check_Decoration_Active(game)

        self.Check_Trap_Active(game)
    
    # Handle tile activity degradation
    def Check_Tile_Active(self, game):
        for tile in self.tiles:
            if tile['active']:
                tile['active'] -= 1
            # Find distance from player and if it's greater than 300, delete it
            distance = math.sqrt((game.player.pos[0] - tile['pos'][0] * 16) ** 2 + (game.player.pos[1] - tile['pos'][1] * 16) ** 2)
            if abs(distance) > self.inactive_distance:
                tile['active'] = 0
                self.tiles.remove(tile)
            
    def Check_Trap_Active(self, game):
        for trap in self.traps:
            if trap.active:
                trap.Reduce_Active()
            else:
                self.traps.remove(trap)
                return
            
            distance = math.sqrt((game.player.pos[0] - trap.pos[0]) ** 2 + (game.player.pos[1] - trap.pos[0]) ** 2)
            if abs(distance) > self.inactive_distance:
                trap.Set_Active(0)
                if trap in self.traps:
                    self.traps.remove(trap)
    
            
    def Check_Decoration_Active(self, game):
        for decoration in self.decorations:
            if decoration.active:
                decoration.Reduce_Active()
            else:
                self.decorations.remove(decoration)
                return
            distance = abs(math.sqrt((game.player.pos[0] - decoration.pos[0]) ** 2 + (game.player.pos[1] - decoration.pos[1]) ** 2))
            if abs(distance) > self.inactive_distance:
                decoration.Set_Active(0)
                if decoration in self.decorations:
                    self.decorations.remove(decoration)
            if decoration.type != 'chest':
                return
            
            if decoration.empty:
                if decoration in self.decorations:
                    self.decorations.remove(decoration)
                return

    def Check_Enemy_Active(self, game):
        for enemy in self.enemies:
            if enemy.active:
                enemy.Reduce_Active()
            else:
                if enemy in self.enemies:
                    self.enemies.remove(enemy)
            distance = math.sqrt((game.player.pos[0] - enemy.pos[0]) ** 2 + (game.player.pos[1] - enemy.pos[1]) ** 2)
            if abs(distance) > self.inactive_distance:
                enemy.Set_Active(0)
                if enemy in self.enemies:
                    self.enemies.remove(enemy)

    def Check_Trap(self, pos):
        for trap in self.game.trap_handler.nearby_traps:
            if self.rect(pos).colliderect(trap.rect()):
                if not trap.active:
                    trap.Set_Active(self.default_activity)
                    self.traps.append(trap)
                else:
                    trap.Set_Active(self.default_activity)   

    def Check_Enemy(self, pos):
        for enemy in self.nearby_enemies:
            # Check if enemy is already in the enemy list
            if self.rect(pos).colliderect(enemy.rect()):
                if not enemy.active:
                    enemy.Set_Active(300)
                    self.enemies.append(enemy)
                else:
                    enemy.Set_Active(300)



    def Check_Item(self, pos):
        for item in self.nearby_items:
            if self.rect(pos).colliderect(item.rect()):
                if not item.active:
                    item.Set_Active(self.default_activity)
                    self.items.append(item)
                else:
                    item.Set_Active(self.default_activity)

    def Check_Decoration(self, pos):
        for decoration in self.nearby_decorations:
            if self.rect(pos).colliderect(decoration.rect()):
                if not decoration.active:
                    decoration.Set_Active(self.default_activity)
                    self.decorations.append(decoration)
                else:
                    decoration.Set_Active(self.default_activity)

    def Check_Items(self, pos):
        for item in self.game.item_handler.nearby_items:
            if self.rect(pos).colliderect(item.rect()):

                if not item.active:
                    item.Set_Active(self.default_activity)
                    self.items.append(item)
                else:
                    item.Set_Active(self.default_activity)

    def Check_Tile(self, pos):
        tile = self.game.tilemap.Current_Tile(pos)
        if tile:
            if not tile['active']:
                tile['active'] = self.default_activity
                self.tiles.append(tile)
            else:
                tile['active'] = self.default_activity

            if 'Wall' in tile['type']:
                return False
            
            if 'Door' in tile['type']:
                return False
            
            
        return True
    
    # Check for entities near to the player
    def Find_Nearby_Entities(self):
        if self.nearby_cooldown:
            self.nearby_cooldown = max(0, self.nearby_cooldown - 1)
            return
        
        # Clear the lists before assigning new values to them
        self.nearby_enemies.clear()
        self.nearby_decorations.clear()
        self.nearby_items.clear()
        # self.nearby_chest.clear()
        # self.nearby_doors.clear()

        # Assign new nerby lists
        player = self.game.player
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(player, 200)
        # self.nearby_chest = self.game.chest_handler.Find_Nearby_Chests(player.pos, 200)
        # self.nearby_doors = self.game.door_handler.Find_Nearby_Doors(player.pos, 200)
        self.nearby_decorations = self.game.decoration_handler.Find_Nearby_Decorations(player.pos, 200)
        self.nearby_cooldown = 20
        return
    
    # Check the tile the player is standing on
    def Check_For_Objects(self, pos):
        if not self.Check_Tile(pos):
            return False
        self.Check_Trap(pos)
        self.Check_Enemy(pos)
        self.Check_Decoration(pos)
        self.Check_Items(pos)
        return True

    def Ray_Caster(self):
        # Basic raycasting attributes
        num_lines = 20 # Define the number of lines and the spread angle (in degrees)
        spread_angle = 120  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1) # Calculate the angle increment between each line
        # Calculate the starting angle
        base_angle = math.atan2(self.game.player.view_direction[1], self.game.player.view_direction[0])
        start_angle = base_angle - math.radians(spread_angle / 2)
        self.Check_For_Objects(self.game.player.pos)
        self.Find_Nearby_Entities()
        

        # Look for tiles that hit the rays
        for j in range(num_lines):
            for i in range(1, 13):
                angle = start_angle + j * math.radians(angle_increment)
                pos_x = self.game.player.pos[0] + math.cos(angle) * 16 * i
                pos_y = self.game.player.pos[1] + math.sin(angle) * 16 * i

                if not self.Check_For_Objects((pos_x, pos_y)):
                    break

                # pygame.draw.line(surf, (255, 255, 255), (self.game.player.pos[0] - offset[0], self.game.player.pos[1] - offset[1]), (pos_x, pos_y), 1)
    
    def Remove_Trap(self, trap):
        if trap in self.traps:  
            self.traps.remove(trap)

    def Remove_Chest(self, chest):
        if chest in self.chests:
            self.chests.remove(chest)

    def rect(self, pos):
        return pygame.Rect(pos[0], pos[1], 10, 10)