from scripts.entities.items.loot.potions.potion import Potion
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random


class Potion_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)
        self.potions = [
            'healing',
            'regen',
            'vampiric',
            'increase_souls',
            'speed',
            'increase_strength',
            'invisibility',
            'silence',
            'fire_resistance',
            'frozen_resistance',
            'poison_resistance',
            'arcane_hunger',
        ]

        self.strength = {
            'healing': 20,
            'regen': 4,
            'increase_souls': 20,
            'speed': 4,
            'increase_strength': 4,
            'invisibility': 3,
            'silence': 3,
            'fire_resistance': 6,
            'frozen_resistance': 6,
            'poison_resistance': 6,
            'vampiric': 5,
            'arcane_hunger': 5,
        }

        self.weights = {
            'healing': 0.1,
            'regen': 0.1,
            'increase_souls': 0.2,
            'speed': 0.2,
            'increase_strength': 0.2,
            'invisibility': 0.2,
            'silence': 0.2,
            'fire_resistance': 0.1,
            'frozen_resistance': 0.1,
            'poison_resistance': 0.1,
            'vampiric': 0.1,
            'arcane_hunger': 0.1,
        }



    def Update_Potion_Weights(self):
        weights = self.weights.copy()
        player = self.game.player
        
        weights = self.Adjust_By_Player_Health(weights, player)
        weights = self.Adjust_By_Souls(weights, player)

        return weights
    
    def Adjust_By_Souls(self, weights, player):
        max_amount = 300
        if player.souls > max_amount:
            return weights
        
        soul_increase =( max_amount - player.souls) / 400
        weights['increase_souls'] += soul_increase 
        weights['arcane_hunger'] += soul_increase

        return weights


    # Adjust the drop chance of healing potions if the players health is low
    def Adjust_By_Player_Health(self, weights, player):
        player_health_missing = player.max_health - player.health
        if player_health_missing < 30:
            return weights
        

        player_health_missing /= 400
        weights['healing'] += player_health_missing
        weights['regen'] += player_health_missing
        weights['vampiric'] += player_health_missing

        return weights
    

    def Loot_Spawner(self, pos):

        weights_dict = self.Update_Potion_Weights()
        
        # Extract weight values in the same order as potions list
        weight_values = [weights_dict[potion] for potion in self.potions]
        potion_type = random.choices(self.potions, weight_values, k=1)[0]
        amount = random.randint(1, 3)

        potion = Potion(self.game, potion_type, pos, amount, self.strength[potion_type])

        self.game.item_handler.Add_Item(potion)
        
        return potion


    def Spawn_Potions(self, name, pos_x, pos_y, amount, data=None):
        name = name.replace("_potion", "")
        # potion_class = self.potion_map.get(name)

        # If none matched, return False
        if name not in self.potions:
            return None

        # Instantiate the matched potion class
        potion = Potion(self.game, name, (pos_x, pos_y), amount, self.strength[name])

        # Load any saved data if present
        if data:
            potion.Load_Data(data)

        # Finally, add the potion to the game’s item handler
        self.game.item_handler.Add_Item(potion)
        return potion