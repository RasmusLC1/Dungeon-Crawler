from scripts.entities.items.loot.utility.utility_loot import Utility_Loot
import random
import pygame

class Ethereal_Chains(Utility_Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'ethereal_chains', pos, 150)
        self.activations = random.randint(2, 4)
        self.Set_Description()
        self.range = 3
        self.Set_Radius_Image()
   

    def Set_Description(self):
        self.description = 'Snares nearby\n enemies' + str(self.activations) + 'times'

    def Update(self):
        return super().Update()

    # If out of activations, reset the hourglass
    def Reset_Chains(self):
        self.activations -= 1

        if self.activations:
            self.clicked = False
            self.Set_Description() # Update description
            return
        
        self.game.item_handler.Remove_Item(self, True)
        self.game.inventory.Remove_Item(self)
    
    # The update function in the inventory
    def Update_In_Inventory(self):
        if not super().Update_In_Inventory():
            return False

        if self.game.mouse.left_click:
            self.Snare_Enemies()

        return True


    def Render_Line(self, surf, offset, alpha):
        pass

    # Effect of opening door on key
    def Snare_Enemies(self):
        self.Find_Nearby_Entities_Mouse()
        for enemy in self.nearby_entities:
            enemy.effects.Set_Effect("snare", 3)
        self.Reset_Chains()
    
    # Setting the radius image and scaling it
    def Set_Radius_Image(self):
        sprite = self.game.assets['radius']
        item_image = sprite[0].convert_alpha()
        range = self.range * self.game.tilemap.tile_size
        self.radius_image = pygame.transform.scale(item_image, (range, range))

    # Render the range of the effect
    def Render_Range(self, surf, offset):
        radius_image = self.radius_image.copy()
        if self.distance_to_player > self.max_distance:
            radius_image.set_alpha(200)
        game = self.game
        range = self.range * self.game.tilemap.tile_size // 2
        surf.blit(radius_image, (game.mouse.mpos[0] - offset[0] - range, game.mouse.mpos[1] - offset[1] - range))
        

    # Seperate find enemies close to the mouse
    def Find_Nearby_Entities_Mouse(self):
        self.nearby_entities = self.game.tilemap.Search_Nearby_Tiles(self.range, self.game.mouse.mpos, 'enemy', self.ID)

    def Render_Active(self, surf, offset=...):
        if self.clicked:
            self.Render_Range(surf, offset)
        return super().Render(surf, offset)