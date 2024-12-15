from scripts.items.weapons.magic_attacks.base_attacks.elemental_explosion import Elemental_Explosion
import pygame
import math

class Ice_Explosion(Elemental_Explosion):
    def __init__(self, game, pos, power, entity = None):
        super().__init__(game, 'ice_explosion', 'frozen', pos, power, 7, 5, entity)

    def Slow_Down_Entities(self):
        for entity in self.nearby_entities:
            entity.effects.Set_Effect("slow_down", self.power)

    def Update_Animation(self):
        self.Slow_Down_Entities()

        return super().Update_Animation()