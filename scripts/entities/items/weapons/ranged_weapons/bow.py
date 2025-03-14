from scripts.entities.items.weapons.ranged_weapons.ranged_weapon import Ranged_Weapon


class Bow(Ranged_Weapon):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'bow', 4, 8, 10, 40)
        self.max_animation = 0
        self.attack_animation_max = 2
        self.attack_animation_counter = 0




    # Charging the crossbow
    def Set_Weapon_Charge(self, offset):
        if not self.entity:
            return
        if self.entity.category == "enemy":
            self.Enemy_Shooting()
            return


        self.is_charging = self.game.mouse.hold_down_left

        if not self.is_charging and self.ready_to_shoot:
            self.Set_Attack()
            self.ready_to_shoot = False
            return

        
        if self.is_charging == 10:
            self.game.sound_handler.Play_Sound('bow_draw', 1)

        if not self.is_charging:
            return

        if self.is_charging < self.max_charge_time:
            self.Update_Attack_Animation()

            return
        
        self.ready_to_shoot = True


    def Enemy_Shooting(self):
        if not self.entity.charge:
            return False

        if self.is_charging > 60:
            self.is_charging = 120
            self.Spawn_Arrow()
            self.arrow.Set_Delete_Countdown(50)
            self.arrow.pickup_allowed = False
            self.Shoot_Arrow()
            self.Reset_Bow()
            return True
        
        self.is_charging = self.entity.charge
        self.attack_animation_counter += 1
        self.Update_Attack_Animation()

        if self.attack_animation_time <= self.attack_animation_counter:
            self.attack_animation_counter = 0
            self.attack_animation = min(self.attack_animation_max, self.attack_animation + 1)
        return False

