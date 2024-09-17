import random
import math
import pygame
from scripts.entities.entities import PhysicsEntity
from scripts.items.utility.textbox import Text_Box




class Item(PhysicsEntity):
    def __init__(self, game, type, category, pos, size, amount):
        super().__init__(game, type, pos, size)
        self.game = game
        self.item_ID = random.randint(1, 100000000) # Create a random ID between 1 and 100 million
        self.category = category
        self.sub_type = ''
        self.used = False
        self.picked_up = True
        self.move_inventory = False # Check for if the item is being moved to a new inventory
        self.inventory_type = None
        self.animation_cooldown = 0
        self.animation_speed = 50
        self.amount = amount
        self.max_amount = 0
        self.damaged = False
        self.max_animation = 0
        self.animation = random.randint(0, self.max_animation)
        self.nearby_entities = []
        self.delete_countdown = 0
        self.text_box = Text_Box(self.game, self)

    def Update_Text_Box(self):
        self.text_box.Update(self.game.render_scroll)

    def Activate(self):
        pass
    
    def Find_Nearby_Entities(self, distance):
        # Set the player first so the player gets priority
        distance_player = math.sqrt((self.game.player.pos[0] - self.pos[0]) ** 2 + (self.game.player.pos[1] - self.pos[1]) ** 2)
        if distance_player < distance:
            self.nearby_entities.append(self.game.player)
        self.nearby_entities.extend(self.game.enemy_handler.Find_Nearby_Enemies(self, distance))


    def Pick_Up(self):
        # First Check if the player is colliding with the object as this is priority
        if self.rect().colliderect(self.game.player.rect()):
            if self.game.item_inventory.Add_Item(self):
                self.picked_up = False
                self.game.entities_render.Remove_Entity(self)
                return self.game.player
        
        self.Find_Nearby_Entities(10)
        for entity in self.nearby_entities:
            if not self.rect().colliderect(entity.rect()):
                continue
            if self.game.item_inventory.Add_Item(self):
                self.picked_up = False
                self.game.entities_render.Remove_Entity(self)
                return entity
                
        return None

    def Place_Down(self):
        nearby_traps = self.game.trap_handler.Find_Nearby_Traps(self.pos, 20)
        for trap in nearby_traps:
            trap.Update(self)
            if self.damaged:
                return True
        self.picked_up = True
        return False

    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = self.animation_speed
            self.animation = random.randint(0,self.max_animation)


    def Distance(self, player_pos, mouse_pos):
        return math.sqrt((player_pos[0] - mouse_pos[0]) ** 2 + (player_pos[1] - mouse_pos[1]) ** 2)
    
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
        if self.Distance(player_pos, mouse_pos) < 40:
            
            # Check if it it touches a floor tile
            for rect in tilemap.floor_rects_around(mouse_pos):
                if not self.rect().colliderect(rect):
                    return False
            # Check for walls
            for rect in tilemap.physics_rects_around(mouse_pos):
                if self.rect().colliderect(rect):
                    return False
            return True
        
        else:
            return False
    
    # Update position
    def Move(self, new_pos):
        self.pos = new_pos

    def Update_Delete_Cooldown(self):
        if not self.delete_countdown:
            return False
        self.delete_countdown = max(0, self.delete_countdown - 1)
        return True

    def Set_Delete_Countdown(self, time):
        self.delete_countdown = time

    def Damage_Taken(self, damage):
        self.damaged = damage
    
    # Render legal position
    def Render(self, surf, offset=(0, 0)):

        item_image = pygame.transform.scale(self.game.assets[self.sub_type][self.animation], self.size)  
        surf.blit(item_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        self.text_box.Render(surf, offset)
        

    # Render item with fadeout if it's in an illegal position
    def render_out_of_bounds(self, player_pos, mouse_pos, surf, offset = (0,0)):
        # Calclate distance between player and mouse
        distance = max(20, 100 - self.Distance(player_pos, mouse_pos))
        item_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        item_image.set_alpha(distance)
        item_image = pygame.transform.scale(item_image, self.size)

        # Render on Mouse position as the item position is not being updated
        surf.blit(item_image, (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1]))