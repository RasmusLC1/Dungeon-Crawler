from scripts.entities.items.loot.potions.potion import Potion
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random


class Potion_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)
        self.potions = [
            game.dictionary.healing,
            game.dictionary.regen,
            game.dictionary.vampiric,
            game.dictionary.increase_souls,
            game.dictionary.speed,
            game.dictionary.increase_strength,
            game.dictionary.invisibility,
            game.dictionary.silence,
            game.dictionary.fire_resistance,
            game.dictionary.frozen_resistance,
            game.dictionary.poison_resistance,
            game.dictionary.arcane_hunger,
        ]

        self.strength = {
            game.dictionary.healing: 20,
            game.dictionary.regen: 4,
            game.dictionary.increase_souls: 20,
            game.dictionary.speed: 4,
            game.dictionary.increase_strength: 4,
            game.dictionary.invisibility: 3,
            game.dictionary.silence: 3,
            game.dictionary.fire_resistance: 6,
            game.dictionary.frozen_resistance: 6,
            game.dictionary.poison_resistance: 6,
            game.dictionary.vampiric: 5,
            game.dictionary.arcane_hunger: 5,
        }

        self.weights = {
            game.dictionary.healing: 0.1,
            game.dictionary.regen: 0.1,
            game.dictionary.increase_souls: 0.2,
            game.dictionary.speed: 0.2,
            game.dictionary.increase_strength: 0.2,
            game.dictionary.invisibility: 0.2,
            game.dictionary.silence: 0.2,
            game.dictionary.fire_resistance: 0.1,
            game.dictionary.frozen_resistance: 0.1,
            game.dictionary.poison_resistance: 0.1,
            game.dictionary.vampiric: 0.1,
            game.dictionary.arcane_hunger: 0.1,
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
        weights[self.game.dictionary.increase_souls] += soul_increase 
        weights[self.game.dictionary.arcane_hunger] += soul_increase

        return weights


    # Adjust the drop chance of healing potions if the players health is low
    def Adjust_By_Player_Health(self, weights, player):
        player_health_missing = player.max_health - player.health
        if player_health_missing < 30:
            return weights
        

        player_health_missing /= 400
        weights[self.game.dictionary.healing] += player_health_missing
        weights[self.game.dictionary.regen] += player_health_missing
        weights[self.game.dictionary.vampiric] += player_health_missing

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
        name = name.replace("_", self.game.dictionary.potion, "")
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