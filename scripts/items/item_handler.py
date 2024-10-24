from scripts.decoration.decoration import Decoration
from scripts.items.weapons.close_combat.torch import Torch
from scripts.items.loot.key import Key
from scripts.items.loot.gold import Gold
from scripts.items.weapons.weapon_handler import Weapon_Handler
from scripts.items.potions.potion_handler import Potion_Handler
from scripts.items.loot.loot_handler import Loot_Handler
import math
import random

# UPDATE for throwable weapons
throwable_weapons = ['spear', 'fire_particle', 'ice_particle', 'arrow', 'spider_web']

class Item_Handler():
    def __init__(self, game):
        self.game = game
        self.items = []
        self.nearby_items = []
        self.nearby_item_cooldown = 0
        self.saved_data = {}
        self.weapon_handler = Weapon_Handler(self.game)
        self.potion_handler = Potion_Handler(self.game)
        self.loot_handler = Loot_Handler(self.game)

    def Save_Item_Data(self):
        for item in self.items:
            item.Save_Data()
            self.saved_data[item.item_ID] = item.saved_data

    def Load_Data(self, data):

        for item_id, item_data in data.items():
            if not item_data:
                continue

            self.Load_Item_From_Data(item_data)

    def Load_Item_From_Data(self, item_data):
        try:
            type = item_data['type']
            pos = item_data['pos']
            amount = item_data['amount']
            if item_data['category'] == 'weapon':
                self.weapon_handler.Weapon_Spawner(type, pos[0], pos[1], amount, item_data)
            elif item_data['category'] == 'potion':
                self.potion_handler.Spawn_Potions(type, pos[0], pos[1], amount, item_data)
            elif item_data['category'] == 'loot':
                self.loot_handler.Loot_Spawner(type, pos[0], pos[1], amount, item_data)
            elif item_data['category'] == 'rune':
                self.game.rune_handler.Rune_Spawner(type, item_data)
            else:
                return False
            
            return True
        except Exception as e:
            print("DATA WRONG", item_data, e)


    def Clear_Items(self):
        self.items.clear()
        self.nearby_items.clear()
        self.saved_data.clear()

    def Initialise(self):
        for torch in self.game.tilemap.extract([('torch', 0)].copy()):
            self.weapon_handler.Weapon_Spawner('torch', torch['pos'][0], torch['pos'][1])
        
        for key in self.game.tilemap.extract([('key', 0)].copy()):
            self.loot_handler.Loot_Spawner('key', key['pos'][0], key['pos'][1])


        for gold in self.game.tilemap.extract([('gold', 0)].copy()):
            amount = random.randint(20, 30)
            self.loot_handler.Loot_Spawner('gold', gold['pos'][0], gold['pos'][1], amount)



    def Add_Item(self, item):
        if item in self.items:
            return
        self.items.append(item)

    
    def Find_Item(self, item_ID):
        for item in self.items:
            if item.item_ID == item_ID:
                return item
        
        return None

    def Remove_Item(self, item, delete_item = False):
        if not item in self.items:
            print("ITEM DOES NOT EXISTS", item)
            return
        
        self.items.remove(item)
        self.game.entities_render.Remove_Entity(item)
        if delete_item:
            del item


    def Find_Nearby_Item(self, entity_pos, max_distance):
        nearby_items = []
        for item in self.items:
            # Calculate the Euclidean distance
            distance = math.sqrt((entity_pos[0] - item.pos[0]) ** 2 + (entity_pos[1] - item.pos[1]) ** 2)
            if distance < max_distance:
                nearby_items.append(item)

        
        return nearby_items


    def Update(self, offset = (0,0)):
        self.Check_Keyboard_Input()
        if self.Update_Nearby_Items_Cooldown():
            self.nearby_items.clear()
            self.nearby_items = self.Find_Nearby_Item(self.game.player.pos, 200)
        
        for item in self.items:

            if item.Update_Delete_Cooldown():
                if not item.delete_countdown:
                    self.Remove_Item(item, True)
                    continue

            if item.picked_up:
                self.items.remove(item)
                continue


            if item.type in throwable_weapons:
                if not item.special_attack:
                    if not item.entity:
                        continue
                    # if item.entity.type == 'player':
                    #     continue
                    if item.shoot_speed and item.entity.category == 'enemy' and not item.delete_countdown:
                        item.Set_Delete_Countdown(10)
                    continue
                try:
                    if not item in self.items:
                        continue
                    item.Shoot()
                except Exception as e:
                    print(f"Item is not throwable {e}", item.type)

    def Check_Keyboard_Input(self):
        if self.game.keyboard_handler.e_pressed:
            if not self.Pick_Up_Items():
                return
            else:
                self.game.keyboard_handler.Set_E_Key(False)
    
    def Pick_Up_Items(self) -> bool:
        nearby_items = self.Find_Nearby_Item(self.game.player.pos, 10)
        if not nearby_items:
            return False
        player_pos = self.game.player.pos
        nearby_items.sort(key=lambda decoration: math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2))
        
        nearby_items[0].Pick_Up()
        return True

    def Reset_Nearby_Items_Cooldown(self):
        self.nearby_item_cooldown = 1

    def Update_Nearby_Items_Cooldown(self):
        if self.nearby_item_cooldown:
            self.nearby_item_cooldown = max(0, self.nearby_item_cooldown - 1)
            return False
        self.nearby_item_cooldown = 30
        return True


