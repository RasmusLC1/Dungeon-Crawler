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

class Potion_Handler:
    def __init__(self, game):
        self.game = game
        # Map part of the name (key) to the corresponding potion class (value)
        self.potion_map = {
            'healing': Healing_Potion,
            'regen': Regen_Potion,
            'soul': Soul_Potion,
            'speed': Speed_Potion,
            'strength': Strength_Potion,
            'invisibility': Invisibility_Potion,
            'silence': Silence_Potion,
            'fire_resistance': Fire_Resistance_Potion,
            'frozen_resistance': Frozen_Resistance_Potion,
            'poison_resistance': Poison_Resistance_Potion,
            'vampiric': Vampiric_Potion,
        }

    def Spawn_Potions(self, name, pos_x, pos_y, amount, data=None) -> bool:
        name = name.replace("_potion", "")
        potion_class = self.potion_map.get(name)

        # If none matched, return False
        if not potion_class:
            return None

        # Instantiate the matched potion class
        potion = potion_class(self.game, (pos_x, pos_y), amount)

        # Load any saved data if present
        if data:
            potion.Load_Data(data)

        # Finally, add the potion to the game’s item handler
        self.game.item_handler.Add_Item(potion)
        return potion