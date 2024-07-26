import math
import random
import pygame

from scripts.particle import Particle
from scripts.traps.trap_handler import Trap_Handler
from scripts.entities.effects import Status_Effect_Handler
from scripts.entities.entities import PhysicsEntity


class Moving_Entity(PhysicsEntity):
    def __init__(self, game, e_type, pos, size):
        super().__init__(game, e_type, pos, size)
        self.velocity = [0, 0, 0, 0]
        self.friction = 2
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.animation_state = 'up'

        self.direction = (0,0,0,0)
        self.direction_x = 0
        self.direction_y = 0
        self.direction_x_holder = 0
        self.direction_y_holder = 0

        self.health = 100
        self.max_health = self.health
        self.mana = 0
        self.max_mana = 100
        self.snared = 0

        self.nearby_traps = []
        self.nearby_enemies = []
        self.player_hit = False
        
        self.action = ''
        self.anim_offset = (0, 0)
        self.flip = [False, False]
        self.set_action('')
        self.frame_movement = (0.0, 0.0)
        self.last_frame_movement = (0.0, 0.0)

        # Status Effects
        self.is_on_fire = 0
        self.fire_cooldown = 0
        self.fire_animation = 0
        self.fire_animation_cooldown = 0

        self.poisoned = 0
        self.poisoned_cooldown = 0
        self.poison_animation = 0
        self.poison_animation_cooldown = 0

        self.is_on_ice = 0
        self.frozen = 0 
        self.frozen_cooldown = 0
        self.frozen_animation = 0
        self.frozen_animation_cooldown = 0

        self.wet = 0 
        self.wet_cooldown = 0
        self.wet_animation = 0
        self.wet_animation_cooldown = 0

        self.active = 0


        self.status_effects = Status_Effect_Handler(self)
    
    # Set new action for animation
    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.type + '_' + self.action

    # Update the entity 
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.direction_x = movement[0]
        self.direction_y = movement[1]
        
        self.frame_movement = (movement[0]*4/self.friction + self.velocity[0], movement[1]*4/self.friction + self.velocity[1])
        self.Update_Status_Effects()


        self.Update_Traps()
        self.nearby_enemies.clear()
        self.Nearby_Enemies(20)

  
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            

        self.Movement(movement, tilemap)
    
    # Movement handling
    # TODO Cleanp
    def Movement(self, movement, tilemap):
        if self.Collision_Detection():
            return


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
        
                
        if movement[0] > 0:
            self.flip[0] = False
            self.set_action('side')
        if movement[0] < 0:
            self.flip[0] = True
            self.set_action('side')
        if movement[1] < 0:
            self.set_action('up')
            self.flip[1] = False
        if movement[1] > 0:
            self.flip[1] = True
            self.set_action('down')

        self.last_frame_movement = self.frame_movement

    def Collision_Detection(self):
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
        self.nearby_traps = Trap_Handler.find_nearby_traps(self.game, self.pos, 20)
        for trap in self.nearby_traps:
            trap.Update(self)

    def Nearby_Enemies(self, max_distance):
        self.nearby_enemies.clear()
        for enemy in self.game.enemies:
            distance = math.sqrt((self.pos[0] - enemy.pos[0]) ** 2 + (self.pos[1] - enemy.pos[1]) ** 2)
            if distance < max_distance and not enemy == self:
                self.nearby_enemies.append(enemy)

    def Damage_Taken(self, damage):
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

    # Ice mechanic
    # TODO Improve
    def On_Ice(self):
        if not self.is_on_ice:
            self.is_on_ice = 10
        else:
            self.is_on_ice -= 1
            self.frame_movement = self.last_frame_movement 

    # Handle status effects
    def Update_Status_Effects(self):
        self.friction = 2
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
    
    #set poison effect
    def Set_Poisoned(self, poison_time):
        self.poisoned =  max(random.randint(2, poison_time), self.poisoned)

    #set frozen effect
    def Set_Frozen(self, freeze_time):
        if self.wet:
            freeze_time *= 2
            self.wet = 0
        self.frozen = max(3, freeze_time)

    # Set wet effect
    def Set_Wet(self, wet_time):
        if self.is_on_fire:
            self.is_on_fire = 0
        if self.frozen:
            self.frozen -= 1
        self.wet = max(2, wet_time)
    
    def Set_Dry(self, drying):
        self.wet = max(0, self.wet - drying)
        print(self.wet)


    #set Fire effect
    def Set_On_Fire(self, fire_time):
        if self.wet:
            return
        self.is_on_fire = max(random.randint(fire_time, fire_time * 2), self.is_on_fire)

    # Slow the entity down by increasing friction
    def Slow_Down(self, effect):
        self.friction = max(2, effect)

    def Set_Active(self, duration):
        self.active = duration

    def Reduce_Active(self):
        self.active -= 1

    # Render entity
    def render(self, surf, offset=(0, 0)):
        entity_image_head = self.game.assets[self.animation + '_head'][0]
        entity_image_head = pygame.transform.scale(entity_image_head, (16, 12))

        entity_image_body = self.game.assets[self.animation + '_body'][0]
        entity_image_body = pygame.transform.scale(entity_image_body, (16, 9))

        entity_image_legs = self.game.assets[self.animation + '_legs'][0]
        entity_image_legs = pygame.transform.scale(entity_image_legs, (16, 3))

        surf.blit(pygame.transform.flip(entity_image_legs, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] + 9))
        surf.blit(pygame.transform.flip(entity_image_body, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        surf.blit(pygame.transform.flip(entity_image_head, self.flip[0], False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1] - 12))
        self.status_effects.render_fire(self.game, surf, offset)
        self.status_effects.render_poison(self.game, surf, offset)
        self.status_effects.render_frozen(self.game, surf, offset)
        self.status_effects.render_wet(self.game, surf, offset)