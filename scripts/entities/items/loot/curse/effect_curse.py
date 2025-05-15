import random
from scripts.engine.assets.keys import keys

class Effect_Curse():

    def __init__(self):
        self.negative_effects = [keys.frozen,
                                 keys.fire,
                                 keys.poison, 
                                 'snare', 
                                'weakness',
                                 keys.electric, 
                                 ]

    def Set_Random_Negative_Effect(self):
        return random.choice(self.negative_effects)