from scripts.entities.items.weapons.magic_attacks.vampiric.soul_reap import Soul_Reap
import math


class Soul_Reap_Shooter():
    def Spawn_Soul_Reap(game, entity):
        damage = 3 # Multiplied with entity strength for damage calc
        speed = 1.5
        max_range = 240
       

        # Calculate the base angle using atan2(y, x)
        base_angle = math.atan2(entity.attack_direction[1], entity.attack_direction[0])

        pos_x = math.cos(base_angle) * speed
        pos_y = math.sin(base_angle) * speed
        direction = (pos_x, pos_y)
        ice_particle = Soul_Reap(
                game,
                entity.rect(),
                damage,
                speed,
                max_range,
                100,
                direction,  # Pass the direction here
                entity
            )
        
        game.item_handler.Add_Item(ice_particle)