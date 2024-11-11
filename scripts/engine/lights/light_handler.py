from scripts.engine.lights.lights import Light
from scripts.engine.utility.helper_functions import Helper_Functions
import math

class Light_Handler():
    def __init__(self, game) -> None:
        self.game = game
        self.lights = []
        self.nearby_light_cooldown = 0

    def Clear_Lights(self):
        self.lights.clear()
    
    # Creates a lightsource
    def Add_Light(self, pos, light_level, tile):
        light = Light(self.game, pos, light_level, tile)
        self.lights.append(light)
        return light
    
    def Add_Light_Source(self, light_source):
        self.lights.append(light_source)

    def distance_from_center(light, center_pos):
        pos = light.pos
        return math.sqrt((pos[0] - center_pos[0]) ** 2 + (pos[1] - center_pos[1]) ** 2)

        
    def Find_Nearby_Lights(self, pos, max_distance):
        nearby_lights = []
        for light in self.lights:
            # Calculate the Euclidean distance
            distance = Helper_Functions.Abs_Distance_Float(pos, light.pos)
            if distance < max_distance:
                nearby_lights.append(light)
        return nearby_lights

    
    def Move_Light(self, pos, light_source, tile):

        # Move the light to the new position
        light_source.pos_holder = light_source.pos
        light_source.tile = tile
        light_source.pos = pos

        # Recalculate the light at the new position
        light_source.Setup_Tile_Light()

        # Update all nearby lights after moving
        nearby_lights = self.Find_Nearby_Lights(light_source.pos, 100)
        for light in nearby_lights:
            light.Setup_Tile_Light()  # Recalculate the light for the nearby light sources

        

    def Remove_Light(self, light_source):
        # light_source.Delete_Light()
        # Update all nearby lights after moving
        nearby_lights = self.Find_Nearby_Lights(light_source.pos_holder, 200)
        for light in nearby_lights:
            light.Delete_Light()  # Recalculate the light for the nearby light sources
        
        if light_source in self.lights:
            self.lights.remove(light_source)

        

    def Restore_Light(self, light_source):
        nearby_lights = self.Find_Nearby_Lights(light_source.pos_holder, 200)

        for light in nearby_lights:
            light.Setup_Tile_Light()  # Recalculate the light for the nearby light sources

    # Set the lightlevel of an object based on the tile it is on
    def Initialise_Light_Level(self, tile):

        # Set the light level based on the tile that the entity is placed on
        tile = self.game.tilemap.Current_Tile(tile)
        if not tile:
            return
        light_level = min(255, tile.light_level * 25)

        light_level = abs(light_level - 255)
        light_level = max(50, 255 - light_level)

        return light_level