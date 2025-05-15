import pygame
from scripts.engine.utility.utils import load_image, load_images, Animation, get_tiles_from_sheet
from scripts.engine.assets.keys import keys

class Graphics_Loader:
    def Run_All(self):
        Graphics_Loader.Asset_Background_List(self)
        Graphics_Loader.Asset_Crypt_Tile_List(self)
        Graphics_Loader.Asset_Trap_List(self)
        Graphics_Loader.Asset_Effect_List(self)
        Graphics_Loader.Asset_Magic_Attack_List(self)
        Graphics_Loader.Asset_Skeleton_Warrior_List(self)
        Graphics_Loader.Asset_Skeleton_Ranger_List(self)
        Graphics_Loader.Asset_Fire_Spirit_List(self)
        Graphics_Loader.Asset_Ice_Spirit_List(self)
        Graphics_Loader.Asset_Skeleton_Bell_Toller_List(self)
        Graphics_Loader.Asset_Skeleton_Cleric_List(self)
        Graphics_Loader.Asset_Skeleton_Undertaker_List(self)
        Graphics_Loader.Wight_King_Spirit_List(self)
        Graphics_Loader.Asset_Spider_List(self)
        Graphics_Loader.Asset_Enemy_Symbols_List(self)
        Graphics_Loader.Asset_Player_List(self)
        Graphics_Loader.Asset_Interative_Objects_List(self)
        Graphics_Loader.Asset_Environment_List(self)
        Graphics_Loader.Asset_Potion_List(self)
        Graphics_Loader.Asset_Decoration_List(self)
        Graphics_Loader.Asset_Weapons_List(self)
        Graphics_Loader.Asset_Weapons_Effects(self)
        Graphics_Loader.Asset_Inventory(self)
        Graphics_Loader.Asset_Font(self)
        Graphics_Loader.Asset_Loot(self)
        Graphics_Loader.Asset_Keys(self)
        Graphics_Loader.Asset_Bombs(self)
        Graphics_Loader.Asset_Rune(self)
        Graphics_Loader.Asset_Menu(self)
        Graphics_Loader.Asset_Health_Bar(self)
        Graphics_Loader.Asset_Particles_List(self)
        Graphics_Loader.Asset_Tooltips(self)

        
    def Asset_Background_List(self):
        background_assets = {'background': load_image('background.png'),}
        self.assets.update(background_assets)
        

    def Asset_Crypt_Tile_List(self):
        tiles_assets = {
            keys.floor : get_tiles_from_sheet('crypt_assets/crypt_floor.png', 5, 1, 0, 0, 32, 32),
            keys.wall_top : get_tiles_from_sheet('crypt_assets/wall_top.png', 3, 0, 0, 0, 32, 32),
            keys.wall_left : get_tiles_from_sheet('crypt_assets/wall_left.png', 0, 3, 0, 0, 32, 32),
            keys.wall_right : get_tiles_from_sheet('crypt_assets/wall_right.png', 0, 3, 0, 0, 32, 32),
            keys.wall_middle : get_tiles_from_sheet('crypt_assets/wall_middle.png', 0, 3, 0, 0, 32, 32),
            keys.wall_bottom : get_tiles_from_sheet('crypt_assets/wall_bottom.png', 3, 0, 0, 0, 32, 32),
            keys.wall_bottom_corner : get_tiles_from_sheet('crypt_assets/wall_bottom_corner.png', 2, 0, 0, 0, 32, 32),
        }
        self.assets.update(tiles_assets)

    def Asset_Trap_List(self):
        white = (255,255,255)
        trap_assets = {
            keys.spike_trap : get_tiles_from_sheet('traps/spike_trap.png', 6, 0, 0, 0, 32, 32, white),
            keys.spike_poison_trap : get_tiles_from_sheet('traps/Spike_Trap_poison.png', 13, 0, 0, 0, 32, 32, white),
            keys.pit_trap : get_tiles_from_sheet('traps/Pit_Trap_Spikes.png', 1, 0, 0, 0, 32, 32, white),
            keys.fire_trap : get_tiles_from_sheet('traps/Fire_Trap.png', 13, 0, 0, 0, 32, 20, white),
            keys.spider_web : get_tiles_from_sheet('entities/enemies/spider/spider_web.png', 3, 0, 0, 0, 32, 32),
            keys.poison_plume : get_tiles_from_sheet('traps/poison_plume.png', 7, 0, 0, 0, 32, 32),
        }

        self.assets.update(trap_assets)

    def Asset_Particles_List(self):
        effect_assets = {
            keys.dash_particle : get_tiles_from_sheet('particles/general/dash.png', 5, 0, 0, 0, 5, 5),
            keys.fire_particle : get_tiles_from_sheet('particles/general/fire.png', 5, 0, 0, 0, 3, 3),
            keys.spark_particle : get_tiles_from_sheet('particles/general/spark.png', 5, 0, 0, 0, 3, 3),
            keys.blood_particle : get_tiles_from_sheet('particles/general/blood.png', 5, 0, 0, 0, 3, 3),
            keys.bone_particle : get_tiles_from_sheet('particles/general/bone.png', 5, 0, 0, 0, 3, 3),
            keys.electric_particle : get_tiles_from_sheet('particles/general/electric.png', 5, 0, 0, 0, 3, 3),
            keys.frost_particle : get_tiles_from_sheet('particles/general/frost.png', 5, 0, 0, 0, 3, 3),
            keys.gold_particle : get_tiles_from_sheet('particles/general/gold.png', 5, 0, 0, 0, 3, 3),
            keys.poison_particle : get_tiles_from_sheet('particles/general/poison.png', 5, 0, 0, 0, 3, 3),
            keys.vampire_particle : get_tiles_from_sheet('particles/general/vampire.png', 5, 0, 0, 0, 3, 3),
            keys.soul_particle : get_tiles_from_sheet('particles/general/soul.png', 5, 0, 0, 0, 3, 3),
            keys.player_particle : get_tiles_from_sheet('particles/general/player.png', 5, 0, 0, 0, 3, 3),
        }
        self.assets.update(effect_assets)

    def Asset_Effect_List(self):
        white = (255,255,255)
        effect_assets = {
            keys.heart : load_image('heart.png'),
            keys.coin : get_tiles_from_sheet('coin_.png', 3, 0, 0, 0, 13, 13, white),
            keys.fire : get_tiles_from_sheet('particles/effects/fire/orange/loops/burning_loop_1.png', 7, 0, 0, 0, 32, 32, white),
            keys.poison : get_tiles_from_sheet('particles/effects/poison.png', 2, 0, 0, 0, 32, 32, white),
            keys.frozen : get_tiles_from_sheet('particles/effects/frozen.png', 2, 0, 0, 0, 32, 32, white),
            keys.wet : get_tiles_from_sheet('particles/effects/wet.png', 2, 0, 0, 0, 32, 32),
            keys.regen : get_tiles_from_sheet('particles/effects/regen.png', 2, 1, 0, 0, 32, 32),
            keys.electric : get_tiles_from_sheet('particles/effects/electric.png', 5, 0, 0, 0, 32, 32),
            keys.invincible : get_tiles_from_sheet('particles/effects/invincible.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(effect_assets)
    
    def Asset_Magic_Attack_List(self):
        particle_assets = {
       keys.fire_particle_attack : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_particle.png', 3, 0, 0, 0, 4, 4),
       keys.fire_ball : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_ball.png', 0, 0, 0, 0, 16, 16),
       keys.fire_explosion : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_explosion.png', 7, 0, 0, 0, 32, 32),

       keys.ice_particle_attack : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_particle.png', 3, 0, 0, 0, 4, 4),
       keys.ice_ball : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_ball.png', 0, 0, 0, 0, 16, 16),
       keys.ice_explosion : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_explosion.png', 5, 0, 0, 0, 32, 32),
       keys.ice_storm : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_storm.png', 9, 0, 0, 0, 32, 32),

       keys.poison_particle_attack : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_particle.png', 3, 0, 0, 0, 4, 4),
       keys.poison_ball : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_ball.png', 0, 0, 0, 0, 16, 16),
       keys.poison_explosion : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_explosion.png', 5, 0, 0, 0, 32, 32),
       keys.poison_cloud : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_cloud.png', 3, 0, 0, 0, 32, 32),


       keys.electric_particle_attack : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_particle.png', 0, 0, 0, 0, 16, 16),
       keys.electric_ball : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_ball.png', 0, 0, 0, 0, 16, 16),
       keys.electric_explosion : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_explosion.png', 5, 0, 0, 0, 32, 32),

        keys.soul_reap : get_tiles_from_sheet('weapons/magic_attacks/vampiric/soul_reap.png', 0, 0, 0, 0, 32, 32),
        keys.vampiric_ball : get_tiles_from_sheet('weapons/magic_attacks/vampiric/vampiric_ball.png', 0, 0, 0, 0, 16, 16),
        keys.soul_pit : get_tiles_from_sheet('weapons/magic_attacks/vampiric/soul_pit.png', 6, 0, 0, 0, 32, 32),
        
        }
        self.assets.update(particle_assets)


    def Asset_Player_List(self):
        entities_assets = {

            keys.player_idle_down : get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 0, 32, 32),
            keys.player_idle_up : get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 0, 32, 32),
            keys.player_standing_still_down : get_tiles_from_sheet('entities/player/standing_still_down.png', 4, 0, 0, 0, 32, 32),
            keys.player_standing_still_up : get_tiles_from_sheet('entities/player/standing_still_up.png', 4, 0, 0, 0, 32, 32),
            keys.player_running_down : get_tiles_from_sheet('entities/player/running_down.png', 4, 0, 0, 0, 32, 32),
            keys.player_running_up : get_tiles_from_sheet('entities/player/running_up.png', 4, 0, 0, 0, 32, 32),
            keys.player_attack : get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 0, 32, 32),


        }
        
        self.assets.update(entities_assets)


    def Asset_Skeleton_Warrior_List(self):
        entities_assets = {
            keys.skeleton_warrior_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_1.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_warrior_1_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_1_attack.png', 6, 0, 0, 0, 32, 32),

            keys.skeleton_warrior_2: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_2.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_warrior_2_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_2_attack.png', 6, 0, 0, 0, 32, 32),

            keys.skeleton_warrior_3: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_3.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_warrior_3_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_3_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Ranger_List(self):
        entities_assets = {
            keys.skeleton_ranger_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_1.png', 5, 0, 0, 0, 32, 32),
            keys.skeleton_ranger_1_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_1_attack.png', 6, 0, 0, 0, 32, 32),

            keys.skeleton_ranger_2: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_2.png', 5, 0, 0, 0, 32, 32),
            keys.skeleton_ranger_2_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_2_attack.png', 6, 0, 0, 0, 32, 32),

            keys.skeleton_ranger_3: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_3.png', 5, 0, 0, 0, 32, 32),
            keys.skeleton_ranger_3_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_3_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Cleric_List(self):
        entities_assets = {
            keys.skeleton_cleric_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_cleric/skeleton_cleric_1.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_cleric_1_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_cleric/skeleton_cleric_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Bell_Toller_List(self):
        entities_assets = {
            keys.skeleton_bell_toller_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_bell/skeleton_bell_1.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_bell_toller_1_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_bell/skeleton_bell_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Undertaker_List(self):
        entities_assets = {
            keys.skeleton_undertaker_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_undertaker/skeleton_undertaker_1.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_undertaker_1_attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_undertaker/skeleton_undertaker_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)



    def Asset_Fire_Spirit_List(self):
        entities_assets = {
            keys.fire_spirit_idle: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_idle.png', 3, 0, 0, 0, 32, 32),
            keys.fire_spirit_running: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_moving.png', 3, 0, 0, 0, 32, 32),
            keys.fire_spirit_attack: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_attacking.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Ice_Spirit_List(self):
        entities_assets = {
            keys.ice_spirit: get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),
            keys.ice_spirit_attack: get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Wight_King_Spirit_List(self):
        entities_assets = {
            keys.wight_king: get_tiles_from_sheet('entities/enemies/undead/wight_king/wight_king.png', 4, 0, 0, 0, 40, 40),
            keys.wight_king_attack: get_tiles_from_sheet('entities/enemies/undead/wight_king/wight_king_attack.png', 6, 0, 0, 0, 40, 40),
        }
        self.assets.update(entities_assets)

    def Asset_Spider_List(self):
        entities_assets = {
            keys.spider_idle: get_tiles_from_sheet('entities/enemies/spider/spider_idle.png', 4, 0, 0, 0, 32, 32),
            keys.spider_running: get_tiles_from_sheet('entities/enemies/spider/spider_running.png', 4, 0, 0, 0, 32, 32),
            keys.friendly_spider_idle: get_tiles_from_sheet('entities/enemies/spider/friendly_spider_idle.png', 4, 0, 0, 0, 32, 32),
            keys.friendly_spider_running: get_tiles_from_sheet('entities/enemies/spider/friendly_spider_running.png', 4, 0, 0, 0, 32, 32),
            keys.spider_attack: get_tiles_from_sheet('entities/enemies/spider/spider_attacking.png', 3, 0, 0, 0, 32, 32),
            keys.spider_jumping: get_tiles_from_sheet('entities/enemies/spider/spider_jumping.png', 8, 0, 0, 0, 32, 32),
            keys.spider_on_back: get_tiles_from_sheet('entities/enemies/spider/spider_on_back.png', 8, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Enemy_Symbols_List(self):
        symbols_assets = {
            keys.exclamation_mark: get_tiles_from_sheet('entities/enemies/symbols/exclamation.png', 0, 0, 0, 0, 32, 32),
            keys.health_bar: get_tiles_from_sheet('entities/enemies/symbols/health_bar.png', 9, 0, 0, 0, 32, 32),
        }
        self.assets.update(symbols_assets)

    def Asset_Weapons_List(self):
        Weapons_assets = {
            keys.sword: get_tiles_from_sheet('weapons/sword/sword.png', 3, 0, 0, 0, 32, 32),
            keys.sword_attack_cut: get_tiles_from_sheet('weapons/sword/sword.png', 3, 0, 0, 0, 32, 32),
            keys.sword_attack_stab: get_tiles_from_sheet('weapons/sword/sword_attack.png', 3, 0, 0, 0, 32, 32),
            
            keys.torch: get_tiles_from_sheet('weapons/torch/torch.png', 8, 0, 0, 0, 32, 32),
            keys.torch_attack_cut: get_tiles_from_sheet('weapons/torch/torch_attack.png', 8, 0, 0, 0, 32, 32),
            
            keys.spear: get_tiles_from_sheet('weapons/spear/spear.png', 8, 0, 0, 0, 32, 32),
            keys.spear_attack_stab: get_tiles_from_sheet('weapons/spear/spear.png', 8, 0, 0, 0, 32, 32),
            
            keys.bow: get_tiles_from_sheet('weapons/bow/bow.png', 0, 0, 0, 0, 32, 32),
            keys.bow_attack: get_tiles_from_sheet('weapons/bow/bow_attack.png', 2, 0, 0, 0, 32, 32),
            
            keys.arrow: get_tiles_from_sheet('weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),
            keys.arrow_attack: get_tiles_from_sheet('weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),

            keys.shield: get_tiles_from_sheet('weapons/shield/shields.png', 4, 4, 0, 0, 32, 32),
            keys.shield_attack: get_tiles_from_sheet('weapons/shield/shields.png', 4, 4, 0, 0, 32, 32),

            keys.halberd: get_tiles_from_sheet('weapons/halberd/halberd.png', 6, 0, 0, 0, 32, 32),
            keys.halberd_attack_stab: get_tiles_from_sheet('weapons/halberd/halberd_stab_attack.png', 6, 0, 0, 0, 32, 50),
            keys.halberd_attack_cut: get_tiles_from_sheet('weapons/halberd/halberd_cut_attack.png', 13, 0, 0, 0, 32, 32),

            keys.battle_axe: get_tiles_from_sheet('weapons/battle_axe/battle_axe.png', 5, 0, 0, 0, 32, 32),
            keys.battle_axe_attack_cut: get_tiles_from_sheet('weapons/battle_axe/battle_axe_cut_attack.png', 15, 0, 0, 0, 32, 32),
            
            keys.hammer: get_tiles_from_sheet('weapons/hammer/hammer.png', 6, 0, 0, 0, 32, 32),
            keys.hammer_attack_cut: get_tiles_from_sheet('weapons/hammer/hammer_cut_attack.png', 9, 0, 0, 0, 32, 32),

            keys.hatchet: get_tiles_from_sheet('weapons/hatchet/hatchet.png', 7, 0, 0, 0, 32, 32),
            keys.hatchet_attack_cut: get_tiles_from_sheet('weapons/hatchet/hatchet_cut_attack.png', 8, 0, 0, 0, 32, 32),

            keys.warhammer: get_tiles_from_sheet('weapons/warhammer/warhammer.png', 6, 0, 0, 0, 32, 32),
            keys.warhammer_attack_cut: get_tiles_from_sheet('weapons/warhammer/warhammer_cut_attack.png', 12, 0, 0, 0, 32, 32),

            keys.crossbow: get_tiles_from_sheet('weapons/crossbow/crossbow.png', 8, 0, 0, 0, 32, 32),
            keys.crossbow_attack: get_tiles_from_sheet('weapons/crossbow/crossbow_attack.png', 2, 0, 0, 0, 32, 32),

            keys.bell: get_tiles_from_sheet('weapons/bell/bell.png', 7, 0, 0, 0, 32, 32),
            keys.bell_attack_cut: get_tiles_from_sheet('weapons/bell/bell_attack_cut.png', 9, 0, 0, 0, 32, 32),

            keys.sceptre: get_tiles_from_sheet('weapons/sceptre/sceptre.png', 7, 0, 0, 0, 32, 32),
            keys.sceptre_attack_cut: get_tiles_from_sheet('weapons/sceptre/sceptre_cut_attack.png', 9, 0, 0, 0, 32, 32),

            keys.scythe: get_tiles_from_sheet('weapons/scythe/scythe.png', 7, 0, 0, 0, 32, 32),
            keys.scythe_attack_cut: get_tiles_from_sheet('weapons/scythe/scythe_attack.png', 9, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)

    def Asset_Weapons_Effects(self):
        Weapons_assets = {
            keys.slash_cut_effect: get_tiles_from_sheet('weapons/weapon_effects/slash_cut_attack.png', 6, 0, 0, 0, 64, 64),
            keys.slash_stab_effect: get_tiles_from_sheet('weapons/weapon_effects/slash_stab_attack.png', 6, 0, 0, 0, 64, 64),
            keys.slash_spin_effect: get_tiles_from_sheet('weapons/weapon_effects/slash_spin_attack.png', 7, 0, 0, 0, 64, 64),
            keys.slash_smash_effect: get_tiles_from_sheet('weapons/weapon_effects/slash_smash_attack.png', 5, 0, 0, 0, 64, 64),
            keys.slash_charge_effect: get_tiles_from_sheet('weapons/weapon_effects/slash_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.blunt_cut_effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_cut_attack.png', 6, 0, 0, 0, 64, 64),
            keys.blunt_stab_effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_stab_attack.png', 6, 0, 0, 0, 64, 64),
            keys.blunt_spin_effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_spin_attack.png', 7, 0, 0, 0, 64, 64),
            keys.blunt_smash_effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_smash_attack.png', 5, 0, 0, 0, 64, 64),
            keys.blunt_charge_effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.electric_cut_effect: get_tiles_from_sheet('weapons/weapon_effects/electric_cut_attack.png', 6, 0, 0, 0, 64, 64),
            keys.electric_stab_effect: get_tiles_from_sheet('weapons/weapon_effects/electric_stab_attack.png', 6, 0, 0, 0, 64, 64),
            keys.electric_spin_effect: get_tiles_from_sheet('weapons/weapon_effects/electric_spin_attack.png', 7, 0, 0, 0, 64, 64),
            keys.electric_smash_effect: get_tiles_from_sheet('weapons/weapon_effects/electric_smash_attack.png', 5, 0, 0, 0, 64, 64),
            keys.electric_charge_effect: get_tiles_from_sheet('weapons/weapon_effects/electric_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.fire_cut_effect: get_tiles_from_sheet('weapons/weapon_effects/fire_cut_attack.png', 6, 0, 0, 0, 64, 64),
            keys.fire_stab_effect: get_tiles_from_sheet('weapons/weapon_effects/fire_stab_attack.png', 6, 0, 0, 0, 64, 64),
            keys.fire_spin_effect: get_tiles_from_sheet('weapons/weapon_effects/fire_spin_attack.png', 7, 0, 0, 0, 64, 64),
            keys.fire_smash_effect: get_tiles_from_sheet('weapons/weapon_effects/fire_smash_attack.png', 5, 0, 0, 0, 64, 64),
            keys.fire_charge_effect: get_tiles_from_sheet('weapons/weapon_effects/fire_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.frozen_cut_effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_cut_attack.png', 6, 0, 0, 0, 64, 64),
            keys.frozen_stab_effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_stab_attack.png', 6, 0, 0, 0, 64, 64),
            keys.frozen_spin_effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_spin_attack.png', 7, 0, 0, 0, 64, 64),
            keys.frozen_smash_effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_smash_attack.png', 5, 0, 0, 0, 64, 64),
            keys.frozen_charge_effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.poison_cut_effect: get_tiles_from_sheet('weapons/weapon_effects/poison_cut_attack.png', 6, 0, 0, 0, 64, 64),
            keys.poison_stab_effect: get_tiles_from_sheet('weapons/weapon_effects/poison_stab_attack.png', 6, 0, 0, 0, 64, 64),
            keys.poison_spin_effect: get_tiles_from_sheet('weapons/weapon_effects/poison_spin_attack.png', 7, 0, 0, 0, 64, 64),
            keys.poison_smash_effect: get_tiles_from_sheet('weapons/weapon_effects/poison_smash_attack.png', 5, 0, 0, 0, 64, 64),
            keys.poison_charge_effect: get_tiles_from_sheet('weapons/weapon_effects/poison_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.regen_cut_effect: get_tiles_from_sheet('weapons/weapon_effects/regen_cut_attack.png', 6, 0, 0, 0, 64, 64),
            keys.regen_stab_effect: get_tiles_from_sheet('weapons/weapon_effects/regen_stab_attack.png', 6, 0, 0, 0, 64, 64),
            keys.regen_spin_effect: get_tiles_from_sheet('weapons/weapon_effects/regen_spin_attack.png', 7, 0, 0, 0, 64, 64),
            keys.regen_smash_effect: get_tiles_from_sheet('weapons/weapon_effects/regen_smash_attack.png', 5, 0, 0, 0, 64, 64),
            keys.regen_charge_effect: get_tiles_from_sheet('weapons/weapon_effects/regen_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.vampiric_cut_effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_cut_attack.png', 6, 0, 0, 0, 64, 64),
            keys.vampiric_stab_effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_stab_attack.png', 6, 0, 0, 0, 64, 64),
            keys.vampiric_spin_effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_spin_attack.png', 7, 0, 0, 0, 64, 64),
            keys.vampiric_smash_effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_smash_attack.png', 5, 0, 0, 0, 64, 64),
            keys.vampiric_charge_effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_charge_attack.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)


    def Asset_Inventory(self):
        Weapon_Inventory_assets = {
            keys.sword_shield: get_tiles_from_sheet('inventory/sword_shield.png', 2, 0, 0, 0, 34, 34),
            keys.duel_wield: get_tiles_from_sheet('inventory/Duel_wield.png', 2, 0, 0, 0, 34, 34),
            keys.bow_arrow: get_tiles_from_sheet('inventory/Bow_Arrow.png', 2, 0, 0, 0, 34, 34),
            keys.left_right: get_tiles_from_sheet('inventory/left_right.png', 2, 0, 0, 0, 34, 34),
            keys.rune_background: get_tiles_from_sheet('inventory/rune_background.png', 1, 0, 0, 0, 34, 34),
        }
        self.assets.update(Weapon_Inventory_assets)

    def Asset_Interative_Objects_List(self):
        white = (255,255,255)
        Objects_assets = {
            keys.chest: get_tiles_from_sheet('decoration/chest.png', 8, 0, 0, 0, 32, 32, white),
            keys.door_basic: get_tiles_from_sheet('decoration/door/door_closed.png', 0, 0, 0, 0, 32, 32),
            keys.rune_shrine: get_tiles_from_sheet('decoration/shrine/rune_shrine.png', 3, 0, 0, 0, 64, 64),
            keys.portal_shrine: get_tiles_from_sheet('decoration/shrine/portal_shrine.png', 3, 0, 0, 0, 64, 64),
            keys.bones: get_tiles_from_sheet('decoration/environment/bones.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(Objects_assets)




    def Asset_Environment_List(self):
        Environment_assets = {
            keys.lava_env: get_tiles_from_sheet('environment/lava.png', 2, 0, 0, 0, 32, 32),
            keys.shallow_water_env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 0, 32, 32),
            keys.medium_water_env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            keys.deep_water_env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            keys.shallow_ice_env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 0, 32, 32),
            keys.medium_ice_env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
            keys.deep_ice_env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
        }
        self.assets.update(Environment_assets)


    def Asset_Decoration_List(self):
        decoration_assets = {
        }
        self.assets.update(decoration_assets)


    def Asset_Potion_List(self):
        potion_assets = {
            keys.empty_bottle: get_tiles_from_sheet('Potions/Healing_potions/empty.png', 0, 0, 0, 0, 32, 32),

            keys.invisibility + '_' + keys.full: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            keys.invisibility + '_' + keys.half: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            keys.invisibility + '_' + keys.low: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),

            keys.healing + '_' + keys.full: get_tiles_from_sheet('Potions/Healing_potions/healing_full.png', 2, 2, 0, 0, 32, 32),
            keys.healing + '_' + keys.half: get_tiles_from_sheet('Potions/Healing_potions/healing_half.png', 2, 2, 0, 0, 32, 32),
            keys.healing + '_' + keys.low: get_tiles_from_sheet('Potions/Healing_potions/healing_low.png', 2, 2, 0, 0, 32, 32),

            keys.increase_souls + '_' + keys.full: get_tiles_from_sheet('Potions/soul_potions/soul_full.png', 2, 2, 0, 0, 32, 32),
            keys.increase_souls + '_' + keys.half: get_tiles_from_sheet('Potions/soul_potions/soul_half.png', 2, 2, 0, 0, 32, 32),
            keys.increase_souls + '_' + keys.low: get_tiles_from_sheet('Potions/soul_potions/soul_low.png', 2, 2, 0, 0, 32, 32),

            keys.arcane_hunger + '_' + keys.full: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_full.png', 2, 2, 0, 0, 32, 32),
            keys.arcane_hunger + '_' + keys.half: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_half.png', 2, 2, 0, 0, 32, 32),
            keys.arcane_hunger + '_' + keys.low: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_low.png', 2, 2, 0, 0, 32, 32),

            keys.speed + '_' + keys.full: get_tiles_from_sheet('Potions/speed_potions/speed_full.png', 2, 2, 0, 0, 32, 32),
            keys.speed + '_' + keys.half: get_tiles_from_sheet('Potions/speed_potions/speed_half.png', 2, 2, 0, 0, 32, 32),
            keys.speed + '_' + keys.low: get_tiles_from_sheet('Potions/speed_potions/speed_low.png', 2, 2, 0, 0, 32, 32),

            keys.green + '_' + keys.full: get_tiles_from_sheet('Potions/Greenpotions/green_full.png', 2, 2, 0, 0, 32, 32),
            keys.green + '_' + keys.half: get_tiles_from_sheet('Potions/Greenpotions/green_half.png', 2, 2, 0, 0, 32, 32),
            keys.green + '_' + keys.low: get_tiles_from_sheet('Potions/Greenpotions/green_low.png', 2, 2, 0, 0, 32, 32),

            keys.increase_strength + '_' + keys.full: get_tiles_from_sheet('Potions/strength_potions/strength_full.png', 2, 2, 0, 0, 32, 32),
            keys.increase_strength + '_' + keys.half: get_tiles_from_sheet('Potions/strength_potions/strength_half.png', 2, 2, 0, 0, 32, 32),
            keys.increase_strength + '_' + keys.low: get_tiles_from_sheet('Potions/strength_potions/strength_low.png', 2, 2, 0, 0, 32, 32),

            keys.poison_resistance + '_' + keys.full: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_full.png', 2, 2, 0, 0, 32, 32),
            keys.poison_resistance + '_' + keys.half: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_half.png', 2, 2, 0, 0, 32, 32),
            keys.poison_resistance + '_' + keys.low: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_low.png', 2, 2, 0, 0, 32, 32),

            keys.purple + '_' + keys.full: get_tiles_from_sheet('Potions/Purplepotions/Purple_full.png', 2, 2, 0, 0, 32, 32),
            keys.purple + '_' + keys.half: get_tiles_from_sheet('Potions/Purplepotions/Purple_half.png', 2, 2, 0, 0, 32, 32),
            keys.purple + '_' + keys.low: get_tiles_from_sheet('Potions/Purplepotions/Purple_low.png', 2, 2, 0, 0, 32, 32),

            keys.frozen_resistance + '_' + keys.full: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_full.png', 2, 2, 0, 0, 32, 32),
            keys.frozen_resistance + '_' + keys.half: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_half.png', 2, 2, 0, 0, 32, 32),
            keys.frozen_resistance + '_' + keys.low: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_low.png', 2, 2, 0, 0, 32, 32),

            keys.silence + '_' + keys.full: get_tiles_from_sheet('Potions/silence_potions/silence_full.png', 2, 2, 0, 0, 32, 32),
            keys.silence + '_' + keys.half: get_tiles_from_sheet('Potions/silence_potions/silence_half.png', 2, 2, 0, 0, 32, 32),
            keys.silence + '_' + keys.low: get_tiles_from_sheet('Potions/silence_potions/silence_low.png', 2, 2, 0, 0, 32, 32),

            keys.regen + '_' + keys.full: get_tiles_from_sheet('Potions/regen_potions/regen_full.png', 2, 2, 0, 0, 32, 32),
            keys.regen + '_' + keys.half: get_tiles_from_sheet('Potions/regen_potions/regen_half.png', 2, 2, 0, 0, 32, 32),
            keys.regen + '_' + keys.low: get_tiles_from_sheet('Potions/regen_potions/regen_low.png', 2, 2, 0, 0, 32, 32),

            keys.vampiric + '_' + keys.full: get_tiles_from_sheet('Potions/vampiric_potions/vampiric_full.png', 2, 2, 0, 0, 32, 32),
            keys.vampiric + '_' + keys.half: get_tiles_from_sheet('Potions/vampiric_potions/vampiric_half.png', 2, 2, 0, 0, 32, 32),
            keys.vampiric + '_' + keys.low: get_tiles_from_sheet('Potions/vampiric_potions/vampiric_low.png', 2, 2, 0, 0, 32, 32),

            keys.fire_resistance + '_' + keys.full: get_tiles_from_sheet('Potions/fire_resistance_potions/fire_resistance_full.png', 2, 2, 0, 0, 32, 32),
            keys.fire_resistance + '_' + keys.half: get_tiles_from_sheet('Potions/fire_resistance_potions/fire_resistance_half.png', 2, 2, 0, 0, 32, 32),
            keys.fire_resistance + '_' + keys.low: get_tiles_from_sheet('Potions/fire_resistance_potions/fire_resistance_low.png', 2, 2, 0, 0, 32, 32),
        }

        self.assets.update(potion_assets)




    def Asset_Loot(self):
        loot = {
            keys.gold: get_tiles_from_sheet('items/valuables/gold_coins.png', 3, 0, 0, 0, 16, 16),
            keys.echo_bell: get_tiles_from_sheet('items/utility/echo_bell.png', 0, 0, 0, 0, 32, 32),
            keys.shadow_cloak: get_tiles_from_sheet('items/utility/shadow_cloak.png', 0, 0, 0, 0, 32, 32),
            keys.lantern: get_tiles_from_sheet('items/passive/lantern.png', 0, 0, 0, 0, 32, 32),
            keys.anchor_stone: get_tiles_from_sheet('items/passive/anchor_stone.png', 0, 0, 0, 0, 32, 32),
            keys.blood_tomb: get_tiles_from_sheet('items/cursed/blood_tomb.png', 0, 0, 0, 0, 32, 32),
            keys.faith_pendant: get_tiles_from_sheet('items/passive/faith_pendant.png', 0, 0, 0, 0, 32, 32),
            keys.lucky_charm: get_tiles_from_sheet('items/passive/lucky_charm.png', 0, 0, 0, 0, 32, 32),
            keys.magnet: get_tiles_from_sheet('items/passive/magnet.png', 0, 0, 0, 0, 32, 32),
            keys.power_totem: get_tiles_from_sheet('items/passive/power_totem.png', 0, 0, 0, 0, 32, 32),
            keys.strength_totem: get_tiles_from_sheet('items/passive/strength_totem.png', 0, 0, 0, 0, 32, 32),
            keys.halo: get_tiles_from_sheet('items/passive/halo.png', 0, 0, 0, 0, 32, 32),
            keys.muffled_boots: get_tiles_from_sheet('items/passive/muffled_boots.png', 0, 0, 0, 0, 32, 32),
            keys.demonic_bargain: get_tiles_from_sheet('items/cursed/demonic_bargain.png', 0, 0, 0, 0, 32, 32),
            keys.temptress_embrace: get_tiles_from_sheet('items/cursed/temptress_embrace.png', 0, 0, 0, 0, 32, 32),
            keys.blood_coin: get_tiles_from_sheet('items/revive/blood_coin.png', 0, 0, 0, 0, 32, 32),
            keys.blood_pact: get_tiles_from_sheet('items/revive/blood_pact.png', 0, 0, 0, 0, 32, 32),
            keys.phoenix_feather: get_tiles_from_sheet('items/revive/phoenix_feather.png', 0, 0, 0, 0, 32, 32),
            keys.light_pendant: get_tiles_from_sheet('items/revive/light_pendant.png', 0, 0, 0, 0, 32, 32),
            keys.faded_hourglass: get_tiles_from_sheet('items/utility/faded_hourglass.png', 4, 0, 0, 0, 32, 32),
            keys.ethereal_chains: get_tiles_from_sheet('items/utility/ethereal_chains.png', 0, 0, 0, 0, 32, 32),
            keys.recall_scroll: get_tiles_from_sheet('items/utility/recall_parchment.png', 0, 0, 0, 0, 32, 32),
            keys.echo_sigil: get_tiles_from_sheet('items/passive/echo_sigil.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)


    def Asset_Keys(self):
        loot = {
            keys.lockpick: get_tiles_from_sheet('items/keys/lockpick.png', 0, 0, 0, 0, 32, 32),
            keys.blood_key: get_tiles_from_sheet('items/keys/blood_key.png', 0, 0, 0, 0, 32, 32),
            keys.skeleton_key: get_tiles_from_sheet('items/keys/skeleton_key.png', 0, 0, 0, 0, 32, 32),
            keys.soul_key: get_tiles_from_sheet('items/keys/soul_key.png', 0, 0, 0, 0, 32, 32),
            keys.cursed_key: get_tiles_from_sheet('items/keys/cursed_key.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Bombs(self):
        loot = {
            keys.fire_bomb: get_tiles_from_sheet('items/bombs/fire_bomb.png', 0, 0, 0, 0, 32, 32),
            keys.frozen_bomb: get_tiles_from_sheet('items/bombs/frozen_bomb.png', 0, 0, 0, 0, 32, 32),
            keys.electric_bomb: get_tiles_from_sheet('items/bombs/electric_bomb.png', 0, 0, 0, 0, 32, 32),
            keys.poison_bomb: get_tiles_from_sheet('items/bombs/poison_bomb.png', 0, 0, 0, 0, 32, 32),
            keys.vampiric_bomb: get_tiles_from_sheet('items/bombs/vampiric_bomb.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Rune(self):
        rune = {
            keys.healing_rune: get_tiles_from_sheet('runes/healing_rune.png', 1, 0, 0, 0, 32, 32),
            keys.regen_rune: get_tiles_from_sheet('runes/regen_rune.png', 1, 0, 0, 0, 32, 32),
            keys.dash_rune: get_tiles_from_sheet('runes/dash_rune.png', 1, 0, 0, 0, 32, 32),
            keys.arcane_conduit_rune: get_tiles_from_sheet('runes/arcane_conduit_rune.png', 1, 0, 0, 0, 32, 32),
            
            keys.fire_cirlce_rune: get_tiles_from_sheet('runes/fire/fire_cirlce_rune.png', 1, 0, 0, 0, 32, 32),
            keys.fire_resistance_rune: get_tiles_from_sheet('runes/fire/fire_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.fire_shield_rune: get_tiles_from_sheet('runes/fire/fire_shield_rune.png', 1, 0, 0, 0, 32, 32),
            keys.fire_spray_rune: get_tiles_from_sheet('runes/fire/fire_spray_rune.png', 1, 0, 0, 0, 32, 32),
            keys.fire_ball_rune: get_tiles_from_sheet('runes/fire/fire_ball_rune.png', 1, 0, 0, 0, 32, 32),

            keys.freeze_circle_rune: get_tiles_from_sheet('runes/frost/frost_circle_rune.png', 1, 0, 0, 0, 32, 32),
            keys.frozen_resistance_rune: get_tiles_from_sheet('runes/frost/frost_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.freeze_storm_rune: get_tiles_from_sheet('runes/frost/frost_storm_rune.png', 1, 0, 0, 0, 32, 32),
            keys.freeze_spray_rune: get_tiles_from_sheet('runes/frost/frost_spray_rune.png', 1, 0, 0, 0, 32, 32),
            keys.freeze_ball_rune: get_tiles_from_sheet('runes/frost/frost_ball_rune.png', 1, 0, 0, 0, 32, 32),
            
            keys.poison_resistance_rune: get_tiles_from_sheet('runes/poison/poison_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.poison_ball_rune: get_tiles_from_sheet('runes/poison/poison_ball_rune.png', 1, 0, 0, 0, 32, 32),
            keys.poison_cloud_rune: get_tiles_from_sheet('runes/poison/poison_cloud_rune.png', 1, 0, 0, 0, 32, 32),
            keys.poison_plume_rune: get_tiles_from_sheet('runes/poison/poison_plume_rune.png', 1, 0, 0, 0, 32, 32),

            keys.electric_resistance_rune: get_tiles_from_sheet('runes/electric/electric_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.electric_ball_rune: get_tiles_from_sheet('runes/electric/electric_ball_rune.png', 1, 0, 0, 0, 32, 32),
            keys.electric_spray_rune: get_tiles_from_sheet('runes/electric/electric_spray_rune.png', 1, 0, 0, 0, 32, 32),
            keys.chain_lightning_rune: get_tiles_from_sheet('runes/electric/chain_lightning_rune.png', 1, 0, 0, 0, 32, 32),
            
            keys.soul_reap_rune: get_tiles_from_sheet('runes/vampiric/soul_reap_rune.png', 1, 0, 0, 0, 32, 32),
            keys.soul_pit_rune: get_tiles_from_sheet('runes/vampiric/soul_pit_rune.png', 1, 0, 0, 0, 32, 32),

            keys.invisibility_rune: get_tiles_from_sheet('runes/invisibility_rune.png', 1, 0, 0, 0, 32, 32),
            keys.key_rune: get_tiles_from_sheet('runes/key_rune.png', 1, 0, 0, 0, 32, 32),
            keys.light_rune: get_tiles_from_sheet('runes/light_rune.png', 1, 0, 0, 0, 32, 32),
            keys.resistance_rune: get_tiles_from_sheet('runes/resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.shield_rune: get_tiles_from_sheet('runes/shield_rune.png', 1, 0, 0, 0, 32, 32),
            keys.silence_rune: get_tiles_from_sheet('runes/silence_rune.png', 1, 0, 0, 0, 32, 32),
            keys.speed_rune: get_tiles_from_sheet('runes/speed_rune.png', 1, 0, 0, 0, 32, 32),
            keys.increase_strength_rune: get_tiles_from_sheet('runes/strength_rune.png', 1, 0, 0, 0, 32, 32),
            keys.vampiric_rune: get_tiles_from_sheet('runes/vampiric_rune.png', 1, 0, 0, 0, 32, 32),
            keys.arcane_hunger_rune: get_tiles_from_sheet('runes/hunger_rune.png', 1, 0, 0, 0, 32, 32),
            keys.magnet_rune: get_tiles_from_sheet('runes/magnet_rune.png', 1, 0, 0, 0, 32, 32),
            keys.invulnerable_rune: get_tiles_from_sheet('runes/invulnerable_rune.png', 1, 0, 0, 0, 32, 32),
        }
        self.assets.update(rune)


    def Asset_Font(self):
        font = {
            keys.font: get_tiles_from_sheet('font/font.png', 7, 5, 0, 0, 16, 16),
            keys.player_damage_font: get_tiles_from_sheet('font/player_damage_font.png', 7, 5, 0, 0, 16, 16),
            keys.small_font: get_tiles_from_sheet('font/small_font.png', 7, 5, 0, 0, 8, 8),
            keys.floating_E: get_tiles_from_sheet('font/floating_e.png', 1, 0, 0, 0, 16, 16),
            keys.symbols: get_tiles_from_sheet('font/symbols.png', 7, 5, 0, 0, 16, 16),
            keys.souls: get_tiles_from_sheet('font/souls.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(font)
    
    def Asset_Health_Bar(self):
        health_bars = {
            keys.healthbar_1: get_tiles_from_sheet('ui/healthbar_1.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_2: get_tiles_from_sheet('ui/healthbar_2.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_3: get_tiles_from_sheet('ui/healthbar_3.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_4: get_tiles_from_sheet('ui/healthbar_4.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_5: get_tiles_from_sheet('ui/healthbar_5.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_6: get_tiles_from_sheet('ui/healthbar_6.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_7: get_tiles_from_sheet('ui/healthbar_7.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_8: get_tiles_from_sheet('ui/healthbar_8.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_9: get_tiles_from_sheet('ui/healthbar_9.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_10: get_tiles_from_sheet('ui/healthbar_10.png', 5, 0, 0, 0, 64, 64),
        }
        self.assets.update(health_bars)

    def Asset_Menu(self):
        menu = {
            keys.loading_bar: get_tiles_from_sheet('menu/loading_screen.png', 6, 0, 0, 0, 96, 96),
        }
        self.assets.update(menu)

    def Asset_Tooltips(self):
        tooltips = {
            keys.radius_tooltip: get_tiles_from_sheet('items/tooltips/radius.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(tooltips)

