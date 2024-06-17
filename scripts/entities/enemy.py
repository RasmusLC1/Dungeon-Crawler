from scripts.entities.entities import PhysicsEntity
import random



class Enemy(PhysicsEntity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, type, pos, size)
        self.animation = 'decrepit_bones'
        self.walking = 0
        self.movement_cooldown = 0

    
    def update(self, tilemap, movement=(0, 0)):
        if self.walking:
            if tilemap.solid_check((self.rect().centerx + (-7 if self.flip[0] else 7), self.pos[1] + 23)):
                if (self.collisions['right'] or self.collisions['left']):
                    self.flip[0] = not self.flip[0]
                else:
                    movement = (movement[0] - 0.5 if self.flip[0] else 0.5, movement[1])
            else:
                self.flip[0] = not self.flip[0]

            self.walking = max(0, self.walking-1)
            
        elif random.random() < 0.01:
            self.walking = random.randint(30, 120)
        
        super().update(tilemap, movement = movement)
        self.animation = 'decrepit_bones'
        

        if abs(self.game.player.dashing) >= 50:
            if self.rect().colliderect(self.game.player.rect()):
                self.game.player.Damage_Taken(5)
                return True

    