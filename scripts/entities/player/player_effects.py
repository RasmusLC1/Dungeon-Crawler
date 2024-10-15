from scripts.entities.effects import Status_Effect_Handler


import random

class Player_Status_Effect_Handler(Status_Effect_Handler):
    def __init__(self, entity):
        super().__init__(entity)

        self.silence = 0 
        self.silence_max = 10 
        self.silence_cooldown = 0

        

        self.effects = {
            'fire': {'current': 0},
            'poisoned': {'current': 0},
            'freeze': {'current': 0},
            'wet': {'current': 0},
            'regen': {'current': 0},
            'speed': {'current': 0},
            'strength': {'current': 0},
            'invisibility': {'current': 0},
            'silence': {'current': 0},
            'fire_resistance': {'current': 0},
            'freeze_resistance': {'current': 0},
            'poison_resistance': {'current': 0}
        }

    def Save_Data(self):
        super().Save_Data()
        self.entity.saved_data['silence'] = self.silence
        self.entity.saved_data['effects'] = self.effects


    def Load_Data(self, data):
        super().Load_Data(data)
        self.silence = data['silence']
        self.effects = data['effects']

    def Set_Effect(self, effect, duration):
        if super().Set_Effect(effect, duration):
           return True

        if effect == 'silence':
            return self.Set_Silence(duration)
        else:
            return False

    def Update_Status_Effects(self):
        super().Update_Status_Effects()
        self.Silence()

    def Update_Effect_List(self, effect, value):
        if effect in self.effects:
            self.effects[effect]['current'] = value

    def Render_Effects_Symbols(self, surf):
        x_pos = 10
        y_pos = 30
        for effect_key, data in self.effects.items():
            if data['current']:
                self.entity.game.symbols.Render_Symbol(surf, effect_key, (x_pos, y_pos))
                self.entity.game.default_font.Render_Word(surf, str(data['current']), (x_pos + 10, y_pos))

                y_pos += 10

    # Set Strength effect, doesn't work when poisoned
    def Set_Silence(self, silence_time):

        if self.silence >= self.silence_max:
            return False
        self.silence = min(silence_time + self.silence, 10)
        return True
    
    def Silence(self):
        if not self.silence:
            return
    
        if self.silence_cooldown:
            self.silence_cooldown -= 1
        else:
            self.silence -= 1
            self.silence_cooldown = random.randint(40, 60)
            self.Update_Effect_List('silence', self.silence)

    def OnFire(self):
        if super().OnFire():
            self.Update_Effect_List('fire', self.fire)

    def Frozen(self):
        if super().Frozen():
            self.Update_Effect_List('freeze', self.frozen)

    def Poison(self):
        if super().Poison():
            self.Update_Effect_List('poison', self.poisoned)

    def Wet(self):
        if super().Wet():
            self.Update_Effect_List('wet', self.wet)

    def Speed(self):
        if super().Speed():
            self.Update_Effect_List('speed', self.speed)

    def Strength(self):
        if super().Strength():
            self.Update_Effect_List('strength', self.strength)

    def Invisibility(self):
        if super().Invisibility():
            self.Update_Effect_List('invisibility', self.invisibility)
    
    def Fire_Resistance(self):
        if super().Fire_Resistance():
            self.Update_Effect_List('fire_resistance', self.fire_resistance)
            self.Update_Effect_List('fire', self.fire)


    def Freeze_Resistance(self):
        if super().Freeze_Resistance():
            self.Update_Effect_List('freeze_resistance', self.freeze_resistance)
            self.Update_Effect_List('freeze', self.frozen)



    def Poison_Resistance(self):
        if super().Poison_Resistance():
            self.Update_Effect_List('poison_resistance', self.poison_resistance)
            self.Update_Effect_List('poison', self.poisoned)


    def Regen(self):
        if super().Regen():
            self.Update_Effect_List('regen', self.regen)
    



