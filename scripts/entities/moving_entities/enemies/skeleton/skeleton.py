from scripts.entities.moving_entities.enemies.enemy import Enemy


class Skeleton(Enemy):
    def __init__(self, game, pos, type, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, type, health, strength, max_speed, agility, intelligence, stamina, 'undead')
        self.animation_num_max = 6
        self.attack_animation_num_cooldown_max = 6
        self.max_weapon_charge = 60
        self.attack_distance  = 60
        self.disengage_distance = 100

    def Update(self, tilemap, movement=(0, 0)):
        super().Update(tilemap, movement)
        self.Update_Active_Weapon()
        self.Weapon_Cooldown()
        if self.distance_to_player < self.attack_distance:
            self.Attack()

        if self.distance_to_player > self.disengage_distance and self.charge:
            self.charge = 0


    def Set_Idle(self):
        pass

    def Set_Action(self,  movement):
        pass

    # Returns true on succesful attack
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

    def Equip_Weapon(self, weapon):
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