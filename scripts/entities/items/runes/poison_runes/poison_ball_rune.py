from scripts.entities.items.runes.projectile_rune import Projectile_Rune
from scripts.entities.items.weapons.magic_attacks.poison.poison_ball import Poison_Ball
import math
import pygame

class Poison_Ball_Rune(Projectile_Rune):
    def __init__(self, game, pos):
        super().__init__(game, game.keys.poison_ball_rune, pos, 1, 20)
        self.animation_time_max = 30
        self.animation_size_max = 15



    def Generate_Projectile(self):
        poison_ball = Poison_Ball(self.game, self.game.player.pos, self.game.player, self.current_power, 2, 100, self.game.player.attack_direction)
        self.game.item_handler.Add_Item(poison_ball)
        self.charge = 0
        return

