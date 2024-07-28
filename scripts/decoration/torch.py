from scripts.decoration.decoration import Decoration
import random


class Torch(Decoration):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.max_animation = 7
        self.aniamtion = random.randint(0, self.max_animation)


        self.light_level = 10
        self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)