from scripts.entities.items.item import Item
from scripts.entities.textbox.weapon_textbox import Weapon_Textbox
import pygame
import math

class Weapon(Item):
    def __init__(self, game, pos, type, damage, speed, range, max_charge_time, weapon_class, effect = 'slash', attack_type = 'cut', size = (32, 32), add_to_tile = True):
        super().__init__(game, type, 'weapon', pos, size, 1, add_to_tile)
        self.damage = damage # The damage the wepaon does
        self.speed = 10 - speed # Speed of the weapon
        self.range = range # Range of the weapon
        self.entity = None # Entity that holds the weapon
        self.effect = effect # Special effects, like poision, ice, fire etc
        self.attack_type = attack_type # Different kinds of attacks, like cutting and stabbing
        self.in_inventory = False # Is the weapon in an inventory
        self.equipped = False # Is the weapon currently equipped and can be used to attack
        self.attacking = 0 # The time it takes for the attack to complete
        self.max_animation = 0 # Max amount of animations

        self.flip_x = False
        self.attack_animation = 0 # Current attack animation
        self.attack_animation_max = 1 # Maximum amount of attack animations
        self.special_attack_effect_animation_max = 1 # Maximum amount of attack animations
        self.attack_animation_time = 0 # Time to shift to new animation
        self.attack_animation_counter = 0 # Animation countdown that ticks up to time
        
        self.attack_effect_animation = 0 # current effect animation frame
        self.attack_effect_animation_max = 7 # Amount of effect animation frames
        self.attack_effect_animation_time = 0 # Time it takes to change between frames
        self.attack_effect_animation_counter = 0 # Animation countdown that ticks up to time



        self.enemy_hit = False # Prevent double damage on attacks
        self.rotate = 0 # Rotation value of weapon
        self.nearby_enemies = [] # Nearby enemies that the weapon can interact with
        # Can be expanded to damaged or dirty versions of weapons later
        self.weapon_class = weapon_class # Determines how it's wielded, one or two hand, bow, etc
        self.charge_time = 0  # Tracks how long the button is held
        self.max_charge_time = max_charge_time  # Maximum time to fully charge
        self.is_charging = False  # Tracks if the player is charging
        self.special_attack = 0 # special attack counter
        self.special_attack_active = False # Check if weapon is special attacking

        self.charge_effect = self.effect + '_charge_effect'
        self.charge_effect_animation = 0
        self.charge_effect_animation_max = 5
        self.charge_effect_cooldown = 0
        self.charge_effect_cooldown_max = (self.max_charge_time // self.charge_effect_animation_max) - (self.max_charge_time // 20)


        self.weapon_cooldown = 0
        self.weapon_cooldown_max = 50 # How fast the weapon can attack

        self.attack_hitbox_size = (5, 5)
        self.attack_hitbox = pygame.Rect(self.pos[0], self.pos[1], self.attack_hitbox_size[0], self.attack_hitbox_size[1])
        self.text_box = Weapon_Textbox(self)

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
        self.saved_data['rotate'] = self.rotate
        self.saved_data['attacking'] = self.attacking
        self.saved_data['special_attack'] = self.special_attack
        

    
    def Load_Data(self, data):
        super().Load_Data(data)
        self.damage = data['damage']
        self.speed = data['speed']
        self.range = data['range']
        self.effect = data['effect']
        self.in_inventory = data['in_inventory']
        self.equipped = data['equipped']
        self.enemy_hit = data['enemy_hit']
        self.rotate = data['rotate']
        self.attacking = data['attacking']
        self.special_attack = data['special_attack']

   
    # General Update function
    def Update(self, offset = (0,0)):
        super().Update()
        self.Update_Animation()
        self.Special_Attack()
        if not self.entity:
            return False
        
        self.Set_Weapon_Charge(offset)
        self.Set_Flip_X()
        return True


    # Update the attack logic
    def Update_Attack(self):
        if not self.attacking:
            return False
        self.Update_Attack_Animation()
        self.Update_Attack_Effect_Animation()
        self.Attack_Collision_Check()
        self.Attack_Align_Weapon()
        self.entity.Reduce_Movement(4) # Reduce movement to a quarter when attacking
        return True

    # Initialise the attack and reset attack values
    def Set_Attack(self):
        if not self.Check_Entity_Cooldown():
            return
        # Compute attack each time to account for changing entity agility level
        self.attacking = max(int((self.speed * 30) // self.entity.agility), self.attack_animation_max) 
        self.enemy_hit = False  # Reset at the start of a new attack
        self.attack_animation_time = int(self.attacking / self.attack_animation_max)
        self.charge_time = 0  # Reset charge time
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, 3) # Find nearby enemies to attack
        self.Set_Attack_Effect_Animation_Time()
        self.Set_Rotation()
        self.rotate += 90


        

    def Set_Rotation(self):
        if self.entity.category == 'enemy':
            self.Point_Towards_Mouse_Enemy()
        else:
            self.Point_Towards_Mouse_Player() 


    # Handle weapon charging
    def Set_Weapon_Charge(self, offset = (0, 0)):
        if self.weapon_cooldown:

            self.weapon_cooldown = max(0, self.weapon_cooldown - 1)
            return
        self.Charge_Player_Or_Enemy()
        
        if self.Check_Charge():
            return
        
        self.Determine_Attack_Type(offset)


    def Determine_Attack_Type(self, offset):
        # If the button is released quickly
        if self.charge_time > 0 and self.charge_time <= 20:
            self.Set_Attack()  # Trigger the attack
            self.Reset_Weapon_Charge()
            return
        
        # Trigger special attack if mouse if held for > 20 frames
        elif self.charge_time >= self.max_charge_time:
            self.Set_Special_Attack(offset)
            self.Reset_Weapon_Charge()
            return
        
        # Resetting weapon if no special attack
        elif self.charge_time >= 20:
            self.Reset_Weapon_Charge()
    

    def Reset_Weapon_Charge(self):
        self.charge_time = 0  # Reset the charge time
        self.weapon_cooldown = self.weapon_cooldown_max
        return

    def Check_Charge(self):
        if not self.is_charging:
            return False
        
        # Slow the entity whilst charging weapon
        self.entity.Reduce_Movement(4)
        # Increase charge time while holding the button
        self.charge_time += 1
        if self.charge_time >= self.max_charge_time:
            self.charge_time = self.max_charge_time  # Cap the charge time
        return True
   
    def Charge_Player_Or_Enemy(self):
        try:
            if 'enemy' == self.entity.category:
                self.Set_Charging_Enemy()
            
            elif 'player' == self.entity.type:
                if not self.inventory_type:
                    return
                self.Set_Charging_Player()
        except TypeError as e:
            print(f"Entity neither enemy nor player: {e}")
    
    
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
        
        self.Set_Attack_Hitbox()


        # Handle enemy attack collision check for player
        player_collision_result = self.Player_Collision(self.attack_hitbox)
        if player_collision_result:
            return player_collision_result

        for enemy in self.nearby_enemies:
            # Check if the enemy is on damage cooldown
            if enemy.damage_cooldown:
                continue
            # Check for collision with enemy
            if self.attack_hitbox.colliderect(enemy.rect()):
                self.Entity_Hit(enemy)
                # Return enemy in case further effects need to be added such as knockback
                return enemy
            
        return None
    

     # Initialise special attack
    def Set_Special_Attack(self, offset = (0, 0)):
        if not self.entity:
            return
        self.entity.Attack_Direction_Handler(offset)
        self.Set_Block_Direction()
        self.special_attack = min(self.charge_time, self.max_charge_time)
        self.Set_Rotation()
        self.special_attack_active = True


    def Reset_Special_Attack(self):
        if not self.special_attack_active:
            return
        self.rotate = 0
        self.special_attack_active = False
        self.attack_effect_animation = 0
        self.attack_effect_animation_counter = 0


    # Initialise the charging of the weapon
    def Set_Charging_Player(self):
        # Detect if the player is holding down the button
        if 'left' in self.inventory_type:
            self.is_charging = self.game.mouse.hold_down_left
        elif 'right' in self.inventory_type:
            self.is_charging = self.game.mouse.hold_down_right
        elif 'bow' in self.inventory_type:
            self.is_charging = self.game.mouse.hold_down_left

    def Calculate_Damage(self):
        return self.entity.strength * self.damage


    # Damage Entity
    def Entity_Hit(self, entity):
        damage = self.Calculate_Damage()
        entity.Damage_Taken(damage, self.entity.attack_direction)
        self.enemy_hit = True

        if entity.effects.thorns.effect:
            self.entity.Damage_Taken(entity.effects.thorns.effect, self.entity.attack_direction)

        # Check if weapon is vampiric first, to avoid double healing
        if self.effect == "vampiric":
            self.entity.Set_Effect("healing", damage // 2)
            return
        
        if self.entity.effects.vampiric.effect:
            self.entity.Set_Effect("healing", damage // 2)


        # Set special status effect of weapon if weapon has one
        if self.effect:
            entity.Set_Effect(self.effect, 3)
    

    
    # Update attack animation logic
    def Update_Attack_Animation(self):
        
        if self.Reset_Attack():
            return
        self.animation = self.attack_animation
        self.sub_type = self.type + '_attack_' + self.attack_type
        self.attacking -= 1
        self.attack_animation_counter += 1
        if self.attack_animation_counter >= self.attack_animation_time:
            self.attack_animation_counter = 0
            self.attack_animation += 1
            if self.attack_animation > self.attack_animation_max:
                self.attack_animation = 0
        return
    
    def Reset_Attack(self):
        if not self.attacking <= 1:
            return False
        
        self.sub_type = self.type
        self.attacking = 0
        self.attack_animation = 0
        self.rotate = 0
        self.entity.Reset_Max_Speed()
        self.Reset_Attack_Effect_Animation()

        return True
        

    # Set the attack direction   
    def Set_Block_Direction(self):
        self.entity.Attack_Direction_Handler(self.game.render_scroll)
        self.entity.attack_direction = self.entity.attack_direction
        if not self.entity.attack_direction[0] or not self.entity.attack_direction[1]:
            return
        # self.entity.attack_direction = pygame.math.Vector2(self.entity.attack_direction[0], self.entity.attack_direction[1])
        self.entity.attack_direction.normalize_ip()
        return

    # Point the weapon towards the mouse
    def Point_Towards_Mouse_Enemy(self):
        # Get the direction using attack_direction
        dx = self.entity.pos[0] + self.entity.attack_direction[0] * 100 - self.entity.pos[0]
        dy = self.entity.pos[1] + self.entity.attack_direction[1] * 100 - self.entity.pos[1]

        # Calculate the angle in degrees
        self.rotate = math.degrees(math.atan2(dx, dy))
    

    # Point the weapon towards the mouse
    def Point_Towards_Mouse_Player(self):
        if self.entity.category != 'player':
            return
        # Get the direction using attack_direction
        dx = self.game.mouse.mpos[0] - self.entity.pos[0]
        dy = self.game.mouse.mpos[1] - self.entity.pos[1]
        # Calculate the angle in degrees
        self.rotate = abs(math.degrees(math.atan2(dx, dy)))

    def Set_Flip_X(self):
        if self.entity.attack_direction[0] < 0:
            self.flip_x = True
        else:
            self.flip_x = False

   # Check if enemy has hit the player
    def Player_Collision(self, weapon_rect):
        if self.entity.category != 'enemy':
            return None
        
        player = self.game.player
        if weapon_rect.colliderect(player.rect()):
            self.Entity_Hit(player)
            return self.game.player
        else:
            return None
    
    #TODO: Make a formula for better computing clatter distance
    # Return False on collision
    def Check_Tile(self, new_pos):
        tile_key = str(int(new_pos[0] // self.game.tilemap.tile_size)) + ';' + str(int(new_pos[1] // self.game.tilemap.tile_size))
        tile = self.game.tilemap.Current_Tile(tile_key)
        if not tile:
            return True
        if 'wall' in tile.type:
            target_position = (self.pos[0] - self.game.tilemap.tile_size * self.entity.attack_direction[0], self.pos[1] - self.game.tilemap.tile_size * self.entity.attack_direction[1])
            self.game.clatter.Generate_Clatter(target_position, 400)
            return False
        
        return True
    
    
    # Reset the attack charge
    def Reset_Charge(self):
        self.is_charging = 0
        self.charge_time = 0
        return

    
    # Compute the hitbox for the weapon when attacking
    def Set_Attack_Hitbox(self):
        if not self.entity:
            return
        pos_x = self.entity.rect().center[0] - 2 + self.entity.attack_direction[0] * self.game.tilemap.tile_size
        pos_y = self.entity.rect().center[1] - 2 + self.entity.attack_direction[1] * self.game.tilemap.tile_size
        self.attack_hitbox = pygame.Rect(pos_x, pos_y, self.attack_hitbox_size[0] * self.range, self.attack_hitbox_size[1] * self.range)


    def Set_Entity(self, entity):
        self.entity = entity
   
    # TODO: Write charge logic for enemy
    def Set_Charging_Enemy(self):
        self.is_charging = self.entity.charge

    def Set_Damage(self, damage):
        self.damage = damage


    def Special_Attack(self):
        pass

    def Slash_Attack(self):
        pass

    # Align the weapon with the attacking entity while attacking
    def Attack_Align_Weapon(self):
        pass
    
    def Stabbing_Attack_Handler(self):
        pass

    def Stabbing_Attack(self):
        pass

    
    def Set_Special_Attack_Effect_Animation_Time(self):
        self.attack_effect_animation_time = self.special_attack / self.special_attack_effect_animation_max

    def Set_Attack_Effect_Animation_Time(self):
        self.attack_effect_animation_time = self.attacking / self.attack_effect_animation_max

    def Update_Attack_Effect_Animation(self):
        if self.attack_effect_animation_counter >= self.attack_effect_animation_time:
            self.attack_effect_animation_counter = 0
            self.attack_effect_animation = min(self.attack_effect_animation + 1, self.attack_animation_max)
            return
        self.attack_effect_animation_counter += 1


    def Update_Special_Attack_Effect_Animation(self):
        if self.attack_effect_animation_counter >= self.attack_effect_animation_time:
            self.attack_effect_animation_counter = 0
            self.attack_effect_animation = min(self.attack_effect_animation + 1, self.special_attack_effect_animation_max)
            return

        self.attack_effect_animation_counter += 1

    def Reset_Attack_Effect_Animation(self):
        self.attack_animation_counter = 0
        self.attack_effect_animation_time = 0
        self.attack_effect_animation = 0


    # Handle computing the weapon's attack effect position
    def Attack_Effect_Position(self, offset):
        pos_x = self.entity.pos[0] - offset[0]
        pos_y = self.entity.pos[1] - offset[1] - 30
        if self.entity.attack_direction[0] < 0:
            pos_x += self.entity.attack_direction[0] * 50
        else:
            pos_x += self.entity.attack_direction[0] * 10
        
        if self.entity.attack_direction[1] < 0:
            pos_y += self.entity.attack_direction[1] * 20
        else:
            pos_y += self.entity.attack_direction[1] * 30

        return (pos_x, pos_y)

   
    # Handle rendering the weapons attack effect
    def Render_Attack_Effect(self, surf, offset):
        if not self.attacking:
            return
        pos = self.Attack_Effect_Position(offset)
        effect_type = self.effect + '_' + self.attack_type + '_effect'
        attack_effect = self.game.assets[effect_type][self.attack_effect_animation]
        # attack_effect.set_alpha()
        attack_effect = pygame.transform.rotate(attack_effect, self.rotate)
        surf.blit( pygame.transform.flip(attack_effect, self.flip_x, False), (pos[0], pos[1]))


    # Render the weapon in player's hand and rotate towards target
    def Render_Equipped(self, surf, offset=(0, 0)):
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        if self.rotate:
            weapon_image = pygame.transform.rotate(weapon_image, self.rotate - 180)

        surf.blit( pygame.transform.flip(weapon_image, self.flip_x, False),
                    (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        
        self.Render_Attack_Effect(surf, offset)
        self.Render_Charge_Effect(surf, offset)
    
    def Reset_Charge_Effect(self):
        if not self.charge_effect_animation:
            return
        self.charge_effect_cooldown = 0
        self.charge_effect_animation = 0


    def Charge_Effect_Update(self):
        if self.charge_effect_cooldown < self.charge_effect_cooldown_max:
            self.charge_effect_cooldown += 1
            return
        
        self.charge_effect_cooldown = 0
        self.charge_effect_animation = min(self.charge_effect_animation_max, self.charge_effect_animation + 1)

    # Handle the charging effect when using special attacks
    def Render_Charge_Effect(self, surf, offset):
        if self.charge_time <= 20 and self.entity:
            self.Reset_Charge_Effect()

            return
        if not self.entity.type == "player":
            return
        self.Charge_Effect_Update()
        charge_effect_animation = self.game.assets[self.charge_effect][self.charge_effect_animation].convert_alpha()

        charge_effect_animation.set_alpha(self.charge_effect_animation * 50)
        surf.blit(charge_effect_animation, (self.pos[0] - offset[0], self.pos[1] - offset[1]))


            
        

    # Render basic function on the map
    def Render(self, surf, offset=(0, 0)):
        
        # Check if item is in inventory. If yes we don't need offset, except if
        # the weapon has been picked up
        
        if self.in_inventory:
            if self.equipped:
                return
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
        
     # Render the weapon inside inventory
    def Render_In_Inventory(self, surf, offset=(0, 0)):
        
        weapon_image = pygame.transform.scale(self.game.assets[self.sub_type][0], self.size)  
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
            pygame.transform.flip(weapon_image, False, False),
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
        if 'left' in self.inventory_type:
            if direction_y < 0:
                self.Move((self.entity.pos[0] - 5 , self.entity.pos[1]))
            else:
                self.Move((self.entity.pos[0] + 5 , self.entity.pos[1]))
        elif 'right' in self.inventory_type:
            if  direction_y < 0:
                self.Move((self.entity.pos[0] + 7, self.entity.pos[1]))
            else:
                self.Move((self.entity.pos[0] - 7, self.entity.pos[1]))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)


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
            self.Reset_Weapon()
            # Remove item from old inventory and save the inventory type
            inventory_type_holder = self.inventory_type

            sending_inventory.Remove_Item(self, True)
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
    
    def Reset_Weapon(self):
        self.rotate = 0
        self.attacking = 0
        self.sub_type = self.type
        self.animation = 0

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
        if state:
            self.render = False
        else:
            self.render = True


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
        if not super().Place_Down():
            return False
        self.entity = None
        self.in_inventory = False
        self.picked_up = False
        if self.equipped:
            self.game.player.Remove_Active_Weapon(self.inventory_type)
            self.Set_Equip(False)
        return True

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