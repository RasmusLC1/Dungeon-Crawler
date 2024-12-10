from scripts.items.potions.potion import Potion



class Invisibility_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'invisibility_potion', pos, amount, 5)
        self.max_amount = 3
        self.max_animation = 0
        self.sub_type = 'empty_bottle'


    def Update_Sub_Type():
        pass

