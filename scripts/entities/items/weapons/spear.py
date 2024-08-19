from scripts.entities.items.weapons.weapon import Weapon
import math
import pygame

class Spear(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 8, 10, 'two_handed_melee')
        self.max_animation = 3
        self.attack_animation_max = 3
        self.return_to_holder = False
        self.distance_from_player = 0
        
    # TODO: Implement this more widely with weapons and player
    def Point_Towards_Mouse(self):
        dx = self.game.mouse.mpos[0] - self.entity.pos[0]
        dy = self.game.mouse.mpos[1] - self.entity.pos[1]
        # Calculate the angle in degrees
        self.rotate = math.degrees(math.atan2(dy, dx)) + 90
        self.rotate *= -1


    def Place_Down(self):
        # Parent class Place_down function
        super().Place_Down()
        return False

    def Set_Attack(self):
        super().Set_Attack()
        if self.attacking == 0 or self.range == 0 or self.attack_animation_time == 0:
            return
        self.attack_animation_time = int(self.attacking / self.range / self.attack_animation_time) 
    
    def Set_Special_Attack(self, offset= (0,0)):
        super().Set_Special_Attack(offset)
        self.Point_Towards_Mouse()


    def Throw_Weapon(self):
        if self.special_attack:
            speed = 1
            dir_x = self.pos[0] + self.attack_direction[0] * speed
            dir_y = self.pos[1] + self.attack_direction[1] * speed
            self.Move((dir_x, dir_y))
            self.special_attack = max(0, self.special_attack - speed)

            

    def Special_Attack(self):
        if not self.special_attack or not self.equipped:
            return
        self.Drop_Weapon_From_Weapon_Inventory()

        
        # distance_player = math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2)
        
    
    def Drop_Weapon_From_Weapon_Inventory(self):
        active_inventory = self.game.weapon_inventory.active_inventory
        weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
        self.game.player.Remove_Active_Weapon(self.inventory_type)
        weapon_inventory.Remove_Item(self, True)
        self.game.item_handler.Add_Item(self)
        self.game.entities_render.Add_Entity(self)
        self.picked_up = True
        self.equipped = False

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()
        # Reset the attack logic
        if not self.attacking:
            self.return_to_holder = False
            self.distance_from_player = 0
            return
        
        # Not updating the animation as the timer hasn't been hit yet
        if not self.attack_animation_counter >= self.attack_animation_time - 1:
            return
        
        
        self.Attack_Direction()
        if not self.return_to_holder:
            self.distance_from_player += 1
            if self.distance_from_player <= self.range:
                return
            elif self.distance_from_player > self.range:
                self.return_to_holder = True
                return
        else:
            self.distance_from_player -= 1


            if self.distance_from_player <= 0:
                self.return_to_holder = False
                
            
    def Attack_Direction(self):
            attack_direction = self.entity.attack_direction
            if abs(attack_direction[0]) >= abs(attack_direction[1]):                
                if attack_direction[0] >= 0:
                    self.rotate = 0
                    self.Move((self.pos[0] + self.distance_from_player, self.pos[1] + 5))
                else:
                    self.rotate = 0
                    self.flip_image = True
                    self.Move((self.pos[0] - self.distance_from_player, self.pos[1] + 5))
            else:
                
                if attack_direction[1] >= 0:
                    self.rotate = -90
                    self.Move((self.pos[0] - 5, self.pos[1] + self.distance_from_player))
                else:
                    self.rotate = 90
                    self.Move((self.pos[0] - 5, self.pos[1] - self.distance_from_player))

    # For some reason calling the parent function does not work for render
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

        if self.special_attack:
            
            weapon_image = pygame.transform.rotate(weapon_image, self.rotate)

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
