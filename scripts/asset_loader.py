import pygame
from scripts.utils import load_image, load_images, Animation, get_tiles_from_sheet

class Asset_Loader:
    def Run_All(self):
        Asset_Loader.Asset_Tile_List(self)
        Asset_Loader.Asset_Trap_List(self)
        Asset_Loader.Asset_Effect_List(self)
        Asset_Loader.Asset_Entities_List(self)
        Asset_Loader.Asset_Objects_List(self)
        Asset_Loader.Asset_Environment_List(self)

    def Asset_Tile_List(self):
        tiles_assets = {
            'wall' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 3, 0, 0, 64, 16, 16),
            'door' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 3, 0, 0, 80, 16, 16),
            'trapdoor' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 5, 0, 0, 128, 16, 16),
            'banner' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 2, 0, 0, 144, 16, 16),
            'stair' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 1, 0, 0, 160, 16, 32),
            'LeftWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 0, 5, 0, 0, 16, 16),
            'RightWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 0, 5, 80, 0, 16, 16),
            'TopWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 0, 16, 0, 16, 16),
            'BottomWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 0, 16, 64, 16, 16),
            'Floor' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 2, 16, 16, 16, 16),
            'background': load_image('background.png'),
        }
        self.assets.update(tiles_assets)

    def Asset_Trap_List(self):
        trap_assets = {
            'spike' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 5, 0, 0, 112, 16, 16),
            'spike_poison' : get_tiles_from_sheet('traps/Spike_Trap_poison.png', 13, 0, 0, 0, 16, 16),
            'BearTrap' : get_tiles_from_sheet('traps/Bear_Trap.png', 3, 0, 0, 0, 32, 32),
            'PitTrap' : get_tiles_from_sheet('traps/Pit_Trap_Spikes.png', 1, 0, 0, 0, 16, 16),
            'TopPush' : get_tiles_from_sheet('traps/Push_Trap_Front.png', 10, 0, 0, 0, 16, 16),
            'Fire_Trap' : get_tiles_from_sheet('traps/Fire_Trap.png', 13, 0, 0, 0, 32, 40),
        }

        self.assets.update(trap_assets)

    def Asset_Effect_List(self):
        effect_assets = {
            'particle/leaf': Animation(load_images('particles/leaf'), img_dur=20, loop=False),
            'particle/particle': Animation(load_images('particles/particle'), img_dur=6, loop=False),
            'heart': load_image('heart.png'),
            'coin': get_tiles_from_sheet('coin_.png', 3, 0, 0, 0, 13, 13),
            'fire': get_tiles_from_sheet('particles/fire/orange/loops/burning_loop_1.png', 7, 0, 0, 0, 16, 16),
            'poison': get_tiles_from_sheet('particles/poison.png', 2, 0, 0, 0, 16, 16),
        }
        self.assets.update(effect_assets)
    
    def Asset_Entities_List(self):
        entities_assets = {
            'player': load_image('entities/player.png'),
            'enemy/idle': Animation(load_images('entities/enemy/idle'), img_dur=6),
            'enemy/run': Animation(load_images('entities/enemy/run'), img_dur=4),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'gun': load_image('gun.png'),
            'projectile': load_image('projectile.png'),
        }
        self.assets.update(entities_assets)

    def Asset_Objects_List(self):
        Objects_assets = {
            'Chest' : get_tiles_from_sheet('chest.png', 8, 0, 0, 0, 16, 16),
            'spawners': load_images('tiles/spawners'),    
        }
        self.assets.update(Objects_assets)

    def Asset_Environment_List(self):
        Environment_assets = {
            'Lava' : get_tiles_from_sheet('environment/lava.png', 2, 0, 0, 0, 16, 16),
        }
        self.assets.update(Environment_assets)
            
    def sound_effects(self):
        self.sfx ={
            'jump' : pygame.mixer.Sound('data/sfx/jump.wav'),
            'dash' : pygame.mixer.Sound('data/sfx/dash.wav'),
            'hit' : pygame.mixer.Sound('data/sfx/hit.wav'),
            'shoot' : pygame.mixer.Sound('data/sfx/shoot.wav'),
            'ambience' : pygame.mixer.Sound('data/sfx/ambience.wav'),
        }

        self.sfx['ambience'].set_volume(0.2)
        self.sfx['shoot'].set_volume(0.4)
        self.sfx['hit'].set_volume(0.8)
        self.sfx['dash'].set_volume(0.3)
        self.sfx['jump'].set_volume(0.7)

    def get_tile_image_from_sheet(file_name, x, y, color):
        sheet = pygame.image.load('data/images/tiles/' + file_name).convert_alpha()
        sheet.set_colorkey(color)
        return sheet