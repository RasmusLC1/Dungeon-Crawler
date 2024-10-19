from scripts.items.runes.rune import Rune

import pygame

class Light_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'light_rune', pos, 7, 0)
        self.effect = 'light'

    def Update(self):
        if self.game.player.light_source.light_level < self.current_strength:
            self.game.player.Update_Light_Source(self.current_strength)

    def Remove_Rune_From_Inventory(self):
        self.game.player.Update_Light_Source(4)

    def Activate(self):
        pass
