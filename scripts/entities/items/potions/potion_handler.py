from scripts.entities.items.potions.potion import Potion

import random


class Potion_Handler:
    def __init__(self, game):
        self.game = game
        # Map part of the name (key) to the corresponding potion class (value)


        self.potions = [
            'healing',
            'regen',
            'vampiric',
            'increase_souls',
            'speed',
            'strength',
            'invisibility',
            'silence',
            'fire_resistance',
            'frozen_resistance',
            'poison_resistance',
            'arcane_hunger',
        ]

        self.potion_strength = {
            'healing': 20,
            'regen': 4,
            'increase_souls': 20,
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

        self.weights = {
            'healing': 0.1,
            'regen': 0.1,
            'increase_souls': 0.2,
            'speed': 0.2,
            'strength': 0.2,
            'invisibility': 0.2,
            'silence': 0.2,
            'fire_resistance': 0.1,
            'frozen_resistance': 0.1,
            'poison_resistance': 0.1,
            'vampiric': 0.1,
            'arcane_hunger': 0.1,
        }

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
        weights['healing'] += player_health_missing
        weights['regen'] += player_health_missing
        weights['vampiric'] += player_health_missing

        return weights
    

    def Spawn_Random_Potion(self, pos):

        weights_dict = self.Update_Potion_Weights()
        
        # Extract weight values in the same order as potions list
        weight_values = [weights_dict[potion] for potion in self.potions]
        potion_type = random.choices(self.potions, weight_values, k=1)[0]
        amount = random.randint(1, 3)

        potion = Potion(self.game, potion_type, pos, amount, self.potion_strength[potion_type])

        self.game.item_handler.Add_Item(potion)
        
        return potion





    def Spawn_Potions(self, name, pos_x, pos_y, amount, data=None):
        name = name.replace("_potion", "")
        # potion_class = self.potion_map.get(name)

        # If none matched, return False
        if name not in self.potions:
            return None

        # Instantiate the matched potion class
        potion = Potion(self.game, name, (pos_x, pos_y), amount, self.potion_strength[name])

        # Load any saved data if present
        if data:
            potion.Load_Data(data)

        # Finally, add the potion to the game’s item handler
        self.game.item_handler.Add_Item(potion)
        return potion