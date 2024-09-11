from scripts.entities.enemies.enemy import Enemy


class Fire_Spirit(Enemy):
    def __init__(self, game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina)
        self.animation = 'fire_spirit'
        
        self.path_finding_strategy = 'ignore_lava'
        self.look_for_health_cooldown = 0

    def Update(self, tilemap, movement = (0, 0)):
        

        super().Update(tilemap, movement)
    
        if self.distance_to_player < 30:
            self.Attack()
        if self.look_for_health_cooldown:
            self.look_for_health_cooldown = max(0, self.look_for_health_cooldown - 1)
            if not self.look_for_health_cooldown:
                self.Set_Target(self.game.player.pos)

        if self.health <= self.max_health / 3 and not self.look_for_health_cooldown:
            self.look_for_health_cooldown = 2000

            nearby_traps = self.game.trap_handler.Find_Nearby_Traps(self.pos, 200)
            for trap in nearby_traps:

                if trap.type == 'Lava_env':
                    print(trap.type)
                    self.Set_Target(trap.pos)
                    self.Find_New_Path(self.target)
                    break
        

    def Look_For_Health(self):
        pass

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
        self.Healing(fire_time)