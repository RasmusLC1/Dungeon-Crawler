from scripts.items.weapons.weapon import Weapon
from scripts.items.weapons.projectiles.fire_particle import Fire_Particle
import math
import pygame


# TODO: Add particle effect on hammer

class Warhammer(Weapon):
    def __init__(self, game, pos, damage_type = 'blunt'):
        super().__init__(game, pos, 'warhammer', 9, 2, 6, 'two_handed_melee', damage_type)
        self.max_animation = 5
        self.attack_animation_max = 5
        self.special_attack_effect_animation_max = 5
        self.max_special_attack = 32



    def Special_Attack(self):
        if not self.special_attack_active or not self.equipped:
            return
        
        if self.special_attack <= 0:
            self.Reset_Special_Attack()
            return
        
        self.special_attack -= 1
        self.Smash_Attack_Effect()


        if self.special_attack == self.max_special_attack // 2:
            damage_holder = self.damage
            self.damage = 1 # quarter damage on stun
            # Stun nearby enemies
            self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, 3)
            for enemy in self.nearby_enemies:
                enemy.Set_Effect('snare', self.max_special_attack * 2)
                self.Entity_Hit(enemy)

            self.damage = damage_holder # Reset Damage
        
    def Smash_Attack_Effect(self):
        self.Update_Special_Attack_Effect_Animation()
        effect_type = self.effect + '_' + self.attack_type + '_effect'
        attack_effect = self.game.assets[effect_type][self.attack_effect_animation]
        pos_x = self.entity.pos[0] - self.game.render_scroll[0] - 10
        pos_y = self.entity.pos[1] - self.game.render_scroll[1] - 10
        self.game.display.blit(attack_effect, (pos_x, pos_y))



    def Set_Special_Attack(self, offset=...):
        self.attack_type = 'smash'
        super().Set_Special_Attack(offset)
        self.Set_Special_Attack_Effect_Animation_Time()
    
    def Reset_Special_Attack(self):
        self.attack_type = 'cut'
        return super().Reset_Special_Attack()
