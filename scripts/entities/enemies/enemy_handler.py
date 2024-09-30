from scripts.entities.enemies.enemy import Enemy
from scripts.entities.enemies.decrepit_bones_melee import Decrepit_Bones_Melee
from scripts.entities.enemies.decrepit_bones_ranged import Decrepit_Bones_Ranged
from scripts.entities.enemies.fire_spirit import Fire_Spirit
from scripts.entities.enemies.ice_spirit import Ice_Spirit
from scripts.entities.enemies.spider import Spider

import random
import math

class Enemy_Handler():
    def __init__(self, game):
        self.game = game
        self.enemies = []
        self.nearby_enemies = []
        self.Initialise()

    
    def Initialise(self):
        spawners = self.game.tilemap.extract([('spawners', 1)])
        spawners_length = len(spawners)
        for i in range(10):
            spawner_index = random.randint(0, spawners_length - 1)
            spawner = spawners[spawner_index]
            enemy_variant = random.randint(0, 4)
            if enemy_variant == 0: # Melee Decrepit Bones
                self.Spawn_Melee_Decrepit_Bones(spawner)
            elif enemy_variant == 1: # Ranged Decrepit Bones
                self.Spawn_Ranged_Decrepit_Bones(spawner)
            elif enemy_variant == 2: # Fire spirit
                self.Spawn_Fire_Spirit(spawner)
            elif enemy_variant == 3: # Ice spirit
                self.Spawn_Ice_Spirit(spawner)
            elif enemy_variant == 4: # Spider
                self.Spawn_Spider(spawner)

    def Spawn_Melee_Decrepit_Bones(self, spawner):
        health = 30
        strength = 2
        speed = 2
        agility = 2 
        intelligence = 2
        stamina = 2
        self.enemies.append(Decrepit_Bones_Melee(
            self.game,
            spawner['pos'], 
            (self.game.assets[spawner['type']][0].get_width(),
            self.game.assets[spawner['type']][0].get_height()),
            'decrepit_bones',
            health,
            strength,
            speed,
            agility,
            intelligence,
            stamina))
        
    def Spawn_Ranged_Decrepit_Bones(self, spawner):
        health = 30
        strength = 2
        speed = 2
        agility = 2 
        intelligence = 2
        stamina = 2
        self.enemies.append(Decrepit_Bones_Ranged(
            self.game,
            spawner['pos'], 
            (self.game.assets[spawner['type']][0].get_width(),
            self.game.assets[spawner['type']][0].get_height()),
            'decrepit_bones',
            health,
            strength,
            speed,
            agility,
            intelligence,
            stamina))
        
    def Spawn_Fire_Spirit(self, spawner):
        health = 60
        strength = 4
        speed = 5
        agility = 4 
        intelligence = 2
        stamina = 2
        self.enemies.append(
            Fire_Spirit(self.game,
                        spawner['pos'], 
                        (self.game.assets[spawner['type']][0].get_width(),
                            self.game.assets[spawner['type']][0].get_height()),
                            'fire_spirit',
                            health,
                            strength,
                            speed,
                            agility,
                            intelligence,
                            stamina))
        

    def Spawn_Ice_Spirit(self, spawner):
        health = 100
        strength = 7
        speed = 3
        agility = 3
        intelligence = 2
        stamina = 2
        self.enemies.append(
            Ice_Spirit(self.game,
                        spawner['pos'], 
                        (self.game.assets[spawner['type']][0].get_width(),
                            self.game.assets[spawner['type']][0].get_height()),
                            'ice_spirit',
                            health,
                            strength,
                            speed,
                            agility,
                            intelligence,
                            stamina))
        
    def Spawn_Spider(self, spawner):
        health = 80
        strength = 4
        speed = 3
        agility = 3
        intelligence = 5
        stamina = 2
        self.enemies.append(
            Spider(self.game,
                        spawner['pos'], 
                        (self.game.assets[spawner['type']][0].get_width(),
                            self.game.assets[spawner['type']][0].get_height()),
                            'spider',
                            health,
                            strength,
                            speed,
                            agility,
                            intelligence,
                            stamina))


    def Delete_Enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
        self.game.entities_render.Remove_Entity(enemy)

    def Update(self):
        for enemy in self.enemies:
            enemy.Update(self.game.tilemap)      
                

    def Find_Nearby_Enemies(self, entity, max_distance):
        nearby_enemies = []
        for enemy in self.enemies:
            distance = math.sqrt((entity.pos[0] - enemy.pos[0]) ** 2 + (entity.pos[1] - enemy.pos[1]) ** 2)
            if distance < max_distance and not enemy == entity:
                nearby_enemies.append(enemy)
        return nearby_enemies
