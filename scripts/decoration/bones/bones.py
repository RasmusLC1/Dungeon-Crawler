from scripts.decoration.decoration import Decoration
import pygame

class Bones(Decoration):
    def __init__(self, game, pos, entity_type) -> None:
        super().__init__(game, "bones", pos, (32, 32))
        self.entity_type = entity_type

    def Revive(self):
        self.game.enemy_handler.Enemy_Spawner(self.entity_type, self.pos)
        self.game.decoration_handler.Remove_Decoration(self)

    

