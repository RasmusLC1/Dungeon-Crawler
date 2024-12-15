from scripts.items.weapons.magic_attacks.base_attacks.elemental_ball import Elemental_Ball
from scripts.items.weapons.magic_attacks.ice.ice_explosion import Ice_Explosion
import pygame

class Ice_Ball(Elemental_Ball):
    def __init__(self, game, pos, entity, damage, speed, special_attack, direction):
        super().__init__(game, pos, entity, 'ice_ball', damage, speed, 2, 'frozen', 200, special_attack, direction)
        


    def Reset_Shot(self):
        fire_explosion = Ice_Explosion(self.game, self.pos, self.damage)
        self.game.item_handler.Add_Item(fire_explosion)
        return super().Reset_Shot()

    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        weapon_image = pygame.transform.rotate(weapon_image, self.rotate)


        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
