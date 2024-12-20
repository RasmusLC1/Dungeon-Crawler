import pygame
from scripts.engine.utility.utils import load_image, load_images, Animation, get_tiles_from_sheet

class Graphics_Loader:
    def Run_All(self):
        Graphics_Loader.Asset_Background_List(self)
        Graphics_Loader.Asset_Crypt_Tile_List(self)
        Graphics_Loader.Asset_Trap_List(self)
        Graphics_Loader.Asset_Effect_List(self)
        Graphics_Loader.Asset_Magic_Attack_List(self)
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
        Graphics_Loader.Asset_Weapons_Effects(self)
        Graphics_Loader.Asset_Inventory(self)
        Graphics_Loader.Asset_Font(self)
        Graphics_Loader.Asset_Loot(self)
        Graphics_Loader.Asset_Rune(self)
        Graphics_Loader.Asset_Menu(self)

        
    def Asset_Background_List(self):
        background_assets = {'background': load_image('background.png'),}
        self.assets.update(background_assets)
        

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
            'electric': get_tiles_from_sheet('particles/effects/electric.png', 5, 0, 0, 0, 32, 32),
            'invincible': get_tiles_from_sheet('particles/effects/invincible.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(effect_assets)
    
    def Asset_Magic_Attack_List(self):
        particle_assets = {
        'fire_particle': get_tiles_from_sheet('weapons/magic_attacks/fire/fire_particle.png', 3, 0, 0, 0, 4, 4),
        'fire_ball': get_tiles_from_sheet('weapons/magic_attacks/fire/fire_ball.png', 0, 0, 0, 0, 16, 16),
        'fire_explosion': get_tiles_from_sheet('weapons/magic_attacks/fire/fire_explosion.png', 7, 0, 0, 0, 32, 32),

        'ice_particle': get_tiles_from_sheet('weapons/magic_attacks/ice/ice_particle.png', 3, 0, 0, 0, 4, 4),
        'ice_ball': get_tiles_from_sheet('weapons/magic_attacks/ice/ice_ball.png', 0, 0, 0, 0, 16, 16),
        'ice_explosion': get_tiles_from_sheet('weapons/magic_attacks/ice/ice_explosion.png', 5, 0, 0, 0, 32, 32),

        'poison_particle': get_tiles_from_sheet('weapons/magic_attacks/poison/poison_particle.png', 3, 0, 0, 0, 4, 4),
        'poison_ball': get_tiles_from_sheet('weapons/magic_attacks/poison/poison_ball.png', 0, 0, 0, 0, 16, 16),
        'poison_explosion': get_tiles_from_sheet('weapons/magic_attacks/poison/poison_explosion.png', 5, 0, 0, 0, 32, 32),


        'electric_particle': get_tiles_from_sheet('weapons/magic_attacks/electric/electric_particle.png', 0, 0, 0, 0, 16, 16),
        'electric_ball': get_tiles_from_sheet('weapons/magic_attacks/electric/electric_ball.png', 0, 0, 0, 0, 16, 16),
        'electric_explosion': get_tiles_from_sheet('weapons/magic_attacks/electric/electric_explosion.png', 5, 0, 0, 0, 32, 32),
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
            'sword' : get_tiles_from_sheet('weapons/sword/sword.png', 3, 0, 0, 0, 32, 32),
            'sword_attack_cut' : get_tiles_from_sheet('weapons/sword/sword.png', 3, 0, 0, 0, 32, 32),
            'sword_attack_stab' : get_tiles_from_sheet('weapons/sword/sword_attack.png', 3, 0, 0, 0, 32, 32),
            
            'torch': get_tiles_from_sheet('weapons/torch/torch.png', 8, 0, 0, 0, 32, 32),
            'torch_attack_cut': get_tiles_from_sheet('weapons/torch/torch_attack.png', 8, 0, 0, 0, 32, 32),
            
            'spear': get_tiles_from_sheet('weapons/spear/spear.png', 8, 0, 0, 0, 32, 32),
            'spear_attack_stab': get_tiles_from_sheet('weapons/spear/spear.png', 8, 0, 0, 0, 32, 32),
            
            'bow': get_tiles_from_sheet('weapons/bow/bow.png', 0, 0, 0, 0, 32, 32),
            'bow_attack': get_tiles_from_sheet('weapons/bow/bow_attack.png', 2, 0, 0, 0, 32, 32),
            
            'arrow': get_tiles_from_sheet('weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),
            'arrow_attack': get_tiles_from_sheet('weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),

            'shield': get_tiles_from_sheet('weapons/shield/shields.png', 4, 4, 0, 0, 32, 32),
            'shield_attack': get_tiles_from_sheet('weapons/shield/shields.png', 4, 4, 0, 0, 32, 32),

            'halberd': get_tiles_from_sheet('weapons/halberd/halberd.png', 6, 0, 0, 0, 32, 32),
            'halberd_attack_stab': get_tiles_from_sheet('weapons/halberd/halberd_stab_attack.png', 6, 0, 0, 0, 32, 50),
            'halberd_attack_cut': get_tiles_from_sheet('weapons/halberd/halberd_cut_attack.png', 13, 0, 0, 0, 32, 32),

            'battle_axe': get_tiles_from_sheet('weapons/battle_axe/battle_axe.png', 5, 0, 0, 0, 32, 32),
            'battle_axe_attack_cut': get_tiles_from_sheet('weapons/battle_axe/battle_axe_cut_attack.png', 15, 0, 0, 0, 32, 32),
            
            'hammer': get_tiles_from_sheet('weapons/hammer/hammer.png', 6, 0, 0, 0, 32, 32),
            'hammer_attack_cut': get_tiles_from_sheet('weapons/hammer/hammer_cut_attack.png', 9, 0, 0, 0, 32, 32),

            'hatchet': get_tiles_from_sheet('weapons/hatchet/hatchet.png', 7, 0, 0, 0, 32, 32),
            'hatchet_attack_cut': get_tiles_from_sheet('weapons/hatchet/hatchet_cut_attack.png', 8, 0, 0, 0, 32, 32),

            'warhammer': get_tiles_from_sheet('weapons/warhammer/warhammer.png', 6, 0, 0, 0, 32, 32),
            'warhammer_attack_cut': get_tiles_from_sheet('weapons/warhammer/warhammer_cut_attack.png', 12, 0, 0, 0, 32, 32),

            'crossbow': get_tiles_from_sheet('weapons/crossbow/crossbow.png', 8, 0, 0, 0, 32, 32),
            'crossbow_attack': get_tiles_from_sheet('weapons/crossbow/crossbow_attack.png', 2, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)

    def Asset_Weapons_Effects(self):
        Weapons_assets = {
            'slash_cut_effect' : get_tiles_from_sheet('weapons/weapon_effects/slash_cut_attack.png', 6, 0, 0, 0, 64, 64),
            'slash_stab_effect' : get_tiles_from_sheet('weapons/weapon_effects/slash_stab_attack.png', 6, 0, 0, 0, 64, 64),
            'slash_spin_effect' : get_tiles_from_sheet('weapons/weapon_effects/slash_spin_attack.png', 7, 0, 0, 0, 64, 64),
            'slash_smash_effect' : get_tiles_from_sheet('weapons/weapon_effects/slash_smash_attack.png', 5, 0, 0, 0, 64, 64),

            'blunt_cut_effect' : get_tiles_from_sheet('weapons/weapon_effects/blunt_cut_attack.png', 6, 0, 0, 0, 64, 64),
            'blunt_stab_effect' : get_tiles_from_sheet('weapons/weapon_effects/blunt_stab_attack.png', 6, 0, 0, 0, 64, 64),
            'blunt_spin_effect' : get_tiles_from_sheet('weapons/weapon_effects/blunt_spin_attack.png', 7, 0, 0, 0, 64, 64),
            'blunt_smash_effect' : get_tiles_from_sheet('weapons/weapon_effects/blunt_smash_attack.png', 5, 0, 0, 0, 64, 64),

            'electric_cut_effect' : get_tiles_from_sheet('weapons/weapon_effects/electric_cut_attack.png', 6, 0, 0, 0, 64, 64),
            'electric_stab_effect' : get_tiles_from_sheet('weapons/weapon_effects/electric_stab_attack.png', 6, 0, 0, 0, 64, 64),
            'electric_spin_effect' : get_tiles_from_sheet('weapons/weapon_effects/electric_spin_attack.png', 7, 0, 0, 0, 64, 64),
            'electric_smash_effect' : get_tiles_from_sheet('weapons/weapon_effects/electric_smash_attack.png', 5, 0, 0, 0, 64, 64),

            'fire_cut_effect' : get_tiles_from_sheet('weapons/weapon_effects/fire_cut_attack.png', 6, 0, 0, 0, 64, 64),
            'fire_stab_effect' : get_tiles_from_sheet('weapons/weapon_effects/fire_stab_attack.png', 6, 0, 0, 0, 64, 64),
            'fire_spin_effect' : get_tiles_from_sheet('weapons/weapon_effects/fire_spin_attack.png', 7, 0, 0, 0, 64, 64),
            'fire_smash_effect' : get_tiles_from_sheet('weapons/weapon_effects/fire_smash_attack.png', 5, 0, 0, 0, 64, 64),

            'frozen_cut_effect' : get_tiles_from_sheet('weapons/weapon_effects/frozen_cut_attack.png', 6, 0, 0, 0, 64, 64),
            'frozen_stab_effect' : get_tiles_from_sheet('weapons/weapon_effects/frozen_stab_attack.png', 6, 0, 0, 0, 64, 64),
            'frozen_spin_effect' : get_tiles_from_sheet('weapons/weapon_effects/frozen_spin_attack.png', 7, 0, 0, 0, 64, 64),
            'frozen_smash_effect' : get_tiles_from_sheet('weapons/weapon_effects/frozen_smash_attack.png', 5, 0, 0, 0, 64, 64),

            'poison_cut_effect' : get_tiles_from_sheet('weapons/weapon_effects/poison_cut_attack.png', 6, 0, 0, 0, 64, 64),
            'poison_stab_effect' : get_tiles_from_sheet('weapons/weapon_effects/poison_stab_attack.png', 6, 0, 0, 0, 64, 64),
            'poison_spin_effect' : get_tiles_from_sheet('weapons/weapon_effects/poison_spin_attack.png', 7, 0, 0, 0, 64, 64),
            'poison_smash_effect' : get_tiles_from_sheet('weapons/weapon_effects/poison_smash_attack.png', 5, 0, 0, 0, 64, 64),

            'regen_cut_effect' : get_tiles_from_sheet('weapons/weapon_effects/regen_cut_attack.png', 6, 0, 0, 0, 64, 64),
            'regen_stab_effect' : get_tiles_from_sheet('weapons/weapon_effects/regen_stab_attack.png', 6, 0, 0, 0, 64, 64),
            'regen_spin_effect' : get_tiles_from_sheet('weapons/weapon_effects/regen_spin_attack.png', 7, 0, 0, 0, 64, 64),
            'regen_smash_effect' : get_tiles_from_sheet('weapons/weapon_effects/regen_smash_attack.png', 5, 0, 0, 0, 64, 64),

            'vampiric_cut_effect' : get_tiles_from_sheet('weapons/weapon_effects/vampiric_cut_attack.png', 6, 0, 0, 0, 64, 64),
            'vampiric_stab_effect' : get_tiles_from_sheet('weapons/weapon_effects/vampiric_stab_attack.png', 6, 0, 0, 0, 64, 64),
            'vampiric_spin_effect' : get_tiles_from_sheet('weapons/weapon_effects/vampiric_spin_attack.png', 7, 0, 0, 0, 64, 64),
            'vampiric_smash_effect' : get_tiles_from_sheet('weapons/weapon_effects/vampiric_smash_attack.png', 5, 0, 0, 0, 64, 64),
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
            'empty_bottle' : get_tiles_from_sheet('Potions/Healing_potions/empty.png', 0, 0, 0, 0, 32, 32,),
            
            'healing_full' : get_tiles_from_sheet('Potions/Healing_potions/healing_full.png', 2, 2, 0, 0, 32, 32,),
            'healing_half' : get_tiles_from_sheet('Potions/Healing_potions/healing_half.png', 2, 2, 0, 0, 32, 32,),
            'healing_low' : get_tiles_from_sheet('Potions/Healing_potions/healing_low.png', 2, 2, 0, 0, 32, 32,),
            
            'soul_full' : get_tiles_from_sheet('Potions/soul_potions/soul_full.png', 2, 2, 0, 0, 32, 32,),
            'soul_half' : get_tiles_from_sheet('Potions/soul_potions/soul_half.png', 2, 2, 0, 0, 32, 32,),
            'soul_low' : get_tiles_from_sheet('Potions/soul_potions/soul_low.png', 2, 2, 0, 0, 32, 32,),

            'speed_full' : get_tiles_from_sheet('Potions/speed_potions/speed_full.png', 2, 2, 0, 0, 32, 32,),
            'speed_half' : get_tiles_from_sheet('Potions/speed_potions/speed_half.png', 2, 2, 0, 0, 32, 32,),
            'speed_low' : get_tiles_from_sheet('Potions/speed_potions/speed_low.png', 2, 2, 0, 0, 32, 32,),

            'green_full' : get_tiles_from_sheet('Potions/Greenpotions/green_full.png', 2, 2, 0, 0, 32, 32,),
            'green_half' : get_tiles_from_sheet('Potions/Greenpotions/green_half.png', 2, 2, 0, 0, 32, 32,),
            'green_low' : get_tiles_from_sheet('Potions/Greenpotions/green_low.png', 2, 2, 0, 0, 32, 32,),

            'strength_full' : get_tiles_from_sheet('Potions/strength_potions/strength_full.png', 2, 2, 0, 0, 32, 32,),
            'strength_half' : get_tiles_from_sheet('Potions/strength_potions/strength_half.png', 2, 2, 0, 0, 32, 32,),
            'strength_low' : get_tiles_from_sheet('Potions/strength_potions/strength_low.png', 2, 2, 0, 0, 32, 32,),

            'poison_resistance_full' : get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_full.png', 2, 2, 0, 0, 32, 32,),
            'poison_resistance_half' : get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_half.png', 2, 2, 0, 0, 32, 32,),
            'poison_resistance_low' : get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_low.png', 2, 2, 0, 0, 32, 32,),

            'purple_full' : get_tiles_from_sheet('Potions/Purplepotions/Purple_full.png', 2, 2, 0, 0, 32, 32,),
            'purple_half' : get_tiles_from_sheet('Potions/Purplepotions/Purple_half.png', 2, 2, 0, 0, 32, 32,),
            'purple_low' : get_tiles_from_sheet('Potions/Purplepotions/Purple_low.png', 2, 2, 0, 0, 32, 32,),

            'frozen_resistance_full' : get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_full.png', 2, 2, 0, 0, 32, 32,),
            'frozen_resistance_half' : get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_half.png', 2, 2, 0, 0, 32, 32,),
            'frozen_resistance_low' : get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_low.png', 2, 2, 0, 0, 32, 32,),

            'silence_full' : get_tiles_from_sheet('Potions/silence_potions/silence_full.png', 2, 2, 0, 0, 32, 32,),
            'silence_half' : get_tiles_from_sheet('Potions/silence_potions/silence_half.png', 2, 2, 0, 0, 32, 32,),
            'silence_low' : get_tiles_from_sheet('Potions/silence_potions/silence_low.png', 2, 2, 0, 0, 32, 32,),

            'regen_full' : get_tiles_from_sheet('Potions/regen_potions/regen_full.png', 2, 2, 0, 0, 32, 32,),
            'regen_half' : get_tiles_from_sheet('Potions/regen_potions/regen_half.png', 2, 2, 0, 0, 32, 32,),
            'regen_low' : get_tiles_from_sheet('Potions/regen_potions/regen_low.png', 2, 2, 0, 0, 32, 32,),

            'vampiric_full' : get_tiles_from_sheet('Potions/vampiric_potions/vampiric_full.png', 2, 2, 0, 0, 32, 32,),
            'vampiric_half' : get_tiles_from_sheet('Potions/vampiric_potions/vampiric_half.png', 2, 2, 0, 0, 32, 32,),
            'vampiric_low' : get_tiles_from_sheet('Potions/vampiric_potions/vampiric_low.png', 2, 2, 0, 0, 32, 32,),

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

            'fire_cirlce_rune' : get_tiles_from_sheet('runes/fire/fire_cirlce_rune.png', 1, 0, 0, 0, 32, 32),
            'fire_resistance_rune' : get_tiles_from_sheet('runes/fire/fire_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            'fire_shield_rune' : get_tiles_from_sheet('runes/fire/fire_shield_rune.png', 1, 0, 0, 0, 32, 32),
            'fire_spray_rune' : get_tiles_from_sheet('runes/fire/fire_spray_rune.png', 1, 0, 0, 0, 32, 32),
            'fire_ball_rune' : get_tiles_from_sheet('runes/fire/fire_ball_rune.png', 1, 0, 0, 0, 32, 32),

            'freeze_circle_rune' : get_tiles_from_sheet('runes/frost/frost_circle_rune.png', 1, 0, 0, 0, 32, 32),
            'frozen_resistance_rune' : get_tiles_from_sheet('runes/frost/frost_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            'freeze_shield_rune' : get_tiles_from_sheet('runes/frost/frost_shield_rune.png', 1, 0, 0, 0, 32, 32),
            'freeze_spray_rune' : get_tiles_from_sheet('runes/frost/frost_spray_rune.png', 1, 0, 0, 0, 32, 32),
            'freeze_ball_rune' : get_tiles_from_sheet('runes/frost/frost_ball_rune.png', 1, 0, 0, 0, 32, 32),
            

            'poison_resistance_rune' : get_tiles_from_sheet('runes/poison/poison_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            'poison_ball_rune' : get_tiles_from_sheet('runes/poison/poison_ball_rune.png', 1, 0, 0, 0, 32, 32),

            'electric_resistance_rune' : get_tiles_from_sheet('runes/electric/electric_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            'electric_ball_rune' : get_tiles_from_sheet('runes/electric/electric_ball_rune.png', 1, 0, 0, 0, 32, 32),
            'electric_spray_rune' : get_tiles_from_sheet('runes/electric/electric_spray_rune.png', 1, 0, 0, 0, 32, 32),

            'invisibility_rune' : get_tiles_from_sheet('runes/invisibility_rune.png', 1, 0, 0, 0, 32, 32),
            'key_rune' : get_tiles_from_sheet('runes/key_rune.png', 1, 0, 0, 0, 32, 32),
            'light_rune' : get_tiles_from_sheet('runes/light_rune.png', 1, 0, 0, 0, 32, 32),
            'resistance_rune' : get_tiles_from_sheet('runes/resistance_rune.png', 1, 0, 0, 0, 32, 32),
            'shield_rune' : get_tiles_from_sheet('runes/shield_rune.png', 1, 0, 0, 0, 32, 32),
            'silence_rune' : get_tiles_from_sheet('runes/silence_rune.png', 1, 0, 0, 0, 32, 32),
            'speed_rune' : get_tiles_from_sheet('runes/speed_rune.png', 1, 0, 0, 0, 32, 32),
            'increase_strength_rune' : get_tiles_from_sheet('runes/strength_rune.png', 1, 0, 0, 0, 32, 32),
            'vampiric_rune' : get_tiles_from_sheet('runes/vampiric_rune.png', 1, 0, 0, 0, 32, 32),
            'hunger_rune' : get_tiles_from_sheet('runes/hunger_rune.png', 1, 0, 0, 0, 32, 32),
            'magnet_rune' : get_tiles_from_sheet('runes/magnet_rune.png', 1, 0, 0, 0, 32, 32),
            'invulnerable_rune' : get_tiles_from_sheet('runes/invulnerable_rune.png', 1, 0, 0, 0, 32, 32),
        }
        self.assets.update(rune)

    def Asset_Font(self):
        font = {
            'font' : get_tiles_from_sheet('font/font.png', 7, 5, 0, 0, 16, 16),
            'player_damage_font' : get_tiles_from_sheet('font/player_damage_font.png', 7, 5, 0, 0, 16, 16),
            'symbols' : get_tiles_from_sheet('font/symbols.png', 7, 4, 0, 0, 16, 16),
            'souls' : get_tiles_from_sheet('font/souls.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(font)

    def Asset_Menu(self):
        menu = {
            'loading_bar' : get_tiles_from_sheet('menu/loading_screen.png', 6, 0, 0, 0, 96, 96),
        }
        self.assets.update(menu)
