from scripts.entities.items.runes.rune import Rune
import math
import pygame

class Hunger_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'hunger_rune', pos, 1, 0)
        self.animation_time_max = 30
        self.animation_size_max = 15

    def Update(self):
        if not self.game.player.effects.hunger.effect:
            self.game.player.Set_Effect(self.effect, self.current_power)
        return super().Update()        

    def Remove_Rune_From_Inventory(self):
        self.game.player.effects.Remove_Effect(self.effect)

    def Activate(self):
        pass
    
    def Render_Animation(self, surf, offset):
        pass