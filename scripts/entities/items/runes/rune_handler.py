from scripts.entities.items.runes.basic_runes.healing_rune import Healing_Rune
from scripts.entities.items.runes.basic_runes.invisibility_rune import Invisibility_Rune
from scripts.entities.items.runes.basic_runes.strength_rune import Strength_Rune
from scripts.entities.items.runes.basic_runes.silence_rune import Silence_Rune
from scripts.entities.items.runes.basic_runes.speed_rune import Speed_Rune
from scripts.entities.items.runes.basic_runes.vampiric_rune import Vampiric_Rune
from scripts.entities.items.runes.basic_runes.invulnerable_rune import Invulnerable_Rune

from scripts.entities.items.runes.random_runes.dash_rune import Dash_Rune
from scripts.entities.items.runes.random_runes.key_rune import Key_Rune

from scripts.entities.items.runes.fire_runes.fire_resistance_rune import Fire_Resistance_Rune
from scripts.entities.items.runes.fire_runes.fire_circle_rune import Fire_Circle_Rune
from scripts.entities.items.runes.fire_runes.fire_ball_rune import Fire_Ball_Rune
from scripts.entities.items.runes.fire_runes.fire_spray_rune import Fire_Spray_Rune

from scripts.entities.items.runes.freeze_runes.frozen_resistance_rune import Frozen_Resistance_Rune
from scripts.entities.items.runes.freeze_runes.freeze_circle_rune import Freeze_Circle_Rune
from scripts.entities.items.runes.freeze_runes.freeze_storm_rune import Freeze_Storm_Rune
from scripts.entities.items.runes.freeze_runes.freeze_spray_rune import Freeze_Spray_Rune
from scripts.entities.items.runes.freeze_runes.freeze_ball_rune import Freeze_Ball_Rune

from scripts.entities.items.runes.poison_runes.poison_resistance_rune import Poison_Resistance_Rune
from scripts.entities.items.runes.poison_runes.poison_ball_rune import Poison_Ball_Rune
from scripts.entities.items.runes.poison_runes.poison_cloud_rune import Poison_Cloud_Rune
from scripts.entities.items.runes.poison_runes.poison_plume_rune import Poison_Plume_Rune

from scripts.entities.items.runes.electric_runes.electric_ball_rune import Electric_Ball_Rune
from scripts.entities.items.runes.electric_runes.electric_spray_rune import Electric_Spray_Rune
from scripts.entities.items.runes.electric_runes.chain_lightning_rune import Chain_Lightning_Rune


from scripts.entities.items.runes.vampiric_runes.soul_reap_rune import Soul_Reap_Rune
from scripts.entities.items.runes.vampiric_runes.soul_pit_rune import Soul_Pit_Rune



from scripts.entities.items.runes.passive_runes.regen_rune import Regen_Rune


from scripts.entities.items.runes.constant_runes.light_rune import Light_Rune
from scripts.entities.items.runes.constant_runes.arcane_conduit_rune import Arcane_Conduit_Rune
from scripts.entities.items.runes.basic_runes.resistance_rune import Resistance_Rune
from scripts.entities.items.runes.constant_runes.shield_rune import Shield_Rune
from scripts.entities.items.runes.constant_runes.arcane_hunger_rune import Arcane_Hunger_Rune
from scripts.entities.items.runes.constant_runes.manget_rune import Magnet_Rune
from scripts.engine.assets.keys import keys

import math

class Rune_Handler():
    def __init__(self, game):
        self.game = game
        self.active_runes = []
        self.saved_data = {}
        self.runes = {}
    

    def Save_Rune_Data(self):
        for rune in self.runes.values():
            self.saved_data[rune.type] = rune.Save_Data()

        return self.saved_data
    
    
    def Load_Data(self, data):
        if not self.runes:
            self.Rune_Spawner()
            
        if not data:
            return None
        
        type = data.get("type")

        if not type:
            return None
        rune = self.runes.get(type)
        
        if not rune:
            return None
        
        rune.Load_Data(data)
        self.active_runes.append(rune)

        return rune

    
    def Update(self, offset = (0,0)):
        for rune in self.active_runes:
            rune.Update()
    
    def Initialise_Runes(self):
        self.Rune_Spawner()
        self.Add_Runes_To_Inventory_TEST()

    def Rune_Spawner(self):
        self.runes = {
        keys.dash_rune : Dash_Rune(self.game, (9999, 9999)),
        keys.key_rune : Key_Rune(self.game, (9999, 9999)),
        keys.regen_rune : Regen_Rune(self.game, (9999, 9999)),

        keys.healing_rune : Healing_Rune(self.game, (9999, 9999)),
        keys.invisibility_rune : Invisibility_Rune(self.game, (9999, 9999)),
        keys.invulnerable_rune: Invulnerable_Rune(self.game, (9999, 9999)),
        keys.resistance_rune : Resistance_Rune(self.game, (9999, 9999)),
        keys.silence_rune : Silence_Rune(self.game, (9999, 9999)),
        keys.speed_rune : Speed_Rune(self.game, (9999, 9999)),
        keys.increase_strength_rune : Strength_Rune(self.game, (9999, 9999)),
        keys.vampiric_rune : Vampiric_Rune(self.game, (9999, 9999)),

        keys.arcane_conduit_rune : Arcane_Conduit_Rune(self.game, (9999, 9999)),
        keys.arcane_hunger_rune : Arcane_Hunger_Rune(self.game, (9999, 9999)),
        keys.light_rune : Light_Rune(self.game, (9999, 9999)),
        keys.magnet_rune : Magnet_Rune(self.game, (9999, 9999)),
        keys.shield_rune : Shield_Rune(self.game, (9999, 9999)),

        keys.fire_resistance_rune : Fire_Resistance_Rune(self.game, (9999, 9999)),
        keys.fire_cirlce_rune : Fire_Circle_Rune(self.game, (9999, 9999)),
        keys.fire_ball_rune : Fire_Ball_Rune(self.game, (9999, 9999)),
        keys.fire_spray_rune : Fire_Spray_Rune(self.game, (9999, 9999)),
        
        keys.freeze_circle_rune : Freeze_Circle_Rune(self.game, (9999, 9999)),
        keys.freeze_storm_rune : Freeze_Storm_Rune(self.game, (9999, 9999)),
        keys.freeze_spray_rune : Freeze_Spray_Rune(self.game, (9999, 9999)),
        keys.freeze_ball_rune : Freeze_Ball_Rune(self.game, (9999, 9999)),
        keys.frozen_resistance_rune : Frozen_Resistance_Rune(self.game, (9999, 9999)),
        
        keys.poison_resistance_rune : Poison_Resistance_Rune(self.game, (9999, 9999)),
        keys.poison_ball_rune : Poison_Ball_Rune(self.game, (9999, 9999)),
        keys.poison_cloud_rune : Poison_Cloud_Rune(self.game, (9999, 9999)),
        keys.poison_plume_rune : Poison_Plume_Rune(self.game, (9999, 9999)),

        keys.electric_ball_rune : Electric_Ball_Rune(self.game, (9999, 9999)),
        keys.electric_spray_rune : Electric_Spray_Rune(self.game, (9999, 9999)),
        keys.chain_lightning_rune : Chain_Lightning_Rune(self.game, (9999, 9999)),

        keys.soul_reap_rune : Soul_Reap_Rune(self.game, (9999, 9999)),
        keys.soul_pit_rune : Soul_Pit_Rune(self.game, (9999, 9999)),

        }


    def Add_Runes_To_Inventory_TEST(self):
        self.Add_Rune_To_Rune_Inventory(keys.key_rune)
        self.Add_Rune_To_Rune_Inventory(keys.freeze_spray_rune )
        self.Add_Rune_To_Rune_Inventory(keys.dash_rune)

    def Clear_Runes(self):
        self.runes.clear()
        self.active_runes.clear()
        self.saved_data.clear()
    
    def Replace_Rune_In_Inventory(self, old_rune, new_rune):
        self.game.inventory.Replace_Rune(old_rune, new_rune)
        new_rune.active = True
        self.active_runes.append(new_rune)

        self.game.item_handler.Add_Item(new_rune)

        old_rune.active = False
        self.active_runes.remove(old_rune)
        self.game.item_handler.Remove_Item(old_rune)




    # Add runes to Active Inventory
    def Add_Rune_To_Rune_Inventory(self, rune_type):
        rune = self.runes[rune_type]
        rune.active = True
        self.active_runes.append(rune)
        self.game.inventory.Add_Rune(rune)

        self.game.item_handler.Add_Item(rune)
        return

    # Only one of each rune, so easy filter by rune_type return when found
    def Remove_Rune_From_Inventory(self, rune_type):
        rune = self.runes[rune_type]
        
        rune.active = False
        self.active_runes.remove(rune)
        self.game.inventory.Update_Runes()
        self.game.item_handler.Remove_Item(rune)

        return True
    
    def Get_Rune(self, type):
        return self.runes[type]
    
    def Find_Nearby_Runes(self, entity_pos, max_distance):
        entity_pos = (entity_pos[0] - self.game.render_scroll[0], entity_pos[1] - self.game.render_scroll[1])
        nearby_runes = []
        for rune in self.active_runes:
            # Calculate the Euclidean distance
            distance = math.sqrt((entity_pos[0] - rune.pos[0]) ** 2 + (entity_pos[1] - rune.pos[1]) ** 2)
            if distance < max_distance:
                nearby_runes.append(rune)

        return nearby_runes


    def Render_Animation(self, surf, offset = (0, 0)):
        for rune in self.active_runes:
            rune.Render_Animation(surf, offset)


