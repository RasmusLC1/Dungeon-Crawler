import pygame


class Effect():
    def __init__(self, entity, animation_max, animation_cooldown_max):
        self.entity = entity
        self.effect = 0
        self.cooldown = 0
        self.animation = 0
        self.animation_max = animation_max
        self.animation_cooldown = 0
        self.animation_cooldown_max = animation_cooldown_max

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        pass
    
    def Update_Effect(self):
        pass

    def Remove_Effect(self):
         self.effect = 0
         self.aniamtion = 0
         self.cooldown = 0
         self.animation_cooldown = 0
   
    def Render_Effect(self, game, surf, condition, animation, effect, offset=(0, 0)):
        if condition:
            try:
                fire_image = game.assets[effect][animation].convert_alpha()
                # Set the opacity to 70%
                fire_image.set_alpha(179)
                surf.blit(pygame.transform.flip(fire_image, self.entity.flip[0], False), (self.entity.pos[0] - offset[0] + self.entity.anim_offset[0], self.entity.pos[1] - offset[1] - 5))
            except Exception as e:
                    print(f"Wrong Render effect input{e}", condition, animation, effect)