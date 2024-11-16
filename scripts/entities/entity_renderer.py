import math
from scripts.engine.utility.helper_functions import Helper_Functions

class Entity_Renderer():
    def __init__(self, game):
        self.game = game
        self.entities = []

    def Clear_Entities(self):
        self.entities.clear()

    def Update(self):
        
        self.Find_Nearby_Entities()
        self.entities.sort(key=lambda entity: entity.pos[1])

    

    def Find_Nearby_Entities(self):
        self.entities.clear()
        for tile in self.game.ray_caster.tiles:
            self.entities.extend(tile.entities)

    def Add_Entity(self, entity):
        if entity in self.entities:
            return
        self.entities.append(entity)

    
    def Remove_Entity(self, entity):
        if not entity in self.entities:
            return
        
        tile = self.game.tilemap.Current_Tile(entity.tile)
        
        tile.Clear_Entity(entity.ID)
        self.entities.remove(entity)

            
        

    def Render(self, surf, offset = (0,0)):
        for entity in self.entities:
            if not entity.render:
                continue
            entity.Render(surf, offset)