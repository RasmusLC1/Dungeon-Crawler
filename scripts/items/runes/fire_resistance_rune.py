from scripts.items.runes.rune import Rune

import pygame

class Fire_Resistance_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'fire_resistance_rune', pos, 5, 5)
        self.animation_time_max = 20
        self.effect = 'fire_resistance'
        self.animation_size_max = 25


        

    def Render_Animation(self, surf, offset=(0, 0)):
        if not self.animation_time:
            return
        inversed_animation_size = 20 - self.animation_size
        temp_surf = pygame.Surface((inversed_animation_size*2, inversed_animation_size*2), pygame.SRCALPHA)

    
        # Draw the circle on the temporary surface
        alpha = 60
        pygame.draw.circle(temp_surf, (255, 0, 0, alpha), (inversed_animation_size, inversed_animation_size), inversed_animation_size)
        
        # Blit the temporary surface onto the main surface at the correct position
        surf.blit(temp_surf, (self.game.player.pos[0] - offset[0] + 8 - inversed_animation_size, self.game.player.pos[1] - offset[1] - inversed_animation_size))

