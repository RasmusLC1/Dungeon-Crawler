import pygame
from collections import deque

class PhysicsEntity:
    _id_counter = 0  # Class variable to generate unique IDs
    _available_IDs = deque() # List of ID's made available on deletion, deque for performance

    def __init__(self, game, type, category, pos, size, sub_category = None):
        self.game = game
        self.Set_ID()
        self.category = category # Category = Potion, enemy, player, etc
        self.sub_category = sub_category # Subcategory = variant of the category item -> weapon item 
        self.type = type # Type = Specific type of entity
        self.sprite = None # The type of animation used
        self.entity_image = None # the full animation with animation frame
        self.rendered_image = None # the actual image being rendered to screen
        self.render_needs_update = True
        self.pos = list(pos)
        self.size = size
        self.active = 0
        self.light_level = 0
        self.render = True
        self.Set_Tile()
        self.saved_data = {}
        self.text_box = None
        self.description = ''


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

    # Should only be called during initalisation
    def Set_ID(self):
        if PhysicsEntity._available_IDs:
            self.ID = PhysicsEntity._available_IDs.popleft()  # O(1) removal
            return
        
        self.ID = PhysicsEntity._id_counter
        PhysicsEntity._id_counter += 1

    # Called when entity is deleted by garbage collection
    def __del__(self):
        PhysicsEntity._available_IDs.append(self.ID)

    # Called when entity is deleted
    # Manually deletes the entity and returns the ID to the pool
    def Delete(self):
        PhysicsEntity._available_IDs.append(self.ID)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Set_Active(self, duration):
        if duration != self.active:
            self.active = duration
            self.render_needs_update = True
            

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

    def Set_Sprite(self):
        pass
        # self.sprite = self.game.assets[self.type]



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

    def Update_Dark_Surface(self, alpha_value):
        # Set image
        self.rendered_image = self.entity_image.copy()

        self.rendered_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(self.rendered_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        self.rendered_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.render_needs_update = False