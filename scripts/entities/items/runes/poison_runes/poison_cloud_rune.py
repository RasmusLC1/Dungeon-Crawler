from scripts.entities.items.runes.rune import Rune
from scripts.entities.items.weapons.magic_attacks.poison.poison_cloud import Poison_Cloud

class Poison_Cloud_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, game.dictionary.poison_cloud_rune, pos, 10, 30)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.clicked = False
        self.poison_cloud = None

    def Save_Data(self):
        super().Save_Data()
        if self.poison_cloud:
            self.saved_data['delete_countdown'] = self.poison_cloud.delete_countdown
        else:
            self.saved_data['delete_countdown'] = 0
        return self.saved_data
    
    def Load_Data(self, data):
        super().Load_Data(data)
        if data['delete_countdown']:
            self.Trigger_Effect()
            self.poison_cloud.Set_Delete_Countdown(data['delete_countdown'])



    def Update(self):
        super().Update()
        if not self.poison_cloud:
            return
        if self.poison_cloud.delete_countdown:
            self.poison_cloud.Update()
            self.poison_cloud.delete_countdown -= 1
            if self.poison_cloud.delete_countdown <= 0:
                self.game.entities_render.Remove_Entity(self.poison_cloud)

                del(self.poison_cloud)
                self.poison_cloud = None

    def Trigger_Effect(self):
        self.Trigger_Rune()
        if self.poison_cloud:
            self.poison_cloud.Set_Duration(self.current_power * 10)
        else:
            self.poison_cloud = Poison_Cloud(self.game, self.game.player.pos, self.current_power, self.game.player)
            self.game.entities_render.Add_Entity(self.poison_cloud)

    def Render_Animation(self, surf, offset=(0, 0)):
        pass
            
