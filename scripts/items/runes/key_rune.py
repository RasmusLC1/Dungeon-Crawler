from scripts.items.runes.rune import Rune

import pygame

class Key_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'key_rune', pos, 1, 20)
        self.animation_time_max = 5
        self.effect = 'key'
        self.animation_size_max = 10


    def Activate(self):
        if not super().Activate():
            return
        nearby_doors = self.game.decoration_handler.Find_Nearby_Decorations(self.game.player.pos, 50)
        if not nearby_doors:
            return

        if not self.game.decoration_handler.Open_Door_Without_Key(nearby_doors):
            return
        
        self.game.player.Decrease_Souls(self.current_soul_cost)
        self.Set_Animation_Time()
        self.Reset_Animation_Size()
        return


    def Render_Animation(self, surf, offset=(0, 0)):
        pass