from scripts.entities.decoration.decoration import Decoration
import random
from scripts.engine.assets.keys import keys

activation_radius = 200

class Brazier(Decoration):
    def __init__(self, game, pos) -> None:
        super().__init__(game, keys.brazier, pos, (32, 32))
        self.max_animation = 5
        self.animation_cooldown = 0
        self.animation_cooldown_max = 50
        self.Add_Light()
        self.animation = 1

    def Update(self):
        if self.animation > 0: # animation 0 is off
            self.Update_Animation()
        self.Update_Light_Level()
        
        return super().Update()

    def Add_Light(self):
        self.light_source = self.game.light_handler.Add_Light(self.pos, 8, self.tile)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)

    # Turn off the fire
    def Open(self, generate_clatter=False):
        if self.animation > 0:
            self.animation = 0
            self.game.light_handler.Remove_Light(self.light_source)
            self.Set_Sprite()
        else:
            self.Add_Light()
            self.Set_Animation()


        
    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.Set_Animation()

    def Set_Animation(self):
        self.Spawn_Fire_Particle()

        self.animation_cooldown = random.randint(self.animation_cooldown_max - 10, self.animation_cooldown_max)
        self.animation = random.randint(1,self.max_animation)
        self.Set_Sprite()


    def Spawn_Fire_Particle(self):
        self.game.particle_handler.Activate_Particles(random.randint(1, 2), keys.fire_particle, self.rect().center, frame=random.randint(80, 90))
        return
