from scripts.items.item import Item
import pygame
import math

class Elemental_Explosion(Item):
    def __init__(self, game, type, effect, pos, power, max_animation, animation_cooldown_max, entity = None):
        super().__init__(game, type, 'magic_attack', pos, (game.tilemap.tile_size, game.tilemap.tile_size))
        self.animation = 0
        self.animation_cooldown = 0
        self.max_animation = max_animation
        self.animation_cooldown_max = animation_cooldown_max
        self.entity = entity
        self.delete_countdown = self.max_animation * self.animation_cooldown_max
        self.power = power
        self.effect = effect
        self.size =( self.power * self.size[0], self.power * self.size[1])
        self.nearby_entities = []
        self.Initialise_Explosion()

    def Initialise_Explosion(self):
        self.Find_Nearby_Entities(self.power)
        self.Check_Player_Distance()
        entity_ID = self.Get_Entity_ID()
        for entity in self.nearby_entities:
            if entity.ID == entity_ID:
                continue
            if not self.Ray_Cast_Towards_Entity(entity):
                continue
    
    def Compute_Damage(self, entity):
        distance = self.Distance(self.pos, entity.pos)
        damage = round(max(5, min(50, self.power * 32 - distance)))
        entity.Damage_Taken(damage, (0,0))
        if self.effect:
            entity.Set_Effect(self.effect, 3)

    def Check_Player_Distance(self):
        distance = self.Distance(self.pos, self.game.player.pos)
        if distance <= self.power * self.game.tilemap.tile_size:
            self.nearby_entities.append(self.game.player)
        
    # Get ID of caster for potential immunity
    def Get_Entity_ID(self):
        if not self.entity:
            return 0
        
        return self.entity.ID

    # Raycaster to check for line of sight
    def Ray_Cast_Towards_Entity(self, entity):
        start_pos = self.pos
        end_pos = entity.pos

        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        angle = math.atan2(dy, dx)

        step_size = self.game.tilemap.tile_size  # Adjust as needed
        steps = self.power

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