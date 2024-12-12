import random
import math
import pygame
from scripts.entities.entities import PhysicsEntity
from scripts.items.utility.textbox import Text_Box



class Item(PhysicsEntity):
    def __init__(self, game, type, sub_category, pos, size, amount = 1, add_to_tile = True):
        super().__init__(game, type, 'item', pos, size)
        self.game = game
        self.sub_type = type
        self.sub_category = sub_category
        self.used = False
        self.picked_up = False
        self.move_inventory_slot = False # Check for if the item is being moved to a new inventory slot
        self.inventory_type = None
        self.inventory_index = None
        self.activate_cooldown = 0
        self.animation_cooldown = 0
        self.animation_cooldown_max = 50
        self.amount = amount
        self.max_amount = 0
        self.damaged = False
        self.max_animation = 0
        self.animation = random.randint(0, self.max_animation)
        self.nearby_entities = []
        self.delete_countdown = 0
        self.value = 100 # Placeholder gold value
        self.text_box = Text_Box(self.game, self)
        if add_to_tile:
            self.game.tilemap.Add_Entity_To_Tile(self.tile, self)


    def Save_Data(self):
        super().Save_Data()
        self.saved_data['ID'] = self.ID
        self.saved_data['sub_type'] = self.sub_type
        self.saved_data['sub_category'] = self.sub_category
        self.saved_data['used'] = self.used
        self.saved_data['picked_up'] = self.picked_up
        self.saved_data['inventory_type'] = self.inventory_type
        self.saved_data['amount'] = self.amount
        self.saved_data['damaged'] = self.damaged
        self.saved_data['inventory_index'] = self.inventory_index

    
    def Load_Data(self, data):
        super().Load_Data(data)
        self.ID = data['ID']
        self.sub_type = data['sub_type']
        self.sub_category = data['sub_category']
        self.used = data['used']
        self.picked_up = data['picked_up']
        self.inventory_type = data['inventory_type']
        self.amount = data['amount']
        self.damaged = data['damaged']
        self.inventory_index = data['inventory_index']

    def Update(self):
        self.Update_Activate_Cooldown()

    def Update_Text_Box(self, hitbox_1, hitbox_2):
        if self.text_box.Update(hitbox_1, hitbox_2):
            return self
        else:
            return None
    
    def Activate(self):
        if self.activate_cooldown:
            return False
        
        self.activate_cooldown = 60
        return True

    def Update_Activate_Cooldown(self):
        if self.activate_cooldown <= 0:
            return
        self.activate_cooldown = max(0, self.activate_cooldown - 1)

    def Set_Inventory_Index(self, index):
        self.inventory_index = index
    
    def Find_Nearby_Entities(self, distance):
        self.nearby_entities = self.game.enemy_handler.Find_Nearby_Enemies(self, distance)


    def Pick_Up(self):
        # First Check if the player is colliding with the object as this is priority
        if self.game.item_inventory.Add_Item(self):
            self.picked_up = True
            self.game.entities_render.Remove_Entity(self)
            self.game.tilemap.Remove_Entity_From_Tile(self.tile, self.ID)

            return self.game.player
        
        self.Find_Nearby_Entities(2)
        for entity in self.nearby_entities:
            if not self.rect().colliderect(entity.rect()):
                continue
            if self.game.item_inventory.Add_Item(self):
                self.picked_up = False
                self.game.entities_render.Remove_Entity(self)
                self.game.tilemap.Remove_Entity_From_Tile(self.tile, self.ID)

                return entity
                
        return None

    def Place_Down(self):
        nearby_traps = self.game.trap_handler.Find_Nearby_Traps(self.pos, 3)
        for trap in nearby_traps:
            trap.Update(self)
            if self.damaged:
                return False
        self.Set_Tile()
        return True

    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = self.animation_cooldown_max
            self.animation = random.randint(0,self.max_animation)


    def Distance(self, start_pos, target_pos):
        return math.sqrt((start_pos[0] - target_pos[0]) ** 2 + (start_pos[1] - target_pos[1]) ** 2)
    
    def Set_Amount(self, amount):
        self.amount = min(self.max_amount, amount)
    
    def Increase_Amount(self, amount):
        self.amount = min(self.max_amount, self.amount + amount)

    def Decrease_Amount(self, amount):
        self.amount = min(self.max_amount, self.amount - amount)

    def Set_Inventory_Type(self, inventory_type):
        self.inventory_type = inventory_type
    
    # Check for out of bounds, return true if valid, else false
    def Move_Legal(self, mouse_pos, player_pos, tilemap, offset = (0,0)):
        # Check if distance is legal, update to account for player strength later
        if self.Distance(player_pos, mouse_pos) < 80:
            
            for rect in tilemap.physics_rects_around(mouse_pos):
                if self.rect().colliderect(rect):
                    return False
            return True
        
        else:
            return False
    
    # Update position
    def Move(self, new_pos):
        self.pos = new_pos

    def Update_Tile(self, new_pos):

        new_tile = str(int(new_pos[0] // self.game.tilemap.tile_size)) + ';' + str(int(new_pos[1] // self.game.tilemap.tile_size))
        if new_tile != self.tile:
            self.game.tilemap.Remove_Entity_From_Tile(self.tile, self.ID)
            self.game.tilemap.Add_Entity_To_Tile(new_tile, self)
            self.tile = new_tile

    def Update_Delete_Cooldown(self):
        if not self.delete_countdown:
            return False
        self.delete_countdown = max(0, self.delete_countdown - 1)
        return True

    def Set_Delete_Countdown(self, time):
        self.delete_countdown = time

    def Damage_Taken(self, damage):
        self.damaged = damage
    
    def Render(self, surf, offset=(0, 0)):
        if self.picked_up:
            self.Render_Inventory(surf, offset)
        else:
            self.Render_Floor(surf, offset)


    # Render legal position
    def Render_Inventory(self, surf, offset=(0, 0)):
        item_image = pygame.transform.scale(self.game.assets[self.sub_type][self.animation], self.size)  
        surf.blit(item_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        

    def Render_Floor(self, surf, offset=(0, 0)):
        
        if not self.Update_Light_Level():
            return
        # Set image
        item_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        item_image =  pygame.transform.scale(self.game.assets[self.sub_type][self.animation], self.size)  
        
        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))

        if not alpha_value:
            return
        
        item_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(self.size, pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        item_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(item_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

        

    # Render item with fadeout if it's in an illegal position
    def Render_Out_Of_Bounds(self, player_pos, mouse_pos, surf, offset = (0,0)):
        # Calculate distance between player and mouse
        distance = max(20, 100 - self.Distance(player_pos, mouse_pos))
        item_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        item_image.set_alpha(distance)
        item_image = pygame.transform.scale(item_image, self.size)

        # Render on Mouse position as the item position is not being updated
        surf.blit(item_image, (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1]))

    
    # Render item with fadeout if it's in an illegal position
    def Render_In_Bounds(self, player_pos, mouse_pos, surf, offset = (0,0)):
        item_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        item_image = pygame.transform.scale(item_image, self.size)

        # Render on Mouse position as the item position is not being updated
        surf.blit(item_image, (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1]))