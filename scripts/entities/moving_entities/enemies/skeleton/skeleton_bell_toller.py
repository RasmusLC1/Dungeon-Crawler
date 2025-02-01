from scripts.entities.moving_entities.enemies.skeleton.skeleton import Skeleton
from scripts.entities.items.weapons.close_combat.bell import Bell

import random


class Skeleton_Bell_Toller(Skeleton):
    def __init__(self, game, pos, health, strength, max_speed, agility, intelligence, stamina):
        type = str(random.randint(1, 1))
        super().__init__(game, pos, 'skeleton_bell_toller_' + type, health, strength, max_speed, agility, intelligence, stamina)
        self.Equip_Weapon(Bell(self.game, self.pos))
        self.max_weapon_charge = 70
        self.bell_ringing_cooldown = 0
        self.intent_manager.Set_Intent(['direct', 'attack', 'attack', 'medium_range'])


    def Update(self, tilemap, movement=(0, 0)):
        self.Update_Bell_Ringing_Cooldown()
        super().Update(tilemap, movement)

    def Update_Bell_Ringing_Cooldown(self):
        if not self.bell_ringing_cooldown:
            return
        
        self.bell_ringing_cooldown = max(0, self.bell_ringing_cooldown - 1)

    def Ring_Bell(self):
        if self.bell_ringing_cooldown:
            return
        self.game.clatter.Generate_Clatter(self.pos, 1000) # Generate clatter to alert nearby enemies
        self.bell_ringing_cooldown = 3000


    def Attack(self):
        if not super().Attack():
            return False
        self.Ring_Bell()

