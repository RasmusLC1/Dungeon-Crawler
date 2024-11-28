from scripts.items.weapons.weapon import Weapon
from scripts.items.weapons.projectiles.fire_particle import Fire_Particle
import math
import pygame


class Battle_Axe(Weapon):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'battle_axe', 1, 2, 3, 'two_handed_melee')
        self.max_animation = 5
        self.attack_animation_max = 5
        self.special_attack_animation_max = 8
        self.spin_index = 0
        self.spin_countdown = 0
        self.max_special_attack = 32
        self.spin_attack_directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]



    def Special_Attack(self):
        if self.special_attack <= 0 or not self.equipped:
            self.Reset_Special_Attack()
            self.Reset_Attack_Effect_Animation()
            self.attack_type = 'cut'
            self.spin_countdown = 0
            return
        
        if not self.spin_countdown:
            self.spin_index = min(self.spin_index + 1, 3)

        self.entity.Set_Attack_Direction(self.spin_attack_directions[self.spin_index])
        self.Set_Attack_Hitbox()
        self.spin_countdown -= 1
        self.rotate += 10

        self.special_attack -= 1

        self.Spin_Attack_Effect()

    def Set_Special_Attack(self, offset=...):
        self.attack_type = 'spin'
        super().Set_Special_Attack(offset)
        self.Set_Special_Attack_Effect_Animation_Time()
    


    def Spin_Attack_Effect(self):
        self.Update_Special_Attack_Effect_Animation()
        effect_type = self.effect + '_' + self.attack_type + '_effect'
        attack_effect = self.game.assets[effect_type][self.attack_effect_animation]
        pos_x = self.entity.pos[0] - self.game.render_scroll[0] - 10
        pos_y = self.entity.pos[1] - self.game.render_scroll[1] - 10
        self.game.display.blit(attack_effect, (pos_x, pos_y))

