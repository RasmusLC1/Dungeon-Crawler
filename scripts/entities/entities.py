import math
import random
import pygame

from scripts.engine.particles.particle import Particle


class PhysicsEntity:
    def __init__(self, game, type, category, pos, size):
        self.game = game
        self.ID = random.randint(1, 10000000)
        self.category = category # Category = Potion, enemy, player, etc
        self.type = type # Type = Specific type of entity
        self.pos = list(pos)
        self.size = size
        self.active = 0
        self.light_level = 0
        self.invincible = False # If something needs to be indestructable
        # self.game.entities_render.Add_Entity(self)
        self.render = True
        self.Set_Tile()
        self.saved_data = {}


    def Save_Data(self):
        self.saved_data['category'] = self.category
        self.saved_data['type'] = self.type
        self.saved_data['pos'] = self.pos
        self.saved_data['size'] = self.size
        self.saved_data['active'] = self.active
        self.saved_data['light_level'] = self.light_level
        self.saved_data['render'] = self.render

    
    def Load_Data(self, data):
        self.saved_data['category'] = self.category
        self.saved_data['type'] = self.type
        self.pos = data['pos']
        self.size = data['size']
        self.active = data['active']
        self.light_level = data['light_level']
        self.render = data['render']
        self.Set_Tile()



    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Set_Active(self, duration):
        self.active = duration

    def Reduce_Active(self):
        self.active -= 1

        
    def Update(self):
        pass

    def Damage_Taken(self, damage):
        pass

    def Set_Effect(self, effect, duration):
        pass
    
    def Set_Tile(self):
        self.tile = str(int(self.pos[0]) // self.game.tilemap.tile_size) + ';' + str(int(self.pos[1]) // self.game.tilemap.tile_size)
        tile = self.game.tilemap.Current_Tile(self.tile)
        if not tile:
            return
        tile.Add_Entity(self)

    def Reset_Effects(self):
        # Status Effects
        self.is_on_fire = 0
        self.poisoned = 0
        self.is_on_ice = 0
        self.frozen = 0 
        self.wet = 0 

    def Set_Active(self, value):
        self.active = value

    def Set_Light_Level(self, value):
        self.light_level = value

    def Update_Light_Level(self):
        # Set the light level based on the tile that the entity is placed on
        tile = self.game.tilemap.Current_Tile(self.tile)
        if not tile:
            return True
        if tile.light_level == self.light_level:
            return True
        
        new_light_level = min(255, tile.light_level * 30)
        if self.light_level < new_light_level:
            self.Set_Light_Level(self.light_level + 5)
        elif self.light_level > new_light_level:
            self.Set_Light_Level(self.light_level - 5)
        self.light_level = abs(self.light_level - 255)
        # 75 is the darkest level we want
        self.light_level = max(75, 255 - self.light_level)
        

        if self.light_level <= 75:
            return False
        else:
            return True

    def Render(self, surf, offset=(0, 0)):
        pass