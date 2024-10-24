from scripts.decoration.decoration import Decoration
import random
import pygame

class Shrine(Decoration):
    def __init__(self, game, pos) -> None:
        super().__init__(game, 'shrine', 'shrine', pos, (32, 32))
        self.is_open = False
        self.animation = 0
        self.animation_cooldown = 0
        self.max_animation = 3
        self.light_level = 8
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['is_open'] = self.is_open

    def Load_Data(self, data):
        super().Load_Data(data)
        self.is_open = data['is_open']

    def Update(self):
        self.Update_Animation()
        return super().Update()

    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = 20
            self.animation = random.randint(0,self.max_animation)

    def Open(self, generate_clatter = False):
        print("TEST")
        self.game.state_machine.Set_State('shrine_menu')


    def Render(self, surf, offset = (0,0)):
        if not self.Update_Light_Level():
            return
        # Set image
        shrine_image = self.game.assets['shrine'][self.animation].convert_alpha()

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))  # Adjust the factor as needed
        if not alpha_value:
            return
        
        shrine_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(shrine_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        shrine_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(shrine_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
