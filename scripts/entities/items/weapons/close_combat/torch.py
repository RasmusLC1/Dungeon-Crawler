from scripts.entities.items.weapons.weapon import Weapon
from scripts.entities.items.weapons.magic_attacks.fire.flame_thrower import Flame_Thrower
import math


class Torch(Weapon):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'torch', 1, 2, 3, 100, 'one_handed_melee', 'fire')
        self.max_animation = 5
        self.attack_animation_max = 5
        self.light_source = self.game.light_handler.Add_Light(self.pos, 8, self.tile)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)
        self.effect = 'fire'
        self.flame_thrower = Flame_Thrower(self.game)


    # Pick up the torch and update the general light in the area
    def Pick_Up(self):
        if not super().Pick_Up():
            return
        self.game.light_handler.Remove_Light(self.light_source)




    def Special_Attack(self):
        if self.special_attack <= 0 or not self.equipped:
            self.light_source.Update_Light_Level(8)
            self.Reset_Special_Attack()
            return
        self.special_attack = self.flame_thrower.Particle_Creation(self.entity, self.special_attack)


    def Set_Special_Attack(self, offset = (0,0)):
        super().Set_Special_Attack(offset)

    def Set_Equip(self, state):
        super().Set_Equip(state)

        if state:
            self.game.player.Update_Light_Source(12)
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
