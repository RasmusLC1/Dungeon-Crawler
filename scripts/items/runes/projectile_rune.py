from scripts.items.runes.rune import Rune
from scripts.items.weapons.magic_attacks.ice.ice_ball import Ice_Ball
import math
import pygame

class Projectile_Rune(Rune):
    def __init__(self, game, type, pos, power, soul_cost):
        super().__init__(game, type, pos, power, soul_cost)
        self.effect = None
        self.charge = 0
        self.shoot_cooldown = 0

    
    def Activate(self):
        if not super().Activate():
            return    
        self.clicked = True
    
    def Update_Shoot_Cooldown(self):
        if self.shoot_cooldown:
            self.shoot_cooldown -= 1

    def Set_Shoot_Cooldown(self, value = 60):
        self.shoot_cooldown = value

    def Update(self):
        super().Update()

        self.Update_Shoot_Cooldown()

        if not self.clicked:
            return 
        
        self.Handle_Shooting()
        if self.game.mouse.right_click:
            self.clicked = False
        
        return

    def Handle_Shooting(self):
        if not self.game.mouse.left_click or self.shoot_cooldown:
            return
        
        # Handle intial setup
        if not self.charge:
            self.Set_Charge()
            self.Set_Shoot_Cooldown()
            self.Compute_Souls_Cost()
        
        # Handle shooting
        if self.charge:
            self.game.player.Attack_Direction_Handler(self.game.render_scroll)
            self.Generate_Projectile()
            return
        

    def Set_Charge(self):
        self.charge = 1

    def Generate_Projectile(self):
        pass

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

    