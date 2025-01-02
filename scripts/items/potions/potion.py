from scripts.items.item import Item
from scripts.entities.textbox.potion_textbox import Potion_Textbox


class Potion(Item):
    def __init__(self, game, type, pos, amount, strength):
        super().__init__(game, type, 'potion', pos, (20, 20), amount)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4
        self.strength = strength
        self.effect = self.type.replace('_potion', '')
        self.text_box = Potion_Textbox(self)
        self.Update_Sub_Type()

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['effect'] = self.effect
        self.saved_data['strength'] = self.strength

    def Update(self):
        super().Update()
    
    def Update_Sub_Type(self):
        if self.amount == 1:
            self.sub_type = self.effect + '_low'
        elif self.amount == 2:
            self.sub_type = self.effect + '_half'
        elif self.amount == 3:
            self.sub_type = self.effect + '_full'

    
    def Load_Data(self, data):
        super().Load_Data(data)
        self.effect = data['effect']
        self.strength = data['strength']

    def Activate(self):
        if not super().Activate():
            return
        if self.game.player.Set_Effect(self.effect, self.strength):
            self.Decrease_Amount(1)
            self.Update_Sub_Type()
        if self.amount <= 0:
            self.used = True
