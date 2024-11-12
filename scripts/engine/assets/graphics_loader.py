import pygame
from scripts.engine.utility.utils import load_image, load_images, Animation, get_tiles_from_sheet

class Graphics_Loader:
    def Run_All(self):
        Graphics_Loader.Asset_Background_List(self)
        Graphics_Loader.Asset_Crypt_Tile_List(self)
        Graphics_Loader.Asset_Trap_List(self)
        Graphics_Loader.Asset_Effect_List(self)
        Graphics_Loader.Asset_Particles_List(self)
        Graphics_Loader.Asset_Dusty_Bones_List(self)
        Graphics_Loader.Asset_Fire_Spirit_List(self)
        Graphics_Loader.Asset_Ice_Spirit_List(self)
        Graphics_Loader.Wight_King_Spirit_List(self)
        Graphics_Loader.Asset_Spider_List(self)
        Graphics_Loader.Asset_Enemy_Symbols_List(self)
        Graphics_Loader.Asset_Player_List(self)
        Graphics_Loader.Asset_Interative_Objects_List(self)
        Graphics_Loader.Asset_Environment_List(self)
        Graphics_Loader.Asset_Objects_List(self)
        Graphics_Loader.Asset_Potion_List(self)
        Graphics_Loader.Asset_Decoration_List(self)
        Graphics_Loader.Asset_Weapons_List(self)
        Graphics_Loader.Asset_Inventory(self)
        Graphics_Loader.Asset_Font(self)
        Graphics_Loader.Asset_Loot(self)
        Graphics_Loader.Asset_Rune(self)

        
    def Asset_Background_List(self):
        background_assets = {'background': load_image('background.png'),}
        self.assets.update(background_assets)
        

    # def Asset_Tile_List(self):
    #     tiles_assets = {
    #         'wall' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 3, 0, 0, 128, 32, 32),
    #         'trapdoor' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 5, 0, 0, 256, 32, 32),
    #         'banner' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 2, 0, 0, 288, 32, 32),
    #         'stair' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 1, 0, 0, 320, 32, 32),
    #         'LeftWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 0, 5, 0, 0, 32, 32),
    #         'RightWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 0, 5, 160, 0, 32, 32),
    #         'TopWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 0, 32, 0, 32, 32),
    #         'BottomWall' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 0, 32, 64, 32, 32),
    #         'Floor' : get_tiles_from_sheet('tiles/dungeon/Dungeon_Tileset.png', 3, 2, 32, 32, 32, 32),
    #     }
    #     self.assets.update(tiles_assets)

    def Asset_Crypt_Tile_List(self):
        tiles_assets = {
            'floor' : get_tiles_from_sheet('crypt_assets/crypt_floor.png', 5, 1, 0, 0, 32, 32),
            'wall_top' : get_tiles_from_sheet('crypt_assets/wall_top.png', 3, 0, 0, 0, 32, 32),
            'wall_left' : get_tiles_from_sheet('crypt_assets/wall_left.png', 0, 3, 0, 0, 32, 32),
            'wall_right' : get_tiles_from_sheet('crypt_assets/wall_right.png', 0, 3, 0, 0, 32, 32),
            'wall_middle' : get_tiles_from_sheet('crypt_assets/wall_middle.png', 0, 3, 0, 0, 32, 32),
            'wall_bottom' : get_tiles_from_sheet('crypt_assets/wall_bottom.png', 3, 0, 0, 0, 32, 32),
            'wall_bottom_corner' : get_tiles_from_sheet('crypt_assets/wall_bottom_corner.png', 2, 0, 0, 0, 32, 32),
        }
        self.assets.update(tiles_assets)

    def Asset_Trap_List(self):
        white = (255,255,255)
        trap_assets = {
            'spike_trap' : get_tiles_from_sheet('tiles/dungeon/dungeon.png', 5, 0, 0, 112, 32, 32, white),
            'spike_poison_trap' : get_tiles_from_sheet('traps/Spike_Trap_poison.png', 13, 0, 0, 0, 32, 32, white),
            'Bear_trap' : get_tiles_from_sheet('traps/Bear_Trap.png', 3, 0, 0, 0, 32, 32, white),
            'Pit_trap' : get_tiles_from_sheet('traps/Pit_Trap_Spikes.png', 1, 0, 0, 0, 32, 32, white),
            'Top_trap' : get_tiles_from_sheet('traps/Push_Trap_Front.png', 10, 0, 0, 0, 32, 32, white),
            'Fire_trap' : get_tiles_from_sheet('traps/Fire_Trap.png', 13, 0, 0, 0, 32, 20, white),
            'spider_web' : get_tiles_from_sheet('entities/enemies/spider/spider_web.png', 3, 0, 0, 0, 32, 32),
        }

        self.assets.update(trap_assets)

    def Asset_Effect_List(self):
        white = (255,255,255)
        effect_assets = {
            'particle/leaf': Animation(load_images('particles/leaf'), img_dur=20, loop=False),
            'particle/particle': Animation(load_images('particles/particle'), img_dur=6, loop=False),
            'heart': load_image('heart.png'),
            'coin': get_tiles_from_sheet('coin_.png', 3, 0, 0, 0, 13, 13, white),
            'fire': get_tiles_from_sheet('particles/effects/fire/orange/loops/burning_loop_1.png', 7, 0, 0, 0, 32, 32, white),
            'poison': get_tiles_from_sheet('particles/effects/poison.png', 2, 0, 0, 0, 32, 32, white),
            'frozen': get_tiles_from_sheet('particles/effects/frozen.png', 2, 0, 0, 0, 32, 32, white),
            'wet': get_tiles_from_sheet('particles/effects/wet.png', 2, 0, 0, 0, 32, 32),
            'regen': get_tiles_from_sheet('particles/effects/regen.png', 2, 1, 0, 0, 32, 32),
        }
        self.assets.update(effect_assets)
    
    def Asset_Particles_List(self):
        particle_assets = {
        'fire_particle': get_tiles_from_sheet('particles/fire_particle/fire_particle.png', 3, 0, 0, 0, 2, 2),
        'ice_particle': get_tiles_from_sheet('particles/ice_particle/ice_particle.png', 3, 0, 0, 0, 2, 2),
        }
        self.assets.update(particle_assets)


    def Asset_Player_List(self):
        entities_assets = {

            'player_idle_down': get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 0, 32, 32),

            'player_idle_up': get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 0, 32, 32),
            
            'player_standing_still_down': get_tiles_from_sheet('entities/player/standing_still_down.png', 4, 0, 0, 0, 32, 32),

            'player_standing_still_up': get_tiles_from_sheet('entities/player/standing_still_up.png', 4, 0, 0, 0, 32, 32),

            'player_running_down': get_tiles_from_sheet('entities/player/running_down.png', 4, 0, 0, 0, 32, 32),

            'player_running_up': get_tiles_from_sheet('entities/player/running_up.png', 4, 0, 0, 0, 32, 32),
            

            'player_attack': get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 0, 32, 32),
        }
        
        self.assets.update(entities_assets)

    def Asset_Dusty_Bones_List(self):
        entities_assets = {
            'decrepit_bones': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones.png', 3, 0, 0, 0, 32, 32),

            'decrepit_bones_attack': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones_attack.png', 3, 0, 0, 0, 32, 32),

        }
        self.assets.update(entities_assets)

    def Asset_Fire_Spirit_List(self):
        entities_assets = {
            'fire_spirit_standing_still': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_idle.png', 3, 0, 0, 0, 32, 32),

            'fire_spirit_running': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_moving.png', 3, 0, 0, 0, 32, 32),

            'fire_spirit_attack': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_attacking.png', 3, 0, 0, 0, 32, 32),

        }
        self.assets.update(entities_assets)

    def Asset_Ice_Spirit_List(self):
        entities_assets = {
            'ice_spirit': get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),

            'ice_spirit_attack': get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Wight_King_Spirit_List(self):
        entities_assets = {
            'wight_king': get_tiles_from_sheet('entities/enemies/wight_king/wight_king.png', 4, 0, 0, 0, 40, 40),

            'wight_king_attack': get_tiles_from_sheet('entities/enemies/wight_king/wight_king_attack.png', 6, 0, 0, 0, 40, 40),
        }
        self.assets.update(entities_assets)

    def Asset_Spider_List(self):
        entities_assets = {
            'spider_idle': get_tiles_from_sheet('entities/enemies/spider/spider_idle.png', 4, 0, 0, 0, 32, 32),

            'spider_running': get_tiles_from_sheet('entities/enemies/spider/spider_running.png', 4, 0, 0, 0, 32, 32),

            'friendly_spider_idle': get_tiles_from_sheet('entities/enemies/spider/friendly_spider_idle.png', 4, 0, 0, 0, 32, 32),

            'friendly_spider_running': get_tiles_from_sheet('entities/enemies/spider/friendly_spider_running.png', 4, 0, 0, 0, 32, 32),

            'spider_attack': get_tiles_from_sheet('entities/enemies/spider/spider_attacking.png', 3, 0, 0, 0, 32, 32),

            'spider_jumping': get_tiles_from_sheet('entities/enemies/spider/spider_jumping.png', 8, 0, 0, 0, 32, 32),

            'spider_on_back': get_tiles_from_sheet('entities/enemies/spider/spider_on_back.png', 8, 0, 0, 0, 32, 32),

            
        }
        self.assets.update(entities_assets)

    def Asset_Enemy_Symbols_List(self):
        symbols_assets = {
            'exclamation_mark': get_tiles_from_sheet('entities/enemies/symbols/exclamation.png', 0, 0, 0, 0, 32, 32),
            'health_bar': get_tiles_from_sheet('entities/enemies/symbols/health_bar.png', 9, 0, 0, 0, 32, 32),
        }
        self.assets.update(symbols_assets)

    def Asset_Weapons_List(self):
        Weapons_assets = {
            'sword' : get_tiles_from_sheet('weapons/sword.png', 3, 0, 0, 0, 32, 32),
            'sword_attack' : get_tiles_from_sheet('weapons/sword_attack.png', 3, 0, 0, 0, 32, 32),
            
            'torch': get_tiles_from_sheet('weapons/torch.png', 8, 0, 0, 0, 32, 32),
            'torch_attack': get_tiles_from_sheet('weapons/torch_attack.png', 8, 0, 0, 0, 32, 32),
            
            'spear': get_tiles_from_sheet('weapons/spear.png', 8, 0, 0, 0, 32, 32),
            'spear_attack': get_tiles_from_sheet('weapons/spear.png', 8, 0, 0, 0, 32, 32),
            
            'bow': get_tiles_from_sheet('weapons/bow.png', 0, 0, 0, 0, 32, 32),
            'bow_attack': get_tiles_from_sheet('weapons/bow_attack.png', 2, 0, 0, 0, 32, 32),
            
            'arrow': get_tiles_from_sheet('weapons/arrow.png', 0, 0, 0, 0, 32, 32),
            'arrow_attack': get_tiles_from_sheet('weapons/arrow.png', 0, 0, 0, 0, 32, 32),

            'shield': get_tiles_from_sheet('weapons/shields.png', 4, 4, 0, 0, 32, 32),
            'shield_attack': get_tiles_from_sheet('weapons/shields.png', 4, 4, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)

    def Asset_Inventory(self):
        Weapon_Inventory_assets = {
            'sword_shield' : get_tiles_from_sheet('inventory/sword_shield.png', 2, 0, 0, 0, 34, 34),
            'duel_wield' : get_tiles_from_sheet('inventory/Duel_wield.png', 2, 0, 0, 0, 34, 34),
            'bow_arrow' : get_tiles_from_sheet('inventory/Bow_Arrow.png', 2, 0, 0, 0, 34, 34),
            'left_right' : get_tiles_from_sheet('inventory/left_right.png', 2, 0, 0, 0, 34, 34),
            'rune_background' : get_tiles_from_sheet('inventory/rune_background.png', 1, 0, 0, 0, 34, 34),
        }
        self.assets.update(Weapon_Inventory_assets)


    def Asset_Interative_Objects_List(self):
        white = (255,255,255)
        Objects_assets = {
            'Chest' : get_tiles_from_sheet('decoration/chest.png', 8, 0, 0, 0, 32, 32, white),
            'Door_Basic' : get_tiles_from_sheet('decoration/door/door_closed.png', 0, 0, 0, 0, 32, 32),
            'shrine' : get_tiles_from_sheet('decoration/shrine.png', 3, 0, 0, 0, 64, 64),
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
            'Lava_env' : get_tiles_from_sheet('environment/lava.png', 2, 0, 0, 0, 32, 32),
            'shallow_water_env' : get_tiles_from_sheet('environment/water.png', 2, 0, 32, 0, 32, 32),
            'medium_water_env' : get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            'deep_water_env' : get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            'shallow_ice_env' : get_tiles_from_sheet('environment/water.png', 1, 0, 112, 0, 32, 32),
            'medium_ice_env' : get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
            'deep_ice_env' : get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),            
        }
        self.assets.update(Environment_assets)

    def Asset_Decoration_List(self):
        decoration_assets = {
        }
        self.assets.update(decoration_assets)


    def Asset_Potion_List(self):

        potion_assets = {
            'empty_bottle' : get_tiles_from_sheet('Potions/Redpotions/empty.png', 0, 0, 0, 0, 32, 32,),
            
            'red_full' : get_tiles_from_sheet('Potions/Redpotions/red_full.png', 2, 2, 0, 0, 32, 32,),
            'red_half' : get_tiles_from_sheet('Potions/Redpotions/red_half.png', 2, 2, 0, 0, 32, 32,),
            'red_low' : get_tiles_from_sheet('Potions/Redpotions/red_low.png', 2, 2, 0, 0, 32, 32,),
            
            'blue_full' : get_tiles_from_sheet('Potions/Bluepotions/blue_full.png', 2, 2, 0, 0, 32, 32,),
            'blue_half' : get_tiles_from_sheet('Potions/Bluepotions/blue_half.png', 2, 2, 0, 0, 32, 32,),
            'blue_low' : get_tiles_from_sheet('Potions/Bluepotions/blue_low.png', 2, 2, 0, 0, 32, 32,),

            'yellow_full' : get_tiles_from_sheet('Potions/Yellowpotions/yellow_full.png', 2, 2, 0, 0, 32, 32,),
            'yellow_half' : get_tiles_from_sheet('Potions/Yellowpotions/yellow_half.png', 2, 2, 0, 0, 32, 32,),
            'yellow_low' : get_tiles_from_sheet('Potions/Yellowpotions/yellow_low.png', 2, 2, 0, 0, 32, 32,),

            'green_full' : get_tiles_from_sheet('Potions/Greenpotions/green_full.png', 2, 2, 0, 0, 32, 32,),
            'green_half' : get_tiles_from_sheet('Potions/Greenpotions/green_half.png', 2, 2, 0, 0, 32, 32,),
            'green_low' : get_tiles_from_sheet('Potions/Greenpotions/green_low.png', 2, 2, 0, 0, 32, 32,),

            'dark_green_full' : get_tiles_from_sheet('Potions/Darkgreenpotions/dark_green_full.png', 2, 2, 0, 0, 32, 32,),
            'dark_green_half' : get_tiles_from_sheet('Potions/Darkgreenpotions/dark_green_half.png', 2, 2, 0, 0, 32, 32,),
            'dark_green_low' : get_tiles_from_sheet('Potions/Darkgreenpotions/dark_green_low.png', 2, 2, 0, 0, 32, 32,),

            'swamp_green_full' : get_tiles_from_sheet('Potions/SwampGreenpotions/swamp_green_full.png', 2, 2, 0, 0, 32, 32,),
            'swamp_green_half' : get_tiles_from_sheet('Potions/SwampGreenpotions/swamp_green_half.png', 2, 2, 0, 0, 32, 32,),
            'swamp_green_low' : get_tiles_from_sheet('Potions/SwampGreenpotions/swamp_green_low.png', 2, 2, 0, 0, 32, 32,),

            'purple_full' : get_tiles_from_sheet('Potions/Purplepotions/Purple_full.png', 2, 2, 0, 0, 32, 32,),
            'purple_half' : get_tiles_from_sheet('Potions/Purplepotions/Purple_half.png', 2, 2, 0, 0, 32, 32,),
            'purple_low' : get_tiles_from_sheet('Potions/Purplepotions/Purple_low.png', 2, 2, 0, 0, 32, 32,),

            'light_blue_full' : get_tiles_from_sheet('Potions/LightBluepotions/lightblue_full.png', 2, 2, 0, 0, 32, 32,),
            'light_blue_half' : get_tiles_from_sheet('Potions/LightBluepotions/lightblue_half.png', 2, 2, 0, 0, 32, 32,),
            'light_blue_low' : get_tiles_from_sheet('Potions/LightBluepotions/lightblue_low.png', 2, 2, 0, 0, 32, 32,),

            'light_grey_full' : get_tiles_from_sheet('Potions/LightGreypotions/light_grey_full.png', 2, 2, 0, 0, 32, 32,),
            'light_grey_half' : get_tiles_from_sheet('Potions/LightGreypotions/light_grey_half.png', 2, 2, 0, 0, 32, 32,),
            'light_grey_low' : get_tiles_from_sheet('Potions/LightGreypotions/light_grey_low.png', 2, 2, 0, 0, 32, 32,),

            'pink_full' : get_tiles_from_sheet('Potions/Pinkpotions/pink_full.png', 2, 2, 0, 0, 32, 32,),
            'pink_half' : get_tiles_from_sheet('Potions/Pinkpotions/pink_half.png', 2, 2, 0, 0, 32, 32,),
            'pink_low' : get_tiles_from_sheet('Potions/Pinkpotions/pink_low.png', 2, 2, 0, 0, 32, 32,),

            'dark_red_full' : get_tiles_from_sheet('Potions/DarkRedpotions/darkred_full.png', 2, 2, 0, 0, 32, 32,),
            'dark_red_half' : get_tiles_from_sheet('Potions/DarkRedpotions/darkred_half.png', 2, 2, 0, 0, 32, 32,),
            'dark_red_low' : get_tiles_from_sheet('Potions/DarkRedpotions/darkred_low.png', 2, 2, 0, 0, 32, 32,),

            'fire_resistance_full' : get_tiles_from_sheet('Potions/Firepotions/fire_resistance_potion_full.png', 2, 2, 0, 0, 32, 32,),
            'fire_resistance_half' : get_tiles_from_sheet('Potions/Firepotions/fire_resistance_potion_half.png', 2, 2, 0, 0, 32, 32,),
            'fire_resistance_low' : get_tiles_from_sheet('Potions/Firepotions/fire_resistance_potion_low.png', 2, 2, 0, 0, 32, 32,),
        }
        self.assets.update(potion_assets)

    def Asset_Loot(self):
        loot = {
            'gold' : get_tiles_from_sheet('loot/gold_coins.png', 3, 0, 0, 0, 16, 16),
            'key' : get_tiles_from_sheet('loot/key.png', 0, 0, 0, 0, 16, 16),
        }
        self.assets.update(loot)

    def Asset_Rune(self):
        rune = {
            'healing_rune' : get_tiles_from_sheet('runes/healing_rune.png', 1, 0, 0, 0, 32, 32),
            'regen_rune' : get_tiles_from_sheet('runes/regen_rune.png', 1, 0, 0, 0, 32, 32),
            'dash_rune' : get_tiles_from_sheet('runes/dash_rune.png', 1, 0, 0, 0, 32, 32),
            'arcane_conduit_rune' : get_tiles_from_sheet('runes/arcane_conduit_rune.png', 1, 0, 0, 0, 32, 32),
            'fire_cirlce_rune' : get_tiles_from_sheet('runes/fire_rune_cirlce.png', 1, 0, 0, 0, 32, 32),
            'fire_resistance_rune' : get_tiles_from_sheet('runes/fire_rune_resistance.png', 1, 0, 0, 0, 32, 32),
            'fire_shield_rune' : get_tiles_from_sheet('runes/fire_rune_shield.png', 1, 0, 0, 0, 32, 32),
            'fire_spray_rune' : get_tiles_from_sheet('runes/fire_rune_spray.png', 1, 0, 0, 0, 32, 32),
            'freeze_circle_rune' : get_tiles_from_sheet('runes/frost_rune_circle.png', 1, 0, 0, 0, 32, 32),
            'freeze_resistance_rune' : get_tiles_from_sheet('runes/frost_rune_resistance.png', 1, 0, 0, 0, 32, 32),
            'freeze_shield_rune' : get_tiles_from_sheet('runes/frost_rune_shield.png', 1, 0, 0, 0, 32, 32),
            'freeze_spray_rune' : get_tiles_from_sheet('runes/frost_rune_spray.png', 1, 0, 0, 0, 32, 32),
            'invisibility_rune' : get_tiles_from_sheet('runes/invisibility_rune.png', 1, 0, 0, 0, 32, 32),
            'key_rune' : get_tiles_from_sheet('runes/key_rune.png', 1, 0, 0, 0, 32, 32),
            'light_rune' : get_tiles_from_sheet('runes/light_rune.png', 1, 0, 0, 0, 32, 32),
            'resistance_rune' : get_tiles_from_sheet('runes/resistance_rune.png', 1, 0, 0, 0, 32, 32),
            'shield_rune' : get_tiles_from_sheet('runes/shield_rune.png', 1, 0, 0, 0, 32, 32),
            'silence_rune' : get_tiles_from_sheet('runes/silence_rune.png', 1, 0, 0, 0, 32, 32),
            'speed_rune' : get_tiles_from_sheet('runes/speed_rune.png', 1, 0, 0, 0, 32, 32),
            'strength_rune' : get_tiles_from_sheet('runes/strength_rune.png', 1, 0, 0, 0, 32, 32),
            'vampiric_rune' : get_tiles_from_sheet('runes/vampiric_rune.png', 1, 0, 0, 0, 32, 32),
        }
        self.assets.update(rune)

    def Asset_Font(self):
        font = {
            'font' : get_tiles_from_sheet('font/font.png', 7, 5, 0, 0, 16, 16),
            'player_damage_font' : get_tiles_from_sheet('font/player_damage_font.png', 7, 5, 0, 0, 16, 16),
            'symbols' : get_tiles_from_sheet('font/symbols.png', 7, 2, 0, 0, 16, 16),
            'souls' : get_tiles_from_sheet('font/souls.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(font)
