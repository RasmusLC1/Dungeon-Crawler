from scripts.entities.player.items.weapons.weapon import Weapon
import random


class Torch(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 3, 2)
        self.max_animation = 7
        self.aniamtion = random.randint(0, self.max_animation)


        self.light_level = 10
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)