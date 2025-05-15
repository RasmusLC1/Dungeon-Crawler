import pygame
from scripts.entities.entities import PhysicsEntity
from scripts.engine.assets.keys import keys



class Decoration(PhysicsEntity):
    def __init__(self, game, type, pos, size, destructable = False, health = 0) -> None:
        super().__init__(game, type, 'decoration', pos, size)
        self.game.tilemap.Add_Entity_To_Tile(self.tile, self)
        self.light_level = 10
        self.animation = 0
        self.destructable = destructable
        self.health = health
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

    def Damage_Taken(self, damage, effect):
        if not self.health:
            return

        # Double damage for blunt weapons
        if effect == 'blunt':
            damage *= 2

        self.health -= damage
        print("CHEST HIT", self.health)
        if self.health <= 0:
            self.Destroyed()
        
    def Destroyed(self):
        pass
        


    def Render(self, surf, offset = (0,0)):
        if not self.Update_Light_Level():
            return

        
        self.Update_Dark_Surface()

        if not self.rendered_image:
            self.render_needs_update = True
            self.Update_Dark_Surface()
            if not self.rendered_image:
                print(vars(self))
                return
        
        # Render the chest
        surf.blit(self.rendered_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    
