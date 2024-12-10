from scripts.entities.effects.effects_handler import Status_Effect_Handler
from scripts.entities.effects.silence import Silence
from scripts.entities.effects.arcane_conduit import Arcane_Conduit
from scripts.entities.effects.hunger import Hunger
from scripts.entities.effects.magnet import Magnet
from scripts.entities.effects.resistance import Resistance


class Player_Status_Effect_Handler(Status_Effect_Handler):
    def __init__(self, entity):
        super().__init__(entity)
        self.silence =  Silence(entity)
        self.arcane_conduit = Arcane_Conduit(entity)
        self.hunger = Hunger(entity)
        self.magnet = Magnet(entity)
        self.resistance = Resistance(entity)

        self.effects[self.silence.effect_type] = self.silence
        self.effects[self.arcane_conduit.effect_type] = self.arcane_conduit
        self.effects[self.hunger.effect_type] = self.hunger
        self.effects[self.magnet.effect_type] = self.magnet
        self.effects[self.resistance.effect_type] = self.resistance



    def Render_Effects_Symbols(self, surf):
        x_pos = 20
        y_pos = 60
        for effect in self.effects.values():
            if not effect.effect:
                continue
            self.entity.game.symbols.Render_Symbol(surf, effect.effect_type, (x_pos, y_pos))
            self.entity.game.default_font.Render_Word(surf, str(effect.effect), (x_pos + 20, y_pos))

            y_pos += 20