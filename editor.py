import sys

import pygame

from scripts.utils import load_images, load_image, get_tiles_from_sheet
from scripts.tilemap import Tilemap
from scripts.asset_loader import Asset_Loader

RENDER_SCALE = 2.0

class Editor:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('editor')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()
        
        self.assets = {
            'spawners': load_images('tiles/spawners'),
            'wall' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 3, 0, 0, 64, 16, 16),
            'door' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 3, 0, 0, 80, 16, 16),
            'torch' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 3, 0, 0, 96, 16, 16),
            'spike' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 5, 0, 0, 112, 16, 16),
            'Fire_Trap' : get_tiles_from_sheet('traps/Fire_Trap.png', 13, 0, 0, 0, 32, 40),
            'trapdoor' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 5, 0, 0, 128, 16, 16),
            'banner' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 2, 0, 0, 144, 16, 16),
            'stair' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 1, 0, 0, 160, 16, 32),
            'LeftWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 0, 5, 0, 0, 16, 16),
            'RightWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 0, 5, 80, 0, 16, 16),
            'TopWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 0, 16, 0, 16, 16),
            'BottomWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 0, 16, 64, 16, 16),
            'Floor' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 2, 16, 16, 16, 16),
            'Chest' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 5, 0, 0, 128, 16, 16),
            'BearTrap' : get_tiles_from_sheet('traps/Bear_Trap.png', 3, 0, 0, 0, 32, 32),
            'PitTrap' : get_tiles_from_sheet('traps/Pit_Trap_Spikes.png', 1, 0, 0, 0, 16, 16),
            'TopPush' : get_tiles_from_sheet('traps/Push_Trap_Front.png', 10, 0, 0, 0, 16, 16),
            'Lava' : get_tiles_from_sheet('traps/lava.png', 2, 0, 0, 0, 16, 16),
        }
        
        self.movement = [False, False, False, False]
        
        self.tilemap = Tilemap(self, tile_size=16)
        
        try:
            self.tilemap.load('map.json')
        except FileNotFoundError:
            pass
        
        self.scroll = [0, 0]
        
        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0
        
        self.clicking = False
        self.right_clicking = False
        self.shift = False
        self.ongrid = True
        
    def run(self):
        while True:
            self.display.fill((0, 0, 0))
            
            self.scroll[0] += (self.movement[1] - self.movement[0]) * 2
            self.scroll[1] += (self.movement[3] - self.movement[2]) * 2
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            
            current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
            current_tile_img.set_alpha(100)
            
            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0] / RENDER_SCALE, mpos[1] / RENDER_SCALE)
            tile_pos = (int((mpos[0] + self.scroll[0]) // self.tilemap.tile_size), int((mpos[1] + self.scroll[1]) // self.tilemap.tile_size))
            
            self.tilemap.render(self.display, offset=render_scroll)
            if self.ongrid:
                self.display.blit(current_tile_img, (tile_pos[0] * self.tilemap.tile_size - self.scroll[0], tile_pos[1] * self.tilemap.tile_size - self.scroll[1]))
            else:
                self.display.blit(current_tile_img, mpos)
            
            offgrid_list = ['spawners', 'BearTrap', 'TopPush', 'Chest', 'Fire_Trap']


            # Placing tiles on the grid
            if self.clicking and self.ongrid:
                if (self.tile_list[self.tile_group] in offgrid_list):
                    self.ongrid = False
                else:
                    self.ongrid = True
                    self.tilemap.tilemap[str(tile_pos[0]) + ';' + str(tile_pos[1])] = {'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': tile_pos}
            if self.right_clicking:
                tile_loc = str(tile_pos[0]) + ';' + str(tile_pos[1])
                if tile_loc in self.tilemap.tilemap:
                    del self.tilemap.tilemap[tile_loc]
                for tile in self.tilemap.offgrid_tiles.copy():
                    tile_img = self.assets[tile['type']][tile['variant']]
                    tile_r = pygame.Rect(tile['pos'][0] - self.scroll[0], tile['pos'][1] - self.scroll[1], tile_img.get_width(), tile_img.get_height())
                    if tile_r.collidepoint(mpos):
                        self.tilemap.offgrid_tiles.remove(tile)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                        # Place tiles off grid
                        if not self.ongrid:
                            self.tilemap.offgrid_tiles.append({'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': (mpos[0] + self.scroll[0], mpos[1] + self.scroll[1])})
                            
                    if event.button == 3:
                        self.right_clicking = True
                    if self.shift:
                        if event.button == 4:
                            self.tile_variant = (self.tile_variant - 1) % len(self.assets[self.tile_list[self.tile_group]])
                        if event.button == 5:
                            self.tile_variant = (self.tile_variant + 1) % len(self.assets[self.tile_list[self.tile_group]])
                    else:
                        if event.button == 4:
                            self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                            self.tile_variant = 0
                        if event.button == 5:
                            self.tile_group = (self.tile_group + 1) % len(self.tile_list)
                            self.tile_variant = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False
                    if event.button == 3:
                        self.right_clicking = False
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_g:
                        self.ongrid = not self.ongrid
                    if event.key == pygame.K_t:
                        self.tilemap.autotile()
                    if event.key == pygame.K_o:
                        self.tilemap.save('map.json')
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
                    if event.key == pygame.K_LSHIFT:
                        self.shift = False
          

            font = pygame.font.Font('freesansbold.ttf', 16)
            self.display.blit(current_tile_img, (5, 5))
            text = font.render(self.tile_list[self.tile_group], True, (255, 255, 255))            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.screen.blit(text, (150, 0))
            pygame.display.update()
            self.clock.tick(60)

Editor().run()