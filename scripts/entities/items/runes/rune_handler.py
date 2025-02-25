from scripts.entities.items.runes.basic_runes.healing_rune import Healing_Rune
from scripts.entities.items.runes.basic_runes.invisibility_rune import Inivisibility_Rune
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
from scripts.entities.items.runes.constant_runes.hunger_rune import Hunger_Rune
from scripts.entities.items.runes.constant_runes.manget_rune import Magnet_Rune

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

        for ID, rune_data in data.items():
            if not rune_data:
                continue
            
            if not ID in self.runes:
                continue
            try:
                rune = self.runes[ID]
                rune.Load_Data(rune_data)
                self.game.item_handler.Add_Item(rune)

                if not rune.active:
                    continue

                for active_rune in self.active_runes:
                    if rune.type == active_rune.type:
                        return
                self.active_runes.append(rune)

            except Exception as e:
                print(f"Wrong loaded data{e}", rune_data, ID)

    
    def Update(self, offset = (0,0)):
        for rune in self.active_runes:
            rune.Update()
    
    def Initialise_Runes(self):
        self.Rune_Spawner()
        self.Add_Runes_To_Inventory_TEST()

    def Rune_Spawner(self):
        self.runes = {
        'healing_run': Healing_Rune(self.game, (9999, 9999)),
        'dash_rune': Dash_Rune(self.game, (9999, 9999)),
        'fire_resistance_run': Fire_Resistance_Rune(self.game, (9999, 9999)),
        'frozen_resistance_rune': Frozen_Resistance_Rune(self.game, (9999, 9999)),
        'key_rune': Key_Rune(self.game, (9999, 9999)),
        'regen_rune': Regen_Rune(self.game, (9999, 9999)),
        'light_rune': Light_Rune(self.game, (9999, 9999)),
        'invisibility_rune': Inivisibility_Rune(self.game, (9999, 9999)),
        'increase_strength_rune': Strength_Rune(self.game, (9999, 9999)),
        'silence_rune': Silence_Rune(self.game, (9999, 9999)),
        'speed_rune': Speed_Rune(self.game, (9999, 9999)),
        'vampiric_rune': Vampiric_Rune(self.game, (9999, 9999)),
        'arcane_conduit_run': Arcane_Conduit_Rune(self.game, (9999, 9999)),
        'resistance_rune': Resistance_Rune(self.game, (9999, 9999)),
        'shield_rune': Shield_Rune(self.game, (9999, 9999)),
        'hunger_rune': Hunger_Rune(self.game, (9999, 9999)),
        'magnet_rune': Magnet_Rune(self.game, (9999, 9999)),
        'invulnerable_rune': Invulnerable_Rune(self.game, (9999, 9999)),
        
        'fire_circle_rune': Fire_Circle_Rune(self.game, (9999, 9999)),
        'fire_ball_rune': Fire_Ball_Rune(self.game, (9999, 9999)),
        'fire_spray_rune': Fire_Spray_Rune(self.game, (9999, 9999)),
        
        'freeze_circle_rune': Freeze_Circle_Rune(self.game, (9999, 9999)),
        'freeze_storm_rune': Freeze_Storm_Rune(self.game, (9999, 9999)),
        'freeze_spray_rune': Freeze_Spray_Rune(self.game, (9999, 9999)),
        'freeze_ball_rune': Freeze_Ball_Rune(self.game, (9999, 9999)),
        
        'poison_resistance_rune': Poison_Resistance_Rune(self.game, (9999, 9999)),
        'poison_ball_rune': Poison_Ball_Rune(self.game, (9999, 9999)),
        'poison_cloud_rune': Poison_Cloud_Rune(self.game, (9999, 9999)),
        'poison_plume_rune': Poison_Plume_Rune(self.game, (9999, 9999)),


        'electric_ball_rune': Electric_Ball_Rune(self.game, (9999, 9999)),
        'electric_spray_rune': Electric_Spray_Rune(self.game, (9999, 9999)),
        'chain_lightning_rune': Chain_Lightning_Rune(self.game, (9999, 9999)),

        'soul_reap_rune': Soul_Reap_Rune(self.game, (9999, 9999)),
        'soul_pit_rune': Soul_Pit_Rune(self.game, (9999, 9999)),

        }


    def Add_Runes_To_Inventory_TEST(self):
        self.Add_Rune_To_Rune_Inventory('key_rune')
        self.Add_Rune_To_Rune_Inventory('dash_rune')
        self.Add_Rune_To_Rune_Inventory('electric_spray_rune')

    def Clear_Runes(self):
        self.runes.clear()
        self.active_runes.clear()
        self.saved_data.clear()
    
        
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
        self.game.inventory.Remove_Item(rune, True)
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


