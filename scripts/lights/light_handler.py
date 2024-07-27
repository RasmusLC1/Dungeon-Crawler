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