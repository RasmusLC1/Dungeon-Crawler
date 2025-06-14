from scripts.entities.items.runes.rune import Rune
from scripts.engine.assets.keys import keys


# TODO: FINISH th erune
class Fire_Circle_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, keys.fire_cirlce_rune, pos, 10, 10)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.clicked = False


    def Activate(self):
        if not super().Activate():
            return    
        self.clicked = True
    
    def Update(self):
        super().Update()
        if not self.clicked:
            return
        if self.game.mouse.left_click:
            if not self.game.player.movement_handler.Dash(self.game.render_scroll):
                return
            self.game.player.Decrease_Souls(self.current_soul_cost)
            self.clicked = False
        
        if self.game.mouse.right_click:
            self.clicked = False

    
    def Render_Animation(self, surf, offset=(0, 0)):
        pass