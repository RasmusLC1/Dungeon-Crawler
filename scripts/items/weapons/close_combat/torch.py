from scripts.items.weapons.weapon import Weapon
from scripts.items.weapons.projectiles.fire_particle import Fire_Particle
import math


class Torch(Weapon):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'torch', 1, 3, 5, 6, 'one_handed_melee', 'fire')
        self.max_animation = 5
        self.attack_animation_max = 5
        self.light_source = self.game.light_handler.Add_Light(self.pos, 8, self.tile)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)
        self.offset = (0,0)
        self.fire_cooldown = 0
        self.effect = 'fire'


    # Pick up the torch and update the general light in the area
    def Pick_Up(self):
        if not super().Pick_Up():
            return
        # self.light_source.picked_up = True
        # self.game.player.Set_Light_State(False)
        self.game.light_handler.Remove_Light(self.light_source)
        self.game.light_handler.Restore_Light(self.light_source)



    def Update_Attack(self):
        if not super().Update_Attack():
            return False
        
        

        self.Set_Attack_Hitbox_Size((32, 16))

    def Special_Attack(self):
        if self.special_attack <= 0 or not self.equipped:
            self.light_source.Update_Light_Level(8)
            self.Reset_Special_Attack()
            return
        self.Fire_Particle_Creation()
        self.light_source.Update_Light_Level(12)
        
    
    def Set_Equipped_Position(self, direction_y):
        if 'left' in self.inventory_type:
            if direction_y < 0:
                self.Move((self.entity.pos[0] - 5 , self.entity.pos[1]))
            else:
                self.Move((self.entity.pos[0] + 5 , self.entity.pos[1]))
        elif 'right' in self.inventory_type:
            if  direction_y < 0:
                self.Move((self.entity.pos[0] + 7, self.entity.pos[1]))
            else:
                self.Move((self.entity.pos[0] - 7, self.entity.pos[1]))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)

    
    def Fire_Particle_Creation(self):
        # Handle cooldown for spacing between fire particles
        if self.fire_cooldown:
            self.fire_cooldown -= 1
            return
        else:
            self.fire_cooldown = 3
            self.special_attack -= 20

        # Basic raycasting attributes
        num_lines = 8  # Define the number of lines and the spread angle (in degrees)
        spread_angle = 50  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1)  # Calculate the angle increment between each line

        # Calculate the base angle using atan2(y, x)
        base_angle = math.atan2(self.entity.attack_direction[1], self.entity.attack_direction[0])
        start_angle = base_angle - math.radians(spread_angle / 2)

        damage = 2
        speed = 1  
        max_range = 50

        # Generate fire particles
        for j in range(num_lines):
            angle = start_angle + j * math.radians(angle_increment)
            pos_x = math.cos(angle) * speed
            pos_y = math.sin(angle) * speed
            direction = (pos_x, pos_y)

            # Create the fire particle with the direction
            fire_particle = Fire_Particle(
                self.game,
                self.entity.rect(),
                damage,
                speed,
                max_range,
                self.special_attack,
                direction,  # Pass the direction here
                self.entity
            )

            self.game.item_handler.Add_Item(fire_particle)

    def Set_Special_Attack(self, offset = (0,0)):
        super().Set_Special_Attack(offset)
        self.offset = offset

    def Set_Equip(self, state):
        super().Set_Equip(state)

        if state:
            self.game.player.Update_Light_Source(8)
        else:
            self.game.player.Update_Light_Source(4)
            

    def Place_Down(self):
        # Parent class Place_down function
        if not super().Place_Down():
            return False

        
        # Set the player light to False to trigger a general update of the light
        # levels around the player and move the torch light to the new location
        # self.game.player.Set_Light_State(False)
        self.game.light_handler.Add_Light_Source(self.light_source)
        self.light_source.Move_Light(self.pos, self.tile)
        
        return True
