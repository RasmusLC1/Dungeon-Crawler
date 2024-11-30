from scripts.entities.enemies.enemy import Enemy
from scripts.entities.enemies.decrepit_bones_melee import Decrepit_Bones_Melee
from scripts.entities.enemies.decrepit_bones_ranged import Decrepit_Bones_Ranged
from scripts.entities.enemies.fire_spirit import Fire_Spirit
from scripts.entities.enemies.ice_spirit import Ice_Spirit
from scripts.entities.enemies.spider import Spider
from scripts.entities.enemies.wight_king import Wight_King

import random
import math

class Enemy_Handler():
    def __init__(self, game):
        self.game = game
        self.enemies = []
        self.nearby_enemies = []
        self.saved_data = {}


    def Save_Enemy_Data(self):
        for enemy in self.enemies:
            enemy.Save_Data()
            self.saved_data[enemy.ID] = enemy.saved_data

    def Load_Data(self, data):
        for ID, item_data in data.items():
            if not item_data:
                continue
            try:
                type = item_data['sub_type']
                pos = item_data['pos']
                if item_data['category'] == 'enemy':
                    self.Enemy_Spawner(type, pos, item_data)
                    continue
            except Exception as e:
                print("DATA WRONG", item_data, e)

    def Clear_Enemies(self):
        self.enemies.clear()
        self.nearby_enemies.clear()
        self.saved_data.clear()


    
    def Initialise(self):
        spawners = self.game.tilemap.extract([('spawners', 1)])
        spawners_length = len(spawners)
        for i in range(20):
            spawner_index = random.randint(0, spawners_length - 1)
            spawner = spawners[spawner_index]
            enemy_variant = random.randint(0, 2)
            type = None
            if enemy_variant < 2: # Melee Decrepit Bones
                random_value = random.randint(0, 10)
                if random_value < 7:
                    type = 'decrepit_bones_melee'
                else:
                    type = 'decrepit_bones_ranged'

            elif enemy_variant == 2: # Fire spirit
                type = 'fire_spirit'
            elif enemy_variant == 3: # Ice spirit
                type = 'ice_spirit'
            elif enemy_variant == 4: # Spider
                type = 'spider'
            elif enemy_variant == 5: # Wight King
                type = 'wight_king'
            if type:
                pos = spawner.pos
                self.Enemy_Spawner(type, pos)

    def Enemy_Spawner(self, type, pos, data = None):
        enemy = None
        if type == 'decrepit_bones_melee':
            enemy = self.Spawn_Melee_Decrepit_Bones(pos)
        elif type == 'decrepit_bones_ranged':
                enemy = self.Spawn_Ranged_Decrepit_Bones(pos)
        elif type == 'fire_spirit':
            enemy = self.Spawn_Fire_Spirit(pos)
        elif type == 'ice_spirit':
            enemy = self.Spawn_Ice_Spirit(pos)
        elif type == 'spider':
            enemy = self.Spawn_Spider(pos)
        elif type == 'wight_king':
            enemy = self.Spawn_Wight_King(pos)
        
        if enemy:
            if data:
                enemy.Load_Data(data)
            self.enemies.append(enemy)
        return enemy

    def Spawn_Melee_Decrepit_Bones(self, pos):
        health = 30
        strength = 2
        speed = 2
        agility = 2 
        intelligence = 2
        stamina = 2
        return Decrepit_Bones_Melee(
            self.game,
            pos, 
            health,
            strength,
            speed,
            agility,
            intelligence,
            stamina)
        
    def Spawn_Ranged_Decrepit_Bones(self, pos):
        health = 30
        strength = 2
        speed = 2
        agility = 2 
        intelligence = 2
        stamina = 2
        return Decrepit_Bones_Ranged(
            self.game,
            pos, 
            health,
            strength,
            speed,
            agility,
            intelligence,
            stamina)
        
    def Spawn_Fire_Spirit(self, pos):
        health = 60
        strength = 4
        speed = 5
        agility = 4 
        intelligence = 2
        stamina = 2
        return Fire_Spirit(self.game,
                            pos, 
                            'fire_spirit',
                            health,
                            strength,
                            speed,
                            agility,
                            intelligence,
                            stamina)
        

    def Spawn_Ice_Spirit(self, pos):
        health = 100
        strength = 7
        speed = 3
        agility = 3
        intelligence = 2
        stamina = 2
        return Ice_Spirit(self.game,
                        pos, 
                        'ice_spirit',
                        health,
                        strength,
                        speed,
                        agility,
                        intelligence,
                        stamina)
        

    def Spawn_Spider(self, pos):
        health = 80
        strength = 4
        speed = 3
        agility = 3
        intelligence = 5
        stamina = 2
        return Spider(self.game,
                    pos, 
                    'spider',
                    health,
                    strength,
                    speed,
                    agility,
                    intelligence,
                    stamina)
    
    def Spawn_Wight_King(self, pos):
        health = 150
        strength = 3
        speed = 3
        agility = 6
        intelligence = 5
        stamina = 5
        return Wight_King(self.game,
                    pos, 
                    health,
                    strength,
                    speed,
                    agility,
                    intelligence,
                    stamina)

    def Delete_Enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
        self.game.entities_render.Remove_Entity(enemy)

    def Update(self):
        for enemy in self.enemies:
            enemy.Update(self.game.tilemap)      
                

    def Find_Nearby_Enemies(self, entity, max_distance):
        if max_distance <= 5:
            return self.game.tilemap.Search_Nearby_Tiles(max_distance, entity.pos, 'enemy')
        else:
            return self.Find_Nearby_Enemies_Long_Distance(entity, max_distance)
    
    # Long distance enemy search
    def Find_Nearby_Enemies_Long_Distance(self, entity, max_distance):
        nearby_enemies = []
        for enemy in self.enemies:
            distance = math.sqrt((entity.pos[0] - enemy.pos[0]) ** 2 + (entity.pos[1] - enemy.pos[1]) ** 2)
            if distance < max_distance and not enemy.ID == entity.ID:
                nearby_enemies.append(enemy)
        return nearby_enemies
    



    def Find_Enemy(self, ID):
        for enemy in self.enemies:
            if enemy.ID == ID:
                return enemy
            
        return None