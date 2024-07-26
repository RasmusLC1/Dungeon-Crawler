import sys

import pygame
import json
import math


from scripts.utils import load_image, load_images, Animation
from scripts.asset_loader import Asset_Loader
from scripts.input.keyboard import Keyboard_Handler
from scripts.input.mouse import Mouse_Handler
from scripts.entities.player import Player
from scripts.tilemap import Tilemap
from scripts.particle_handler import Particle_Handler
from scripts.projectile.projectile_handler import Projectile_Handler
from scripts.traps.trap_handler import Trap_Handler
from scripts.interface.health_bar import Health_Bar
from scripts.interface.ammo_bar import Ammo_Bar
from scripts.interface.mana_bar import Mana_Bar
from scripts.interface.coins import Coins
from scripts.inventory.Chest_handler import Chest_Handler
from scripts.entities.enemy import Enemy
from scripts.a_star import A_Star
from scripts.light_handler import Light_Handler
from scripts.inventory.inventory import Inventory
from scripts.ray_caster import Ray_Caster 

import numpy as np

import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        self.render_scale = 4
        
        self.screen_width = 1280
        self.screen_height = 960
        self.screen = pygame.display.set_mode((1280, 960))
        self.display = pygame.Surface((self.screen_width/self.render_scale, self.screen_height/self.render_scale))

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False, False, False]
        self.assets = {}
        Asset_Loader.Run_All(self)

        self.player = Player(self, (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)
        self.inventory = Inventory(self)
        self.mouse = Mouse_Handler(self)
        self.ray_caster = Ray_Caster(self)
        self.a_star = A_Star()


        self.level = 0
        self.load_level(self.level)
        self.scroll = [0, 0]

        rows = 100  # Number of rows
        cols = 100  # Number of columns

        # Create a 2D array with all elements initialized to None
        self.test_array = np.zeros((rows, cols), dtype=int)
        # self.light_handler = Light_Handler(self)


        



    def tilemap_2d(self):
        for loc in self.tilemap:
            tile = self.tilemap[loc]

    def count_lines_in_json_file(file_path):
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count

    def load_level(self, map_id):
        self.tilemap.load('data/maps/' + str(map_id) + '.json')
        
        self.items = []
        self.particles = []
        self.sparks = []
        self.scroll = [0, 0]
        self.projectiles = []
        self.enemies = []

        for enemy in self.tilemap.extract([('spawners', 1)]):
            self.enemies.append(Enemy(self, enemy['pos'],  (self.assets[enemy['type']][0].get_width(), self.assets[enemy['type']][0].get_height()), 'DecrepitBones'))
            pass


        Trap_Handler.__init__(self)
        Chest_Handler.__init__(self)
 
        Ammo_Bar.__init__(self)
        Mana_Bar.__init__(self)
        Health_Bar.__init__(self)
        Coins.__init__(self)
        
        self.a_star.Setup_Map(self)
        # A_Star.Setup_Map(self)
        # self.light_handler.Setup_Shadow_Map()

        # Printing the map
        # for row in self.shadow_map:
        #     print(row)



    def Update(self, render_scroll):
            fps = int(self.clock.get_fps())
            pygame.display.set_caption('Dungeons of Madness             FPS: ' + str(fps))
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]), render_scroll)
            Particle_Handler.particle_update(self, render_scroll)
            Projectile_Handler.Projectile_Update(self, self.render_scale, render_scroll)
            Trap_Handler.Update(self)
            Chest_Handler.Update(self)

            for enemy in self.enemies:
                enemy.update(self.tilemap)
                if enemy.health <= 0:
                    self.enemies.remove(enemy)

            for item in self.items:
                if not item.picked_up:
                    self.items.remove(item)

            self.inventory.Update(render_scroll)
            Coins.Update(self)
            self.ray_caster.Update(self)
            # self.light_handler.Update(render_scroll)

            

    
    

    def Render(self, render_scroll):

        self.ray_caster.Ray_Caster()
        self.tilemap.render_tiles(self.ray_caster.tiles, self.display, offset=render_scroll)
        
        Trap_Handler.Render(self, render_scroll)
        Chest_Handler.Render(self, render_scroll)


        for item in self.items:
            item.render(self.display, offset = render_scroll)

        for enemy in self.ray_caster.enemies:
            enemy.render(self.display, offset=render_scroll)
        
        self.player.render(self.display, offset=render_scroll)
        Health_Bar.Health_Bar(self)
        Ammo_Bar.Attack_Recharge_Bar(self)
        Mana_Bar.Mana_Bar(self)
        Coins.Render(self)
        self.inventory.render(self.display)
        for particle in self.particles:
            particle.render(self.display, render_scroll)





        
    def run(self):  
        while True:
            self.display.blit(self.assets['background'], (0, 0))
            # Get the scroll offset
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            Game.Render(self, render_scroll)
            Game.Update(self, render_scroll)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.mouse.Mouse_Input(event, render_scroll)

                Keyboard_Handler.keyboard_Input(self, event, offset = render_scroll)

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()