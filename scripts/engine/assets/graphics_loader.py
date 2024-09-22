import pygame
from scripts.engine.utility.utils import load_image, load_images, Animation, get_tiles_from_sheet

class Graphics_Loader:
    def Run_All(self):
        Graphics_Loader.Asset_Background_List(self)
        Graphics_Loader.Asset_Tile_List(self)
        Graphics_Loader.Asset_Trap_List(self)
        Graphics_Loader.Asset_Effect_List(self)
        Graphics_Loader.Asset_Particles_List(self)
        Graphics_Loader.Asset_Dusty_Bones_List(self)
        Graphics_Loader.Asset_Fire_Spirit_List(self)
        Graphics_Loader.Asset_Ice_Spirit_List(self)
        Graphics_Loader.Asset_Spider_List(self)
        Graphics_Loader.Asset_Enemy_Symbols_List(self)
        Graphics_Loader.Asset_Player_List(self)
        Graphics_Loader.Asset_Interative_Objects_List(self)
        Graphics_Loader.Asset_Environment_List(self)
        Graphics_Loader.Asset_Objects_List(self)
        Graphics_Loader.Asset_Potion_List(self)
        Graphics_Loader.Asset_Decoration_List(self)
        Graphics_Loader.Asset_Weapons_List(self)
        Graphics_Loader.Asset_Weapon_Inventory(self)
        Graphics_Loader.Asset_Font(self)
        Graphics_Loader.Asset_Loot(self)

        
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
            'spider_web' : get_tiles_from_sheet('entities/enemies/spider/spider_web.png', 3, 0, 0, 0, 16, 16),
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
            'wet': get_tiles_from_sheet('particles/effects/wet.png', 2, 0, 0, 0, 16, 16),
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

            'player_idle_down_head': get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 0, 16, 8),
            'player_idle_down_body': get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 9, 16, 6),
            'player_idle_down_legs': get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 15, 16, 2),

            'player_idle_up_head': get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 0, 16, 8),
            'player_idle_up_body': get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 9, 16, 6),
            'player_idle_up_legs': get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 15, 16, 2),
            
            'player_standing_still_down_head': get_tiles_from_sheet('entities/player/standing_still_down.png', 4, 0, 0, 0, 16, 8),
            'player_standing_still_down_body': get_tiles_from_sheet('entities/player/standing_still_down.png', 4, 0, 0, 9, 16, 6),
            'player_standing_still_down_legs': get_tiles_from_sheet('entities/player/standing_still_down.png', 4, 0, 0, 15, 16, 3),

            'player_standing_still_up_head': get_tiles_from_sheet('entities/player/standing_still_up.png', 4, 0, 0, 0, 16, 8),
            'player_standing_still_up_body': get_tiles_from_sheet('entities/player/standing_still_up.png', 4, 0, 0, 9, 16, 6),
            'player_standing_still_up_legs': get_tiles_from_sheet('entities/player/standing_still_up.png', 4, 0, 0, 15, 16, 2),

            'player_running_down_head': get_tiles_from_sheet('entities/player/running_down.png', 4, 0, 0, 0, 16, 8),
            'player_running_down_body': get_tiles_from_sheet('entities/player/running_down.png', 4, 0, 0, 9, 16, 6),
            'player_running_down_legs': get_tiles_from_sheet('entities/player/running_down.png', 4, 0, 0, 15, 16, 2),

            'player_running_up_head': get_tiles_from_sheet('entities/player/running_up.png', 4, 0, 0, 0, 16, 8),
            'player_running_up_body': get_tiles_from_sheet('entities/player/running_up.png', 4, 0, 0, 9, 16, 6),
            'player_running_up_legs': get_tiles_from_sheet('entities/player/running_up.png', 4, 0, 0, 15, 16, 2),
            

            'player_attack_head': get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 0, 16, 8),
            'player_attack_body': get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 9, 16, 6),
            'player_attack_legs': get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 15, 16, 2),


            'gun': load_image('gun.png'),
            'projectile': load_image('projectile.png'),
        }
        self.assets.update(entities_assets)

    def Asset_Dusty_Bones_List(self):
        entities_assets = {
            'decrepit_bones_head': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones.png', 3, 0, 0, 0, 16, 8),
            'decrepit_bones_body': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones.png', 3, 0, 0, 9, 16, 6),
            'decrepit_bones_legs': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones.png', 3, 0, 0, 15, 16, 2),

            'decrepit_bones_attack_head': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones_attack.png', 3, 0, 0, 0, 16, 8),
            'decrepit_bones_attack_body': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones_attack.png', 3, 0, 0, 9, 16, 6),
            'decrepit_bones_attack_legs': get_tiles_from_sheet('entities/enemies/BasicUndeadAnimations/DecrepitBones/DecrepitBones_attack.png', 3, 0, 0, 15, 16, 2),

        }
        self.assets.update(entities_assets)

    def Asset_Fire_Spirit_List(self):
        entities_assets = {
            'fire_spirit_standing_still_head': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_idle.png', 3, 0, 0, 0, 16, 8),
            'fire_spirit_standing_still_body': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_idle.png', 3, 0, 0, 9, 16, 6),
            'fire_spirit_standing_still_legs': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_idle.png', 3, 0, 0, 15, 16, 2),

            'fire_spirit_running_head': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_moving.png', 3, 0, 0, 0, 16, 8),
            'fire_spirit_running_body': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_moving.png', 3, 0, 0, 9, 16, 6),
            'fire_spirit_running_legs': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_moving.png', 3, 0, 0, 15, 16, 2),

            'fire_spirit_attack_head': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_attacking.png', 3, 0, 0, 0, 16, 8),
            'fire_spirit_attack_body': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_attacking.png', 3, 0, 0, 9, 16, 6),
            'fire_spirit_attack_legs': get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_attacking.png', 3, 0, 0, 15, 16, 2),

        }
        self.assets.update(entities_assets)

    def Asset_Ice_Spirit_List(self):
        entities_assets = {
            'ice_spirit_head': get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 16, 8),
            'ice_spirit_body': get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 9, 16, 6),
            'ice_spirit_legs': get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 15, 16, 2),

            'ice_spirit_attack_head': get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 16, 8),
            'ice_spirit_attack_body': get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 9, 16, 6),
            'ice_spirit_attack_legs': get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 15, 16, 2),
        }
        self.assets.update(entities_assets)

    def Asset_Spider_List(self):
        entities_assets = {
            'spider_idle_head': get_tiles_from_sheet('entities/enemies/spider/spider_idle.png', 4, 0, 0, 0, 16, 8),
            'spider_idle_body': get_tiles_from_sheet('entities/enemies/spider/spider_idle.png', 4, 0, 0, 9, 16, 6),
            'spider_idle_legs': get_tiles_from_sheet('entities/enemies/spider/spider_idle.png', 4, 0, 0, 15, 16, 2),

            'spider_running_head': get_tiles_from_sheet('entities/enemies/spider/spider_running.png', 4, 0, 0, 0, 16, 8),
            'spider_running_body': get_tiles_from_sheet('entities/enemies/spider/spider_running.png', 4, 0, 0, 9, 16, 6),
            'spider_running_legs': get_tiles_from_sheet('entities/enemies/spider/spider_running.png', 4, 0, 0, 15, 16, 2),

            'friendly_spider_idle_head': get_tiles_from_sheet('entities/enemies/spider/friendly_spider_idle.png', 4, 0, 0, 0, 16, 8),
            'friendly_spider_idle_body': get_tiles_from_sheet('entities/enemies/spider/friendly_spider_idle.png', 4, 0, 0, 9, 16, 6),
            'friendly_spider_idle_legs': get_tiles_from_sheet('entities/enemies/spider/friendly_spider_idle.png', 4, 0, 0, 15, 16, 2),

            'friendly_spider_running_head': get_tiles_from_sheet('entities/enemies/spider/friendly_spider_running.png', 4, 0, 0, 0, 16, 8),
            'friendly_spider_running_body': get_tiles_from_sheet('entities/enemies/spider/friendly_spider_running.png', 4, 0, 0, 9, 16, 6),
            'friendly_spider_running_legs': get_tiles_from_sheet('entities/enemies/spider/friendly_spider_running.png', 4, 0, 0, 15, 16, 2),

            'spider_attack_head': get_tiles_from_sheet('entities/enemies/spider/spider_attacking.png', 3, 0, 0, 0, 16, 8),
            'spider_attack_body': get_tiles_from_sheet('entities/enemies/spider/spider_attacking.png', 3, 0, 0, 9, 16, 6),
            'spider_attack_legs': get_tiles_from_sheet('entities/enemies/spider/spider_attacking.png', 3, 0, 0, 15, 16, 2),

            'spider_jumping_head': get_tiles_from_sheet('entities/enemies/spider/spider_jumping.png', 8, 0, 0, 0, 16, 8),
            'spider_jumping_body': get_tiles_from_sheet('entities/enemies/spider/spider_jumping.png', 8, 0, 0, 9, 16, 6),
            'spider_jumping_legs': get_tiles_from_sheet('entities/enemies/spider/spider_jumping.png', 8, 0, 0, 15, 16, 2),

            'spider_on_back_head': get_tiles_from_sheet('entities/enemies/spider/spider_on_back.png', 8, 0, 0, 0, 16, 8),
            'spider_on_back_body': get_tiles_from_sheet('entities/enemies/spider/spider_on_back.png', 8, 0, 0, 9, 16, 6),
            'spider_on_back_legs': get_tiles_from_sheet('entities/enemies/spider/spider_on_back.png', 8, 0, 0, 15, 16, 2),
        }
        self.assets.update(entities_assets)

    def Asset_Enemy_Symbols_List(self):
        symbols_assets = {
            'exclamation_mark': get_tiles_from_sheet('entities/enemies/symbols/exclamation.png', 0, 0, 0, 0, 16, 16),
            'health_bar': get_tiles_from_sheet('entities/enemies/symbols/health_bar.png', 9, 0, 0, 0, 16, 16),
        }
        self.assets.update(symbols_assets)

    def Asset_Weapons_List(self):
        Weapons_assets = {
            'sword' : get_tiles_from_sheet('weapons/sword.png', 3, 0, 0, 0, 16, 16),
            'sword_attack' : get_tiles_from_sheet('weapons/sword_attack.png', 3, 0, 0, 0, 16, 16),
            
            'torch': get_tiles_from_sheet('weapons/torch.png', 8, 0, 0, 0, 16, 16),
            'torch_attack': get_tiles_from_sheet('weapons/torch_attack.png', 8, 0, 0, 0, 16, 16),
            
            'spear': get_tiles_from_sheet('weapons/spear.png', 8, 0, 0, 0, 16, 16),
            'spear_attack': get_tiles_from_sheet('weapons/spear.png', 8, 0, 0, 0, 16, 16),
            
            'bow': get_tiles_from_sheet('weapons/bow.png', 0, 0, 0, 0, 16, 16),
            'bow_attack': get_tiles_from_sheet('weapons/bow_attack.png', 2, 0, 0, 0, 16, 16),
            
            'arrow': get_tiles_from_sheet('weapons/arrow.png', 0, 0, 0, 0, 16, 16),
            'arrow_attack': get_tiles_from_sheet('weapons/arrow.png', 0, 0, 0, 0, 16, 16),

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
            'empty_bottle' : get_tiles_from_sheet('Potions/Redpotions/empty.png', 0, 0, 0, 0, 16, 16,),
            
            'red_full' : get_tiles_from_sheet('Potions/Redpotions/red_full.png', 2, 2, 0, 0, 16, 16,),
            'red_half' : get_tiles_from_sheet('Potions/Redpotions/red_half.png', 2, 2, 0, 0, 16, 16,),
            'red_low' : get_tiles_from_sheet('Potions/Redpotions/red_low.png', 2, 2, 0, 0, 16, 16,),
            
            'blue_full' : get_tiles_from_sheet('Potions/Bluepotions/blue_full.png', 2, 2, 0, 0, 16, 16,),
            'blue_half' : get_tiles_from_sheet('Potions/Bluepotions/blue_half.png', 2, 2, 0, 0, 16, 16,),
            'blue_low' : get_tiles_from_sheet('Potions/Bluepotions/blue_low.png', 2, 2, 0, 0, 16, 16,),

            'yellow_full' : get_tiles_from_sheet('Potions/Yellowpotions/yellow_full.png', 2, 2, 0, 0, 16, 16,),
            'yellow_half' : get_tiles_from_sheet('Potions/Yellowpotions/yellow_half.png', 2, 2, 0, 0, 16, 16,),
            'yellow_low' : get_tiles_from_sheet('Potions/Yellowpotions/yellow_low.png', 2, 2, 0, 0, 16, 16,),

            'green_full' : get_tiles_from_sheet('Potions/Greenpotions/Green_full.png', 2, 2, 0, 0, 16, 16,),
            'green_half' : get_tiles_from_sheet('Potions/Greenpotions/Green_half.png', 2, 2, 0, 0, 16, 16,),
            'green_low' : get_tiles_from_sheet('Potions/Greenpotions/Green_low.png', 2, 2, 0, 0, 16, 16,),

            'purple_full' : get_tiles_from_sheet('Potions/Purplepotions/Purple_full.png', 2, 2, 0, 0, 16, 16,),
            'purple_half' : get_tiles_from_sheet('Potions/Purplepotions/Purple_half.png', 2, 2, 0, 0, 16, 16,),
            'purple_low' : get_tiles_from_sheet('Potions/Purplepotions/Purple_low.png', 2, 2, 0, 0, 16, 16,),

            'light_blue_full' : get_tiles_from_sheet('Potions/LightBluepotions/lightblue_full.png', 2, 2, 0, 0, 16, 16,),
            'light_blue_half' : get_tiles_from_sheet('Potions/LightBluepotions/lightblue_half.png', 2, 2, 0, 0, 16, 16,),
            'light_blue_low' : get_tiles_from_sheet('Potions/LightBluepotions/lightblue_low.png', 2, 2, 0, 0, 16, 16,),

            'pink_full' : get_tiles_from_sheet('Potions/Pinkpotions/pink_full.png', 2, 2, 0, 0, 16, 16,),
            'pink_half' : get_tiles_from_sheet('Potions/Pinkpotions/pink_half.png', 2, 2, 0, 0, 16, 16,),
            'pink_low' : get_tiles_from_sheet('Potions/Pinkpotions/pink_low.png', 2, 2, 0, 0, 16, 16,),

            'dark_red_full' : get_tiles_from_sheet('Potions/DarkRedpotions/darkred_full.png', 2, 2, 0, 0, 16, 16,),
            'dark_red_half' : get_tiles_from_sheet('Potions/DarkRedpotions/darkred_half.png', 2, 2, 0, 0, 16, 16,),
            'dark_red_low' : get_tiles_from_sheet('Potions/DarkRedpotions/darkred_low.png', 2, 2, 0, 0, 16, 16,),
        }
        self.assets.update(potion_assets)

    def Asset_Loot(self):
        loot = {
            'gold_coins' : get_tiles_from_sheet('loot/gold_coins.png', 3, 0, 0, 0, 8, 8),
        }
        self.assets.update(loot)

    def Asset_Font(self):
        font = {
            'font' : get_tiles_from_sheet('font/font.png', 7, 5, 0, 0, 8, 8),
            'symbols' : get_tiles_from_sheet('font/symbols.png', 7, 1, 0, 0, 8, 8),
            'souls' : get_tiles_from_sheet('font/souls.png', 3, 0, 0, 0, 16, 16),
        }
        self.assets.update(font)
