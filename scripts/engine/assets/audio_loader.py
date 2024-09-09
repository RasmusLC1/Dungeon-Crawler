import pygame
from scripts.engine.utility.utils import load_image, load_images, Animation, get_tiles_from_sheet

class Audio_Loader:
    def Run_All(self):
        self.sfx = {}
        Audio_Loader.Chest_Effects(self)
        Audio_Loader.Weapons_Effects(self)


    def Chest_Effects(self):
        chest_effects ={
            'chest_open' : pygame.mixer.Sound('data/sounds/decorations/chest_open.wav'),
        }
        self.sfx.update(chest_effects)
        self.sfx['chest_open'].set_volume(0.1)

    def Weapons_Effects(self):
        weapon_effects ={
            'sword_impact_wall' : pygame.mixer.Sound('data/sounds/weapons/sword_impact_wall.wav'),
            'bow_draw' : pygame.mixer.Sound('data/sounds/weapons/bow_draw.wav'),
            'arrow_shot' : pygame.mixer.Sound('data/sounds/weapons/arrow_shot.wav'),
            'torch_fire_ball' : pygame.mixer.Sound('data/sounds/weapons/torch_fire_ball.wav'),
            'projectile_impact' : pygame.mixer.Sound('data/sounds/weapons/projectile_impact.wav'),
            'stab_attack_impact' : pygame.mixer.Sound('data/sounds/weapons/stab_attack_impact.wav'),
            'torch_attack' : pygame.mixer.Sound('data/sounds/weapons/torch_attack.wav'),
            'torch_equipped' : pygame.mixer.Sound('data/sounds/weapons/torch_equipped.wav'),
            'sword_swing' : pygame.mixer.Sound('data/sounds/weapons/sword_swing.wav'),
        }

        self.sfx.update(weapon_effects)

        self.sfx['sword_impact_wall'].set_volume(0.2)
        self.sfx['bow_draw'].set_volume(0.3)
        self.sfx['arrow_shot'].set_volume(0.4)
        self.sfx['torch_fire_ball'].set_volume(0.2)
        self.sfx['projectile_impact'].set_volume(0.3)
        self.sfx['stab_attack_impact'].set_volume(0.2)
        self.sfx['torch_attack'].set_volume(0.2)
        self.sfx['torch_equipped'].set_volume(0.2)
        self.sfx['sword_swing'].set_volume(0.2)
    