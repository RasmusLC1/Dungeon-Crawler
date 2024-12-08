from scripts.entities.effects.effect import Effect
import pygame
import random


class Fire(Effect):
    def __init__(self, entity):
        super().__init__(entity, 7, 20)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        # if self.wet or self.fire_resistance:
        #     return False
        # if self.frozen:
        #     self.Remove_Frozen()
        self.effect = max(random.randint(effect_time, effect_time * 2), self.effect)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        # self.entity.status_effects.active_effects

        # if self.fire_resistance or self.wet:
        #     self.effect = 0
        #     self.cooldown = 0
        #     return False
        
        if self.cooldown:
            self.cooldown -= 1
        elif self.effect:
            damage = random.randint(1, 3)
            self.entity.Damage_Taken(damage)
            self.effect -= 1
            self.cooldown = random.randint(30, 50)
            return True
        # self.Effect_Animation('fire_animation_cooldown', 'fire_animation', self.animation_max, self.animation_cooldown_max)
        return False
   
    