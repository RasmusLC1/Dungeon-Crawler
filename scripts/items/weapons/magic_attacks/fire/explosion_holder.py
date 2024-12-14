from scripts.items.item import Item
import pygame
import math

class Fire_Explosion(Item):
    def __init__(self, game, pos, effect, entity = None):
        super().__init__(game, 'fire_explosion', 'magic_attack', pos, (32, 32))
        self.max_animation = 7
        self.animation = 0
        self.animation_cooldown = 0
        self.animation_cooldown_max = 5
        self.entity = entity
        self.delete_countdown = self.max_animation * self.animation_cooldown_max
        self.effect = effect
        self.size =( self.effect * self.size[0], self.effect * self.size[1])
        # self.light_source = self.game.light_handler.Add_Light(self.pos, 8, self.tile)
        # self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)
        self.Initialise_Explosion()

    def Initialise_Explosion(self):
        self.Find_Nearby_Entities(self.effect)
        self.Check_Player_Distance()
        entity_ID = self.Get_Entity_ID()
        for entity in self.nearby_entities:
            if entity.ID == entity_ID:
                continue
            if not self.Ray_Cast_Towards_Entity(entity):
                continue
            distance = self.Distance(self.pos, entity.pos)
            damage = round(max(5, min(50, self.effect * 32 - distance)))
            entity.Damage_Taken(damage, (0,0))

    def Check_Player_Distance(self):
        distance = self.Distance(self.pos, self.game.player.pos)
        if distance <= self.effect * 32:
            self.nearby_entities.append(self.game.player)
        

    def Get_Entity_ID(self):
        if not self.entity:
            return 0
        
        return self.entity.ID

    def Ray_Cast_Towards_Entity(self, entity):
        start_pos = self.pos
        end_pos = entity.pos

        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        distance = math.sqrt(dx * dx + dy * dy)
        angle = math.atan2(dy, dx)

        step_size = self.game.tilemap.tile_size  # Adjust as needed
        steps = self.effect

        for i in range(steps):
            pos_x = start_pos[0] + math.cos(angle) * step_size * i
            pos_y = start_pos[1] + math.sin(angle) * step_size * i
            tile_key = str(int(pos_x) // self.game.tilemap.tile_size) + ';' + str(int(pos_y) // self.game.tilemap.tile_size)


            # If Check_Tile returns False, it means a tile blocked the ray
            if not self.Check_Tile(tile_key):
                return False  # Ray is blocked

        return True  # Reached the entity without tile blockage

    def Check_Tile(self, tile):
        tile = self.game.tilemap.Current_Tile(tile)
        if tile:
            if not tile.type:
                print(tile)
                return False
            
            if tile.physics:
                return False
            
        return True

    def Update_Animation(self):
        # if self.delete_countdown <= 1:
        #     self.game.light_handler.Remove_Light(self.light_source)
            
        
        if self.animation_cooldown >= self.animation_cooldown_max:
            self.animation_cooldown = 0
            self.animation = min(self.animation + 1, self.max_animation)
            return
        self.animation_cooldown += 1

    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):
        self.Update_Animation()
        weapon_image = self.game.assets[self.type][self.animation].convert_alpha()
        weapon_image = pygame.transform.scale(weapon_image, self.size)
        width, height = self.size

        # Adjust position to center the image
        x = self.pos[0] - offset[0] - width // 2
        y = self.pos[1] - offset[1] - height // 2

        surf.blit(weapon_image, (x, y))

    def Update_Text_Box(self, hitbox_1, hitbox_2):
        pass
