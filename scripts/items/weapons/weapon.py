from scripts.decoration.decoration import Decoration
from scripts.items.item import Item
from scripts.engine.clatter import Clatter
import random
import pygame
import math


class Weapon(Item):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class, damage_type = 'slash'):
        super().__init__(game, type, 'weapon', pos, size, 1)
        self.damage = damage # The damage the wepaon does
        self.speed = speed # Speed of the weapon
        self.range = range # Range of the weapon
        self.entity = None # Entity that holds the weapon
        self.effect = damage_type # Special effects, like poision, ice, fire etc
        self.in_inventory = False # Is the weapon in an inventory
        self.equipped = False # Is the weapon currently equipped and can be used to attack
        self.hold_down = 0 # Timer for charge attacks
        self.hold_down_counter = 0 # Timer for charge attacks
        self.animation_speed = 30 # Animation speed that it cycles through animations
        self.max_animation = 0 # Max amount of animations
        self.attacking = 0 # The time it takes for the attack to complete
        self.attack_animation = 0 # Current attack animation
        self.attack_animation_max = 1 # Maximum amount of attack animations
        self.attack_animation_time = 0 # Time to shift to new animation
        self.attack_animation_counter = 0 # Animation countdown that ticks up to animation time
        self.enemy_hit = False # Prevent double damage on attacks
        self.flip_image = False # Check if image is flipped
        self.rotate = 0 # Rotation value of weapon
        self.distance_from_entity = 0 # Weapon's distance from entity, in case it needs to be retracted
        self.nearby_enemies = [] # Nearby enemies that the weapon can interact with
        # Can be expanded to damaged or dirty versions of weapons later
        self.weapon_class = weapon_class # Determines how it's wielded, one or two hand, bow, etc
        
        self.charge_time = 0  # Tracks how long the button is held
        self.max_charge_time = 100  # Maximum time to fully charge
        self.is_charging = False  # Tracks if the player is charging
        self.attack_ready = False  # Track when the attack is ready to be triggered
        self.charged_attack = False  # Determine if a charged attack should occur
        self.special_attack = 0 # special attack counter
        self.return_to_holder = False # Return the weapon to original positon after stab


    def Save_Data(self):
        if self.entity:
            if self.entity.category == 'enemy':
                return
        super().Save_Data()
        self.saved_data['damage'] = self.damage
        self.saved_data['speed'] = self.speed
        self.saved_data['range'] = self.range
        self.saved_data['effect'] = self.effect
        self.saved_data['in_inventory'] = self.in_inventory
        self.saved_data['equipped'] = self.equipped
        self.saved_data['enemy_hit'] = self.enemy_hit

    
    def Load_Data(self, data):
        super().Load_Data(data)
        self.damage = data['damage']
        self.speed = data['speed']
        self.range = data['range']
        self.effect = data['effect']
        self.in_inventory = data['in_inventory']
        self.equipped = data['equipped']
        self.enemy_hit = data['enemy_hit']

   
    # General Update function
    def Update(self, offset = (0,0)):
        super().Update()
        self.Update_Animation()
        self.Special_Attack()
        if not self.entity:
            return False
        self.Update_Flip()
        
        self.Charge_Attack(offset)

        return True

        

    # Reset the attack charge
    def Reset_Charge(self):
        self.is_charging = 0
        self.charge_time = 0
        return

    # Change the rotation
    def Change_Rotate(self, change):
        self.rotate += change

    # Update the attack logic
    def Update_Attack(self):
        if not self.attacking:
            return False
            
        self.Update_Attack_Animation()
        self.Attack_Collision_Check()
        self.Attack_Align_Weapon()
        return True

    # Initialise the attack
    def Set_Attack(self):
        if not self.attack_ready:
            return
        if not self.Check_Entity_Cooldown():
            return
        
        self.attacking = max(self.attack_animation_max * 3, int(100 / self.speed))
        self.enemy_hit = False  # Reset at the start of a new attack
        self.attack_animation_time = int(self.attacking / self.attack_animation_max)
        self.charge_time = 0  # Reset charge time
        self.rotate = 0
        self.Set_Attack_Ready(False) # Reset attack trigger
        self.charged_attack = False  # Reset charged attack flag
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, self.range * 8) # Find nearby enemies to attack

    def Set_Damage(self, damage):
        self.damage = damage
    
    def Special_Attack(self):
        pass
    
    # Handle weapon charging
    def Charge_Attack(self, offset = (0, 0)):

        try:
            if 'player' == self.entity.type:
                if not self.inventory_type:
                    return
                self.Set_Charging_Player()
            elif 'enemy' == self.entity.category:
                self.Set_Charging_Enemy()
        except TypeError as e:
            print(f"Entity neither enemy nor player: {e}")

        
        if self.is_charging:
            # Increase charge time while holding the button
            self.charge_time += 1
            if self.charge_time >= self.max_charge_time:
                self.charge_time = self.max_charge_time  # Cap the charge time
                self.charged_attack = True  # Mark the attack as charged
        else:
            # If the button is released
            if self.charge_time > 0 and self.charge_time < 20:
                self.Set_Attack_Ready(True)  # Ready to trigger an attack
                self.Set_Attack()  # Trigger the attack
            if self.charge_time > 20:
                self.Set_Special_Attack(offset)
            self.charge_time = 0  # Reset the charge time

    # Initialise special attack
    def Set_Special_Attack(self, offset = (0, 0)):
        if not self.entity:
            return
        self.entity.Attack_Direction_Handler(offset)
        self.Set_Block_Direction()
        self.special_attack = self.charge_time

    # Initialise the charging of the weapon
    def Set_Charging_Player(self):
        # Detect if the player is holding down the button
        if 'left' in self.inventory_type:
            self.is_charging = self.game.mouse.hold_down_left
        elif 'right' in self.inventory_type:
            self.is_charging = self.game.mouse.hold_down_right
        elif 'bow' in self.inventory_type:
            self.is_charging = self.game.mouse.hold_down_left

    # TODO: Write charge logic for enemy
    def Set_Charging_Enemy(self):
        self.is_charging = self.entity.charge
    
    # Return False if entity weapon cooldown is not off
    def Check_Entity_Cooldown(self):
        if not self.inventory_type:
            return False
        elif 'left' in self.inventory_type:
                if self.entity.left_weapon_cooldown:
                    return False
        elif 'right' in self.inventory_type:
            if self.entity.right_weapon_cooldown:
                return False
        return True
        
    # Check for collision on attack
    def Attack_Collision_Check(self):
        # Check if the weapon has already hit an enemy this attack
        if self.enemy_hit:
            return None
        weapon_rect = self.rect_attack()

        # Handle enemy attack collision check for player
        player_collision_result = self.Player_Collision(weapon_rect)
        if player_collision_result:
            return player_collision_result

        for enemy in self.nearby_enemies:
            # Check if the enemy is on damage cooldown
            if enemy.damage_cooldown:
                continue
            # Check for collision with enemy
            if weapon_rect.colliderect(enemy.rect()):
                self.Entity_Hit(enemy)
                # Return enemy in case further effects need to be added such as knockback
                return enemy
            
        return None
    
    def Entity_Hit(self, entity):
        target_position = (self.pos[0] - 16 * self.entity.attack_direction[0], self.pos[1] - 16 * self.entity.attack_direction[1])
        self.game.clatter.Generate_Clatter(target_position, 200)
        damage = self.entity.strength * self.damage
        entity.Damage_Taken(damage, self.entity.attack_direction)
        self.enemy_hit = True

        # Set special status effect of weapon if weapon has one
        if self.effect:
            entity.Set_Effect(self.effect, 3)
    

    # Check if enemy has hit the player
    def Player_Collision(self, weapon_rect):
        if self.entity.category == 'enemy':
            player = self.game.player
            if weapon_rect.colliderect(player.rect()):
                self.Entity_Hit(player)
                return self.game.player
            else:
                return None
    
    #TODO: Make a formula for better computing clatter distance
    # Return False on collision
    def Check_Tile(self, new_pos):
        tile = self.game.tilemap.Current_Tile(new_pos)
        if not tile:
            return True
        
        if 'Wall' in tile['type']:
            target_position = (self.pos[0] - 16 * self.entity.attack_direction[0], self.pos[1] - 16 * self.entity.attack_direction[1])
            self.game.clatter.Generate_Clatter(target_position, 400)
            return False
        
        return True
    
    # Set the rect of the weapon to be a bit forward for better detection
    def rect_attack(self):
        extra_reach_x = 3
        extra_reach_y = 3
        if self.entity.attack_direction[0] < 0:
            extra_reach_x *= -1
        if self.entity.attack_direction[1] < 0:
            extra_reach_y *= -1

        return pygame.Rect(self.pos[0] + extra_reach_x, self.pos[1] + self.entity.attack_direction[1] + extra_reach_y, self.size[0]*2, self.size[1]*2)

    # Update attack animation logic
    def Update_Attack_Animation(self):
        
        if self.attacking <= 1:
            self.sub_type = self.type
            self.attacking = 0
            self.attack_animation = 0
            return
        self.animation = self.attack_animation
        self.sub_type = self.type + '_attack'
        self.attacking -= 1
        self.attack_animation_counter += 1
        if self.attack_animation_counter >= self.attack_animation_time:
            self.attack_animation_counter = 0
            self.attack_animation += 1
            if self.attack_animation > self.attack_animation_max:
                self.attack_animation = 0
        return
    
    def Slash_Attack(self):
        pass

    # Align the weapon with the attacking entity while attacking
    def Attack_Align_Weapon(self):
        pass
    
    def Stabbing_Attack_Handler(self):
        pass

    def Stabbing_Attack(self):
        pass

    # Input true or False
    def Set_Attack_Ready(self, state) -> None:
        self.attack_ready = state

    # Set the attack direction   
    def Set_Block_Direction(self):
        self.entity.Attack_Direction_Handler(self.game.render_scroll)
        self.entity.attack_direction = self.entity.attack_direction
        if not self.entity.attack_direction:
            return
        # self.entity.attack_direction = pygame.math.Vector2(self.entity.attack_direction[0], self.entity.attack_direction[1])
        self.entity.attack_direction.normalize_ip()
        return

    # Point the weapon towards the mouse
    def Point_Towards_Mouse(self):
        self.rotate = 0
        
        # Get the direction
        dx = self.game.mouse.mpos[0] - self.entity.pos[0]
        dy = self.game.mouse.mpos[1] - self.entity.pos[1]

        # Calculate the angle in degrees
        self.rotate = math.degrees(math.atan2(dy, dx)) + 90

       
    # Check if the weapon sprites needs to be flipped
    def Update_Flip(self):
        if abs(self.entity.attack_direction[0]) >= abs(self.entity.attack_direction[1]):
            if self.entity.attack_direction[0] < 0:
                self.flip_image = True
            else:
                self.flip_image = False
   

    def Set_Entity(self, entity):
        self.entity = entity
   

    # Render the weapon inside inventory
    def Render_In_Inventory(self, surf, offset=(0, 0)):
        
        weapon_image = pygame.transform.scale(self.game.assets[self.sub_type][self.animation], self.size)  
        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))




    # Render the weapon in entity's hand
    def Render_Equipped(self, surf, offset=(0, 0)):
        
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        if self.rotate:
            weapon_image = pygame.transform.rotate(weapon_image, self.rotate)
        
        surf.blit( pygame.transform.flip(weapon_image, self.flip_image, False),
                    (self.pos[0] - offset[0], self.pos[1] - offset[1]))
  
        
            

    # Render basic function on the map
    def Render(self, surf, offset=(0, 0)):
        
        # Check if item is in inventory. If yes we don't need offset, except if
        # the weapon has been picked up
        
        if self.in_inventory:
            self.Render_In_Inventory(surf)
        
        if not self.Update_Light_Level():
            return
        # Set image
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        
        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))

        if not alpha_value:
            return
        
        weapon_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(weapon_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        weapon_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

        

    # Render the weapon in entity's hand
    def Render_Equipped_Enemy(self, surf, offset=(0, 0)):
        
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        if self.rotate:
            weapon_image = pygame.transform.rotate(weapon_image, self.rotate)
        
        alpha_value = max(0, min(255, self.active)) 
        weapon_image.set_alpha(alpha_value)


         # Create a darkening surface that is affected by darkness
        dark_surface = pygame.Surface(weapon_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface.fill((self.light_level, self.light_level, self.light_level, 255))  

        weapon_image.blit(dark_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


        surf.blit(
            pygame.transform.flip(weapon_image, self.flip_image, False),
                                  (self.pos[0] - offset[0], self.pos[1] - offset[1]))
            

    # Inventory Logic below
    #######################################################
    # Pick up the weapon and update the general light in the area
    def Pick_Up(self):
        if self.in_inventory:
            return False
        self.entity = super().Pick_Up()

        if not self.entity:
            return False
        
        self.Pickup_Reset_Weapon(self.entity)
        return True
    
    def Pickup_Reset_Weapon(self, entity):
        self.entity = entity
        self.in_inventory = True
        self.picked_up = True
        self.rotate = 0
        self.enemy_hit = False
        self.light_level = 10

    def Set_Equipped_Position(self, direction_y):
        pass


    # Initialise the double clikc
    def Handle_Double_Click(self, sending_inventory, receiving_inventory):
        # Check if there is a free inventory slot
        recieving_inventory_slot = None
        for i in range(8):
            recieving_inventory_slot = receiving_inventory.Find_Available_Inventory_Slot(recieving_inventory_slot)
            if not self.Check_Legal_Move(recieving_inventory_slot, sending_inventory, receiving_inventory):
                recieving_inventory_slot = None
                continue

            break
            
        
        if not recieving_inventory_slot:
            self.Reset_Inventory_Slot(sending_inventory)
            return False
        # Check if we can send the item to the new inventroy slot
        if self.Send_To_Inventory(recieving_inventory_slot, sending_inventory, receiving_inventory):
            return True
        else:
            self.Reset_Inventory_Slot(sending_inventory)
            return False

    def Check_Legal_Move(self, inventory_slot, sending_inventory, receiving_inventory):
        if not inventory_slot:
            return False
        
        if not self.Check_Two_Handed(inventory_slot, sending_inventory, receiving_inventory):
            return False
    
        if not self.Check_For_Two_Handed_In_Weapon_Inventory(inventory_slot, sending_inventory, receiving_inventory):
            return False
        
        if not self.Check_Two_Handed_Left_Hand(inventory_slot):
            return False
        
        if not self.Bow_Check(inventory_slot):
            return False
        
        if not self.Arrow_Check(inventory_slot):
            return False
        
        return True


    # Attempt to move the item to the receiving inventory slot by double clicking
    def Send_To_Inventory(self, inventory_slot, sending_inventory, receiving_inventory):
       
        if not self.Check_Legal_Move(inventory_slot, sending_inventory, receiving_inventory):
            return False

        # Move the item
        move_successful = receiving_inventory.Move_Item(self, inventory_slot)
        # If the move was successful, remove it from the sending inventory
        if move_successful:

            # Remove item from old inventory and save the inventory type
            inventory_type_holder = self.inventory_type

            sending_inventory.Remove_Item(self, move_successful)
            # send weapon into weapon inventory, checked by seeing if it has an inventory_type
            if self.inventory_type:

                # If weapon is already equipped in the other hand, remove it before adding to new hand
                if self.equipped:
                    self.game.player.Remove_Active_Weapon(inventory_type_holder)
                self.Equip()
            else: # Drag weapon back into item inventory
                self.Set_Equip(False)
                self.game.player.Remove_Active_Weapon(inventory_type_holder)

            return True
        
        
        return False
    
    # Add weapons from a sending inventory to a receiving inventory using drag
    # Example: weapon_inventory (sending) -> inventory (receiving) 
    def Move_To_Other_Inventory(self, sending_inventory, receiving_inventory, offset = (0,0)):
        if self.game.mouse.left_click:
            return
        # Check for collision with new ivnentory slot
        for receiving_inventory_slot in receiving_inventory:
            if receiving_inventory_slot.rect().colliderect(self.game.mouse.rect_pos(offset)):
                if self.Send_To_Inventory(receiving_inventory_slot, sending_inventory, receiving_inventory):
                    for inventory_slot in sending_inventory.inventory:
                        if not inventory_slot.active: # Reset active state after dragging
                            continue
                        inventory_slot.Set_Active(False)
                        break
                    return True             
        return False

    # Check if the weapon can be moved to the weapon inventory
    def Move_Inventory_Check(self, offset = (0,0)):
        if not self.picked_up:
            active_inventory = self.game.weapon_inventory.active_inventory
            weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
            if self.equipped: # Move to normal inventory
                if self.Move_To_Other_Inventory(weapon_inventory, self.game.item_inventory, offset):
                    self.Set_Equip(False)
                    self.game.player.Remove_Active_Weapon(self.inventory_type)
                    return True
                
                
            else: # Move to weapon inventory
                if self.Move_To_Other_Inventory(self.game.item_inventory, weapon_inventory, offset):
                    self.Equip()
                    return True
                
        return False
    
    # Equip the weapon
    def Equip(self):
        self.Set_Equip(True)
        self.game.player.Set_Active_Weapon(self, self.inventory_type)

    def Set_Equip(self, state):
        self.equipped = state

    # Check for out of bounds, return true if valid, else false
    def Move_Legal(self, mouse_pos, player_pos, tilemap, offset = (0,0)):

        # Check if the weapon can be moved to the weapon inventory
        if self.Move_Inventory_Check(offset):
            self.picked_up = True
            self.move_inventory_slot = True
            return False
        if super().Move_Legal(mouse_pos, player_pos, tilemap, offset):
            return True
        else:
            return False
        
    def Check_Inventory_Type(self, type):
        legal_inventories = ['left_hand', 'right_hand', 'bow', 'arrow']
        if type not in legal_inventories:
            return False
        
        self.inventory_type = type
        return True

    def Update_Player_Hand(self, prev_hand):
        # Check if the weapon has changed hands
        if self.inventory_type != prev_hand:
            self.Set_Equip(True)
            if prev_hand == 'left_hand':
                self.game.player.Remove_Active_Weapon(prev_hand)
                self.game.player.Set_Active_Weapon(self, self.inventory_type)
            elif prev_hand == 'right_hand':
                self.game.player.Remove_Active_Weapon(prev_hand)
                self.game.player.Set_Active_Weapon(self, self.inventory_type)
            elif 'bow' in prev_hand:
                self.game.player.Remove_Active_Weapon(prev_hand)
                self.game.player.Set_Active_Weapon(self, self.inventory_type)


    def Place_Down(self):
        super().Place_Down()
        self.entity = None
        self.in_inventory = False
        if self.equipped:
            self.game.player.Remove_Active_Weapon(self.inventory_type)
            self.Set_Equip(False)
        return False

    def Set_In_Inventory(self, state):
        self.in_inventory = state

    def Bow_Check(self, inventory_slot):
        if not inventory_slot.inventory_type:
            return True
        if 'bow' in inventory_slot.inventory_type:
            if 'bow' in self.type:
                return True
            else:
                return False
        return True
        
        
    def Arrow_Check(self, inventory_slot):

        if not inventory_slot.inventory_type:
            return True
        if 'arrow' in inventory_slot.inventory_type:
            if 'arrow' in self.weapon_class:
                return True
            else:
                return False
        return True

    def Check_Two_Handed(self, inventory_slot, sending_inventory, receiving_inventory):
        if not 'two' in self.weapon_class:
            return True
        if inventory_slot.inventory_type:
            # Try to find the inventory_slot, only the weapon inventory has this property
            try:
                if receiving_inventory.Find_Inventory_Slot(inventory_slot):
                    # Find the original position of the item in the inventory
                    self.Reset_Inventory_Slot(sending_inventory)
                    return False
            except TypeError as e:
                print(f"Receiving inventory not a weapon inventory: {e}")
        return True
    
    def Check_Two_Handed_Left_Hand(self, inventory_slot):
        if self.entity.type == 'player':
            self.entity.Set_Inventory_Interaction(20)

        if not inventory_slot.inventory_type:
            return True
        if not 'two' in self.weapon_class:
            return True
        if 'left' in inventory_slot.inventory_type:
            return True
        else:
            return False
    
    
    def Check_For_Two_Handed_In_Weapon_Inventory(self, inventory_slot, sending_inventory, receiving_inventory):
        # Check for weapon inventory
        

        if not inventory_slot.inventory_type:
            return True
        
        for weapon_inventory_slot in receiving_inventory:
            if not weapon_inventory_slot.item:
                continue
            # Check to ensure that item is a weapon
            if not weapon_inventory_slot.item.category == 'weapon':
                continue
            
            # Check if there is already a two handed weapon in the inventory
            if 'two' in weapon_inventory_slot.item.weapon_class:
                self.Reset_Inventory_Slot(sending_inventory)

                return False
        
        return True
          
    

    def Reset_Inventory_Slot(self, inventory_slot):
        original_inventory_slot = inventory_slot.Find_Item_In_Inventory(self)
        # Reset it back to not active if found
        if original_inventory_slot:
            original_inventory_slot.Set_Active(False)
        return
    ####################################################### 