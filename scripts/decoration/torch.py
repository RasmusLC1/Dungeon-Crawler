from scripts.decoration.decoration import Decoration
import random


class Torch(Decoration):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.light = 10
        self.light = self.game.light_handler.Initialise_Light_Level(self.pos)
        self.max_animation = 7
        self.aniamtion = random.randint(0, self.max_animation)