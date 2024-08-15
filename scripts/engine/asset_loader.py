import pygame
from scripts.engine.utils import load_image, load_images, Animation, get_tiles_from_sheet

class Asset_Loader:
    def Run_All(self):
        Asset_Loader.Asset_Background_List(self)
        Asset_Loader.Asset_Tile_List(self)
        Asset_Loader.Asset_Trap_List(self)
        Asset_Loader.Asset_Effect_List(self)
        Asset_Loader.Asset_Enemies_List(self)
        Asset_Loader.Asset_Player_List(self)
        Asset_Loader.Asset_Interative_Objects_List(self)
        Asset_Loader.Asset_Environment_List(self)
        Asset_Loader.Asset_Objects_List(self)
        Asset_Loader.Asset_Potion_List(self)
        Asset_Loader.Asset_Decoration_List(self)
        Asset_Loader.Asset_Weapons_List(self)
        Asset_Loader.Asset_Weapon_Inventory(self)

        
    def Asset_Background_List(self):
        background_assets = {'background': load_image('background.png'),}
        self.assets.update(background_assets)
        

    def Asset_Tile_List(self):
        white = (255,255,255)
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
        }
        self.assets.update(tiles_assets)

    def Asset_Trap_List(self):
        white = (255,255,255)
        trap_assets = {
            'spike_trap' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 5, 0, 0, 112, 16, 16, white),
            'spike_poison_trap' : get_tiles_from_sheet('traps/Spike_Trap_poison.png', 13, 0, 0, 0, 16, 16, white),
            'Bear_trap' : get_tiles_from_sheet('traps/Bear_Trap.png', 3, 0, 0, 0, 32, 32, white),
            'Pit_trap' : get_tiles_from_sheet('traps/Pit_Trap_Spikes.png', 1, 0, 0, 0, 16, 16, white),
            'Top_trap' : get_tiles_from_sheet('traps/Push_Trap_Front.png', 10, 0, 0, 0, 16, 16, white),
            'Fire_trap' : get_tiles_from_sheet('traps/Fire_Trap.png', 13, 0, 0, 0, 16, 20, white),
        }

        self.assets.update(trap_assets)

    def Asset_Effect_List(self):
        white = (255,255,255)
        effect_assets = {
            'particle/leaf': Animation(load_images('particles/leaf'), img_dur=20, loop=False),
            'particle/particle': Animation(load_images('particles/particle'), img_dur=6, loop=False),
            'heart': load_image('heart.png'),
            'coin': get_tiles_from_sheet('coin_.png', 3, 0, 0, 0, 13, 13, white),
            'fire': get_tiles_from_sheet('particles/effects/fire/orange/loops/burning_loop_1.png', 7, 0, 0, 0, 16, 16, white),
            'poison': get_tiles_from_sheet('particles/effects/poison.png', 2, 0, 0, 0, 16, 16, white),
            'frozen': get_tiles_from_sheet('particles/effects/frozen.png', 2, 0, 0, 0, 16, 16, white),
            'wet': get_tiles_from_sheet('particles/effects/wet.png', 1, 0, 0, 0, 13, 17, white),
        }
        self.assets.update(effect_assets)
    
    def Asset_Player_List(self):
        entities_assets = {

            'player_idle_down_head': get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 0, 16, 8),
            'player_idle_down_body': get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 8, 16, 6),
            'player_idle_down_legs': get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 14, 16, 2),

            'player_idle_up_head': get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 0, 16, 8),
            'player_idle_up_body': get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 8, 16, 6),
            'player_idle_up_legs': get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 14, 16, 2),

            'player_attack_head': get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 0, 16, 8),
            'player_attack_body': get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 8, 16, 6),
            'player_attack_legs': get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 14, 16, 2),


            'gun': load_image('gun.png'),
            'projectile': load_image('projectile.png'),
        }
        self.assets.update(entities_assets)

    def Asset_Enemies_List(self):
        entities_assets = {
            'decrepit_bones_head': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones.png', 2, 0, 0, 0, 16, 8),
            'decrepit_bones_body': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones.png', 2, 0, 0, 8, 16, 6),
            'decrepit_bones_legs': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones.png', 2, 0, 0, 14, 16, 2),

        }
        self.assets.update(entities_assets)

    def Asset_Weapons_List(self):
        Weapons_assets = {
            'sword' : get_tiles_from_sheet('weapons/sword.png', 1, 0, 0, 0, 16, 16),
            'sword_attack' : get_tiles_from_sheet('weapons/sword.png', 1, 0, 0, 0, 16, 16), # TEMP REMOVE
            'torch': get_tiles_from_sheet('weapons/torch.png', 8, 0, 0, 0, 16, 16),
            'torch_attack': get_tiles_from_sheet('weapons/torch_attack.png', 8, 0, 0, 0, 16, 16),
            'spear': get_tiles_from_sheet('weapons/spear.png', 8, 0, 0, 0, 16, 16),
            'spear_attack': get_tiles_from_sheet('weapons/spear_attack.png', 8, 0, 0, 0, 16, 16),

        }
        self.assets.update(Weapons_assets)

    def Asset_Weapon_Inventory(self):
        Weapon_Inventory_assets = {
            'sword_shield' : get_tiles_from_sheet('weapon_inventory/sword_shield.png', 2, 0, 0, 0, 17, 17),
            'duel_wield' : get_tiles_from_sheet('weapon_inventory/Duel_wield.png', 2, 0, 0, 0, 17, 17),
            'bow_arrow' : get_tiles_from_sheet('weapon_inventory/Bow_Arrow.png', 2, 0, 0, 0, 17, 17),
            'left_right' : get_tiles_from_sheet('weapon_inventory/left_right.png', 2, 0, 0, 0, 17, 17),
        }
        self.assets.update(Weapon_Inventory_assets)


    def Asset_Interative_Objects_List(self):
        white = (255,255,255)
        Objects_assets = {
            'Chest' : get_tiles_from_sheet('chest.png', 8, 0, 0, 0, 16, 16, white),
        }
        self.assets.update(Objects_assets)


    def Asset_Objects_List(self):
        Objects_assets = {
            'spawners': load_images('tiles/spawners'),   

        }
        self.assets.update(Objects_assets)

    # def Asset_Enemy_List(self):
    #     Objects_assets = {
    #     }
    #     self.assets.update(Objects_assets)

    def Asset_Environment_List(self):
        Environment_assets = {
            'Lava_env' : get_tiles_from_sheet('environment/lava.png', 2, 0, 0, 0, 16, 16),
            'shallow_water_env' : get_tiles_from_sheet('environment/water.png', 2, 0, 32, 0, 16, 16),
            'medium_water_env' : get_tiles_from_sheet('environment/water.png', 2, 0, 32, 16, 16, 16),
            'deep_water_env' : get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 16, 16),
            'shallow_ice_env' : get_tiles_from_sheet('environment/water.png', 1, 0, 112, 0, 16, 16),
            'medium_ice_env' : get_tiles_from_sheet('environment/water.png', 1, 0, 112, 16, 16, 16),
            'deep_ice_env' : get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 16, 16),            
        }
        self.assets.update(Environment_assets)

    def Asset_Decoration_List(self):
        decoration_assets = {
        }
        self.assets.update(decoration_assets)


    def Asset_Potion_List(self):
        white = (255,255,255)

        potion_assets = {
            'empty_bottle' : get_tiles_from_sheet('Potions/Redpotions/empty.png', 0, 0, 0, 0, 16, 16, white),
            'red_full' : get_tiles_from_sheet('Potions/Redpotions/red_full.png', 2, 2, 0, 0, 16, 16, white),
            'red_half' : get_tiles_from_sheet('Potions/Redpotions/red_half.png', 2, 2, 0, 0, 16, 16, white),
            'red_low' : get_tiles_from_sheet('Potions/Redpotions/red_low.png', 2, 2, 0, 0, 16, 16, white),
            'blue_full' : get_tiles_from_sheet('Potions/Bluepotions/blue_full.png', 2, 2, 0, 0, 16, 16, white),
            'blue_half' : get_tiles_from_sheet('Potions/Bluepotions/blue_half.png', 2, 2, 0, 0, 16, 16, white),
            'blue_low' : get_tiles_from_sheet('Potions/Bluepotions/blue_low.png', 2, 2, 0, 0, 16, 16, white),
        }
        self.assets.update(potion_assets)
            
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

    