import math
import pygame

class Ray_Caster():
    def __init__(self, game):
        self.entities = []
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
        self.nearby_decorations = []
        self.nearby_items = []
        
        self.nearby_cooldown = 0
        self.inactive_distance = 300
        
        self.game = game
        self.default_activity = 700

    def Update(self):
        
        self.Check_Tile_Active()

        self.Update_Entities()


    def Update_Entities(self):
        for tile in self.tiles:
            tile.Set_Entity_Active()
    
    # Handle tile activity degradation
    def Check_Tile_Active(self):
        for tile in self.tiles:
            if tile.active:
                tile.active -= 1
            # Find distance from player and if it's greater than 300, delete it
            distance = math.sqrt((self.game.player.pos[0] - tile.pos[0] * 16) ** 2 + (self.game.player.pos[1] - tile.pos[1] * 16) ** 2)
            if abs(distance) > self.inactive_distance:
                tile.active = 0
                self.tiles.remove(tile)


    def Check_Tile(self, pos):
        tile = self.game.tilemap.Current_Tile(pos)
        if tile:
            if not tile.active:
                tile.active = self.default_activity
                self.tiles.append(tile)
            else:
                tile.active = self.default_activity
            if not tile.type:
                print(tile)
                return False
            
            if 'Wall' in tile.type:
                return False
            
            if 'Door' in tile.type:
                return False
            
            
        return True

    def Ray_Caster(self):
        # Basic raycasting attributes
        num_lines = 20 # Define the number of lines and the spread angle (in degrees)
        spread_angle = 120  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1) # Calculate the angle increment between each line
        # Calculate the starting angle
        base_angle = math.atan2(self.game.player.view_direction[1], self.game.player.view_direction[0])
        start_angle = base_angle - math.radians(spread_angle / 2)
        self.Check_Tile(self.game.player.pos)
        

        # Look for tiles that hit the rays
        for j in range(num_lines):
            for i in range(1, 13):
                angle = start_angle + j * math.radians(angle_increment)
                pos_x = self.game.player.pos[0] + math.cos(angle) * 16 * i
                pos_y = self.game.player.pos[1] + math.sin(angle) * 16 * i
                if not self.Check_Tile((pos_x, pos_y)):
                    break
    
        

    def Remove_Trap(self, trap):
        if trap in self.traps:  
            self.traps.remove(trap)

    def Remove_Chest(self, chest):
        if chest in self.chests:
            self.chests.remove(chest)

    def rect(self, pos):
        return pygame.Rect(pos[0], pos[1], 10, 10)