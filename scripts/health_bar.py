import pygame

class Health_Bar:
    def normalize_health(current_health, max_health, bar_length):
        # Calculate the normalization factor
        normalization_factor = bar_length / max_health
        
        # Calculate the normalized health
        normalized_health = current_health * normalization_factor
        
        return normalized_health
    
    def Health_Bar(self):
        bar_length=80
        # Define the color and rectangle dimensions
        green = (0, 255, 0)  # RGB color for green
        red = (255, 0, 0)  # RGB color for green
        rect_x = 20
        rect_y = self.screen_height / self.render_scale - 20
        normalised_health = Health_Bar.normalize_health(self.player.health, self.player.max_health, bar_length)
        rect_height = 5
        # Ensure the font is loaded correctly
        try:
            font = pygame.font.Font('freesansbold.ttf', 10)
        except Exception as e:
            print(f"Font load error: {e}")
            font = pygame.font.SysFont('freesans', 10)  # Fallback font

        text = font.render(str(self.player.health) + '/' + str(self.player.max_health), True, (255, 255, 255))
        
        # Use self.display consistently if it's the initialized display surface
        self.display.blit(text, (rect_x, rect_y - 10))
        pygame.draw.rect(self.display, green, (rect_x, rect_y, normalised_health, rect_height))
        pygame.draw.rect(self.display, red, (rect_x + normalised_health, rect_y, bar_length-normalised_health, rect_height))