from scripts.traps.trap import Trap

import random


class Spike_Poisoned(Trap):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)
        self.animation = random.randint(0, 13)

    def Update(self):
        if self.Cooldown > 0:
            self.Cooldown -= 1

        if self.rect().colliderect(self.game.player.rect()) and self.Cooldown == 0 and self.animation > 8 and self.animation < 12 and not self.game.player.dashing:
            if not self.game.player.dashing:
                self.game.player.Damage_Taken(2)
                self.game.player.Set_Poisoned(3)
                self.Cooldown = 100

        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 13:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(10, 20)