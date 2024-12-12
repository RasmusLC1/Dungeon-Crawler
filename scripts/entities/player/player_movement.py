import pygame
import random
import math
from scripts.engine.particles.particle import Particle


class Player_Movement():
    def __init__(self, game, player) -> None:
        self.game = game
        self.player = player
        self.dashing = 0
        self.back_step = 0
        self.roll_forward = 0
        self.stamina = 0

    
    def Update(self):
        self.Update_Stamina()
        self.Dashing_Update()
        self.Back_Step_Update()
        self.Roll_Forward_Update()
        self.Check_Keyboard_input()

    def Update_Stamina(self):
        if self.stamina <= 0:
            return
        self.stamina = max(0, self.stamina - 1)

    def Set_Stamina(self, value):
        self.stamina = value

    def Check_Keyboard_input(self):
        keyboard = self.game.keyboard_handler
        if keyboard.space_pressed:
            self.Roll_Forward(self.game.render_scroll)
        elif keyboard.alt_pressed:
            self.Back_Step(self.game.render_scroll)

    def Back_Step(self,  offset=(0, 0)):
        if self.back_step or self.stamina:
            return
        self.player.Attack_Direction_Handler(offset)
        # Inverse attack Direction
        self.player.attack_direction = pygame.math.Vector2(self.player.attack_direction[0] * -1, self.player.attack_direction[1] * -1)
        self.back_step = 20
        self.Set_Stamina(60)

    def Back_Step_Update(self):
        if not self.back_step:
            return
        
        self.player.effects.Set_Effect("player_movement_invunerable", 1)
        self.back_step = max(0, self.back_step - 1)
        if self.back_step < 15:
            return
        
        if self.player.attack_direction.length() > 0:

            self.player.friction = 0
            self.player.max_speed = 40  # Adjust max speed speed for dashing distance


            # Set the velocity directly based on dash without friction interference
            self.player.velocity[0] = self.player.attack_direction[0] * 20
            self.player.velocity[1] = self.player.attack_direction[1] * 20

    def Roll_Forward(self,  offset=(0, 0)):
        if self.roll_forward or self.stamina:
            return
        self.player.Attack_Direction_Handler(offset)
        self.roll_forward = 30
        self.Set_Stamina(120)

    def Roll_Forward_Update(self):
        if not self.roll_forward:
            return
        
        self.player.effects.Set_Effect("player_movement_invunerable", 1)
        self.roll_forward = max(0, self.roll_forward - 1)
        if self.roll_forward < 20:
            return
        
        if self.player.attack_direction.length() > 0:

            self.player.friction = 0
            self.player.max_speed = 40  # Adjust max speed speed for dashing distance


            # Set the velocity directly based on dash without friction interference
            self.player.velocity[0] = self.player.attack_direction[0] * 20
            self.player.velocity[1] = self.player.attack_direction[1] * 20

    def Dashing_Update(self, offset=(0, 0)):
        if not self.dashing:
            return
            
        self.player.effects.Set_Effect("player_movement_invunerable", 1)


        if abs(self.dashing) in {60, 50}:
            for i in range(20):
                angle = random.random() * math.pi * 2
                speed = random.random() * 0.5 + 0.5
                pvelocity = [math.cos(angle) * speed, math.sin(angle) * speed]
                self.game.particles.append(Particle(self.game, 'particle', self.player.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

        if self.dashing > 0:
            self.dashing = max(0, self.dashing - 1)


        if self.dashing > 50:
            
            if self.player.attack_direction.length() > 0:
                # Temporarily set friction to zero to avoid deceleration during dash
                self.player.friction = 0
                self.player.max_speed = 40  # Adjust max speed speed for dashing distance


                # Set the velocity directly based on dash without friction interference
                self.player.velocity[0] = self.player.attack_direction[0] * self.dashing
                self.player.velocity[1] = self.player.attack_direction[1] * self.dashing

                if abs(self.dashing) == 51:
                    self.player.velocity[0] *= 0.1
                    self.player.velocity[1] *= 0.1

                pvelocity = [abs(self.dashing) / self.dashing * random.random() * 3, 0]
                self.game.particles.append(Particle(self.game, 'particle', self.player.rect().center, velocity=pvelocity, frame=random.randint(0, 7)))

    def Dash(self, offset=(0, 0)):
        if not self.dashing:
            self.player.Attack_Direction_Handler(offset)
            self.dashing = 60
            return True
        
        return False