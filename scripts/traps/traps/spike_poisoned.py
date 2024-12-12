from scripts.traps.trap import Trap

import random


class Spike_Poisoned(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.animation = random.randint(0, 13)

    def Update(self, entity):
        if entity.category == 'item':
            return
        
        if self.rect().colliderect(entity.rect()) and self.Cooldown == 0 and self.animation > 8 and self.animation < 12:
            if entity.effects.invulnerable.effect:
                return
            entity.Damage_Taken(2)
            entity.Set_Effect('poison', random.randint(3,5))

    def Animation_Update(self):
        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 13:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(10, 20)
