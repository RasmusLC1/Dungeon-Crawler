from scripts.entities.items.weapons.magic_attacks.base_attacks.elemental_ball import Elemental_Ball
from scripts.entities.items.weapons.magic_attacks.ice.ice_explosion import Ice_Explosion
import pygame

class Ice_Ball(Elemental_Ball):
    def __init__(self, game, pos, entity, damage, speed, special_attack, direction):
        super().__init__(game, pos, entity, game.keys.ice_ball, damage, speed, 2, game.keys.frozen, 200, special_attack, direction)
        


    def Reset_Shot(self):
        fire_explosion = Ice_Explosion(self.game, self.pos, self.damage)
        self.game.item_handler.Add_Item(fire_explosion)
        return super().Reset_Shot()

