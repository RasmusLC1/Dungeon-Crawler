from scripts.entities.moving_entities.effects.fire import Fire
from scripts.entities.moving_entities.effects.poison import Poison
from scripts.entities.moving_entities.effects.frozen import Frozen
from scripts.entities.moving_entities.effects.wet import Wet
from scripts.entities.moving_entities.effects.regen import Regen
from scripts.entities.moving_entities.effects.speed import Speed
from scripts.entities.moving_entities.effects.Increase_Strength import Increase_Strength
from scripts.entities.moving_entities.effects.invisibility import Invisibility
from scripts.entities.moving_entities.effects.fire_resistance import Fire_Resistance
from scripts.entities.moving_entities.effects.frozen_resistance import Frozen_Resistance
from scripts.entities.moving_entities.effects.poison_resistance import Poison_Resistance
from scripts.entities.moving_entities.effects.snare import Snare
from scripts.entities.moving_entities.effects.healing import Healing
from scripts.entities.moving_entities.effects.slow_down import Slow_Down
from scripts.entities.moving_entities.effects.vampiric import Vampiric
from scripts.entities.moving_entities.effects.invulnerable import Invulnerable
from scripts.entities.moving_entities.effects.thorns import Thorns
from scripts.entities.moving_entities.effects.eletric import Electric
from scripts.entities.moving_entities.effects.electric_resistance import Electric_Resistance


class Status_Effect_Handler:
    

    def __init__(self, entity):
        self.entity = entity

        self.fire = Fire(self.entity)

        self.poison = Poison(self.entity)
        
        self.frozen = Frozen(self.entity)

        self.wet = Wet(self.entity)

        self.regen = Regen(self.entity)
        
        self.speed = Speed(self.entity)

        self.increase_strength = Increase_Strength(self.entity)

        self.invisibility = Invisibility(self.entity)
        
        self.fire_resistance = Fire_Resistance(self.entity)

        self.poison_resistance = Poison_Resistance(self.entity)
        
        self.frozen_resistance = Frozen_Resistance(self.entity)

        self.snare = Snare(self.entity)

        self.healing = Healing(self.entity)
        
        self.slow_down = Slow_Down(self.entity)
        
        self.vampiric = Vampiric(self.entity)

        self.invulnerable = Invulnerable(self.entity)

        self.thorns = Thorns(self.entity)

        self.electric = Electric(self.entity)

        self.electric_resistance = Electric_Resistance(self.entity)

        self.effects = {
            self.fire.effect_type: self.fire,
            self.poison.effect_type: self.poison,
            self.frozen.effect_type: self.frozen,
            self.wet.effect_type: self.wet,
            self.regen.effect_type: self.regen,
            self.speed.effect_type: self.speed,
            self.increase_strength.effect_type: self.increase_strength,
            self.invisibility.effect_type: self.invisibility,
            self.fire_resistance.effect_type: self.fire_resistance,
            self.poison_resistance.effect_type: self.poison_resistance,
            self.frozen_resistance.effect_type: self.frozen_resistance,
            self.snare.effect_type: self.snare,
            self.healing.effect_type: self.healing,
            self.slow_down.effect_type: self.slow_down,
            self.vampiric.effect_type: self.vampiric,
            self.invulnerable.effect_type: self.invulnerable,
            self.thorns.effect_type: self.thorns,
            self.electric.effect_type: self.electric,
            self.electric_resistance.effect_type: self.electric_resistance,
        }

        self.active_effects = []
        
        self.is_on_ice = 0
        self.saved_data = {}



    def Save_Data(self):
        for effect in self.active_effects:
            self.saved_data[effect.effect_type] = effect.Save_Data()

        return self.saved_data


    def Load_Data(self, data):
        for ID, effect_data in data.items():
            if not effect_data:
                continue
            
            if not ID in self.effects:
                continue
            try:
                self.effects[ID].Load_Data(effect_data)
                self.active_effects.append(self.effects[ID])
            except Exception as e:
                print(f"Wrong loaded data{e}", effect_data, ID)

    def Set_Effect(self, effect, duration):
        if not effect:
            return False
        if self.entity.effects.invulnerable.effect:
            return False
        if effect == 'slash' or effect == 'blunt':
            return False
        try:
            effect = self.effects[effect]
            effect_set_success = effect.Set_Effect(duration)
            if effect_set_success:
                if effect not in self.active_effects:
                    self.active_effects.append(effect)
            return effect_set_success
        except Exception as e:
            print(f"Wrong effect input{e}", effect, duration)

    def Reset_Effects(self):
        for effect in self.active_effects:
            effect.Remove_Effect()
            self.active_effects.remove(effect)


    def Update_Status_Effects(self):
        for effect in self.active_effects:
            effect.Update_Effect()
            if not effect.effect and effect in self.active_effects:
                self.active_effects.remove(effect)
        

    def Remove_Effect(self, effect):
        
        try:
            remove_effect_succes = self.effects[effect].Remove_Effect()
            if remove_effect_succes:
                self.active_effects.remove(self.effects[effect])
            return remove_effect_succes 
        
        except Exception as e:
                print(f"Wrong effect input{e} EFFECT NAME", effect)


    def Render_Effects(self, surf, offset=(0, 0)):
        for effect in self.active_effects:
            effect.Render_Effect(surf, offset)