from scripts.entities.items.weapons.close_combat.scythe import Scythe
from scripts.entities.moving_entities.enemies.skeleton.skeleton import Skeleton

import random


class Skeleton_Undertaker(Skeleton):
    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        type = str(random.randint(1, 1))
        super().__init__(game, pos, 'skeleton_undertaker_' + type, health, strength, max_speed, agility, intelligence, stamina, 50)
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
        
        if self.rect().colliderect(self.target_bones.rect()):
            self.target_bones.Revive()
            self.target_bones = None
            self.bones_search_cooldown = random.randint(2500, 3000)
            return
        else:
            self.target_bones_collision_cooldown = 50


    def Search_For_Bones(self):
        if self.bones_search_cooldown:
            return
        self.bones_search_cooldown = random.randint(900, 1100)
        nearby_decorations = self.game.tilemap.Search_Nearby_Tiles(5, self.pos, "decoration", self.ID)
        nearby_bones = []
        for decoration in nearby_decorations:
            if decoration.type == 'bones':
                nearby_bones.append(decoration)
        
        if not nearby_bones:
            return
        self.locked_on_target = False
        self.Set_Destination(nearby_bones[0].pos)
        self.Find_New_Path()
        self.target_bones = nearby_bones[0]



