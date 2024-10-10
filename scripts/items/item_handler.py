from scripts.decoration.decoration import Decoration
from scripts.items.weapons.close_combat.torch import Torch
from scripts.items.loot.key import Key
from scripts.items.loot.gold import Gold
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
        self.Initialise()

    def Initialise(self):
        for torch in self.game.tilemap.extract([('torch', 0)].copy()):
            self.items.append(Torch(self.game, torch['pos'], (16, 16)))
        
        for key in self.game.tilemap.extract([('key', 0)].copy()):
            self.items.append(Key(self.game, key['pos']))

        for gold in self.game.tilemap.extract([('gold', 0)].copy()):
            amount = random.randint(20, 30)
            self.items.append(Gold(self.game, gold['pos'], amount))



    def Add_Item(self, item):
        if item in self.items:
            return
        self.items.append(item)


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


            if item.sub_type in throwable_weapons:
                if not item.special_attack:
                    if not item.entity:
                        continue
                    # if item.entity.type == 'player':
                    #     continue
                    if item.shoot_speed and item.entity.subtype == 'enemy' and not item.delete_countdown:
                        item.Set_Delete_Countdown(10)
                    continue
                try:
                    if not item in self.items:
                        continue
                    item.Shoot()
                except Exception as e:
                    print(f"Item is not throwable {e}", item.sub_type)

    def Reset_Nearby_Items_Cooldown(self):
        self.nearby_item_cooldown = 1

    def Update_Nearby_Items_Cooldown(self):
        if self.nearby_item_cooldown:
            self.nearby_item_cooldown = max(0, self.nearby_item_cooldown - 1)
            return False
        self.nearby_item_cooldown = 30
        return True

