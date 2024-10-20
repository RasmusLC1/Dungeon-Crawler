from scripts.decoration.decoration import Decoration
import random

class Shrine(Decoration):
    def __init__(self, game, type, pos, size) -> None:
        super().__init__(game, type, 'shrine', pos, size)
        self.is_open = False
        self.attack_animation_num = 0
        self.attack_animation_num_max = 0
        self.attack_animation_num_cooldown = 0
        self.attack_animation_num_cooldown_max = 50

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['is_open'] = self.is_open

    def Load_Data(self, data):
        super().Load_Data(data)
        self.is_open = data['is_open']

    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = self.animation_speed
            self.animation = random.randint(0,self.max_animation)

    def Open(self, generate_clatter = False):
        print("TEST")

