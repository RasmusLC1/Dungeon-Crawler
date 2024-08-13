import math
import random
import pygame

from scripts.engine.particles.particle import Particle
from scripts.traps.trap_handler import Trap_Handler
from scripts.entities.effects import Status_Effect_Handler
from scripts.entities.entities import PhysicsEntity


class Moving_Entity(PhysicsEntity):
    def __init__(self, game, e_type, pos, size):
        super().__init__(game, e_type, pos, size)
        self.velocity = [0, 0] # Velocity of the player
        self.friction = self.game.render_scale # Friction, set to the renderscale
        self.friction_holder = self.friction # Holder for friction to reset it
        self.acceleration = 1 # Default acceleration
        self.acceleration_holder = self.acceleration # accelarition holder to reset it
        self.max_speed = 2.0  # Max speed of the entity
        self.max_speed_holder = self.max_speed # Max speed holder to reset it
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False} # Check for wall collision in each direction

        self.animation_state = 'up'
        self.idle_count = 0
        self.animation_num = 0
        self.animation_num_max = 1
        self.animation_num_cooldown = 0
        self.attacking = 0


        self.direction = (0,0,0,0)
        self.direction_x = 0
        self.direction_y = 0
        self.direction_x_holder = 0
        self.direction_y_holder = 0

        self.health = 100
        self.max_health = self.health
        self.damage_cooldown = 0
        self.mana = 0
        self.max_mana = 100
        self.snared = 0

        self.nearby_traps = []
        self.nearby_traps_cooldown = 0
        self.nearby_enemies = []
        self.player_hit = False
        
        self.action = ''
        self.anim_offset = (0, 0)
        self.flip = [False, False]
        self.Set_Animation('')
        self.frame_movement = (0.0, 0.0)
        self.last_frame_movement = (0.0, 0.0)

        # Attributes, placeholder should be assigned on creation
        self.strength = 5 # Damage and moving items
        self.agility = 5 # weapon recharge speed, movement speed and lockpicking
        self.intelligence = 5 # spells and trap detection
        self.stamina = 5 # movement ability recharge and weapon cooldown

        
        


        self.status_effects = Status_Effect_Handler(self)
    
    # Set new action for animation
    def Set_Animation(self, action):
        

        if action != self.action:
            self.action = action
            self.animation = self.type + '_' + self.action

    # Update the entity 
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.Update_Movement(movement)
        self.Update_Status_Effects()


        self.Update_Traps()
        self.nearby_enemies.clear()
        self.Nearby_Enemies(20)
        self.Update_Damage_Cooldown()

  
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            

        self.Movement(movement, tilemap)
    
    def Update_Movement(self, movement):
        # Apply acceleration to velocity based on input
        self.velocity[0] += movement[0] * self.acceleration
        self.velocity[1] += movement[1] * self.acceleration

        # Clamp the velocity to max speed
        self.velocity[0] = max(-self.max_speed, min(self.velocity[0], self.max_speed))
        self.velocity[1] = max(-self.max_speed, min(self.velocity[1], self.max_speed))

        # Apply friction when there's no input
        if movement[0] == 0:
            if self.velocity[0] > 0:
                self.velocity[0] = max(self.velocity[0] - self.friction, 0)
            else:
                self.velocity[0] = min(self.velocity[0] + self.friction, 0)
        
        if movement[1] == 0:
            if self.velocity[1] > 0:
                self.velocity[1] = max(self.velocity[1] - self.friction, 0)
            else:
                self.velocity[1] = min(self.velocity[1] + self.friction, 0)

        self.direction_x = movement[0]
        self.direction_y = movement[1]

        # Calculate frame movement based on updated velocity
        self.frame_movement = (self.velocity[0] / self.game.render_scale, self.velocity[1] / self.game.render_scale)

    # Movement handling
    # TODO Cleanp
    def Movement(self, movement, tilemap):
        if self.Entity_Collision_Detection():
            return

        self.Tile_Map_Collision_Detection(tilemap)
        self.Update_Animation()
        if self.attacking:
            self.Set_Animation('attack')
            return
        
        # if movement[0] or movement[1]:
        #     self.idle_count = 0
        self.Set_Action(movement)

        if self.idle_count > 60:
            self.Set_Idle()
        else:
            self.idle_count += 1

        self.last_frame_movement = self.frame_movement
    


    def Update_Animation(self):
        if not self.animation_num_cooldown:
            self.animation_num += 1
            if self.animation_num >= self.animation_num_max:
                self.animation_num = 0
            self.animation_num_cooldown = 10
        else:
            self.animation_num_cooldown -= 1

    # Set the idle state every 60 ticks to either up or down depending on last input
    def Set_Idle(self):
        
        if self.direction_y_holder < 0:
            self.Set_Animation('idle_up')
        else:
            self.Set_Animation('idle_down')

    def Set_Action(self, movement):
        # Check for movement
        if not movement[0] and not movement[1]:
            return
        self.idle_count = 0
        

        
        if movement[0] > 0:
            self.flip[0] = False
            self.Set_Animation('idle_down')
        if movement[0] < 0:
            self.flip[0] = True
            self.Set_Animation('idle_down')
        if movement[1] < 0:
            self.Set_Animation('idle_up')
        if movement[1] > 0:
            self.Set_Animation('idle_down')
        

    def Tile_Map_Collision_Detection(self, tilemap):
        self.pos[0] += self.frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if self.frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
        
        self.pos[1] += self.frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if self.frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y

    def Entity_Collision_Detection(self):
        future_pos = (self.pos[0] + self.frame_movement[0], self.pos[1] + self.frame_movement[1])
        for enemy in self.nearby_enemies:
            if enemy.rect().colliderect(self.rect_future(future_pos)):
                if not self.type == 'player':
                    return True
        if not self.type == 'player': 
            if self.game.player.rect().colliderect(self.rect_future(future_pos)):
                self.player_hit = True
                return True
            
        return False


    def rect_future(self, future_pos):
        return pygame.Rect(future_pos[0], future_pos[1], self.size[0], self.size[1])     
    
    # Update only the nearby traps
    def Update_Traps(self):
        if not self.nearby_traps_cooldown:
            self.Find_Nearby_Traps(40)
            self.nearby_traps_cooldown = 10
        else:
            self.nearby_traps_cooldown -= 1
        for trap in self.nearby_traps:
            trap.Update(self)

    def Find_Nearby_Traps(self, distance):
        self.nearby_traps = self.game.trap_handler.find_nearby_traps(self.pos, distance)

    def Nearby_Enemies(self, max_distance):
        self.nearby_enemies.clear()
        for enemy in self.game.enemies:
            distance = math.sqrt((self.pos[0] - enemy.pos[0]) ** 2 + (self.pos[1] - enemy.pos[1]) ** 2)
            if distance < max_distance and not enemy == self:
                self.nearby_enemies.append(enemy)

    def Update_Damage_Cooldown(self):
        if self.damage_cooldown:
            print(self.damage_cooldown)
            self.damage_cooldown -= 1

    def Damage_Taken(self, damage):
        print(self.type)
        if self.damage_cooldown:
            return
        
        self.damage_cooldown = 10
        self.health -= damage
        if self.health <= 0:
            print("GAME OVER")

    # Return true if healing was successfull
    def Healing(self, healing):
        if self.health >= self.max_health:
            return False     
        self.health = min(self.max_health, self.health + healing)
        return True
    
    def Increase_Mana(self, added_mana):
        if self.mana >= self.max_mana:
            return False     
        self.mana = min(self.max_mana, self.mana + added_mana)
        return True
        
    # Push the entity in the given direction
    def Push(self, x_direction, y_direction):
        self.pos[0] += x_direction
        self.pos[1] += y_direction

    # Ice mechanic, lower friction and acceleration to simulate ice
    def On_Ice(self, effect):
        self.friction = max(0.1, self.friction / effect)
        self.acceleration = max(0.4, self.acceleration / effect)

    # Handle status effects
    def Update_Status_Effects(self):
        self.friction = self.friction_holder
        self.max_speed = self.max_speed_holder
        self.status_effects.OnFire()
        self.status_effects.Snare()
        self.status_effects.Poisoned()
        self.status_effects.Frozen()
        self.status_effects.Wet()
    
    def Set_Effect(self, effect, duration):
        if effect == 'Snare':
            self.Set_Snare(duration)
        elif effect == 'Poison':
            self.Set_Poisoned(duration)
        elif effect == 'Freeze':
            self.Set_Frozen(duration)
        elif effect == 'Fire':
            self.Set_On_Fire(duration)
        elif effect == 'Wet':
            self.Set_Wet(duration)
        elif effect == 'Dry':
            self.Set_Dry(duration)
        elif effect == 'Slow_Down':
            self.Slow_Down(duration)
        else:
            print("EFFECT MISSING", effect)
            exit()

    #set snare effect
    def Set_Snare(self, snare_time):
        self.snared = snare_time
    
    
    # Slow the entity down by increasing friction
    def Slow_Down(self, effect):
        self.max_speed = max(0.1, self.max_speed / effect)


    
    
    # Render entity
    def Render(self, surf, offset=(0, 0)):
        # Don't Render the enemy if their light level is very low
        # Simulates low visibility
        if not self.Update_Light_Level():
            return
        

        # Load and scale the entity images, split to allow better animation
        entity_image_head = self.game.assets[self.animation + '_head'][0]
        entity_image_head = pygame.transform.scale(entity_image_head, (16, 12))

        entity_image_body = self.game.assets[self.animation + '_body'][0]
        entity_image_body = pygame.transform.scale(entity_image_body, (16, 9))

        entity_image_legs = self.game.assets[self.animation + '_legs'][0]
        entity_image_legs = pygame.transform.scale(entity_image_legs, (16, 3))
        
        # Set the alpha value to make the entity fade out
        alpha_value = max(0, min(255, self.active)) 
        entity_image_head.set_alpha(alpha_value)
        entity_image_body.set_alpha(alpha_value)
        entity_image_legs.set_alpha(alpha_value)

         # Create a darkening surface that is affected by darkness
        dark_surface_head = pygame.Surface(entity_image_head.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))  

        dark_surface_body = pygame.Surface(entity_image_body.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_body.fill((self.light_level, self.light_level, self.light_level, 255))

        dark_surface_legs = pygame.Surface(entity_image_legs.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_legs.fill((self.light_level, self.light_level, self.light_level, 255))


        # Apply darkening effect using BLEND_RGBA_MULT
        entity_image_head.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        entity_image_body.blit(dark_surface_body, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        entity_image_legs.blit(dark_surface_legs, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        surf.blit(pygame.transform.flip(entity_image_legs, self.flip[0], False), 
                (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] + 9))
        surf.blit(pygame.transform.flip(entity_image_body, self.flip[0], False), 
                (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        surf.blit(pygame.transform.flip(entity_image_head, self.flip[0], False), 
                (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] - 12))

        # Render status effects
        self.status_effects.render_fire(self.game, surf, offset)
        self.status_effects.render_poison(self.game, surf, offset)
        self.status_effects.render_frozen(self.game, surf, offset)
        self.status_effects.render_wet(self.game, surf, offset)
