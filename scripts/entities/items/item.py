import random
import math
import pygame
from scripts.entities.entities import PhysicsEntity
from scripts.engine.assets.keys import keys

class Item(PhysicsEntity):
    def __init__(self, game, type, sub_category, pos, size, amount = 1, add_to_tile = True, value = 100):
        super().__init__(game, type, 'item', pos, size, sub_category)
        self.game = game
        self.sub_type = type
        self.used = False
        self.picked_up = False
        self.clicked = False # Used for if the item is active
        self.move_inventory_slot = False # Check for if the item is being moved to a new inventory slot
        self.inventory_type = None
        self.inventory_index = None
        self.activate_cooldown = 0
        self.animation_cooldown = 0
        self.animation_cooldown_max = 50
        self.amount = amount
        self.max_amount = 1
        self.max_animation = 0
        self.animation = random.randint(0, self.max_animation)
        self.nearby_entities = []
        self.delete_countdown = 0
        self.value = value # Placeholder gold value
        self.is_projectile = False
        self.Set_Sprite()
        if add_to_tile:
            self.game.tilemap.Add_Entity_To_Tile(self.tile, self)


    def Save_Data(self):
        super().Save_Data()
        self.saved_data['sub_type'] = self.sub_type
        self.saved_data['sub_category'] = self.sub_category
        self.saved_data['used'] = self.used
        self.saved_data['picked_up'] = self.picked_up
        self.saved_data['inventory_type'] = self.inventory_type
        self.saved_data['amount'] = self.amount
        self.saved_data['inventory_index'] = self.inventory_index

    
    def Load_Data(self, data):
        super().Load_Data(data)
        self.sub_type = data['sub_type']
        self.sub_category = data['sub_category']
        self.used = data['used']
        self.picked_up = data['picked_up']
        self.inventory_type = data['inventory_type']
        self.amount = data['amount']
        self.inventory_index = data['inventory_index']
        
    def Update(self):
        self.Update_Activate_Cooldown()

    def Update_In_Inventory(self):
        pass

    
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
        if not self.game.inventory.Add_Item(self):
            return None
        
        self.picked_up = True
        self.Remove_Tile()

        self.game.entities_render.Remove_Entity(self)

        self.game.sound_handler.Play_Sound('item_pickup', 0.4)

        return self.game.player
        

         

    # TODO: Might crash, need to update traps or remove damage
    def Place_Down(self):
        # nearby_traps = self.game.trap_handler.Find_Nearby_Traps(self, 3)
        # for trap in nearby_traps:
        #     trap.Update(self)
        self.Set_Tile()
        self.picked_up = False
        self.in_inventory = False
        self.game.sound_handler.Play_Sound('item_placedown', 0.2)
        return True

    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = self.animation_cooldown_max
            self.animation = random.randint(0,self.max_animation)
            self.Set_Entity_Image()

    

    def Distance(self, start_pos, target_pos):
        return math.sqrt((start_pos[0] - target_pos[0]) ** 2 + (start_pos[1] - target_pos[1]) ** 2)
    
    def Set_Amount(self, amount):
        self.amount = min(self.max_amount, amount)

    # Setting the initial sprite type from assets, only called during initial setup
    def Set_Sprite(self):
        self.sprite = self.game.assets[self.sub_type]
        self.Set_Entity_Image()

    # Setting the item image and scaling it
    def Set_Entity_Image(self):
        try:
            item_image = self.sprite[self.animation].convert_alpha()
            self.entity_image = pygame.transform.scale(item_image, self.size)
        except Exception as e:
            print(f'SET Entity image failed {e}', self.type, self.pos, self.animation, self.max_animation, self.size, self.entity_image, self.sprite)

    
    def Increase_Amount(self, amount):
        self.amount = min(self.max_amount, self.amount + amount)

    def Decrease_Amount(self, amount):
        self.amount = max(0, self.amount - amount)
        if self.amount <= 0:
            self.used = True

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

        new_tile_key = str(int(self.pos[0] // self.game.tilemap.tile_size)) + ';' + str(int(self.pos[1] // self.game.tilemap.tile_size))
        new_tile = self.game.tilemap.Current_Tile(new_tile_key)
        if not (new_tile, self.tile):
            return
        if new_tile_key != self.tile.pos:
            self.game.tilemap.Remove_Entity_From_Tile(self.tile, self.ID)
            self.game.tilemap.Add_Entity_To_Tile(new_tile, self)
            self.tile = new_tile

    

    def Update_Delete_Cooldown(self):
        if not self.delete_countdown:
            return False
        self.delete_countdown = max(0, self.delete_countdown - 1)

        if self.delete_countdown <= 0:
            self.Delete_Item()
        return True

    def Set_Delete_Countdown(self, time):
        self.delete_countdown = time
    
    def Delete_Item(self):
        self.game.item_handler.Remove_Item(self, True)
        
    # Destroy item when damaged
    def Damage_Taken(self, damage):
        self.game.item_handler.Remove_Item(self, True)
    
    def Render(self, surf, offset=(0, 0)):
        
        if self.picked_up:
            self.Render_Inventory(surf, offset)
        else:
            self.Render_Floor(surf, offset)


    # Render legal position
    def Render_Inventory(self, surf, offset=(0, 0)):
        surf.blit(self.entity_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        

    def Render_Floor(self, surf, offset=(0, 0)):
        
        if not self.Update_Light_Level():
            return
        
        self.Update_Dark_Surface()
        
        # Render the item
        surf.blit(self.rendered_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))


    # Render item with fadeout if it's in an illegal position
    def Render_Out_Of_Bounds(self, player_pos, mouse_pos, surf, offset = (0,0)):
        # Calculate distance between player and mouse
        distance = max(20, 100 - self.Distance(player_pos, mouse_pos))
        entity_image = self.entity_image.copy()
        entity_image.set_alpha(distance)

        # Render on Mouse position as the item position is not being updated
        surf.blit(entity_image, (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1]))

    
    # Render item with fadeout if it's in an illegal position
    def Render_In_Bounds(self, player_pos, mouse_pos, surf, offset = (0,0)):

        # Render on Mouse position as the item position is not being updated
        surf.blit(self.entity_image, (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1]))
    
    # Used to render effect when active
    def Render_Active(self, surf, offset = (0,0)):
        pass