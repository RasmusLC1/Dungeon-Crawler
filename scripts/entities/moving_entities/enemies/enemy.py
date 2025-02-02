from scripts.entities.moving_entities.moving_entity import Moving_Entity
from scripts.entities.moving_entities.enemies.behavior.path_finding import Path_Finding
from scripts.entities.moving_entities.enemies.behavior.attack_strategies import Attack_Stategies
from scripts.entities.textbox.enemy_textbox import Enemy_Textbox
from scripts.decoration.bones.bones import Bones 
from scripts.entities.moving_entities.enemies.behavior.intent_manager import Intent_Manager


import pygame



class Enemy(Moving_Entity):
    def __init__(self, game, pos, type, health, strength, max_speed, agility, intelligence, stamina, sub_category, size = (32, 32)):

        super().__init__(game, type, 'enemy', pos, size, health, strength, max_speed, agility, intelligence, stamina, sub_category)
        self.random_movement_cooldown = 0
        self.alert_cooldown = 0
        self.active_weapon = None
        self.weapon_cooldown = 0
        self.target = self.game.player.pos # Default target is set to player

        self.path_finding = Path_Finding(game, self) # Pathfinding logic for enemy
        self.destination = (0,0)
        self.attack_strategies = Attack_Stategies(game, self) # Pathfinding logic for enemy
        self.intent_manager = Intent_Manager(game, self)

        self.distance_to_player = 9999 # Distance to player
        self.charge = 0 # Determines when the enemy attacks
        self.attack_strategy = 'direct' # Attack strategy that the enemy utalises
        self.path_finding_strategy = 'standard' # Maptype that is used for navigation

        self.attack_distance  = 60
        self.disengage_distance = 100
        self.max_weapon_charge = 60


        self.locked_on_target = 0 # If the enemy is locked onto a target, then it will not switch based on clatter

        self.attack_symbol_offset = 20
        

        self.text_box = Enemy_Textbox(self)
    
    def Save_Data(self):
        super().Save_Data()
        self.intent_manager.Save_Data()
        self.saved_data['alert_cooldown'] = self.alert_cooldown
        self.saved_data['random_movement_cooldown'] = self.random_movement_cooldown
        self.saved_data['distance_to_player'] = self.distance_to_player
        self.saved_data['charge'] = self.charge
        self.saved_data['attack_strategy'] = self.attack_strategy
        self.saved_data['path_finding_strategy'] = self.path_finding_strategy
        self.saved_data['locked_on_target'] = self.locked_on_target
        self.saved_data['target'] = self.target
        self.saved_data['ID'] = self.ID



    def Load_Data(self, data):
        super().Load_Data(data)
        self.intent_manager.Load_Data(data)
        self.alert_cooldown = data['alert_cooldown']
        self.random_movement_cooldown = data['random_movement_cooldown']
        self.distance_to_player = data['distance_to_player']
        self.charge = data['charge']
        self.attack_strategy = data['attack_strategy']
        self.path_finding_strategy = data['path_finding_strategy']
        self.locked_on_target = data['locked_on_target']
        self.ID = data['ID']
        self.target = data['target']



    def Update(self, tilemap, movement=(0, 0)):
        self.intent_manager.Update_Behavior()
        self.path_finding.Path_Finding()
        movement = self.direction
        
        super().Update(tilemap, movement = movement)

        self.Set_Direction_Holder()

        self.Update_Alert_Cooldown()
        self.Update_Locked_On_Target()


        
    def Set_Attack_Strategy(self, strategy):
        self.attack_strategy = strategy
    
    def Set_Direction_Holder(self):
        if self.direction_x or self.direction_y:
            self.direction_x_holder = self.direction_x
            self.direction_y_holder = self.direction_y

    def Reset_Charge(self):
        self.charge = 0

    def Set_Charge_To_Max(self):
        self.charge = self.max_weapon_charge
    
    def Entity_Collision_Detection(self, tilemap):
        colliding_entity = super().Entity_Collision_Detection(tilemap)

        if colliding_entity:
            if colliding_entity.type == 'player':
                # Prevent further movement towards the player by stopping the enemy's movement
                self.direction = (0, 0)
                return colliding_entity

            # Collision logic for other entities
            collision_vector = pygame.math.Vector2(self.pos[0] - colliding_entity.pos[0],
                                                self.pos[1] - colliding_entity.pos[1])
            if collision_vector.length() > 0:
                collision_vector = collision_vector.normalize()
                direction_vector = pygame.math.Vector2(self.direction)
                reflected_direction = direction_vector.reflect(collision_vector)

                if self.Future_Rect(reflected_direction).colliderect(self.game.player.rect()):
                    self.direction = (0, 0)

                    return self.game.player

                self.direction = (reflected_direction.x, reflected_direction.y)

        return None
    
    def Attack(self):
        
        # Check if the player is invisible
        if self.game.player.effects.invisibility.effect:
            return False
        return True

    def Set_Attack_Direction(self):
        if not self.charge:
            self.attack_direction = (0, 0)
            return
        
        super().Set_Attack_Direction()
        
    def Attack_Strategy(self):
        return self.attack_strategies.Attack_Strategy()


    def Update_Movement(self, movement):
        return super().Update_Movement(movement)

    
    def Set_Active_Weapon(self, weapon):
        self.active_weapon = weapon

    def Update_Alert_Cooldown(self):
        if self.alert_cooldown:
            self.alert_cooldown = max(0, self.alert_cooldown - 1)

    def Set_Alert_Cooldown(self, amount):
        self.alert_cooldown = amount

    def Set_Destination(self, destination):
        self.destination = destination

    def Find_New_Path(self):
        
        self.Set_Target(self.destination)
        self.path_finding.Find_Shortest_Path()

    def Weapon_Cooldown(self):
        if self.weapon_cooldown:
            self.weapon_cooldown = max(0, self.weapon_cooldown - 1)

    def Set_Idle(self):
        pass

    def Update_Locked_On_Target(self):
        if not self.locked_on_target:
            return
        self.locked_on_target = max(0, self.locked_on_target - 1)
    
    def Set_Locked_On_Target(self, value):
        self.locked_on_target = value
        
    def Damage_Taken(self, damage, direction = (0, 0)):
        # No damage done simply return
        if not super().Damage_Taken(damage, direction):
            return
        if self.health <= 0:
            self.Spawn_Bones()
            self.Drop_Weapon()

            self.game.enemy_handler.Delete_Enemy(self)
            if self.distance_to_player < 150:
                self.game.player.Increase_Souls(5)



        self.direction = pygame.math.Vector2(self.direction_x, self.direction_y)

    def Spawn_Bones(self):
        bones = Bones(self.game, self.pos, self.type)
        self.game.decoration_handler.Add_Decoration(bones)
        return

    def Drop_Weapon(self):
        if not self.active_weapon:
            return
        # Remove weapon from Tile
        tile = self.game.tilemap.Current_Tile(self.active_weapon.tile)
        if not tile:
            tile = self.game.tilemap.Current_Tile(self.active_weapon.tile)
            if not tile:
                return

        tile.Clear_Entity(self.active_weapon.ID)

        self.active_weapon.pos = self.pos.copy()
        self.active_weapon.Set_Equip(False)
        self.active_weapon.Place_Down()
        self.game.item_handler.Add_Item(self.active_weapon)
        self.active_weapon.Set_Tile()
        self.active_weapon.Set_Delete_Countdown()
        self.active_weapon = None

    def Trap_Collision_Handler(self):
        for trap in self.nearby_traps:
            if self.rect().colliderect(trap.rect()):
                # Run away in in the same direction the enemy was moving previously
                # Use min and max to prevent it teleporting
                if self.direction_x_holder < 0:
                    self.direction_x = max(-0.4, self.direction_x_holder * 4)
                else:
                    self.direction_x = min(0.4, self.direction_x_holder * 4)

                if self.direction_y_holder < 0:
                    self.direction_y = max(-0.4, self.direction_y_holder * 4)
                else:
                    self.direction_y = min(0.4, self.direction_y_holder * 4)

                self.direction = (self.direction_x, self.direction_y)
            else:
                # Check if the enemy will collide soon, if yes redirect in the opposite direction
                if self.Future_Rect(self.direction).colliderect(trap.rect()):
                    self.direction_x *= -1
                    self.direction_y *= -1
                    self.direction = (self.direction_x, self.direction_y)
                    break

    def Future_Rect(self, direction):
             return pygame.Rect(self.pos[0] + direction[0]*32, self.pos[1] + direction[1]*32, self.size[0], self.size[1])

    
    def Render(self, surf, offset = (0,0)):
        super().Render(surf, offset)
        if self.active < 30:
            return
        self.Render_Weapons(surf, offset)
        self.Render_Health_Bar(surf, offset)
        self.Render_Attacking_Symbol(surf, offset)

    def Render_Health_Bar(self, surf, offset = (0,0)):
        health_fraction = self.health / self.max_health

        # Map the fraction to an index from 0 to 9 (assuming 10 total images)
        health_index = max(-1, min(int((1 - health_fraction) * 9), 9))  # Invert fraction and scale to index range

        # Correct potential rounding issues at full health
        if self.health == self.max_health:
            health_index = 0

        health_Bar = self.game.assets['health_bar'][health_index]
        alpha_value = 150
        health_Bar.set_alpha(alpha_value)
        surf.blit(health_Bar, (self.rect().left - offset[0], self.rect().bottom - offset[1] - self.size[1] // 2 + 4))


    def Render_Attacking_Symbol(self, surf, offset = (0,0)):
        if self.charge < 20:
            return
        exclamation_mark = self.game.assets['exclamation_mark'][0]

        alpha_value = max(0, min(255, self.charge * 7))
        exclamation_mark.set_alpha(alpha_value)
        surf.blit(exclamation_mark, (self.rect().left - offset[0], self.rect().top - offset[1] - self.attack_symbol_offset))


    def Render_Weapons(self, surf, offset):
        if self.active_weapon:
            self.active_weapon.Render_Equipped_Enemy(surf, offset)
        