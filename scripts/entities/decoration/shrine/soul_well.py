from scripts.entities.decoration.decoration import Decoration
import random
from scripts.engine.assets.keys import keys
import math

class Soul_Well(Decoration):
    def __init__(self, game, pos) -> None:
        super().__init__(game, keys.soul_well, pos, (64, 64))
        self.description = "sacrifice gold\nfor souls"
        self.animation_cooldown = 0
        self.distance_to_player = 0
        self.max_animation = 3



    def Update(self):
        self.Check_For_Gold_Collision()
        return super().Update()

    # TODO: Add sprite for shrine with animation
    def Update_Animation(self):
        # use the logic animation_cooldown as it basically needs the same
        if self.animation_cooldown:
            return
        if self.distance_to_player > 200:
            return
        
        self.animation += 1
        if self.animation > self.max_animation:
            self.animation = 0
        self.Set_Entity_Image()
        spawn_particles = random.randint(0, 4)
        if spawn_particles == 4:
            self.game.particle_handler.Activate_Particles(random.randint(2, 4), keys.soul_particle, self.rect().center, frame=random.randint(50, 70))


    def animation_cooldown_Handler(self):
        if self.animation_cooldown <= 0:
            self.animation_cooldown = random.randint(40, 60)
            return True
        
        self.animation_cooldown -= 1
        return False

    def Check_Player_Dis(self):
        player_pos = self.game.player.pos
        self.distance_to_player = math.sqrt((player_pos[0] - self.pos[0]) ** 2 + (player_pos[1] - self.pos[1]) ** 2)
        if self.distance_to_player > 200:
            self.animation_animation_cooldown = self.distance_to_player * 2
            return False
        
        return True

    def Check_For_Gold_Collision(self):
        if not self.animation_cooldown_Handler():
            return
        
        if not self.Check_Player_Dis():
            return
        
        nearby_items = self.game.item_handler.Find_Nearby_Item(self.pos, 2)

        for item in nearby_items:
            if not item.type == keys.gold:
                continue
            self.game.player.Increase_Souls(item.amount)
            self.game.item_handler.Remove_Item(item, True)
            self.game.particle_handler.Activate_Particles(random.randint(8, 12), keys.soul_particle, self.rect().center, frame=random.randint(50, 70))


    def Render(self, surf, offset=...):
        super().Render(surf, offset)
        self.Update_Animation()