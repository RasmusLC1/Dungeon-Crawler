from scripts.entities.moving_entities.enemies.enemy import Enemy
from scripts.entities.items.weapons.close_combat.scythe import Scythe

import random


class Skeleton_Undertaker(Enemy):
    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        type = str(random.randint(1, 1))
        super().__init__(game, pos, 'skeleton_undertaker_' + type, health, strength, max_speed, agility, intelligence, stamina, 'undead')
        self.animation_num_max = 6
        self.attack_animation_num_cooldown_max = 6
        self.Equip_Weapon()
        self.max_charge = 60
        self.bones_search_cooldown = 0
        self.target_bones_collision_cooldown = 0
        self.target_bones = None
        self.attack_strategy = 'long_range'


    def Update(self, tilemap, movement=(0, 0)):
        super().Update(tilemap, movement)
        self.Update_Active_Weapon()
        self.Weapon_Cooldown()
        self.Update_Bones_Search_Cooldown()
        self.Search_For_Bones()
        self.Resurrect_Enemy()
        if self.distance_to_player < 40:
            self.Attack()

        if self.distance_to_player > 60 and self.charge:
            self.charge = 0

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
            self.bones_search_cooldown = 3000
            return
        else:
            self.target_bones_collision_cooldown = 50


    def Search_For_Bones(self):
        if self.bones_search_cooldown:
            return
        self.bones_search_cooldown = 1000
        nearby_decorations = self.game.tilemap.Search_Nearby_Tiles(5, self.pos, "decoration", self.ID)
        nearby_bones = []
        for decoration in nearby_decorations:
            if decoration.type == 'bones':
                nearby_bones.append(decoration)
        
        if not nearby_bones:
            return
        self.locked_on_target = False
        self.Find_New_Path(nearby_bones[0].pos)
        self.target_bones = nearby_bones[0]


    def Set_Idle(self):
        pass

    def Set_Action(self,  movement):
        pass

    def Attack(self):
        if not super().Attack():
            return
        
        self.charge = min(self.max_charge, self.charge + 1)
        if not self.active_weapon:
            return

        if self.charge < self.max_charge:
            return
        
        self.Set_Target(self.game.player.pos)
        self.active_weapon.Set_Attack()
        self.Reset_Charge()

    def Equip_Weapon(self):
        weapon = Scythe(self.game, self.pos)

        if not weapon:
            return False

        if not weapon.Check_Inventory_Type('left_hand'):
            return False
        weapon.Pickup_Reset_Weapon(self)
        weapon.Set_Equip(True)
        self.Set_Active_Weapon(weapon)
        

        self.active_weapon.render = False
        del(weapon)
        return True
    
    
    def Update_Active_Weapon(self, offset=(0, 0)):
        if not self.active_weapon:
            return

        # Set the active and light to match the enemy itself
        self.active_weapon.Set_Active(self.active)
        self.active_weapon.Set_Light_Level(self.light_level)

        self.active_weapon.Set_Equipped_Position(self.direction_y_holder)
        # self.active_weapon.Update(offset)
        if not self.active_weapon:
            return
        
        self.active_weapon.Update_Attack()


        return