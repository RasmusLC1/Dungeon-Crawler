from scripts.entities.items.loot.loot import Loot
import math

class Bomb(Loot):
    def __init__(self, game, type, pos):
        super().__init__(game, type, 'loot', pos, (20, 20), 1)
        self.distance_to_player = 0
        self.max_distance = 128

    def Update(self):
        if self.game.mouse.right_click:
            self.clicked = False

        return super().Update()

    def Calculate_Distance_To_Player(self):
        player_pos = self.game.player.pos
        mpos = self.game.mouse.mpos
        self.distance_to_player = math.sqrt((player_pos[0] - mpos[0]) ** 2 + (player_pos[1] - mpos[1]) ** 2)

    def Activate(self):
        if not super().Activate():
            return
        self.clicked = True

    # The update function in the inventory
    def Update_In_Inventory(self):
        if not self.clicked:
            return False
        
        # Set range limit for the key
        self.Calculate_Distance_To_Player()
        if self.distance_to_player > self.max_distance:
            return False
        
        


    def Render_Active(self, surf, offset = (0,0)):
        if not self.clicked:
            return
        rendered_image = self.entity_image.copy()
        # Fade the key out if distance is to great
        if self.distance_to_player > self.max_distance:
            rendered_image.set_alpha(100)
        mpos = self.game.mouse.mpos
        surf.blit(rendered_image, (mpos[0] - offset[0] - 10, mpos[1] - offset[1] - 5))
        return