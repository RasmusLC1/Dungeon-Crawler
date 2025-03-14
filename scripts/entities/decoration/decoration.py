import pygame
from scripts.entities.entities import PhysicsEntity



class Decoration(PhysicsEntity):
    def __init__(self, game, type, pos, size) -> None:
        super().__init__(game, type, 'decoration', pos, size)
        self.game.tilemap.Add_Entity_To_Tile(self.tile, self)
        self.animation = 0
        self.Set_Sprite()


    def Update_Animation(self):
        pass

    def Open(self, generate_clatter = False):
        pass
    
    # Setting the initial sprite type from assets, only called during initial setup
    def Set_Sprite(self):
        self.sprite = self.game.assets[self.type]
        self.Set_Entity_Image()

    # Setting the item image and scaling it
    def Set_Entity_Image(self):
        entity_image = self.sprite[self.animation].convert_alpha()
        self.entity_image = pygame.transform.scale(entity_image, self.size)


    def Render(self, surf, offset = (0,0)):
        if not self.Update_Light_Level():
            return

        
        self.Update_Dark_Surface()

        if not self.rendered_image:
            self.render_needs_update = True
            self.Update_Dark_Surface()
            print("DECORATION ERROR", vars(self))
            return
        
        # Render the chest
        surf.blit(self.rendered_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    
