from scripts.entities.decoration.decoration import Decoration
import pygame

class Bones(Decoration):
    def __init__(self, game, pos, entity_type) -> None:
        super().__init__(game, "bones", pos, (32, 32))
        self.entity_type = entity_type
        self.activated = False

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['entity_type'] = self.entity_type


    def Load_Data(self, data):
        super().Load_Data(data)
        self.entity_type = data['entity_type']

    def Revive(self):
        if self.activated:
            return
        self.activated = True
        self.game.enemy_handler.Enemy_Spawner(self.entity_type, self.pos)
        self.game.decoration_handler.Remove_Decoration(self)

    

