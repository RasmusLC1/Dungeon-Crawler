import random

class Effect_Curse():

    def __init__(self):
        self.negative_effects = ['frozen',
                                 'fire',
                                 'poison', 
                                 'snare', 
                                'weakness'
                                 'electric', 
                                 ]

    def Set_Random_Negative_Effect(self):
        return random.choice(self.negative_effects)