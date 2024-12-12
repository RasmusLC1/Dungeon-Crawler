from scripts.items.runes.basic_runes.healing_rune import Healing_Rune
from scripts.items.runes.basic_runes.invisibility_rune import Inivisibility_Rune
from scripts.items.runes.basic_runes.strength_rune import Strength_Rune
from scripts.items.runes.basic_runes.silence_rune import Silence_Rune
from scripts.items.runes.basic_runes.speed_rune import Speed_Rune
from scripts.items.runes.basic_runes.vampiric_rune import Vampiric_Rune
from scripts.items.runes.basic_runes.invulnerable_rune import Invulnerable_Rune

from scripts.items.runes.random_runes.dash_rune import Dash_Rune
from scripts.items.runes.random_runes.key_rune import Key_Rune

from scripts.items.runes.fire_runes.fire_resistance_rune import Fire_Resistance_Rune
from scripts.items.runes.fire_runes.fire_circle_rune import Fire_Circle_Rune
from scripts.items.runes.fire_runes.fire_ball_rune import Fire_Ball_Rune
from scripts.items.runes.fire_runes.fire_spray_rune import Fire_Spray_Rune

from scripts.items.runes.freeze_runes.freeze_resistance_rune import Freeze_Resistance_Rune
from scripts.items.runes.freeze_runes.freeze_circle_rune import Freeze_Circle_Rune
from scripts.items.runes.freeze_runes.freeze_shield_rune import Freeze_Shield_Rune
from scripts.items.runes.freeze_runes.freeze_spray_rune import Freeze_Spray_Rune

from scripts.items.runes.poison_runes.poison_resistance_rune import Poison_Resistance_Rune



from scripts.items.runes.passive_runes.regen_rune import Regen_Rune


from scripts.items.runes.constant_runes.light_rune import Light_Rune
from scripts.items.runes.constant_runes.arcane_conduit_rune import Arcane_Conduit_Rune
from scripts.items.runes.basic_runes.resistance_rune import Resistance_Rune
from scripts.items.runes.constant_runes.shield_rune import Shield_Rune
from scripts.items.runes.constant_runes.hunger_rune import Hunger_Rune
from scripts.items.runes.constant_runes.manget_rune import Magnet_Rune

import math
import pygame

class Rune_Handler():
    def __init__(self, game):
        self.game = game
        self.runes = []
        self.active_runes = []
        self.saved_data = {}
        self.rune_types = [
                    'healing_rune',
                    'dash_rune',
                    'fire_resistance_rune',
                    'key_rune',
                    'freeze_resistance_rune',
                    'regen_rune',
                    'light_rune',
                    'invisibility_rune',
                    'strength_rune',
                    'silence_rune',
                    'speed_rune',
                    'vampiric_rune',
                    'fire_circle_rune',
                    'fire_ball_rune',
                    'fire_spray_rune',
                    'freeze_circle_rune',
                    'freeze_shield_rune',
                    'freeze_spray_rune',
                    'arcane_conduit_rune',
                    'resistance_rune',
                    'shield_rune',
                    'hunger_rune',
                    'magnet_rune',
                    'invulnerable_rune',
                    'poison_resistance_rune',
                    ]              

    
    def Add_Runes_To_Inventory_TEST(self):
        self.Add_Rune_To_Rune_Inventory('poison_resistance_rune')
        self.Add_Rune_To_Rune_Inventory('invulnerable_rune')
        self.Add_Rune_To_Rune_Inventory('invisibility_rune')

    def Clear_Runes(self):
        self.runes.clear()
        self.active_runes.clear()
        self.saved_data.clear()


    def Initialise_Runes(self):
        for rune_type in self.rune_types:
            self.Rune_Spawner(rune_type)

        self.Add_Runes_To_Inventory_TEST()
        
        
    def Save_Rune_Data(self):
        for rune in self.runes:
            rune.Save_Data()
            self.saved_data[rune.type] = rune.saved_data

    def Load_Data(self, data):
        for ID, item_data in data.items():
            if not item_data:
                continue
            try:
                type = item_data['type']
                self.Rune_Spawner(type, item_data)
            except Exception as e:
                print("DATA WRONG RUNE HANDLER", item_data, e)


    def Update(self, offset = (0,0)):
        for rune in self.active_runes:
            rune.Update()
  

    def Rune_Spawner(self, name, data = None):
        rune = None
        if 'healing' == name:
            rune = self.Init_Healing_Rune()
        elif 'dash' == name:
            rune = self.Init_Dash_Rune()
        elif 'fire_resistance' == name:
            rune = self.Init_Fire_Resistance_Rune()
        elif 'freeze_resistance' == name:
            rune = self.Init_Freeze_Resistance_Rune()
        elif 'key' == name:
            rune = self.Init_Key_Rune()
        elif 'regen' == name:
            rune = self.Init_Regen_Rune()
        elif 'light_rune' == name:
            rune = self.Init_Light_Rune()
        elif 'invisibility_rune' == name:
            rune = self.Init_Inivisibility_Rune()
        elif 'strength_rune' == name:
            rune = self.Init_Strength_Rune()
        elif 'silence_rune' == name:
            rune = self.Init_Silence_Rune()
        elif 'speed_rune' == name:
            rune = self.Init_Speed_Rune()
        elif 'vampiric_rune' == name:
            rune = self.Init_Vampiric_Rune()
        elif 'fire_circle_rune' == name:
            rune = self.Init_Fire_Circle_Rune()
        elif 'fire_ball_rune' == name:
            rune = self.Init_Fire_Ball_Rune()
        elif 'fire_spray_rune' == name:
            rune = self.Init_Fire_Spray_Rune()
        elif 'freeze_circle_rune' == name:
            rune = self.Init_Freeze_Circle_Rune()
        elif 'freeze_shield_rune' == name:
            rune = self.Init_Freeze_Shield_Rune()
        elif 'freeze_spray_rune' == name:
            rune = self.Init_Freeze_Spray_Rune()
        elif 'arcane_conduit_rune' == name:
            rune = self.Init_Arcane_Conduit_Rune()
        elif 'resistance_rune' == name:
            rune = self.Init_Resistance_Rune()
        elif 'shield_rune' == name:
            rune = self.Init_Shield_Rune()        
        elif 'magnet_rune' == name:
            rune = self.Init_Magnet_Rune()
        elif 'hunger_rune' == name:
            rune = self.Init_Hunger_Rune()
        elif 'invulnerable_rune' == name:
            rune = self.Invulnerable_Rune()
        elif 'poison_resistance_rune' == name:
            rune = self.Poison_Resistance_Rune()
        if not rune:
            return False
        
        if data:
            rune.Load_Data(data)
            if rune.active:
                for active_rune in self.active_runes:
                    if rune.type == active_rune.type:
                        return
                self.active_runes.append(rune)
        self.Initiailise_Rune(rune)
        
        return True
        


    
    

    def Initiailise_Rune(self, rune):
        if rune in self.runes:
            return
        self.runes.append(rune)
        self.game.item_handler.Add_Item(rune)
    


    # Add runes to Active Inventory
    def Add_Rune_To_Rune_Inventory(self, rune_type):
        for rune in self.runes:
            if rune_type != rune.type:
                continue
            
            rune.active = True
            self.active_runes.append(rune)
            self.game.rune_inventory.Add_Item(rune)
            self.game.item_handler.Add_Item(rune)
            return

    # Only one of each rune, so easy filter by rune_type return when found
    def Remove_Rune_From_Inventory(self, rune_type):
        for rune in self.runes:
            if rune_type != rune.type:
                continue
            
            rune.active = False
            self.active_runes.remove(rune)
            self.game.rune_inventory.Remove_Item(rune, True)
            self.game.item_handler.Remove_Item(rune)

            return True
    
        return False

    
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


    
    def Init_Healing_Rune(self):
        return Healing_Rune(self.game, (9999, 9999))
    
    def Init_Dash_Rune(self):
        return Dash_Rune(self.game, (9999, 9999))

    def Init_Fire_Resistance_Rune(self):
        return Fire_Resistance_Rune(self.game, (9999, 9999))

    def Init_Freeze_Resistance_Rune(self):
        return Freeze_Resistance_Rune(self.game, (9999, 9999))

    def Init_Key_Rune(self):
        return Key_Rune(self.game, (9999, 9999))

    def Init_Regen_Rune(self):
        return Regen_Rune(self.game, (9999, 9999))

    def Init_Light_Rune(self):
        return Light_Rune(self.game, (9999, 9999))

    def Init_Inivisibility_Rune(self):
        return Inivisibility_Rune(self.game, (9999, 9999))
    
    def Init_Strength_Rune(self):
        return Strength_Rune(self.game, (9999, 9999))
    
    def Init_Silence_Rune(self):
        return Silence_Rune(self.game, (9999, 9999))
    
    def Init_Speed_Rune(self):
        return Speed_Rune(self.game, (9999, 9999))
    
    def Init_Vampiric_Rune(self):
        return Vampiric_Rune(self.game, (9999, 9999))
    
    def Init_(self):
        return Light_Rune(self.game, (9999, 9999))
    
    def Init_Fire_Circle_Rune(self):
        return Fire_Circle_Rune(self.game, (9999, 9999))
    
    def Init_(self):
        return Light_Rune(self.game, (9999, 9999))
    
    def Init_Fire_Ball_Rune(self):
        return Fire_Ball_Rune(self.game, (9999, 9999))
    
    def Init_Fire_Spray_Rune(self):
        return Fire_Spray_Rune(self.game, (9999, 9999))
    
    def Init_Freeze_Circle_Rune(self):
        return Freeze_Circle_Rune(self.game, (9999, 9999))
    
    def Init_Freeze_Shield_Rune(self):
        return Freeze_Shield_Rune(self.game, (9999, 9999))
    
    def Init_Freeze_Spray_Rune(self):
        return Freeze_Spray_Rune(self.game, (9999, 9999))
    
    def Init_(self):
        return Light_Rune(self.game, (9999, 9999))
    
    def Init_Arcane_Conduit_Rune(self):
        # Create arcane rune for easy reference
        self.arcane_conduit_rune = Arcane_Conduit_Rune(self.game, (9999, 9999))
        return self.arcane_conduit_rune
    
    def Init_Resistance_Rune(self):
        return Resistance_Rune(self.game, (9999, 9999))
    
    def Init_Shield_Rune(self):
        return Shield_Rune(self.game, (9999, 9999))

    def Init_Hunger_Rune(self):
        return Hunger_Rune(self.game, (9999, 9999))

    def Init_Magnet_Rune(self):
        return Magnet_Rune(self.game, (9999, 9999))

    def Invulnerable_Rune(self):
        return Invulnerable_Rune(self.game, (9999, 9999))

    def Poison_Resistance_Rune(self):
        print("TESTETSTETST")
        return Poison_Resistance_Rune(self.game, (9999, 9999))
