from scripts.entities.items.loot.loot import Loot
import random

class Key(Loot):
    def __init__(self, game, type, pos):
        super().__init__(game, type, 'loot', pos, (20, 20), 1)

    def Update(self):
        if self.game.mouse.right_click:
            self.clicked = False

        return super().Update()


    def Activate(self):
        if not super().Activate():
            return
        self.clicked = True

    # The update function in the inventory
    def Update_In_Inventory(self):
        if not self.clicked:
            return
        nearby_decorations = self.game.decoration_handler.Find_Nearby_Decorations(self.game.player.pos, 3)

        # Filter for doors
        doors = [decoration for decoration in nearby_decorations if 'door' in decoration.type]

        for door in doors:
            if door.rect().colliderect(self.game.mouse.rect_pos()):
                door.Set_Highlight()
                if not self.game.mouse.left_click:
                    continue
                door.Open()
                self.Open_Door()

    # Effect of opening door on key
    def Open_Door(self):
        pass

    def Render_Active(self, surf, offset = (0,0)):
        if self.clicked:
            surf.blit(self.entity_image, (self.game.mouse.mpos[0] - offset[0] - 10, self.game.mouse.mpos[1] - offset[1] - 5))
            return