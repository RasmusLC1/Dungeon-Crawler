from scripts.items.runes.rune import Rune
import math
import pygame

class Dash_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'dash_rune', pos, 10, 10)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.clicked = False


    def Activate(self):
        if not super().Activate():
            return    
        self.clicked = True
    
    def Update(self):
        super().Update()
        if not self.clicked:
            return
        if self.game.mouse.left_click:
            if not self.game.player.movement_handler.Dash(self.game.render_scroll):
                return
            self.Compute_Souls_Cost()
            self.clicked = False
        
        if self.game.mouse.right_click:
            self.clicked = False

    
    def Render_Animation(self, surf, offset=(0, 0)):
        if not self.clicked:
            return
        
        temp_surf = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
        # Draw a line on the temporary surface
        player_pos = (self.game.player.pos[0] - offset[0], self.game.player.pos[1] - offset[1])
        mouse_pos = (self.game.mouse.player_mouse[0] - offset[0], self.game.mouse.player_mouse[1] - offset[1])

        distance =  math.sqrt((player_pos[0] - mouse_pos[0]) ** 2 + (player_pos[1] - mouse_pos[1]) ** 2)
        alpha = 160
        if distance > 100:
            alpha = 50

        light_grey = (211,211,211, alpha)

        pygame.draw.line(temp_surf, light_grey, player_pos, mouse_pos, 2) 

        surf.blit(temp_surf, (0, 0))
