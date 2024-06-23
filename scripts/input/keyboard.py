import pygame

class Keyboard_Handler:
    def keyboard_Input(self, key_press, offset=(0, 0)):
        if key_press.type == pygame.KEYDOWN:
            if key_press.key == pygame.K_a:
                self.movement[0] = True
            if key_press.key == pygame.K_d:
                self.movement[1] = True
            if key_press.key == pygame.K_w:
                self.movement[2] = True
            if key_press.key == pygame.K_s:
                self.movement[3] = True
            if key_press.key == pygame.K_SPACE:
                self.player.Shooting(offset)
            if key_press.key == pygame.K_x:
                self.player.Dash(offset)
        if key_press.type == pygame.KEYUP:
            if key_press.key == pygame.K_a:
                self.movement[0] = False
            if key_press.key == pygame.K_d:
                self.movement[1] = False
            if key_press.key == pygame.K_w:
                self.movement[2] = False
            if key_press.key == pygame.K_s:
                self.movement[3] = False