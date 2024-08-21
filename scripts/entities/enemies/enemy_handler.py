from scripts.entities.enemies.enemy import Enemy
import math

class Enemy_Handler():
    def __init__(self, game):
        self.game = game
        self.enemies = []
        self.nearby_enemies = []
        self.Initialise()

    
    def Initialise(self):
        for spawner in self.game.tilemap.extract([('spawners', 1)]):
            if spawner['variant'] == 1:
                self.enemies.append(Enemy(self.game, spawner['pos'],  (self.game.assets[spawner['type']][0].get_width(), self.game.assets[spawner['type']][0].get_height()), 'DecrepitBones'))

    def Delete_Enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
        self.game.entities_render.Remove_Entity(enemy)

    def Update(self):
        for enemy in self.enemies:
            enemy.update(self.game.tilemap)
            
            
                

    def Find_Nearby_Enemies(self, entity, max_distance):
        nearby_enemies = []
        for enemy in self.enemies:
            distance = math.sqrt((entity.pos[0] - enemy.pos[0]) ** 2 + (entity.pos[1] - enemy.pos[1]) ** 2)
            if distance < max_distance and not enemy == entity:
                nearby_enemies.append(enemy)
        return nearby_enemies