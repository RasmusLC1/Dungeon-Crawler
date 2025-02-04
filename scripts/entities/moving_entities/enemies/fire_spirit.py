from scripts.entities.moving_entities.enemies.enemy import Enemy
from scripts.entities.items.weapons.magic_attacks.fire.fire_particle import Fire_Particle
from scripts.entities.items.weapons.magic_attacks.fire.flame_thrower import Flame_Thrower


import math


class Fire_Spirit(Enemy):
    def __init__(self, game, pos, type, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, type, health, strength, max_speed, agility, intelligence, stamina, 100, 'elemental')
        
        self.animation = 'fire_spirit'
        self.path_finding_strategy = 'ignore_lava'
        self.attack_strategy = 'medium_range'
        self.intent_manager.Set_Intent(['attack'])

        self.look_for_health_cooldown = 0
        self.fire_cooldown = 0
        self.spewing_fire = False

        self.animation_num_max = 3
        self.attack_animation_num_max = 3
        self.attack_animation_num_cooldown_max = 100
        self.animation_num_cooldown_max = 100
        self.flame_thrower = Flame_Thrower(self.game, 60)

    def Update(self, tilemap, movement = (0, 0)):
        
        super().Update(tilemap, movement)

        self.Look_For_Health()

        if self.distance_to_player < 120:
            self.Attack()

        if self.distance_to_player > 150 and self.charge:
            self.charge = 0


        
    
    def Attack(self):
        if not super().Attack():
            return
        self.charge += 1
        if self.charge >= self.max_weapon_charge:
            self.spewing_fire = True

        if self.spewing_fire:
            self.Shoot_Fire()

        if self.charge <= 0:
            self.spewing_fire = False
    
    def Shoot_Fire(self):
        self.Set_Target(self.game.player.pos)
        self.Set_Attack_Direction()
        self.charge = self.flame_thrower.Fire_Particle_Creation(self, self.charge)


    # TODO: IMPLEMENT
    def Look_For_Health(self):
        if self.look_for_health_cooldown:
            self.look_for_health_cooldown = max(0, self.look_for_health_cooldown - 1)
            return
        

        if self.health < self.max_health / 2:
            self.Set_Locked_On_Target(0)

            self.look_for_health_cooldown = 2000

            nearby_traps = self.game.trap_handler.Find_Nearby_Traps(self.pos, 200)
            for trap in nearby_traps:

                if trap.type == 'Lava_env':
                    self.Set_Destination(trap.pos)
                    self.Find_New_Path()
                    self.locked_on_target = True
                    break

            self.Set_Locked_On_Target(4000)
        
        return

    def Set_Idle(self):
        pass

    def Set_Action(self, movement):
        # Check for movement
        if not movement[0] and not movement[1]:
            self.Set_Animation('standing_still')
            return
        

        if movement[1] or movement[0]:
            self.Set_Animation('running')
            return

    def Set_On_Fire(self, fire_time):
        self.effects.Set_Effect('healing', fire_time)
        return False