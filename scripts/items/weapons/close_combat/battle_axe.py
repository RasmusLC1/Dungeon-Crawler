from scripts.items.weapons.weapon import Weapon
from scripts.items.weapons.projectiles.fire_particle import Fire_Particle
import math
import pygame


class Battle_Axe(Weapon):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'battle_axe', 1, 2, 3, 'two_handed_melee')
        self.max_animation = 5
        self.attack_animation_max = 5
        self.spin_countdown = 0
        self.spin_index = 0
        self.spin_attack_directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]



    def Special_Attack(self):
        if self.special_attack <= 0 or not self.equipped:
            self.Reset_Special_Attack()
            return
        
        if not self.spin_countdown:
            self.spin_index = min(self.spin_index + 1, 3)
            self.spin_countdown = self.special_attack // 4

        self.entity.Set_Attack_Direction(self.spin_attack_directions[self.spin_index])
        self.Set_Attack_Hitbox()
        self.spin_countdown -= 1
        self.rotate += 10

        self.special_attack -= 2 

        self.Spin_Attack_Effect()




    def Spin_Attack_Effect(self):
        pos = self.Attack_Effect_Position(self.game.render_scroll)
        effect_type = self.effect + '_' + self.attack_type + '_effect'
        attack_effect = self.game.assets[effect_type][self.attack_effect_animation]
        # attack_effect.set_alpha()
        attack_effect = pygame.transform.rotate(attack_effect, self.rotate)
        flip_x = False
        if self.entity.attack_direction[0] > 0 and abs(self.entity.attack_direction[0]) > abs(self.entity.attack_direction[1]):
            flip_x = True
        self.game.display.blit( pygame.transform.flip(attack_effect, flip_x, False), (pos[0], pos[1]))