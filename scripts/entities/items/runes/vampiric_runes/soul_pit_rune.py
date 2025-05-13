from scripts.entities.items.runes.projectile_rune import Projectile_Rune
from scripts.entities.items.weapons.magic_attacks.vampiric.vampiric_ball import Vampiric_Ball
import math
import pygame

class Soul_Pit_Rune(Projectile_Rune):
    def __init__(self, game, pos):
        super().__init__(game, game.keys.soul_pit_rune, pos, 2, 30)
        self.animation_time_max = 30
        self.animation_size_max = 15



    def Generate_Projectile(self):
        vampiric_ball = Vampiric_Ball(self.game, self.game.player.pos, self.game.player, self.current_power, 2, 100, self.game.player.attack_direction)
        self.game.item_handler.Add_Item(vampiric_ball)
        self.charge = 0
        return

