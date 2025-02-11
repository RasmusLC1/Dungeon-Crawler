import random
import pygame

class Particle:
    def __init__(self, game):
        self.game = game
        self.type = None
        self.pos = (-999, -999)
        self.velocity = (0, 0)
        self.image = None
        self.active = False
        self.frame_count = 0
        self.animation = 0 # Sparks always have 6 variations

    def Set_Image(self, type):
        self.type = type
        self.animation = random.randint(0, 5)
        self.image = self.game.assets[self.type + '_particle'][self.animation]

    def Set_Frame(self, frame):
        self.frame_count = frame

    def Set_Position(self, pos):
        self.pos = pos

    def Set_Velocity(self, velocity):
        self.velocity = velocity

    def Set_Active(self, type, pos, velocity, frame):
        self.Set_Image(type)
        self.Set_Frame(frame)
        self.Set_Position(pos)
        self.Set_Velocity(velocity)
        self.active = True

    def Disable(self):
        self.image = None
        self.frame_count = 0
        self.active = False
        self.Set_Position((-999, -999))
        self.Set_Velocity((0,0))

    def Update(self):
        if not self.active:
            return True
        
        self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])

        self.Update_Frame_Count()
            
    
    # If framecount is zero, return true to signal the particle is finished
    def Update_Frame_Count(self):
        self.frame_count = self.frame_count - 1
        if self.frame_count <= 0:
            self.Disable()
            return True
        return False 


    def Render(self, surf, offset=(0, 0)):
        if not self.active:
            return
        surf.blit(self.image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    