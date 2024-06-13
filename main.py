import sys

import pygame


from scripts.utils import load_image, load_images, Animation
from scripts.asset_loader import Asset_Loader
from scripts.keyboard import Keyboard_Handler
from scripts.player import Player
from scripts.tilemap import Tilemap
from scripts.particle_handler import Particle_Handler
from scripts.projectile_handler import Projectile_Handler
from scripts.traps.trap_handler import Trap_Handler
from scripts.interface.health_bar import Health_Bar
from scripts.interface.ammo_bar import Ammo_Bar
from scripts.interface.coins import Coins
from scripts.Chest.Chest_handler import Chest_Handler


class Game:
    def __init__(self):
        pygame.init()
        self.render_scale = 4
        pygame.display.set_caption('Dungeons of Madness')
        self.screen_width = 1280
        self.screen_height = 960
        self.screen = pygame.display.set_mode((1280, 960))
        self.display = pygame.Surface((self.screen_width/self.render_scale, self.screen_height/self.render_scale))

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False, False, False]
        Asset_Loader.asset_list(self)

        self.player = Player(self, (50, 50), (8, 15))
        self.tilemap = Tilemap(self, tile_size=16)


        self.level = 0
        self.load_level(self.level)
        self.scroll = [0, 0]
        self.mpos = 0
   

    def load_level(self, map_id):
        self.tilemap.load('data/maps/' + str(map_id) + '.json')
        
        self.particles = []
        self.sparks = []
        self.scroll = [0, 0]
        self.projectiles = []
        Trap_Handler.__init__(self)
        Chest_Handler.__init__(self)

        Ammo_Bar.__init__(self)
        Health_Bar.__init__(self)
        Coins.__init__(self)

    def Update(self, render_scroll):
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]), render_scroll)
            Particle_Handler.particle_update(self, render_scroll)
            Projectile_Handler.Projectile_Update(self, self.render_scale, render_scroll)
            Trap_Handler.Update(self)
            Chest_Handler.Update(self)

            Coins.Update(self)
    
    

    def Render(self, render_scroll):

        self.tilemap.render(self.display, offset=render_scroll)
        
        Trap_Handler.Render(self, render_scroll)
        Chest_Handler.Render(self, render_scroll)

        self.player.render(self.display, offset=render_scroll)
        Health_Bar.Health_Bar(self)
        Ammo_Bar.Ammo_Bar(self)
        Coins.Render(self)

        
        


        
    def run(self):  
        while True:
            self.display.blit(self.assets['background'], (0, 0))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            Game.Render(self, render_scroll)
            Game.Update(self, render_scroll)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                Keyboard_Handler.keyboard_Input(self, event, offset = render_scroll)

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()