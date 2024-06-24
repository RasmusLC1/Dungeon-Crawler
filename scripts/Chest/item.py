import random
import math
import pygame

class Item:
    def __init__(self, game, pos, type, quality):
        self.game = game
        self.type = type
        self.quality = quality
        self.pos = pos
        self.active = True
        self.animation = 0
        self.animation_cooldown = 0
        self.size = (8,8)


    def Update(self):
        pass

    def Pick_Up(self):
        if self.rect().colliderect(self.game.player.rect()):
            if self.game.inventory.Add_Item(self):
                self.active = False

    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = 50
            self.animation = random.randint(0,8)
    
    def Move_Legal(self, mouse, player_pos, tilemap):
        mouse_pos = mouse.mpos

        distance = math.sqrt((player_pos[0] - mouse_pos[0]) ** 2 + (player_pos[1] - mouse_pos[1]) ** 2)
        if distance < 40:
            for rect in tilemap.floor_rects_around(mouse_pos):
                if not self.rect().colliderect(rect):
                    return False

            for rect in tilemap.physics_rects_around(mouse_pos):
                if self.rect().colliderect(rect):
                    return False
            return True
        else:
            return False
    
    def Move(self, mouse_pos):
            self.pos = mouse_pos


    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def render(self, surf, offset=(0, 0)):
        item_image = pygame.transform.scale(self.game.assets[self.type][self.animation], self.size)
        
        surf.blit(item_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))


    def render_out_of_bounds(self, player_pos, mouse_pos, surf, offset = (0,0)):
        distance = 100 - math.sqrt((player_pos[0] - mouse_pos[0]) ** 2 + (player_pos[1] - mouse_pos[1]) ** 2)
        item_image = self.game.assets[self.type][self.animation].convert_alpha()
        item_image.set_alpha(distance)
        item_image = pygame.transform.scale(item_image, self.size)


        
        
        surf.blit(item_image, (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1]))