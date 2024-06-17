from scripts.entities.entities import PhysicsEntity
import random



class Enemy(PhysicsEntity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, type, pos, size)
        self.animation = 'decrepit_bones'
        self.walking = 0
        self.health = 30
        self.movement_cooldown = 0
        self.direction = (0,0,0,0)
    
    def update(self, tilemap, movement=(0, 0)):
        movement = self.direction
        if self.movement_cooldown:
            self.movement_cooldown -= 1
        else:
            self.direction = (random.randint(-1, 1) / 10,random.randint(-1, 1) / 10)
            self.movement_cooldown = 100
            self.walking = max(0, self.walking-1)
        # else: 
        #     self.walking = random.randint(30, 120)
        
        super().update(tilemap, movement = movement)
        self.animation = 'decrepit_bones'
        

        if abs(self.game.player.dashing) >= 50:
            if self.rect().colliderect(self.game.player.rect()):
                self.game.player.Damage_Taken(5)
                return True

    