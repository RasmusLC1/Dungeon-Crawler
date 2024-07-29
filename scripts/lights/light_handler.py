from scripts.lights.lights import Light

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