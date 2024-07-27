from scripts.lights.lights import Light

class Light_Handler():
    def __init__(self, game):
        self.game = game
        self.lights = []

    def Update(self):
        for light in self.lights:
            light.Update()
    
    def Add_Light(self, pos, light_level):
        self.lights.append(Light(self.game, pos, light_level))

    def Initialise_Light_Level(self, pos):
        # Set the light level based on the tile that the entity is placed on
        light_level = min(255, self.game.tilemap.Current_Tile(pos)['light'] * 25)

        light_level = abs(light_level - 255)
        light_level = max(50, 255 - light_level)

        return light_level