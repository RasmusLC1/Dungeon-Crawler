import sys

import pygame
import random
import math
import os

from scripts.utils import load_image, load_images, Animation
from scripts.asset_loader import Asset_Loader
from scripts.keyboard import Keyboard_Handler
from scripts.entities import PhysicsEntity
from scripts.player import Player
from scripts.tilemap import Tilemap
from scripts.particle import Particle
from scripts.spark import Spark
from scripts.particle_handler import Particle_Handler




class Game:
    def __init__(self):
        pygame.init()
        self.render_scale = 4
        pygame.display.set_caption('Dungeons of Madness')
        self.screen_height = 1280
        self.screen_width = 960
        self.screen = pygame.display.set_mode((1280, 960))
        self.display = pygame.Surface((self.screen_height/self.render_scale, self.screen_width/self.render_scale))

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



    def Update(self):
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]))

        
    def Render(self, render_scroll):
        self.player.render(self.display, offset=render_scroll)

        self.tilemap.render(self.display, offset=render_scroll)

        
        
    def run(self):
        

        while True:
            self.display.blit(self.assets['background'], (0, 0))


            Game.Update(self)
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            Game.Render(self, render_scroll)
            
            
            for particle in self.particles.copy():
                kill = particle.update()
                particle.render(self.display, offset=render_scroll)
                particle.render(self.display, offset = render_scroll)
                if kill:
                    self.particles.remove(particle)

            # [[x, y], direction, timer]
            for projectile in self.projectiles.copy():
                projectile[0][0] += projectile[1][0]
                projectile[0][1] += projectile[1][1]
                projectile[2] += 1
                img = self.assets['projectile']
                self.display.blit(img, (projectile[0][0] - img.get_width() / self.render_scale - render_scroll[0], projectile[0][1] - img.get_height() / self.render_scale - render_scroll[1]))
                if self.tilemap.solid_check(projectile[0]):
                    self.projectiles.remove(projectile)
                    # for i in range(4):
                        # self.sparks.append(Spark(projectile[0], random.random() - 0.5 + (math.pi if projectile[1] > 0 else 0), 2 + random.random()))
                    
                elif projectile[2] > 360:
                    self.projectiles.remove(projectile)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                Keyboard_Handler.keyboard_Input(self, event, offset = render_scroll)

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()