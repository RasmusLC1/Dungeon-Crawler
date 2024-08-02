import pygame
from scripts.entities.player.items.item import Item
from scripts.entities.entities import PhysicsEntity

class Weapon(Item):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class):
        super().__init__(game, type, pos, size, 1)
        self.damage = damage
        self.speed = speed
        self.range = range
        self.in_inventory = False
        self.equipped = False
        # Can be expanded to damaged or dirty versions of weapons later
        self.sub_type = self.type
        self.weapon_class = weapon_class


    # Add weapons from a sending inventory to a receiving inventory
    # Example: weapon_inventory (sending) -> inventory (receiving) 
    def Move_To_Other_Inventory(self, sending_inventory, receiving_inventory, offset = (0,0)):
        if self.game.mouse.left_click:
            return
        
        for inventory_slot in receiving_inventory:
            if inventory_slot.rect().colliderect(self.game.mouse.rect_pos(offset)):
                if not inventory_slot.active:
                    for weapon_inventory_slot in sending_inventory:
                        if weapon_inventory_slot.active:
                            inventory_slot.Add_Item(self)
                            weapon_inventory_slot.Remove_Item()
                            return True             
        return False



    # Check for out of bounds, return true if valid, else false
    def Move_Legal(self, mouse_pos, player_pos, tilemap, offset = (0,0)):
        # Check if the weapon can be moved to the weapon inventory
        if self.picked_up:
            active_inventory = self.game.weapon_inventory.active_inventory
            weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
            if self.equipped:
                if self.Move_To_Other_Inventory(weapon_inventory, self.game.inventory.inventory, offset):
                    self.equipped = False
                    return False
            else:
                if self.Move_To_Other_Inventory(self.game.inventory.inventory, weapon_inventory, offset):
                    self.equipped = True
                    return False



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
        
    def Place_Down(self):
        super().Place_Down()
        self.equipped = False
        return False


    def Render_In_Inventory(self, surf, offset=(0, 0)):
        item_image = pygame.transform.scale(self.game.assets[self.sub_type][self.animation], self.size)  
        surf.blit(item_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

    def Render(self, surf, offset=(0, 0)):
        # Check if item is in inventory. If yes we don't need offset, except if
        # the weapon has been picked up
        if self.in_inventory:
            if self.picked_up:
                self.Render_In_Inventory(surf, offset)
            else:
                self.Render_In_Inventory(surf)

        if not self.Update_Light_Level():
            return
        
        # Set image
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))
        weapon_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(weapon_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        weapon_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
