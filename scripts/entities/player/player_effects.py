from scripts.entities.effects.effects_handler import Status_Effect_Handler
from scripts.entities.effects.silence import Silence
from scripts.entities.effects.arcane_conduit import Arcane_Conduit



import random

class Player_Status_Effect_Handler(Status_Effect_Handler):
    def __init__(self, entity):
        super().__init__(entity)
        self.silence =  Silence(entity)
        self.arcane_conduit = Arcane_Conduit(entity)

        self.effects[self.silence.effect_type] = self.silence
        self.effects[self.arcane_conduit.effect_type] = self.arcane_conduit



    def Render_Effects_Symbols(self, surf):
        x_pos = 20
        y_pos = 60
        for effect in self.effects.values():
            if not effect.effect:
                continue
            self.entity.game.symbols.Render_Symbol(surf, effect.effect_type, (x_pos, y_pos))
            self.entity.game.default_font.Render_Word(surf, str(effect.effect), (x_pos + 20, y_pos))

            y_pos += 20