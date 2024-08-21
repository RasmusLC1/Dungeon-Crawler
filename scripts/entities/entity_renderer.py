import math

class Entity_Renderer():
    def __init__(self, game):
        self.game = game
        self.entities = []
        self.nearby_entities = []
        self.nearby_entities_cooldown = 0

    def Update(self):

        if not self.nearby_entities_cooldown:
            self.Find_Nearby_Entities()
            self.nearby_entities_cooldown = 50
        else:
            self.nearby_entities_cooldown -= 1
        self.nearby_entities.sort(key=lambda entity: entity.pos[1])

    def Find_Nearby_Entities(self):
        self.nearby_entities.clear()
        for entity in self.entities:
            distance = math.sqrt((entity.pos[0] - self.game.player.pos[0]) ** 2 + (entity.pos[1] - self.game.player.pos[1]) ** 2)
            if distance < 300:
                self.nearby_entities.append(entity)

    def Add_Entity(self, entity):
        self.entities.append(entity)
        self.nearby_entities_cooldown = 0
    
    def Remove_Entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            self.nearby_entities_cooldown = 0

    def Render(self, surf, offset = (0,0)):
        for entity in self.nearby_entities:
            entity.Render(surf, offset)
