from scripts.decoration.decoration import Decoration
from scripts.entities.items.item import Item
from scripts.entities.items.weapons.weapon import Weapon
from scripts.entities.items.weapons.projectiles.fire_particle import Fire_Particle
import random
import pygame


class Torch(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 1, 3, 5, 'one_handed_melee')
        self.max_animation = 5
        self.attack_animation_max = 5
        self.light_level = 8
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)
        self.offset = (0,0)
        self.Set_Effect('Fire')


    # Pick up the torch and update the general light in the area
    def Pick_Up(self):
        if not super().Pick_Up():
            return
        self.light_source.picked_up = True
        self.game.player.Set_Light_State(False)
        self.game.light_handler.Remove_Light(self.light_source)
        self.game.light_handler.Restore_Light(self.light_source)

    def Update(self, offset=(0, 0)):
        super().Update(offset)
        self.light_source.Move_Light(self.pos)

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()

    def Special_Attack(self):
        if not self.special_attack or not self.equipped:
            return
        fire_particle = Fire_Particle(self.game, self.pos, (2,2), 'fire_particle', self.special_attack, 1, self.special_attack, 'fire_particle', self.entity, self.special_attack, self.offset)
        self.game.item_handler.Add_Item(fire_particle)
        self.special_attack = 0

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
