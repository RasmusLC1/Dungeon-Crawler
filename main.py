import sys

import pygame
import json
import math


from scripts.utils import load_image, load_images, Animation
from scripts.engine.asset_loader import Asset_Loader
from scripts.input.keyboard import Keyboard_Handler
from scripts.input.mouse import Mouse_Handler
from scripts.entities.player.player import Player
from scripts.engine.tilemap import Tilemap
from scripts.engine.particles.particle_handler import Particle_Handler
from scripts.projectile.projectile_handler import Projectile_Handler
from scripts.traps.trap_handler import Trap_Handler
from scripts.decoration.decoration_handler import Decoration_Handler
from scripts.entities.player.items.item_handler import Item_Handler
from scripts.engine.lights import light_handler
from scripts.interface.health_bar import Health_Bar
from scripts.interface.ammo_bar import Ammo_Bar
from scripts.interface.mana_bar import Mana_Bar
from scripts.interface.coins import Coins
from scripts.decoration.chest.Chest_handler import Chest_Handler
from scripts.entities.enemy import Enemy
from scripts.engine.a_star import A_Star
from scripts.engine.lights.light_handler import Light_Handler
from scripts.inventory.inventory import Inventory
from scripts.inventory.weapon_inventory_handler import Weapon_Inventory_Handler
from scripts.engine.ray_caster import Ray_Caster 

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
        self.player = None


        self.tilemap = Tilemap(self, tile_size=16)
        self.inventory = Inventory(self)
        # TODO: PLACEHOLDER CODE, Implement proper class system later
        self.proffeciency = {'sword, shield, bow, arrow, axe, mace'}
        self.weapon_inventory = Weapon_Inventory_Handler(self, 'warrior', self.proffeciency)
        self.mouse = Mouse_Handler(self)
        self.ray_caster = Ray_Caster(self)
        self.a_star = A_Star()

        self.level = 0
        self.scroll = [0, 0]
        self.entities_render = []

        self.load_level(self.level)

        



    def tilemap_2d(self):
        for loc in self.tilemap:
            tile = self.tilemap[loc]

    def count_lines_in_json_file(file_path):
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count

    def load_level(self, map_id):
        self.tilemap.load('data/maps/' + str(map_id) + '.json')
         # Setup handlers
        self.light_handler = Light_Handler(self)
        
        
        self.particles = []
        self.sparks = []
        self.scroll = [0, 0]
        self.projectiles = []
        self.enemies = []
        for spawner in self.tilemap.extract([('spawners', 0), ('spawners', 1)]):
            if spawner['variant'] == 0:
                self.player = Player(self, spawner['pos'], (8, 16))

            else:
                self.enemies.append(Enemy(self, spawner['pos'],  (self.assets[spawner['type']][0].get_width(), self.assets[spawner['type']][0].get_height()), 'DecrepitBones'))

        self.trap_handler = Trap_Handler(self)
        self.decoration_handler = Decoration_Handler(self)
        self.chest_handler = Chest_Handler(self)
        self.item_handler = Item_Handler(self)
 
        Ammo_Bar.__init__(self)
        Mana_Bar.__init__(self)
        Health_Bar.__init__(self)
        Coins.__init__(self)
        
        self.a_star.Setup_Map(self)

        



        # Printing the map
        # for row in self.shadow_map:
        #     print(row)



    def Update(self, render_scroll):
            fps = int(self.clock.get_fps())
            pygame.display.set_caption('Dungeons of Madness             FPS: ' + str(fps))
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]), render_scroll)
            Particle_Handler.particle_update(self, render_scroll)
            Projectile_Handler.Projectile_Update(self, self.render_scale, render_scroll)
            self.trap_handler.Update()
            self.chest_handler.Update()
            self.decoration_handler.Update()
            self.item_handler.Update()

            for enemy in self.enemies:
                enemy.update(self.tilemap)
                if enemy.health <= 0:
                    self.enemies.remove(enemy)

            self.inventory.Update(render_scroll)
            Coins.Update(self)
            self.ray_caster.Update(self)
    

    def Render(self, render_scroll):
        self.ray_caster.Ray_Caster()
        self.tilemap.render_tiles(self.ray_caster.tiles, self.display, offset=render_scroll)

        self.trap_handler.Render(self.ray_caster.traps, self.display, render_scroll)

        self.entities_render.sort(key=lambda entity: entity.pos[1])
        for entity in self.entities_render:
            entity.Render(self.display, render_scroll)


        Health_Bar.Health_Bar(self)
        Ammo_Bar.Attack_Recharge_Bar(self)
        Mana_Bar.Mana_Bar(self)
        Coins.Render(self)
        self.inventory.Render(self.display)
        self.weapon_inventory.Render(self.display)
        for particle in self.particles:
            particle.Render(self.display, render_scroll)





        
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