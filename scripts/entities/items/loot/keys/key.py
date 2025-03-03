from scripts.entities.items.loot.loot import Loot
import random

class Key(Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'key', 'loot', pos, (20, 20), 1)
        self.clicked = False


    def Unlock_Door(self):
        pass

    def Activate(self):
        if not super().Activate():
            return
        
        self.clicked = True


    def Update_In_Inventory(self):
        if not self.clicked:
            return
        nearby_decorations = self.game.decoration_handler.Find_Nearby_Decorations(self.game.player.pos, 3)

        # Filter for doors
        doors = [decoration for decoration in nearby_decorations if decoration.type == 'door']

        for door in doors:
            if door.rect().colliderect(self.game.mouse.rect_pos()):
                door.Set_Highlight()