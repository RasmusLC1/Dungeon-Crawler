import pygame

class Ammo_Bar:
    def __init__(self):
        pass
    
    # TODO: REDO THIS CODE, normalising does not work
    def normalize_ammo(current_health, max_health, bar_length):
        # Calculate the normalization factor
        normalization_factor = bar_length / max_health
        
        # Calculate the normalized health
        normalized_health = current_health * normalization_factor
        
        # Clamp the value to ensure it doesn't exceed the bar length
        return min(max(normalized_health, 0), bar_length)

    
    def Attack_Recharge_Bar(self):
        bar_length = 80
        rect_x = self.screen_width / self.render_scale - bar_length - 20
        rect_y = self.screen_height / self.render_scale - 30
        normalised_cooldown = Ammo_Bar.normalize_ammo(self.player.left_weapon_cooldown, 20, bar_length)
        rect_height = 5
        # Ensure the font is loaded correctly
        try:
            font = pygame.font.Font('freesansbold.ttf', 10)
        except Exception as e:
            print(f"Font load error: {e}")
            font = pygame.font.SysFont('freesans', 10)  # Fallback font

        text = font.render(str(self.player.ammo) + '/' + str(self.player.max_ammo), True, (255, 255, 255))
        
        # Use self.display consistently if it's the initialized display surface
        self.display.blit(text, (rect_x, rect_y - 10))
        pygame.draw.rect(self.display, (255, 0, 0), (rect_x, rect_y, normalised_cooldown, rect_height))
        pygame.draw.rect(self.display, (155, 155, 155), (rect_x + normalised_cooldown, rect_y, bar_length-normalised_cooldown, rect_height))
        
        # scaled_weapon = self.player.active_weapon_left
        # if not scaled_weapon:
        #     return
        # weapon_image = self.assets[scaled_weapon.sub_type][scaled_weapon.animation]
        # self.display.blit(weapon_image, (rect_x + 40, rect_y - 12))
        # return