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
from scripts.entities.items.potions.potion import Potion

import random


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

        self.potions = [
            'healing',
            'regen',
            'vampiric',
            'soul',
            'speed',
            'strength',
            'invisibility',
            'silence',
            'fire_resistance',
            'frozen_resistance',
            'poison_resistance',
        ]

        self.potion_strength = {
            'healing': 20,
            'regen': 4,
            'soul': 20,
            'speed': 4,
            'strength': 4,
            'invisibility': 3,
            'silence': 3,
            'fire_resistance': 6,
            'frozen_resistance': 6,
            'poison_resistance': 6,
            'vampiric': 5,
            'arcane_hunger': 5,
        }

        self.weights = [
            0.1,
            0.1,
            0.1,
            0.2,
            0.2,
            0.2,
            0.1,
            0.2,
            0.1,
            0.1,
            0.1,
        ]

        self.update_weight_counter = False

    # TODO: Remove individual potions and consolidate into central potion

    def Update_Potion_Weights(self):
        weights = self.weights.copy()
        player = self.game.player
        
        weights = self.Adjust_By_Player_Health(weights, player)

        return weights
    
    def Adjust_By_Souls(self, weights, player):
        if player.souls > 200:
            return weights
        
        health_index = self.potions.index('healing')



    # Adjust the drop chance of healing potions if the players health is low
    def Adjust_By_Player_Health(self, weights, player):
        player_health_missing = player.max_health - player.health
        if player_health_missing < 30:
            return weights
        

        player_health_missing /= 200
        health_index = self.potions.index('healing')
        regen_index = self.potions.index('regen')
        vampiric_index = self.potions.index('vampiric')
        weights[health_index] += player_health_missing
        weights[regen_index] += player_health_missing
        weights[vampiric_index] += player_health_missing

        return weights
    

    def Spawn_Random_Potion(self, pos):

        weights = self.Update_Potion_Weights()
        potion_type = random.choices(self.potions, weights, k=1)[0]
        amount = random.randint(1, 3)

        potion_class = self.potion_map.get(potion_type)

        potion = potion_class(self.game, pos, amount)

        self.game.item_handler.Add_Item(potion)
        
        return potion





    def Spawn_Potions(self, name, pos_x, pos_y, amount, data=None):
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