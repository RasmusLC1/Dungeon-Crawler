from scripts.items.runes.projectile_rune import Projectile_Rune
from scripts.items.weapons.magic_attacks.electric.electric_ball import Electric_Ball
import math
import pygame

class Electric_Ball_Rune(Projectile_Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'electric_ball_rune', pos, 1, 25)
        self.animation_time_max = 30
        self.animation_size_max = 15


    def Generate_Projectile(self):
        electric_ball = Electric_Ball(self.game, self.game.player.pos, self.game.player, self.current_power, 2, 100, self.game.player.attack_direction)
        self.game.item_handler.Add_Item(electric_ball)
        self.charge = 0
        return
