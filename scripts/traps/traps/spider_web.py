from scripts.traps.trap import Trap
import random
import math
import pygame


class Spider_Web(Trap):
    def __init__(self, game, pos, size, type, duration = 0):
        super().__init__(game, pos, size, type)
        self.duration = duration
        self.from_spider = False
        self.animation_max = 3
        self.delete = False

        if self.duration:
            self.from_spider = True
            self.animation = 0
        else:
            self.animation = self.animation_max


    def Update(self, entity):
        if self.Cooldown > 0:
            self.Cooldown -= 1
            return

        if self.delete:
            self.game.trap_handler.Remove_Trap(self)
            return

        if self.rect().colliderect(entity.rect()) and self.Cooldown == 0:
            if entity.type == 'player':
                if entity.dashing:
                    return
            
            entity.Set_Effect('Snare', 100)
            self.Cooldown = 100
            self.delete = True


    def Update_Duration(self):
        if not self.from_spider:
            return False
        
        if not self.duration:
            return True
        
        self.duration = max(0, self.duration - 1)
        return False

    # # TODO: Logic for spider shooting web
    # def Shoot(self, entity):
    #     pass

    def rect(self):
        return pygame.Rect(self.pos[0]+10, self.pos[1]+10, self.size[0], self.size[1])
    