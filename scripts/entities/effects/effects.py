from scripts.entities.effects.fire import Fire
from scripts.entities.effects.poison import Poison
from scripts.entities.effects.frozen import Frozen
from scripts.entities.effects.wet import Wet
from scripts.entities.effects.regen import Regen
from scripts.entities.effects.speed import Speed
from scripts.entities.effects.strength import Strength
from scripts.entities.effects.invisibility import Invisibility
from scripts.entities.effects.fire_resistance import Fire_Resistance
from scripts.entities.effects.frozen_resistance import Frozen_Resistance
from scripts.entities.effects.poison_resistance import Poison_Resistance
from scripts.entities.effects.snare import Snare
from scripts.entities.effects.health import Health
from scripts.entities.effects.slow_down import Slow_Down

class Status_Effect_Handler:
    def __init__(self, entity):
        self.entity = entity

        self.fire = Fire(self.entity)

        self.poison = Poison(self.entity)
        
        self.frozen = Frozen(self.entity)

        self.wet = Wet(self.entity)

        self.regen = Regen(self.entity)
        
        self.speed = Speed(self.entity)

        self.strength = Strength(self.entity)

        self.invisibility = Invisibility(self.entity)
        
        self.fire_resistance = Fire_Resistance(self.entity)

        self.poison_resistance = Poison_Resistance(self.entity)
        
        self.Frozen_Resistance = Frozen_Resistance(self.entity)

        self.snare = Snare(self.entity)

        self.health = Health(self.entity)
        
        self.slow_down = Slow_Down(self.entity)

        self.effects = {
            "fire": self.fire,
            "poison": self.poison,
            "frozen": self.frozen,
            "wet": self.wet,
            "regen": self.regen,
            "speed": self.speed,
            "strength": self.strength,
            "invisibility": self.invisibility,
            "fire_resistance": self.fire_resistance,
            "poison_resistance": self.poison_resistance,
            "frozen_resistance": self.Frozen_Resistance,
            "snare": self.snare,
            "health": self.health,
            "slow_down": self.slow_down,
        }
        
        self.is_on_ice = 0
        self.saved_data = {}



    def Save_Data(self):
        for effect in self.effects.values():
            effect.Save_Data()
            self.saved_data[effect.effect_type] = effect.saved_data


    def Load_Data(self, data):
        for ID, effect_data in data.items():
            if not effect_data:
                continue
        print(ID, effect_data)
        self.effects[ID].Load_Data(effect_data)

    def Set_Effect(self, effect, duration):
        if self.entity.invincible:
            return False
        
        try:
            return self.effects[effect].Set_Effect(duration)
        except Exception as e:
            print(f"Wrong effect input{e}", effect, duration)

        
    def Update_Status_Effects(self):
        for effect in self.effects.values():
            effect.Update_Effect()
        

    def Remove_Effect(self, effect):
        try:
            return self.effects[effect].Remove_Effect()
        except Exception as e:
                print(f"Wrong effect input{e}", effect)


    def Render_Effects(self, surf, offset=(0, 0)):
        for effect in self.effects.values():
            effect.Render_Effect(surf, offset)