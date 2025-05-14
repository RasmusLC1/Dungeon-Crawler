from scripts.traps.trap import Trap
from scripts.engine.assets.keys import keys

import random

class Poison_Plume(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.animation = 0

    def Update(self, entity):

        if entity.category == 'item':
            return

        if self.rect().colliderect(entity.rect()) and self.Cooldown == 0 and self.animation > 3:
            if entity.effects.invulnerable.effect:
                return
            entity.Damage_Taken(2)
            # entity.Set_Effect('slow_down', 4)
            

    def Animation_Update(self):
        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 5:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(20, 30)