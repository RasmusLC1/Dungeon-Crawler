from scripts.engine.lights.lights import Light
import math

class Light_Handler():
    def __init__(self, game):
        self.game = game
        self.lights = []

    def Update(self):
        for light in self.lights:
            light.Update()
    
    # Creates a lightsource
    def Add_Light(self, pos, light_level):
        light = Light(self.game, pos, light_level)
        self.lights.append(light)
        return light
    
    def Find_Nearby_Lights(self, center_pos, max_distance):
        def distance_from_center(light, center_pos):
            pos = light.pos
            return math.sqrt((pos[0] - center_pos[0]) ** 2 + (pos[1] - center_pos[1]) ** 2)
        
        nearby_lights = []
        for light in self.lights:
            if light.picked_up:
                continue
            # Calculate the Euclidean distance
            distance = math.sqrt((center_pos[0] - light.pos[0]) ** 2 + (center_pos[1] - light.pos[1]) ** 2)
            if distance < max_distance:
                nearby_lights.append(light)
        
        # Sort the lights based on their distance from the center position in descending order
        nearby_lights = sorted(nearby_lights, key=lambda light: distance_from_center(light, center_pos), reverse=True)
        
        return nearby_lights
    
    def Move_Light(self, pos, light_source):

        # Move the light to the new position
        light_source.pos_holder = light_source.pos
        light_source.pos = pos

        # Recalculate the light at the new position
        light_source.Setup_Tile_Light()

        # Update all nearby lights after moving
        nearby_lights = self.Find_Nearby_Lights(light_source.pos, 100)
        for light in nearby_lights:
            light.Setup_Tile_Light()  # Recalculate the light for the nearby light sources

        

    def Remove_Light(self, light_source):
        light_source.Delete_Light()

        # Update all nearby lights after moving
        nearby_lights = self.Find_Nearby_Lights(light_source.pos_holder, 100)
        for light in nearby_lights:
            light.Delete_Light()  # Recalculate the light for the nearby light sources

        

    def Restore_Light(self, light_source):
        nearby_lights = self.Find_Nearby_Lights(light_source.pos_holder, 100)

        for light in nearby_lights:
            light.Setup_Tile_Light()  # Recalculate the light for the nearby light sources




    # Set the lightlevel of an object based on the tile it is on
    def Initialise_Light_Level(self, pos):

        # Set the light level based on the tile that the entity is placed on
        tile = self.game.tilemap.Current_Tile(pos)
        if not tile:
            return
        light_level = min(255, tile['light'] * 25)

        light_level = abs(light_level - 255)
        light_level = max(50, 255 - light_level)

        return light_level