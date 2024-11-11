import math
from scripts.engine.utility.helper_functions import Helper_Functions

class Entity_Renderer():
    def __init__(self, game):
        self.game = game
        self.entities = []
        self.nearby_entities = []

    def Clear_Entities(self):
        self.entities.clear()
        self.nearby_entities.clear()

    def Update(self):
        
        self.Find_Nearby_Entities()
        self.nearby_entities.sort(key=lambda entity: entity.pos[1])

    

    def Find_Nearby_Entities(self):
        self.nearby_entities.clear()
        self.entities = []
        for tile in self.game.ray_caster.tiles:
            self.entities.extend(tile.entities)

    def Add_Entity(self, entity):
        if entity in self.entities:
            return
        self.entities.append(entity)
        self.nearby_entities_cooldown = 0

    
    def Remove_Entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            
        if entity in self.nearby_entities:
            self.nearby_entities.remove(entity)
            self.nearby_entities_cooldown = 0

    def Render(self, surf, offset = (0,0)):
        for entity in self.entities:
            entity.Render(surf, offset)