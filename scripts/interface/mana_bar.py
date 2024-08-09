import pygame

class Mana_Bar:
    def __init__(self):
        pass

    def normalize_health(current_health, max_health, bar_length):
        # Calculate the normalization factor
        normalization_factor = bar_length / max_health
        
        # Calculate the normalized health
        normalized_health = current_health * normalization_factor
        
        return normalized_health
    
    def Mana_Bar(self):
        bar_length=80
        rect_x = self.screen_width / self.render_scale - bar_length - 20
        rect_y = self.screen_height / self.render_scale - 10
        normalised_cooldown = Mana_Bar.normalize_health(self.player.mana, self.player.max_mana, bar_length)
        rect_height = 5
        # Ensure the font is loaded correctly
        try:
            font = pygame.font.Font('freesansbold.ttf', 10)
        except Exception as e:
            print(f"Font load error: {e}")
            font = pygame.font.SysFont('freesans', 10)  # Fallback font
        
        text = font.render(str(self.player.mana) + '/' + str(self.player.max_mana), True, (255, 255, 255))
        
        # Use self.display consistently if it's the initialized display surface
        self.display.blit(text, (rect_x, rect_y - 10))
        # Use self.display consistently if it's the initialized display surface
        pygame.draw.rect(self.display, (0, 0, 255), (rect_x, rect_y, normalised_cooldown, rect_height))
        pygame.draw.rect(self.display, (255, 0, 0), (rect_x + normalised_cooldown, rect_y, bar_length-normalised_cooldown, rect_height))
