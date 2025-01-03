from scripts.entities.items.potions.healing_potion import Healing_Potion
from scripts.entities.items.potions.soul_potion import Soul_Potion
from scripts.entities.items.potions.regen_potion import Regen_Potion
from scripts.entities.items.potions.speed_potion import Speed_Potion
from scripts.entities.items.potions.strength_potion import Strength_Potion
from scripts.entities.items.potions.invisibility_potion import Invisibility_Potion
from scripts.entities.items.potions.silence_potion import Silence_Potion
from scripts.entities.items.potions.fire_resistance_potion import Fire_Resistance_Potion
from scripts.entities.items.potions.frozen_resistance import Frozen_Resistance_Potion
from scripts.entities.items.potions.poison_resistance import Poison_Resistance_Potion
from scripts.entities.items.potions.vampiric_potion import Vampiric_Potion


class Potion_Handler():
    def __init__(self, game):
        self.game = game    

    def Spawn_Potions(self, name, pos_x, pos_y, amount, data = None) -> bool:
        potion = None
        if 'healing' in name:
            potion = self.Spawn_Healing_Potion(pos_x, pos_y, amount)

        elif 'regen' in name:
            potion = self.Spawn_Regen_Potion(pos_x, pos_y, amount)

        elif 'soul' in name:
            potion = self.Spawn_Soul_Potion(pos_x, pos_y, amount)

        elif 'speed' in name:
            potion = self.Spawn_Speed_Potion(pos_x, pos_y, amount)

        elif 'strength' in name:
            potion = self.Spawn_Strength_Potion(pos_x, pos_y, amount)

        elif 'invisibility' in name:
            potion = self.Spawn_Invisibility_Potion(pos_x, pos_y, amount)

        elif 'silence' in name:
            potion = self.Spawn_Silence_Potion(pos_x, pos_y, amount)

        elif 'fire_resistance' in name:
            potion = self.Spawn_Fire_Resistance_Potion(pos_x, pos_y, amount)

        elif 'frozen_resistance' in name:
            potion = self.Spawn_Frozen_Resistance_Potion(pos_x, pos_y, amount)

        elif 'poison_resistance' in name:
            potion = self.Spawn_Poison_Resistance_Potion(pos_x, pos_y, amount)

        elif 'vampiric' in name:
            potion = self.Spawn_Vampiric_Potion(pos_x, pos_y, amount)


        if not potion:
            return False
        
        if data:
            potion.Load_Data(data)

        self.game.item_handler.Add_Item(potion)
        return True


    def Spawn_Healing_Potion(self, pos_x, pos_y, amount):
        return Healing_Potion(self.game, (pos_x, pos_y), amount)
    
    def Spawn_Regen_Potion(self, pos_x, pos_y, amount):
        print((pos_x, pos_y), amount)
        return Regen_Potion(self.game, (pos_x, pos_y), amount)
    
    def Spawn_Soul_Potion(self, pos_x, pos_y, amount):
        return Soul_Potion(self.game, (pos_x, pos_y), amount)
        
    def Spawn_Speed_Potion(self, pos_x, pos_y, amount):
        return Speed_Potion(self.game, (pos_x, pos_y), amount)
        
    def Spawn_Strength_Potion(self, pos_x, pos_y, amount):
        return Strength_Potion(self.game, (pos_x, pos_y), amount)
        
    def Spawn_Invisibility_Potion(self, pos_x, pos_y, amount):
        return Invisibility_Potion(self.game, (pos_x, pos_y), amount)

    def Spawn_Silence_Potion(self, pos_x, pos_y, amount):
        return Silence_Potion(self.game, (pos_x, pos_y), amount)
    
    def Spawn_Fire_Resistance_Potion(self, pos_x, pos_y, amount):
        return Fire_Resistance_Potion(self.game, (pos_x, pos_y), amount)
    
    def Spawn_Frozen_Resistance_Potion(self, pos_x, pos_y, amount):
        return Frozen_Resistance_Potion(self.game, (pos_x, pos_y), amount)
    
    def Spawn_Poison_Resistance_Potion(self, pos_x, pos_y, amount):
        return Poison_Resistance_Potion(self.game, (pos_x, pos_y), amount)
    
    def Spawn_Vampiric_Potion(self, pos_x, pos_y, amount):
        return Vampiric_Potion(self.game, (pos_x, pos_y), amount)