from scripts.decoration.decoration import Decoration
from scripts.entities.player.items.item import Item
from scripts.entities.player.items.weapons.weapon import Weapon
import random
import pygame


class Torch(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 1, 3, 1, 'one_handed_melee')
        self.effect = 'Fire'
        self.max_animation = 5
        self.attack_animation_max = 5
        self.light_level = 8
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)

    # Pick up the torch and update the general light in the area
    def Pick_Up(self):
        if self.rect().colliderect(self.game.player.rect()):
            if self.game.item_inventory.Add_Item(self):
                self.in_inventory = True
                self.light_source.picked_up = True
                self.game.player.Set_Light_State(False)
                self.game.light_handler.Remove_Light(self.light_source)
                self.game.light_handler.Restore_Light(self.light_source)
                self.picked_up = False
                self.game.entities_render.remove(self)

    def Update(self):
        self.Set_Effect('Poison')
        super().Update()
        self.light_source.Move_Light(self.pos)

    def Update_Attack_Animation(self, entity):
        super().Update_Attack_Animation(entity)

  

    def Place_Down(self):
        # Parent class Place_down function
        super().Place_Down()

        
        # Set the player light to False to trigger a general update of the light
        # levels around the player and move the torch light to the new location
        self.game.player.Set_Light_State(False)
        self.light_source.Move_Light(self.pos)
        self.light_source.picked_up = False
        
        return False
