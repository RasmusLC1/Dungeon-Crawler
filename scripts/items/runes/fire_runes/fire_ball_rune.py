from scripts.items.runes.rune import Rune
from scripts.items.weapons.projectiles.magic_attacks.fire_ball import Fire_Ball
import math
import pygame

class Fire_Ball_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'fire_ball_rune', pos, 4, 20)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.clicked = False
        self.effect = None


    def Activate(self):
        if not super().Activate():
            return    
        self.clicked = True
    
    def Update(self):
        super().Update()
        if not self.clicked:
            return
        if self.game.mouse.left_click:
            self.game.player.Attack_Direction_Handler(self.game.render_scroll)
            self.Generate_Fire_Ball()
            self.Compute_Souls_Cost()
            self.clicked = False
        
        if self.game.mouse.right_click:
            self.clicked = False

    def Generate_Fire_Ball(self):
        fire_ball = Fire_Ball(self.game, self.game.player.pos, self.game.player, self.current_power, 2, 100, self.game.player.attack_direction)
        self.game.item_handler.Add_Item(fire_ball)
        return

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

    