import random
import pygame

class Particle:
    def __init__(self, particle_handler):
        self.particle_handler = particle_handler
        self.type = None # Dictates it's movement and texture
        self.pos = (-999, -999) # Position is set off screen and moved to correct location on demand
        self.velocity = (0, 0) # Handles the movement pattern
        self.image = None # Set the image when particle is activated
        self.frame_count = 0 # How many frames a particle is active
        self.animation = 0 # Sparks always have 6 variations

    def Set_Type(self, type):
        self.type = type
        self.animation = random.randint(0, 5)

    def Set_Image(self, image):
        self.image = image

    def Set_Frame(self, frame):
        self.frame_count = frame

    def Set_Position(self, pos):
        self.pos = pos

    def Set_Velocity(self, velocity):
        self.velocity = velocity

    # Activate the particle by setting attributes
    def Set_Active(self, type, pos, velocity, frame):
        self.Set_Type(type)
        self.Set_Frame(frame)
        self.Set_Position(pos)
        self.Set_Velocity(velocity)
    
    # Disable the particle, by setting all the attributes back to default
    def Disable(self):
        self.image = None
        self.frame_count = 0
        self.Set_Position((-999, -999))
        self.Set_Velocity((0,0))
        self.particle_handler.Disable_Particle(self)

    def Update(self):
        # If framecount = 0 then the particle is not active and therefore does not need to be updated
        if not self.frame_count:
            return True
        self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])

        self.Update_Frame_Count()        
    
    # If framecount is zero, return true to signal the particle is finished and no longer active
    def Update_Frame_Count(self):
        self.frame_count = self.frame_count - 1
        # Set disable here, as this is only called once when framecount hits 0
        if self.frame_count <= 0:
            self.Disable()
            return True
        return False 


    def Render(self, surf, offset=(0, 0)):
        if not self.frame_count:
            return
        surf.blit(self.image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    