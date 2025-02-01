from scripts.entities.moving_entities.enemies.enemy import Enemy
from scripts.entities.items.weapons.close_combat.sword import Sword
from scripts.entities.items.weapons.projectiles.spear import Spear
from scripts.entities.moving_entities.enemies.behavior.intent_manager import Intent_Manager

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
        self.intent_manager = Intent_Manager(game, self, 400, ['direct', 'charge', 'attack', 'attack', 'medium_range',])

    def Update(self, tilemap, movement=(0, 0)):
        super().Update(tilemap, movement)
        self.Update_Active_Weapon()
        self.Weapon_Cooldown()
        self.Update_Animation()
        self.intent_manager.Update_Behavior()


    def Set_Idle(self):
        pass

    def Set_Action(self,  movement):
        pass

    def Attack(self):
        if not super().Attack():
            return False
        
        if not self.active_weapon:
            return False

        
        self.charge = min(self.max_weapon_charge, self.charge + 1)
        if not self.active_weapon:
            return False

        if self.charge < self.max_weapon_charge:
            return False
        
        self.Set_Target(self.game.player.pos)
        self.active_weapon.Set_Enemy_Attack()
        self.Reset_Charge()
        return True

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
    

    