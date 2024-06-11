import pygame

class Coins:
    def __init__(self):
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

    def Render(self):
        rect_x = self.screen_width / self.render_scale - 40
        rect_y = 20
        rect_height = 5
        # Ensure the font is loaded correctly
        try:
            font = pygame.font.Font('freesansbold.ttf', 10)
        except Exception as e:
            print(f"Font load error: {e}")
            font = pygame.font.SysFont('freesans', 10)  # Fallback font

        text = font.render(str(self.player.coins), True, (255, 255, 255))
        
        # Use self.display consistently if it's the initialized display surface
        self.display.blit(text, (rect_x, rect_y))
        scaled_coin_image = pygame.transform.scale(self.assets['coin'][self.animation], (8, 8))
        self.display.blit(scaled_coin_image, (rect_x + 20, rect_y))