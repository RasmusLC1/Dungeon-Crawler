from scripts.entities.items.item import Item
from scripts.entities.items.weapons.weapon_charge_effect import Weapon_Charge_Effect
from scripts.entities.items.weapons.weapon_attack_effect import Weapon_Attack_Effect
from scripts.entities.items.weapons.player_weapon_attack import Player_Weapon_Attack
from scripts.entities.items.weapons.enemy_weapon_attack import Enemy_Weapon_Attack
from scripts.entities.textbox.weapon_textbox import Weapon_Textbox
import pygame
import math
import random
from scripts.engine.assets.keys import keys

class Weapon(Item):
    def __init__(self, game, pos, type, damage, speed, range, max_charge_time, weapon_class, effect = 'slash', attack_type = 'cut', size = (32, 32), add_to_tile = True):
        super().__init__(game, type, keys.weapon, pos, size, 1, add_to_tile)
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
        self.attack_animation_time = 0 # Time to shift to new animation
        self.attack_animation_counter = 0 # Animation countdown that ticks up to time
        

        self.enemy_hit = False # Prevent double damage on attacks
        self.rotate = 0 # Rotation value of weapon
        self.nearby_enemies = [] # Nearby enemies that the weapon can interact with
        self.nearby_decoration = [] # Nearby decoration that the weapon can interact with
        # Can be expanded to damaged or dirty versions of weapons later
        self.weapon_class = weapon_class # Determines how it's wielded, one or two hand, bow, etc
        self.charge_time = 0  # Tracks how long the button is held
        self.max_charge_time = max_charge_time  # Maximum time to fully charge
        self.is_charging = False  # Tracks if the player is charging
        self.special_attack = 0 # special attack counter
        self.special_attack_active = False # Check if weapon is special attacking
        self.entities_hit = [] # Index of entities hit by weapon in attack

        self.weapon_cooldown = 0
        self.weapon_cooldown_max = 50 # How fast the weapon can attack

        self.delete_timer = 0 # time before weapon is deleted

        self.attack_hitbox_size = (5, 5)
        self.attack_hitbox = pygame.Rect(self.pos[0], self.pos[1], self.attack_hitbox_size[0], self.attack_hitbox_size[1])
        self.text_box = Weapon_Textbox(self)
        self.entity_attack_type = None # Used to determine if the weapon is being used by enemy or player
        self.weapon_charge_effect = Weapon_Charge_Effect(game, self)
        self.weapon_attack_effect = Weapon_Attack_Effect(game, self)
        self.description = (
                            f"{self.effect} {self.damage}\n"
                            f"speed {self.speed}\n"
                            f"range {self.range}\n"
                            f"gold {self.value}\n"
                        )

    def Save_Data(self):
        if self.entity:
            if self.entity.category == keys.enemy:
                return
        super().Save_Data()
        
        self.saved_data['damage'] = self.damage
        self.saved_data[keys.speed] = self.speed
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
        self.speed = data[keys.speed]
        self.range = data['range']
        self.effect = data['effect']
        self.in_inventory = data['in_inventory']
        self.equipped = data['equipped']
        self.enemy_hit = data['enemy_hit']
        self.rotate = data['rotate']
        self.attacking = data['attacking']
        self.special_attack = data['special_attack']

   
    # General Update function, handles setting the attack and general logic
    def Update(self, offset = (0,0)):
        super().Update()
        self.Update_Animation()
        self.Special_Attack()
        self.Update_Delete_Countdown()
        if not self.entity:
            return False
        
        self.Set_Weapon_Charge(offset)
        self.Set_Flip_X()
        return True

    def Reset_Attack_Animation(self):
        self.sub_type = self.type
        self.attack_animation = 0
        self.animation = 0
        self.rotate = 0
        self.entity.Reset_Max_Speed()
        self.weapon_attack_effect.Reset_Attack_Effect_Animation()

    # Update the attack logic
    def Update_Attack(self):
        if not self.entity_attack_type:
            return False
        
        self.entity_attack_type.Update_Attack()
        self.Update_Attack_Animation()
        self.weapon_attack_effect.Update_Attack_Effect_Animation()
        self.Attack_Align_Weapon()

    # Initialise the attack and reset attack values
    def Set_Attack(self):
        if not self.entity_attack_type:
            return False
        if not self.entity_attack_type.Set_Attack():
            return False
        
        self.Set_Attack_Animation_Time(int(self.attacking / self.attack_animation_max))
        self.Set_Charge_Time(0)  # Reset charge time
        
        self.Handle_Attack_Animation()
        return True

    
    def Check_Tile(self, new_pos):
        tile_key = str(int(new_pos[0] // self.game.tilemap.tile_size)) + ';' + str(int(new_pos[1] // self.game.tilemap.tile_size))
        tile = self.game.tilemap.Current_Tile(tile_key)
        if not tile:
            return True
        if 'wall' in tile.type:
            target_position = (self.pos[0] - self.game.tilemap.tile_size * self.entity.attack_direction[0], self.pos[1] - self.game.tilemap.tile_size * self.entity.attack_direction[1])
            self.game.clatter.Generate_Clatter(target_position, 400)
            self.Spawn_Spark()
            return False
        
        return True
    

    def Handle_Attack_Animation(self):
        self.weapon_attack_effect.Set_Attack_Effect_Animation_Time()
        self.Set_Rotation()
        self.rotate += 90

    def Set_Attack_Animation_Time(self, state):
        self.attack_animation_time = state


    def Set_Enemy_Attack(self):
        if not self.Check_Entity_Cooldown():
            return
        self.attacking = max(int((self.speed * 30) // self.entity.agility), self.attack_animation_max) 
        self.attack_animation_time = int(self.attacking / self.attack_animation_max)
        self.charge_time = 0  # Reset charge time
        self.enemy_hit = True # Set enemy hit to true to prevent collision detection
        self.weapon_attack_effect.Set_Attack_Effect_Animation_Time()
        self.Set_Rotation()
        self.rotate += 90
        
        if self.entity.distance_to_player > self.game.tilemap.tile_size * 1.5:
            return
        self.Entity_Hit(self.game.player)
        

    def Set_Rotation(self):
        if self.entity.category == keys.enemy:
            self.Point_Towards_Mouse_Enemy()
        else:
            self.Point_Towards_Mouse_Player() 

    def Update_Animation(self):
        if not self.equipped:
            return
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = self.animation_cooldown_max
            self.animation = random.randint(0,self.max_animation)

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
            if keys.enemy == self.entity.category:
                self.Set_Charging_Enemy()
            
            elif keys.player == self.entity.type:
                self.Set_Charging_Player()
        except TypeError as e:
            print(f"Entity neither enemy nor player: {e}")
    


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
        self.weapon_attack_effect.Set_Attack_Effect_Animation(0)
        self.weapon_attack_effect.Set_Attack_Effect_Animation_Counter(0)


    # Initialise the charging of the weapon
    def Set_Charging_Player(self):
        # Detect if the player is holding down the button
        self.is_charging = self.game.mouse.hold_down_left

    def Calculate_Damage(self):
        return self.entity.strength * self.damage
    

    # Damage Entity
    def Entity_Hit(self, entity):
        if not self.entity:
            return
        damage = self.Calculate_Damage()
        entity.Damage_Taken(damage, self.entity.attack_direction)
        self.enemy_hit = True

        if entity.effects.thorns.effect:
            self.entity.Damage_Taken(entity.effects.thorns.effect, self.entity.attack_direction)

        if not self.entity:
            return
        
        self.Check_Effects(damage, entity)
    
    def Check_Effects(self, damage, entity):
        # Check if weapon is vampiric first, to avoid double healing
        if self.effect == keys.vampiric:
            self.entity.Set_Effect(keys.healing, damage // 2)
            return
        

        if self.entity.effects.vampiric:
            if self.entity.effects.vampiric.effect:
                self.entity.Set_Effect(keys.healing, damage // 2)


        # Set special status effect of weapon if weapon has one
        if self.effect:
            entity.Set_Effect(self.effect, 3)
    
    
    # Update attack animation logic
    def Update_Attack_Animation(self):
        if not self.entity_attack_type:
            print("ATTACK TYPE MISSING WEAPON ", self.entity.type)
            return
        
        if self.entity_attack_type.Reset_Attack():
            return
        self.animation = self.attack_animation
        self.sub_type = self.type + '_attack_' + self.attack_type
        self.attack_animation_counter += 1
        if self.attack_animation_counter >= self.attack_animation_time:
            self.attack_animation_counter = 0
            self.attack_animation += 1
            if self.attack_animation > self.attack_animation_max:
                self.attack_animation = 0
        return
    

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
        if self.entity.category != keys.player:
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


    # Handle deletion of items when enemies drop weapons, don't want them to linger forever
    def Update_Delete_Countdown(self):
        if not self.delete_countdown:
            return
        self.delete_countdown = max(0, self.delete_countdown - 1)
        if not self.delete_countdown:
            self.game.item_handler.Remove_Item(self, True)


    def Set_Delete_Countdown(self, delete_countdown = 2000):
        self.delete_countdown = delete_countdown

    # Reset the attack charge
    def Reset_Charge(self):
        self.is_charging = 0
        self.charge_time = 0
        return

  
    def Set_Entity(self, entity):
        self.entity = entity
        if not entity:
            return
        
        self.Set_Entity_Attack_Type(entity.type)
        
    
    def Set_Entity_Attack_Type(self, type):
        if type == keys.player:
            self.entity_attack_type = Player_Weapon_Attack(self.game, self)
        else:
            self.entity_attack_type = Enemy_Weapon_Attack(self.game, self)


   
    # TODO: Write charge logic for enemy
    def Set_Charging_Enemy(self):
        self.is_charging = self.entity.charge

    def Set_Damage(self, damage):
        self.damage = damage

    def Set_Charge_Time(self, state):
        self.charge_time = state

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

    
    # Render the weapon in player's hand and rotate towards target
    def Render_Equipped(self, surf, offset=(0, 0)):
        weapon_image = self.entity_image.copy()
        if self.rotate:
            weapon_image = pygame.transform.rotate(weapon_image, self.rotate - 180)

        surf.blit( pygame.transform.flip(weapon_image, self.flip_x, False),
                    (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        
        self.weapon_attack_effect.Render_Attack_Effect(surf, offset)
        self.weapon_charge_effect.Render_Charge_Effect(surf, offset)
    

    # Render the weapon in entity's hand
    def Render_Equipped_Enemy(self, surf, offset=(0, 0)):
       
        alpha_value = max(0, min(255, self.active)) 

        if not alpha_value:
            return

        self.Update_Dark_Surface_Enemy(alpha_value)

        if not self.rendered_image:
            self.rendered_image = self.entity_image.copy()
        
        surf.blit(
            pygame.transform.flip(self.rendered_image, False, False),
                                  (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    
    # Updates the dark surface for enemies
    def Update_Dark_Surface_Enemy(self, alpha_value):
        if not self.render_needs_update:
            return
        self.rendered_image = self.entity_image.copy()
        self.rendered_image.set_alpha(alpha_value)


         # Create a darkening surface that is affected by darkness
        dark_surface = pygame.Surface(self.rendered_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface.fill((self.light_level, self.light_level, self.light_level, 255))  

        self.rendered_image.blit(dark_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    
    # Used to reset weapon when equipped by enemy
    def Pickup_Reset_Weapon(self, entity):
        self.entity = entity
        self.in_inventory = True
        self.picked_up = True
        self.rotate = 0
        self.enemy_hit = False
        self.light_level = 10
    
    # Prevent textbox when carried by enemy
    def Update_Text_Box(self, hitbox_1, hitbox_2):
        if self.entity:
            if self.entity.category == keys.enemy:
                return
        return super().Update_Text_Box(hitbox_1, hitbox_2)


    def Set_Equip(self, state, entity):
        self.Set_Entity(entity)
        self.equipped = state
        if state:
            self.render = False
        else:
            self.render = True

    def Set_Equipped_Position(self, direction_y):
        if not self.entity:
            return
        if direction_y < 0:
            self.Move((self.entity.pos[0] - 5 , self.entity.pos[1]))
        else:
            self.Move((self.entity.pos[0] + 5 , self.entity.pos[1]))

    def Place_Down(self):
        self.entity = None
        return super().Place_Down()

    def Equip(self):
        self.Set_Equip(True, self.game.player)
        self.game.player.Set_Active_Weapon(self)

    def Unequip(self):
        self.Set_Equip(False, None)
