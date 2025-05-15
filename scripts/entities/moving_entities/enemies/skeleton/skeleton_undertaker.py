from scripts.entities.items.weapons.close_combat.scythe import Scythe
from scripts.entities.moving_entities.enemies.skeleton.skeleton import Skeleton
from scripts.engine.assets.keys import keys

import random


class Skeleton_Undertaker(Skeleton):
    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        type = str(random.randint(1, 1))
        super().__init__(game, pos, keys.skeleton_undertaker + '_' + type, health, strength, max_speed, agility, intelligence, stamina, 50)
        self.Equip_Weapon(Scythe(self.game, self.pos))
        self.bones_search_cooldown = 0
        self.target_bones_collision_cooldown = 0
        self.target_bones = None
        self.intent_manager.Set_Intent(['direct', 'attack', 'attack', 'medium_range', 'medium_range', 'medium_range',])

    def Update(self, tilemap, movement=(0, 0)):
        self.Update_Bones_Search_Cooldown()
        self.Search_For_Bones()
        self.Resurrect_Enemy()
        super().Update(tilemap, movement)
        

    def Update_Bones_Search_Cooldown(self):
        if not self.bones_search_cooldown:
            return
        
        self.bones_search_cooldown = max(0, self.bones_search_cooldown - 1)

    def Resurrect_Enemy(self):
        if not self.target_bones:
            return
        if self.target_bones_collision_cooldown:
            self.target_bones_collision_cooldown = max(0, self.target_bones_collision_cooldown - 1)
            return
        else:
            self.target_bones_collision_cooldown = 50
            self.Revive()

    def Revive(self):
        if self.rect().colliderect(self.target_bones.rect()):
            self.game.particle_handler.Activate_Particles(10, 'vampire', self.rect().center, frame=random.randint(20, 40))
            self.target_bones.Revive()
            self.target_bones = None
            self.bones_search_cooldown = random.randint(2500, 3000)
            return

    def Search_For_Bones(self):
        if self.bones_search_cooldown:
            return
        # self.bones_search_cooldown = random.randint(900, 1100)
        self.bones_search_cooldown = random.randint(100, 200)
        nearby_bones = self.game.tilemap.Search_Nearby_Tiles_For_Type(5, self.pos, keys.bones, self.ID)
        if not nearby_bones:
            return
            
        self.locked_on_target = False
        self.Set_Destination(nearby_bones[0].pos)
        self.Find_New_Path()
        self.Set_Attack_Strategy("medium_range")
        self.target_bones = nearby_bones[0]



