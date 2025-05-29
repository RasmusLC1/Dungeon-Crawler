from scripts.entities.decoration.decoration import Decoration
import random
from scripts.engine.assets.keys import keys
import math

activation_radius = 200

class Soul_Well(Decoration):
    def __init__(self, game, pos) -> None:
        super().__init__(game, keys.soul_well, pos, (64, 64))
        self.description = "sacrifice gold\nfor souls"
        self.animation_cooldown = 0
        self.distance_to_player = 0
        self.max_animation = 3



    def Update(self):
        self.Update_Animation()
        return super().Update()

    # TODO: Add sprite for shrine with animation
    def Update_Animation(self):
        # use the logic animation_cooldown as it basically needs the same
        if self.animation_cooldown:
            return
        if self.distance_to_player > activation_radius:
            return
        
        self.animation += 1
        if self.animation > self.max_animation:
            self.Set_Animation(0)
        spawn_particles = random.randint(0, 4)
        if spawn_particles == 4:
            self.game.particle_handler.Activate_Particles(random.randint(2, 4), keys.soul_particle, self.rect().center, frame=random.randint(50, 70))


    def animation_cooldown_Handler(self):
        if self.animation_cooldown <= 0:
            self.animation_cooldown = random.randint(40, 60)
            return True
        
        self.animation_cooldown -= 1
        return False


    def Spawn_Reward(self, item):
        if not item.type == keys.gold:
                return False
        self.game.player.Increase_Souls(item.amount * 2)
        self.game.item_handler.Remove_Item(item, True)
        self.game.particle_handler.Activate_Particles(random.randint(8, 12), keys.soul_particle, self.rect().center, frame=random.randint(50, 70))
        
        self.game.clatter.Generate_Clatter(self.pos, 1000) # Generate clatter to alert nearby enemies
        self.game.sound_handler.Play_Sound('soul_well', 0.6)

        return True