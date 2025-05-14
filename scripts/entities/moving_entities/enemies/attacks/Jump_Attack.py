import pygame
from scripts.engine.assets.keys import keys


class Jump_Attack():
    def __init__(self):
        self.attack_length = 0
    
    def Jump_Attack(self, entity):
        # Return true and end the attack if attack is complete
        if self.Update_Attack_Length():
            return True
        
        attack_direction = self.Set_Attack_Direction(entity)
        entity.attack_direction = attack_direction
        if not attack_direction:
            return
        
        
        entity.Set_Frame_movement((attack_direction[0], attack_direction[1]))
        entity.Tile_Map_Collision_Detection(entity.game.tilemap)
        if entity.max_speed == entity.max_speed_holder:
            entity.max_speed *= 15

        if entity.Attack():
            return True
        else:
            return False

    def Set_Attack_Length(self, attack_length):
        if self.attack_length:
            return
        self.attack_length = attack_length

    def Update_Attack_Length(self):
        if not self.attack_length:
            return False
        
        self.attack_length = max(0, self.attack_length - 1)
        if not self.attack_length:
            return True
        
        return False
    

    def Set_Attack_Direction(self, entity):
            attack_direction = pygame.math.Vector2(entity.target[0] - entity.pos[0], entity.target[1] - entity.pos[1])
            if not attack_direction:
                return (0, 0)
            attack_direction.normalize_ip()

            return attack_direction