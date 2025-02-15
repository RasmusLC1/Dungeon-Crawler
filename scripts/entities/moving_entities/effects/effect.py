import pygame
import random

class Effect():
    def __init__(self, entity, effect_type, animation_max, animation_cooldown_max, cooldown_range, description):
        self.entity = entity
        self.effect_type = effect_type
        self.effect_max = 10
        self.effect = 0
        self.cooldown = 0
        self.animation = 0
        self.animation_max = animation_max
        self.animation_cooldown = 0
        self.animation_cooldown_max = animation_cooldown_max
        self.cooldown_range = cooldown_range
        self.description = description
        self.saved_data = {}

    def Save_Data(self):
        self.saved_data['effect'] = self.effect
        self.saved_data['cooldown'] = self.cooldown
        self.saved_data['animation'] = self.animation
        self.saved_data['animation_cooldown'] = self.animation_cooldown
        return self.saved_data


    def Load_Data(self, data):
        self.effect = data['effect']
        self.cooldown = data['cooldown']
        self.animation = data['animation']
        self.animation_cooldown = data['animation_cooldown']


    #set effect
    def Set_Effect(self, effect_time):
        if self.effect >= self.effect_max:
            return False
        self.effect = min(effect_time + self.effect, self.effect_max)
        return True
    
    def Update_Effect(self):
        pass

    def Remove_Effect(self):
         self.effect = 0
         self.aniamtion = 0
         self.cooldown = 0
         self.animation_cooldown = 0

    def Decrease_Effect(self):
        self.effect = max(self.effect - 1, 0)

    def Update_Cooldown(self) -> bool: 
        if self.cooldown:
            self.cooldown -= 1
            return False
        
        self.effect -= 1
        self.cooldown = random.randint(self.cooldown_range[0], self.cooldown_range[1])
        return True

    def Effect_Animation_Cooldown(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
            return
        
        self.animation_cooldown = self.animation_cooldown_max
        if self.animation >= self.animation_max:
            self.animation = 0
        else:
            self.animation += 1

   
    def Render_Effect(self, surf, offset=(0, 0)):
        if not self.effect:
            return
        
        if self.animation_max == 0:
            return
        image = self.entity.game.assets[self.effect_type][self.animation].convert_alpha()
        # Set the opacity to 70%
        image.set_alpha(179)
        surf.blit(pygame.transform.flip(image, self.entity.flip[0], False), (self.entity.pos[0] - offset[0] + self.entity.anim_offset[0], self.entity.pos[1] - offset[1] - 5))


