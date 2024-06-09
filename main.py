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
from scripts.projectile_handler import Projectile_Handler
from scripts.traps.spike import Spike
from scripts.traps.bear_trap import Bear_Trap
from scripts.traps.spike_pit import Spike_Pit
from scripts.traps.top_push_trap import Top_Push_Trap




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
        self.spikes = []
        self.bear_traps = []
        self.spike_pits = []
        self.top_pushers = []
        # Spawner initialisation
        for spawner in self.tilemap.extract([('spawners', 0), ('spawners', 1)]):
            if spawner['variant'] == 0:
                self.player.pos = spawner['pos']

        # Spike initialisation
        for spike_tile in self.tilemap.extract([('spike', 0)], True):
            self.spikes.append(Spike(self, spike_tile['pos'], (self.assets[spike_tile['type']][0].get_width(), self.assets[spike_tile['type']][0].get_height())))
        
        # top pusher initialisation
        for top_push in self.tilemap.extract([('TopPush', 0)]):
            self.top_pushers.append(Top_Push_Trap(self, top_push['pos'], (self.assets[top_push['type']][0].get_width(), self.assets[top_push['type']][0].get_height())))

        # Bear Trap initialisation
        for trap in self.tilemap.extract([('BearTrap', 0)]):
            self.bear_traps.append(Bear_Trap(self, trap['pos'], (10, 5)))

        # Spike pit initialisation
        for spike_pit in self.tilemap.extract([('PitTrap', 0)], True):
            self.spike_pits.append(Spike_Pit(self, spike_pit['pos'], (self.assets[spike_pit['type']][0].get_width(), self.assets[spike_pit['type']][0].get_height())))



    def Update(self, render_scroll):
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]), render_scroll)
            Particle_Handler.particle_update(self, render_scroll)
            Projectile_Handler.Projectile_Update(self, self.render_scale, render_scroll)
            for spike in self.spikes:
                spike.Update()

            for bear_trap in self.bear_traps:
                bear_trap.Update()

            for spike_pit in self.spike_pits:
                spike_pit.Update()

            for top_pusher in self.top_pushers:
                top_pusher.Update()
        
    def Render(self, render_scroll):

        self.tilemap.render(self.display, offset=render_scroll)
        
        for spike in self.spikes:
            spike.Render(self.display, 'spike', offset=render_scroll)

        for bear_trap in self.bear_traps:
            bear_trap.Render(self.display, 'BearTrap', offset=render_scroll)

        for spike_pit in self.spike_pits:
            spike_pit.Render(self.display, 'PitTrap', offset=render_scroll)
        
        for top_pusher in self.top_pushers:
            top_pusher.Render(self.display, 'TopPush', offset=render_scroll)


        self.player.render(self.display, offset=render_scroll)

        
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