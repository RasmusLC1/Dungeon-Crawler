from scripts.decoration.decoration import Decoration
from scripts.entities.items.weapons.close_combat.torch import Torch
import math

# UPDATE for throwable weapons
throwable_weapons = ['spear', 'fire_particle']

class Item_Handler():
    def __init__(self, game):
        self.game = game
        self.items = []
        self.nearby_items = []
        self.nearby_item_cooldown = 0
        self.Initialise()

    def Initialise(self):
        for torch in self.game.tilemap.extract([('torch', 0)].copy()):
            self.items.append(Torch(self.game, torch['pos'], (16, 16), torch['type']))


    def Add_Item(self, item):
        self.items.append(item)


    def Remove_Item(self, item, delete_item = False):
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
        self.nearby_items = self.Find_Nearby_Item(self.game.player.pos, 200)
        
        for item in self.items:
            
            item.Update_Animation()
            if not item.picked_up:
                self.items.remove(item)

            if item.sub_type in throwable_weapons:
                if not item.special_attack:
                    continue
                try:
                    item.Shoot()
                except Exception as e:
                    print(f"Item is not throwable {e}", item.sub_type)

    def Render(self, decorations, surf, render_scroll = (0, 0)):
        for decoration in decorations:
            decoration.Render(surf, render_scroll)