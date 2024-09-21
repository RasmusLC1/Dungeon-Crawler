import math
import random
import pygame


class Status_Effect_Handler:
    def __init__(self, entity):
        self.entity = entity

    def Set_Effect(self, effect, duration):
        if effect == 'Snare':
            return self.Set_Snare(duration)
        elif effect == 'Poison':
            return self.Set_Poisoned(duration)
        elif effect == 'Freeze':
            return self.Set_Frozen(duration)
        elif effect == 'Fire':
            return self.Set_On_Fire(duration)
        elif effect == 'Wet':
            return self.Set_Wet(duration)
        elif effect == 'Dry':
            return self.Set_Dry(duration)
        elif effect == 'Slow_Down':
            return self.Slow_Down(duration)
        else:
            return False

     #set poison effect
    def Set_Poisoned(self, poison_time):
        self.entity.poisoned =  max(random.randint(2, poison_time), self.entity.poisoned)
        return True

    #set frozen effect
    def Set_Frozen(self, freeze_time):
        if self.entity.is_on_fire:
            return
        
        if self.entity.wet:
            freeze_time *= 2
            self.entity.wet = 0
        self.entity.frozen = max(3, freeze_time)
        return True
    
    def Remove_Frozen(self):
        self.entity.frozen = 0

    # Set wet effect
    def Set_Wet(self, wet_time):
        if self.entity.is_on_fire:
            self.entity.is_on_fire = 0
        if self.entity.frozen:
            self.entity.frozen -= 1
        self.entity.wet = max(2, wet_time)
        return True

    
    def Set_Dry(self, drying):
        self.entity.wet = max(0, self.entity.wet - drying)
        return True



    #set Fire effect
    def Set_On_Fire(self, fire_time):
        if self.entity.wet:
            return False
        if self.entity.frozen:
            self.Remove_Frozen()
        self.entity.is_on_fire = max(random.randint(fire_time, fire_time * 2), self.entity.is_on_fire)
        return True
    
    #set snare effect
    def Set_Snare(self, snare_time):
        self.entity.snared = snare_time
        return True

    def Snare(self):
        if self.entity.snared:
            self.entity.snared -= 1
            self.entity.frame_movement = (0, 0)

    def OnFire(self):
        if self.entity.fire_cooldown:
            self.entity.fire_cooldown -= 1
        elif self.entity.is_on_fire:
                damage = random.randint(1, 3)
                self.entity.Damage_Taken(damage)
                self.entity.is_on_fire -= 1
                self.entity.fire_cooldown = random.randint(30, 50)
        self.Fire_Animation()

    def Fire_Animation(self):
        if self.entity.fire_animation_cooldown:
            self.entity.fire_animation_cooldown -= 1
        else:
            self.entity.fire_animation_cooldown = 15
            if self.entity.fire_animation >= 7:
                self.entity.fire_animation = 0
            else:
                self.entity.fire_animation += 1

    # Slow the entity down by increasing friction
    def Slow_Down(self, effect):
        if not effect:
            return
        try:
            self.entity.max_speed = max(0.1, self.entity.max_speed / effect)
        except ZeroDivisionError as e:
            print(self.entity.max_speed, effect)
            print(f"SLOWDOWN: {e}")

    def Poisoned(self):
        if not self.entity.poisoned:
            return
        if self.entity.poisoned_cooldown:
            self.entity.poisoned_cooldown -= 1

        if not self.entity.poisoned_cooldown:
            self.entity.Damage_Taken(self.entity.poisoned)
            self.entity.poisoned_cooldown = random.randint(50, 70)
            self.entity.poisoned -= 1
        self.entity.Slow_Down(self.entity.poisoned)
        self.Poision_Animation()

    def Poision_Animation(self):
        if self.entity.poison_animation_cooldown:
            self.entity.poison_animation_cooldown -= 1
        else:
            self.entity.poison_animation_cooldown = 30
            if self.entity.poison_animation >= 2:
                self.entity.poison_animation = 0
            else:
                self.entity.poison_animation += 1

    

    def Frozen(self):
        if self.entity.frozen <= 1:
            self.entity.frozen = 0
            return
        elif self.entity.frozen_cooldown:
            self.entity.frozen_cooldown -= 1

        if not self.entity.frozen_cooldown:
            self.entity.frozen_cooldown = random.randint(160, 200)
            self.entity.frozen -= 1
        self.entity.Slow_Down(self.entity.frozen)
        self.Frozen_Animation()

    def Frozen_Animation(self):
        if self.entity.frozen_animation_cooldown:
            self.entity.frozen_animation_cooldown -= 1
        else:
            self.entity.frozen_animation_cooldown = 30
            if self.entity.frozen_animation >= 2:
                self.entity.frozen_animation = 0
            else:
                self.entity.frozen_animation += 1

    def Wet(self):
        if self.entity.wet <= 1:
            self.entity.wet = 0
            return
        elif self.entity.wet_cooldown:
            self.entity.wet_cooldown -= 1

        if not self.entity.wet_cooldown:
            self.entity.wet_cooldown = random.randint(160, 200)
            self.entity.wet -= 1
        self.Wet_Animation()

    def Wet_Animation(self):
        if self.entity.wet_animation_cooldown:
            self.entity.wet_animation_cooldown -= 1
        else:
            self.entity.wet_animation_cooldown = 10
            if self.entity.wet_animation >= 10:
                self.entity.wet_animation = 0
            else:
                self.entity.wet_animation += 1

    
    
    def render_fire(self, game, surf, offset=(0, 0)):
        if self.entity.is_on_fire:
            fire_image = game.assets['fire'][self.entity.fire_animation].convert_alpha()
            # Set the opacity to 70%
            fire_image.set_alpha(179)
            surf.blit(pygame.transform.flip(fire_image, self.entity.flip[0], False), (self.entity.pos[0] - offset[0] + self.entity.anim_offset[0], self.entity.pos[1] - offset[1] - 5))

    def render_poison(self, game, surf, offset=(0, 0)):
        if self.entity.poisoned:
            poison_image = game.assets['poison'][self.entity.poison_animation].convert_alpha()
            # Set the opacity to 70%
            poison_image.set_alpha(179)
            poison_image = pygame.transform.scale(poison_image, (12, 12))
            surf.blit(pygame.transform.flip(poison_image, self.entity.flip[0], False), (self.entity.pos[0] - offset[0] + self.entity.anim_offset[0], self.entity.pos[1] - offset[1] - 5))

    def render_frozen(self, game, surf, offset=(0, 0)):
        if self.entity.frozen:
            frozen_image = game.assets['frozen'][self.entity.frozen_animation].convert_alpha()
            # Set the opacity to 70%
            frozen_image.set_alpha(179)
            frozen_image = pygame.transform.scale(frozen_image, (12, 12))
            surf.blit(pygame.transform.flip(frozen_image, self.entity.flip[0], False), (self.entity.pos[0] - offset[0] + self.entity.anim_offset[0], self.entity.pos[1] - offset[1] - 5))

    def render_wet(self, game, surf, offset=(0, 0)):
        if self.entity.wet:
            wet_image = game.assets['wet'][0].convert_alpha()
            # Set the opacity to 70%
            wet_image.set_alpha(179)
            wet_image = pygame.transform.scale(wet_image, (10, 10))
            surf.blit(pygame.transform.flip(wet_image, self.entity.flip[0], False), (self.entity.pos[0] - offset[0] + self.entity.anim_offset[0], self.entity.pos[1] - offset[1] + self.entity.wet_animation - 5))