from scripts.items.weapons.magic_attacks.base_attacks.elemental_explosion import Elemental_Explosion
import pygame
import math

class Fire_Explosion(Elemental_Explosion):
    def __init__(self, game, pos, effect, entity = None):
        super().__init__(game, 'fire_explosion', pos, effect, entity)
        self.max_animation = 7
        self.animation_cooldown_max = 5
        self.light_source = self.game.light_handler.Add_Light(self.pos, 8, self.tile)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)
        self.Initialise_Explosion()


    def Update_Animation(self):
        if self.delete_countdown <= 1:
            self.game.light_handler.Remove_Light(self.light_source)
            
        
        super().Update_Animation()
