import math
import random
import pygame




class PhysicsEntity:
    def __init__(self, game, type, category, pos, size, sub_category = None):
        self.game = game
        self.ID = random.randint(1, 10000000)
        self.category = category # Category = Potion, enemy, player, etc
        self.sub_category = sub_category # Subcategory = variant of the category item -> weapon item 
        self.type = type # Type = Specific type of entity
        self.pos = list(pos)
        self.size = size
        self.active = 0
        self.light_level = 0
        self.render = True
        self.Set_Tile()
        self.saved_data = {}
        self.text_box = None


    def Save_Data(self):
        self.saved_data['category'] = self.category
        self.saved_data['type'] = self.type
        self.saved_data['pos'] = self.pos
        self.saved_data['size'] = self.size
        self.saved_data['active'] = self.active
        self.saved_data['light_level'] = self.light_level
        self.saved_data['render'] = self.render

    
    def Load_Data(self, data):
        self.category = data['category']
        self.type = data['type']
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

    def Remove_Tile(self):
        if not self.tile:
            return
        self.game.tilemap.Remove_Entity_From_Tile(self.tile, self.ID)
        self.tile = None

    def Set_Position(self, position):
        self.pos = position


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
        self.light_level = max(40, 255 - self.light_level)
        

        if self.light_level <= 40:
            return False
        else:
            return True

    def Update_Text_Box(self, hitbox_1, hitbox_2):
        if not self.text_box:
            return None
        if self.text_box.Update(hitbox_1, hitbox_2):
            return self
        else:
            return None

    def Render(self, surf, offset=(0, 0)):
        pass