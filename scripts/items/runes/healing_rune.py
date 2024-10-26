from scripts.items.runes.rune import Rune

import pygame

class Healing_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'healing_rune', pos, 10, 30)
        self.animation_time_max = 30
        self.effect = 'health'
        self.animation_size_max = 15

    def Render_Animation(self, surf, offset=(0, 0)):
        if not self.animation_time:
            return
        
        temp_surf = pygame.Surface((self.animation_size*2, self.animation_size*2), pygame.SRCALPHA)
    
        # Draw the circle on the temporary surface
        alpha = 60
        pygame.draw.circle(temp_surf, (255, 0, 0, alpha), (self.animation_size, self.animation_size), self.animation_size)
        
        # Blit the temporary surface onto the main surface at the correct position
        surf.blit(temp_surf, (self.game.player.pos[0] - offset[0] + 8 - self.animation_size, self.game.player.pos[1] - offset[1] - self.animation_size))

