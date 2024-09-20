import pygame
import math

class Souls:
    def __init__(self, game):
        self.game = game
        self.animation = 0
        self.cooldown = 0
        self.max_animation = 3

    def Update(self):
        if not self.cooldown:
            if self.animation >= self.max_animation:
                self.animation = 0
            else:
                self.animation += 1
            self.cooldown = 20

        self.cooldown -= 1

    def move_text_based_on_soul(self, soul_count, base_position_x):
        # Get the number of digits in the soul count
        num_digits = math.floor(math.log10(soul_count)) + 1 if soul_count > 0 else 1
        
        # Calculate the new position by moving 8 pixels left per extra digit
        new_position_x = base_position_x - (num_digits - 1) * 8
        
        return new_position_x


    def Render(self, surf):
        rect_x = self.game.screen_width / self.game.render_scale - 20
        rect_y = 20

        new_x = self.move_text_based_on_soul(self.game.player.souls, rect_x)


        # Render the text
        self.game.default_font.Render_Word(surf, str(self.game.player.souls), (new_x, rect_y))


        scaled_soul_image = pygame.transform.scale(self.game.assets['souls'][self.animation], (8, 8))
        surf.blit(scaled_soul_image, (rect_x + 10, rect_y))