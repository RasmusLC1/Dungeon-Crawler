import math

class Boss_Room():
    def __init__(self, game, pos, radius, level) -> None:
        self.game = game
        self.pos = pos
        self.boss = None
        self.radius = radius
        self.level = level
        self.shrine = None
        self.distance_cooldown = 0

    def Update(self):
        if self.Calculate_Distance:
            self.Spawn_Boss()
    
    
    # Spawn boss
    # Close Doors and replace with walls
    def Spawn_Boss(self):
        # Spawn Temp decrepit bones
        self.game.enemy_handler.Enemy_Spawner(
            'decrepit_bones_melee',
            
        )

    def Calculate_Distance(self):
        if self.distance_cooldown:
            self.distance_cooldown -= 1
            return False
        
        # Calculate distance and set the cooldown to the distance to avoid computation
        distance = math.sqrt((self.game.player.pos[0] - self.pos[0]) ** 2 + (self.game.player.pos[1] - self.pos[0]) ** 2)        
        self.distance_cooldown = distance

        if distance < self.radius - 2:
            return True
        
        return False