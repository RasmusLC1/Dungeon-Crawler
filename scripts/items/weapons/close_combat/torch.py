from scripts.decoration.decoration import Decoration
from scripts.items.item import Item
from scripts.items.weapons.weapon import Weapon
from scripts.items.weapons.projectiles.fire_particle import Fire_Particle
import math


class Torch(Weapon):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size, 'torch', 1, 3, 5, 'one_handed_melee')
        self.max_animation = 5
        self.attack_animation_max = 5
        self.light_level = 12
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)
        self.offset = (0,0)
        self.fire_cooldown = 0
        self.effect = 'Fire'


    # Pick up the torch and update the general light in the area
    def Pick_Up(self):
        if not super().Pick_Up():
            return
        self.light_source.picked_up = True
        # self.game.player.Set_Light_State(False)
        self.game.light_handler.Remove_Light(self.light_source)
        self.game.light_handler.Restore_Light(self.light_source)

    def Update(self, offset=(0, 0)):
        super().Update(offset)
        self.light_source.Move_Light(self.pos)

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()

    def Special_Attack(self):
        if self.special_attack <= 0 or not self.equipped:
            self.light_level = 8
            return
        self.Fire_Particle_Creation()
        self.light_level = 12

    def Attack_Align_Weapon(self):
        if 'left' in self.inventory_type:
            if self.flip_image:
                self.Move((self.pos[0] - 3, self.pos[1] - 2))
            else:
                self.Move((self.pos[0] + 3, self.pos[1] - 2))
            return
        if 'right' in self.inventory_type:
            if abs(self.entity.attack_direction[0]) < abs(self.entity.attack_direction[1]):
                self.Move((self.pos[0], self.pos[1] - 2))
            elif self.flip_image:
                self.Move((self.pos[0] + 3, self.pos[1] - 2))
            else:
                self.Move((self.pos[0] + 4, self.pos[1] - 2))
            return
    
    def Set_Equipped_Position(self, direction_y):
        if 'left' in self.inventory_type:
            if direction_y < 0:
                self.Move((self.entity.pos[0] - 5 , self.entity.pos[1] - 10 ))
            else:
                self.Move((self.entity.pos[0] + 5 , self.entity.pos[1] - 10))
        elif 'right' in self.inventory_type:
            if  direction_y < 0:
                self.Move((self.entity.pos[0] + 7, self.entity.pos[1] - 10))
            else:
                self.Move((self.entity.pos[0] - 7, self.entity.pos[1] - 10))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)


    def Fire_Particle_Creation(self):
        if self.fire_cooldown:
            self.fire_cooldown -= 1
            return
        else:
            self.fire_cooldown = 3
            self.special_attack -= 20
            
        # Basic raycasting attributes
        num_lines = 8 # Define the number of lines and the spread angle (in degrees)
        spread_angle = 50  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1) # Calculate the angle increment between each line
        # Calculate the starting angle
        base_angle = math.atan2(self.attack_direction[1], self.attack_direction[0])
        start_angle = base_angle - math.radians(spread_angle / 2)
         # Look for tiles that hit the rays
        for j in range(num_lines):
            angle = start_angle + j * math.radians(angle_increment)
            pos_x = math.cos(angle)
            pos_y = math.sin(angle)
            fire_particle = Fire_Particle(self.game, self.entity.rect().midtop, (2,2), 'fire_particle', 2, 4, 30, 'particle', self.special_attack, (pos_x, pos_y), self.entity)
            self.game.item_handler.Add_Item(fire_particle)
        

    def Set_Special_Attack(self, offset = (0,0)):
        super().Set_Special_Attack(offset)
        self.offset = offset

    def Place_Down(self):
        # Parent class Place_down function
        super().Place_Down()

        
        # Set the player light to False to trigger a general update of the light
        # levels around the player and move the torch light to the new location
        self.game.player.Set_Light_State(False)
        self.light_source.Move_Light(self.pos)
        self.light_source.picked_up = False
        
        return False