from scripts.decoration.decoration import Decoration
from scripts.entities.player.items.item import Item
from scripts.entities.player.items.weapons.weapon import Weapon
import random
import pygame


class Torch(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 1, 1, 1)
        self.max_animation = 7
        self.aniamtion = random.randint(0, self.max_animation)
        self.light_level = 6
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)

    def Pick_Up(self):
        if self.rect().colliderect(self.game.player.rect()):
            if self.game.inventory.Add_Item(self):
                # self.light_source.Delete_Light()
                self.game.light_handler.Remove_Light(self.light_source)
                self.picked_up = False
                self.game.entities_render.remove(self)

    def Place_Down(self):
        nearby_traps = self.game.trap_handler.find_nearby_traps(self.pos, 20)
        for trap in nearby_traps:
            trap.Update(self)
            if self.damaged:
                return True
                
        # First iteration is to update the tile underneath, second is to get the light radius
        self.light_source.Move_Light(self.pos)
        self.light_source.Move_Light(self.pos)
        print(self.light_level)
        # self.light_source.Setup_Tile_Light()
        # self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)
        return False
