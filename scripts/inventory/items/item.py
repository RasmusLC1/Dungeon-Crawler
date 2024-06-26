import random
import math
import pygame
from scripts.entities.entities import PhysicsEntity



class Item(PhysicsEntity):
    def __init__(self, game, type, pos, amount):
        super().__init__(game, type, pos, (10,10))
        self.game = game
        self.sub_type = ''
        self.used = False
        self.picked_up = True
        self.animation = 0
        self.animation_cooldown = 0
        self.amount = amount
        self.max_amount = 0
        

    def Activate(self):
        pass

    def Update(self):
        pass

    def Pick_Up(self):
        
        if self.rect().colliderect(self.game.player.rect()):
            if self.game.inventory.Add_Item(self):
                self.picked_up = False

    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = 50
            self.animation = random.randint(0,8)


    def Distance(self, player_pos, mouse_pos):
        return math.sqrt((player_pos[0] - mouse_pos[0]) ** 2 + (player_pos[1] - mouse_pos[1]) ** 2)
    
    def Set_Amount(self, amount):
        self.amount = min(self.max_amount, amount)
    
    def Increase_Amount(self, amount):
        self.amount = min(self.max_amount, self.amount + amount)
    
    # Check for out of bounds, return true if valid, else false
    def Move_Legal(self, mouse_pos, player_pos, tilemap):

        
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

    
    # Rener legal position
    def render(self, surf, offset=(0, 0)):
        item_image = pygame.transform.scale(self.game.assets[self.sub_type][self.animation], self.size)
        
        surf.blit(item_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

    # Render item with fadeout if it's in an illegal position
    def render_out_of_bounds(self, player_pos, mouse_pos, surf, offset = (0,0)):
        # Calclate distance between player and mouse
        distance = max(20, 100 - self.Distance(player_pos, mouse_pos))
        item_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        item_image.set_alpha(distance)
        item_image = pygame.transform.scale(item_image, self.size)

        # Render on Mouse position as the item position is not being updated
        surf.blit(item_image, (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1]))