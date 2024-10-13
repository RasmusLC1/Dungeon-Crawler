from scripts.items.item import Item
class Rune(Item):
    def __init__(self, game, type, pos, strength, soul_cost):
        super().__init__(game,  type, 'rune', pos, (16, 16), 1)
        self.max_amount = 1
        self.original_strength = strength
        self.current_strength = strength
        self.original_soul_cost = soul_cost
        self.current_soul_cost = soul_cost
        self.animation_time_max = 1
        self.animation_time = 0
        self.animation_size = 0
        self.animation_size_max = 0
        self.active = False
        self.effect = ''

    def Update(self):
        pass

    
    def Activate(self):
        if self.game.player.souls < self.current_soul_cost:
            return
        if self.game.player.Set_Effect(self.effect, self.current_strength):
            self.game.player.Decrease_Souls(self.current_soul_cost)
            self.Set_Animation_Time()
            self.Reset_Animation_Size()


    def Increase_cost(self, change):
        self.current_soul_cost += change

    def Decrease_cost(self, change):
        self.current_soul_cost -= change

    def Increase_srength(self, change):
        self.current_strength += change

    def Decrease_strength(self, change):
        self.current_strength -= change

    def Set_Animation_Time(self):
        self.animation_time = self.animation_time_max

    def Reset_Animation_Size(self):
        self.animation_size = 0

    def Increase_Animation_Size(self):
        self.animation_size = min(self.animation_size + 1, self.animation_size_max)


    def Update_Animation(self):

        if self.animation_time:
            self.animation_time = max(0, self.animation_time - 1)
            self.Increase_Animation_Size()
            

    
    def Render_Animation(self, surf, offset=(0, 0)):
        pass