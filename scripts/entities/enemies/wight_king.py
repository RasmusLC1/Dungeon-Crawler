from scripts.entities.enemies.enemy import Enemy
from scripts.items.weapons.close_combat.sword import Sword
from scripts.items.weapons.close_combat.torch import Torch
from scripts.items.weapons.projectiles.spear import Spear

import random


class Wight_King(Enemy):
    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, 'wight_king', health, strength, max_speed, agility, intelligence, stamina, 'undead', (40, 40))
        self.animation_num_max = 4
        self.attack_animation_num_max = 4
        self.attack_animation_num_cooldown_max = 8
        self.animation = 'wight_king'
        self.attack_strategy = 'medium_range'
        self.Equip_Weapon()
        self.max_charge = 40

    def Update(self, tilemap, movement=(0, 0)):
        super().Update(tilemap, movement)
        self.Update_Active_Weapon()
        self.Weapon_Cooldown()
        self.Update_Animation()
        if self.distance_to_player < 30:
            self.Attack()

        if self.distance_to_player > 30 and self.charge:
            self.charge = 0


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
        self.active_weapon.Set_Attack_Ready(True)
        self.active_weapon.Set_Attack()
        self.Reset_Charge()

    def Equip_Weapon(self):
        weapon = None

        random_weapon = random.randint(0, 1)

        if random_weapon == 0:
            weapon = Sword(self.game, self.pos)

        elif random_weapon == 1:
            weapon = Spear(self.game, self.pos)
        

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
    

    