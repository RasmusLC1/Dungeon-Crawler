from scripts.items.potions.health_potion import Health_Potion
from scripts.items.potions.soul_potion import Soul_Potion
from scripts.items.potions.regen_potion import Regen_Potion
from scripts.items.potions.speed_potion import Speed_Potion
from scripts.items.potions.strength_potion import Strength_Potion
from scripts.items.potions.invisibility_potion import Invisibility_Potion
from scripts.items.potions.silence_potion import Silence_Potion
from scripts.items.potions.fire_resistance_potion import Fire_Resistance_Potion
from scripts.items.potions.freeze_resistance import Freeze_Resistance_Potion
from scripts.items.potions.poison_resistance import Poison_Resistance_Potion


class Potion_Handler():
    def __init__(self, game):
        self.game = game    

    def Spawn_Potions(self, pos_x, pos_y, amount, name) -> bool:
        if 'health' in name:
            self.Spawn_Health_Potion(pos_x, pos_y, amount)
            return True

        elif 'regen' in name:
            self.Spawn_Regen_Potion(pos_x, pos_y, amount)
            return True

        elif 'soul' in name:
            self.Spawn_Soul_Potion(pos_x, pos_y, amount)
            return True

        elif 'speed' in name:
            self.Spawn_Speed_Potion(pos_x, pos_y, amount)
            return True

        elif 'strength' in name:
            self.Spawn_Strength_Potion(pos_x, pos_y, amount)
            return True

        elif 'invisibility' in name:
            self.Spawn_Invisibility_Potion(pos_x, pos_y, amount)
            return True

        elif 'silence' in name:
            self.Spawn_Silence_Potion(pos_x, pos_y, amount)
            return True

        elif 'fire_resistance' in name:
            self.Spawn_Fire_Resistance_Potion(pos_x, pos_y, amount)
            return True

        elif 'freeze_resistance' in name:
            self.Spawn_Freeze_Resistance_Potion(pos_x, pos_y, amount)
            return True

        elif 'poison_resistance' in name:
            self.Spawn_Poison_Resistance_Potion(pos_x, pos_y, amount)
            return True

        return False

    def Spawn_Health_Potion(self, pos_x, pos_y, amount):
        item = Health_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)
    
    def Spawn_Regen_Potion(self, pos_x, pos_y, amount):
        item = Regen_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)
    
    def Spawn_Soul_Potion(self, pos_x, pos_y, amount):
        item = Soul_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)
    
    def Spawn_Speed_Potion(self, pos_x, pos_y, amount):
        item = Speed_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)
    
    def Spawn_Strength_Potion(self, pos_x, pos_y, amount):
        item = Strength_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)
    
    def Spawn_Invisibility_Potion(self, pos_x, pos_y, amount):
        item = Invisibility_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)

    def Spawn_Silence_Potion(self, pos_x, pos_y, amount):
        item = Silence_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)

    def Spawn_Fire_Resistance_Potion(self, pos_x, pos_y, amount):
        item = Fire_Resistance_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)

    def Spawn_Freeze_Resistance_Potion(self, pos_x, pos_y, amount):
        item = Freeze_Resistance_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)

    def Spawn_Poison_Resistance_Potion(self, pos_x, pos_y, amount):
        item = Poison_Resistance_Potion(self.game, (pos_x, pos_y), amount)
        self.game.item_handler.Add_Item(item)