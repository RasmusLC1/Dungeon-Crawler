import pygame
from scripts.engine.utility.utils import load_image, load_images, Animation, get_tiles_from_sheet

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
            self.dictionary.Get_Floor : get_tiles_from_sheet('crypt_assets/crypt_floor.png', 5, 1, 0, 0, 32, 32),
            self.dictionary.Get_Wall_Top : get_tiles_from_sheet('crypt_assets/wall_top.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Wall_Left : get_tiles_from_sheet('crypt_assets/wall_left.png', 0, 3, 0, 0, 32, 32),
            self.dictionary.Get_Wall_Right : get_tiles_from_sheet('crypt_assets/wall_right.png', 0, 3, 0, 0, 32, 32),
            self.dictionary.Get_Wall_Middle : get_tiles_from_sheet('crypt_assets/wall_middle.png', 0, 3, 0, 0, 32, 32),
            self.dictionary.Get_Wall_Bottom : get_tiles_from_sheet('crypt_assets/wall_bottom.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Wall_Bottom_Corner : get_tiles_from_sheet('crypt_assets/wall_bottom_corner.png', 2, 0, 0, 0, 32, 32),
        }
        self.assets.update(tiles_assets)

    def Asset_Trap_List(self):
        white = (255,255,255)
        trap_assets = {
            self.dictionary.Get_Spike_Trap : get_tiles_from_sheet('traps/spike_trap.png', 6, 0, 0, 0, 32, 32, white),
            self.dictionary.Get_Spike_Poison_Trap : get_tiles_from_sheet('traps/Spike_Trap_poison.png', 13, 0, 0, 0, 32, 32, white),
            self.dictionary.Get_Pit_Trap : get_tiles_from_sheet('traps/Pit_Trap_Spikes.png', 1, 0, 0, 0, 32, 32, white),
            self.dictionary.Get_Fire_Trap : get_tiles_from_sheet('traps/Fire_Trap.png', 13, 0, 0, 0, 32, 20, white),
            self.dictionary.Get_Spider_Web_Trap : get_tiles_from_sheet('entities/enemies/spider/spider_web.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Poison_Plume_Trap : get_tiles_from_sheet('traps/poison_plume.png', 7, 0, 0, 0, 32, 32),
        }

        self.assets.update(trap_assets)

    def Asset_Particles_List(self):
        effect_assets = {
            self.dictionary.Get_Dash_Particle : get_tiles_from_sheet('particles/general/dash.png', 5, 0, 0, 0, 5, 5),
            self.dictionary.Get_Fire_Particle : get_tiles_from_sheet('particles/general/fire.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Spark_Particle : get_tiles_from_sheet('particles/general/spark.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Blood_Particle : get_tiles_from_sheet('particles/general/blood.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Bone_Particle : get_tiles_from_sheet('particles/general/bone.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Electric_Particle : get_tiles_from_sheet('particles/general/electric.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Frost_Particle : get_tiles_from_sheet('particles/general/frost.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Gold_Particle : get_tiles_from_sheet('particles/general/gold.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Poison_Particle : get_tiles_from_sheet('particles/general/poison.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Vampire_Particle : get_tiles_from_sheet('particles/general/vampire.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Soul_Particle : get_tiles_from_sheet('particles/general/soul.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Get_Player_Particle : get_tiles_from_sheet('particles/general/player.png', 5, 0, 0, 0, 3, 3),
        }
        self.assets.update(effect_assets)

    def Asset_Effect_List(self):
        white = (255,255,255)
        effect_assets = {
            self.dictionary.Get_Heart : load_image('heart.png'),
            self.dictionary.Get_Coin : get_tiles_from_sheet('coin_.png', 3, 0, 0, 0, 13, 13, white),
            self.dictionary.Get_Fire_Effect : get_tiles_from_sheet('particles/effects/fire/orange/loops/burning_loop_1.png', 7, 0, 0, 0, 32, 32, white),
            self.dictionary.Get_Poison_Effect : get_tiles_from_sheet('particles/effects/poison.png', 2, 0, 0, 0, 32, 32, white),
            self.dictionary.Get_Frozen_Effect : get_tiles_from_sheet('particles/effects/frozen.png', 2, 0, 0, 0, 32, 32, white),
            self.dictionary.Get_Wet_Effect : get_tiles_from_sheet('particles/effects/wet.png', 2, 0, 0, 0, 32, 32),
            self.dictionary.Get_Regen_Effect : get_tiles_from_sheet('particles/effects/regen.png', 2, 1, 0, 0, 32, 32),
            self.dictionary.Get_Electric_Effect : get_tiles_from_sheet('particles/effects/electric.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Get_Invincible_Effect : get_tiles_from_sheet('particles/effects/invincible.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(effect_assets)
    
    def Asset_Magic_Attack_List(self):
        particle_assets = {
       self.dictionary.Get_Fire_Particle_Attack : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_particle.png', 3, 0, 0, 0, 4, 4),
       self.dictionary.Get_Fire_Ball : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_ball.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Get_Fire_Explosion : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_explosion.png', 7, 0, 0, 0, 32, 32),

       self.dictionary.Get_Ice_Particle_Attack : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_particle.png', 3, 0, 0, 0, 4, 4),
       self.dictionary.Get_Ice_Ball : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_ball.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Get_Ice_Explosion : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_explosion.png', 5, 0, 0, 0, 32, 32),
       self.dictionary.Get_Ice_Storm : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_storm.png', 9, 0, 0, 0, 32, 32),

       self.dictionary.Get_Poison_Particle_Attack : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_particle.png', 3, 0, 0, 0, 4, 4),
       self.dictionary.Get_Poison_Ball : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_ball.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Get_Poison_Explosion : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_explosion.png', 5, 0, 0, 0, 32, 32),
       self.dictionary.Get_Poison_Cloud : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_cloud.png', 3, 0, 0, 0, 32, 32),


       self.dictionary.Get_Electric_Particle_Attack : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_particle.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Get_Electric_Ball : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_ball.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Get_Electric_Explosion : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_explosion.png', 5, 0, 0, 0, 32, 32),

        self.dictionary.Get_Soul_Reap : get_tiles_from_sheet('weapons/magic_attacks/vampiric/soul_reap.png', 0, 0, 0, 0, 32, 32),
        self.dictionary.Get_Vampiric_Ball : get_tiles_from_sheet('weapons/magic_attacks/vampiric/vampiric_ball.png', 0, 0, 0, 0, 16, 16),
        self.dictionary.Get_Soul_Pit : get_tiles_from_sheet('weapons/magic_attacks/vampiric/soul_pit.png', 6, 0, 0, 0, 32, 32),
        
        }
        self.assets.update(particle_assets)


    def Asset_Player_List(self):
        entities_assets = {

            self.dictionary.Get_Player_Idle_Down : get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Player_Idle_Up : get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Player_Standing_Still_Down : get_tiles_from_sheet('entities/player/standing_still_down.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Player_Standing_Still_Up : get_tiles_from_sheet('entities/player/standing_still_up.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Player_Running_Down : get_tiles_from_sheet('entities/player/running_down.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Player_Running_Up : get_tiles_from_sheet('entities/player/running_up.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Player_Attack : get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 0, 32, 32),


        }
        
        self.assets.update(entities_assets)


    def Asset_Skeleton_Warrior_List(self):
        entities_assets = {
            self.dictionary.Get_Skeleton_Warrior_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_1.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Warrior_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_1_attack.png', 6, 0, 0, 0, 32, 32),

            self.dictionary.Get_Skeleton_Warrior_2: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_2.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Warrior_2_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_2_attack.png', 6, 0, 0, 0, 32, 32),

            self.dictionary.Get_Skeleton_Warrior_3: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_3.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Warrior_3_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_3_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Ranger_List(self):
        entities_assets = {
            self.dictionary.Get_Skeleton_Ranger_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_1.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Ranger_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_1_attack.png', 6, 0, 0, 0, 32, 32),

            self.dictionary.Get_Skeleton_Ranger_2: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_2.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Ranger_2_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_2_attack.png', 6, 0, 0, 0, 32, 32),

            self.dictionary.Get_Skeleton_Ranger_3: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_3.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Ranger_3_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_3_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Cleric_List(self):
        entities_assets = {
            self.dictionary.Get_Skeleton_Cleric_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_cleric/skeleton_cleric_1.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Cleric_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_cleric/skeleton_cleric_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Bell_Toller_List(self):
        entities_assets = {
            self.dictionary.Get_Skeleton_Bell_Toller_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_bell/skeleton_bell_1.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Bell_Toller_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_bell/skeleton_bell_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Undertaker_List(self):
        entities_assets = {
            self.dictionary.Get_Skeleton_Undertaker_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_undertaker/skeleton_undertaker_1.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Undertaker_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_undertaker/skeleton_undertaker_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)



    def Asset_Fire_Spirit_List(self):
        entities_assets = {
            self.dictionary.Get_Fire_Spirit_Idle: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_idle.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Fire_Spirit_Running: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_moving.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Fire_Spirit_Attack: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_attacking.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Ice_Spirit_List(self):
        entities_assets = {
            self.dictionary.Get_Ice_Spirit: get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Ice_Spirit_Attack: get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Wight_King_Spirit_List(self):
        entities_assets = {
            self.dictionary.Get_Wight_King: get_tiles_from_sheet('entities/enemies/undead/wight_king/wight_king.png', 4, 0, 0, 0, 40, 40),
            self.dictionary.Get_Wight_King_Attack: get_tiles_from_sheet('entities/enemies/undead/wight_king/wight_king_attack.png', 6, 0, 0, 0, 40, 40),
        }
        self.assets.update(entities_assets)

    def Asset_Spider_List(self):
        entities_assets = {
            self.dictionary.Get_Spider_Idle: get_tiles_from_sheet('entities/enemies/spider/spider_idle.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Spider_Running: get_tiles_from_sheet('entities/enemies/spider/spider_running.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Friendly_Spider_Idle: get_tiles_from_sheet('entities/enemies/spider/friendly_spider_idle.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Friendly_Spider_Running: get_tiles_from_sheet('entities/enemies/spider/friendly_spider_running.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Spider_Attack: get_tiles_from_sheet('entities/enemies/spider/spider_attacking.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Spider_Jumping: get_tiles_from_sheet('entities/enemies/spider/spider_jumping.png', 8, 0, 0, 0, 32, 32),
            self.dictionary.Get_Spider_On_Back: get_tiles_from_sheet('entities/enemies/spider/spider_on_back.png', 8, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Enemy_Symbols_List(self):
        symbols_assets = {
            self.dictionary.Get_Exclamation_Mark: get_tiles_from_sheet('entities/enemies/symbols/exclamation.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Health_Bar: get_tiles_from_sheet('entities/enemies/symbols/health_bar.png', 9, 0, 0, 0, 32, 32),
        }
        self.assets.update(symbols_assets)

    def Asset_Weapons_List(self):
        Weapons_assets = {
            self.dictionary.Get_Sword: get_tiles_from_sheet('weapons/sword/sword.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Sword_Attack_Cut: get_tiles_from_sheet('weapons/sword/sword.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Get_Sword_Attack_Stab: get_tiles_from_sheet('weapons/sword/sword_attack.png', 3, 0, 0, 0, 32, 32),
            
            self.dictionary.Get_Torch: get_tiles_from_sheet('weapons/torch/torch.png', 8, 0, 0, 0, 32, 32),
            self.dictionary.Get_Torch_Attack_Cut: get_tiles_from_sheet('weapons/torch/torch_attack.png', 8, 0, 0, 0, 32, 32),
            
            self.dictionary.Get_Spear: get_tiles_from_sheet('weapons/spear/spear.png', 8, 0, 0, 0, 32, 32),
            self.dictionary.Get_Spear_Attack_Stab: get_tiles_from_sheet('weapons/spear/spear.png', 8, 0, 0, 0, 32, 32),
            
            self.dictionary.Get_Bow: get_tiles_from_sheet('weapons/bow/bow.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Bow_Attack: get_tiles_from_sheet('weapons/bow/bow_attack.png', 2, 0, 0, 0, 32, 32),
            
            self.dictionary.Get_Arrow: get_tiles_from_sheet('weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Arrow_Attack: get_tiles_from_sheet('weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),

            self.dictionary.Get_Shield: get_tiles_from_sheet('weapons/shield/shields.png', 4, 4, 0, 0, 32, 32),
            self.dictionary.Get_Shield_Attack: get_tiles_from_sheet('weapons/shield/shields.png', 4, 4, 0, 0, 32, 32),

            self.dictionary.Get_Halberd: get_tiles_from_sheet('weapons/halberd/halberd.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Halberd_Attack_Stab: get_tiles_from_sheet('weapons/halberd/halberd_stab_attack.png', 6, 0, 0, 0, 32, 50),
            self.dictionary.Get_Halberd_Attack_Cut: get_tiles_from_sheet('weapons/halberd/halberd_cut_attack.png', 13, 0, 0, 0, 32, 32),

            self.dictionary.Get_Battle_Axe: get_tiles_from_sheet('weapons/battle_axe/battle_axe.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Get_Battle_Axe_Attack_Cut: get_tiles_from_sheet('weapons/battle_axe/battle_axe_cut_attack.png', 15, 0, 0, 0, 32, 32),
            
            self.dictionary.Get_Hammer: get_tiles_from_sheet('weapons/hammer/hammer.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Hammer_Attack_Cut: get_tiles_from_sheet('weapons/hammer/hammer_cut_attack.png', 9, 0, 0, 0, 32, 32),

            self.dictionary.Get_Hatchet: get_tiles_from_sheet('weapons/hatchet/hatchet.png', 7, 0, 0, 0, 32, 32),
            self.dictionary.Get_Hatchet_Attack_Cut: get_tiles_from_sheet('weapons/hatchet/hatchet_cut_attack.png', 8, 0, 0, 0, 32, 32),

            self.dictionary.Get_Warhammer: get_tiles_from_sheet('weapons/warhammer/warhammer.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Get_Warhammer_Attack_Cut: get_tiles_from_sheet('weapons/warhammer/warhammer_cut_attack.png', 12, 0, 0, 0, 32, 32),

            self.dictionary.Get_Crossbow: get_tiles_from_sheet('weapons/crossbow/crossbow.png', 8, 0, 0, 0, 32, 32),
            self.dictionary.Get_Crossbow_Attack: get_tiles_from_sheet('weapons/crossbow/crossbow_attack.png', 2, 0, 0, 0, 32, 32),

            self.dictionary.Get_Bell: get_tiles_from_sheet('weapons/bell/bell.png', 7, 0, 0, 0, 32, 32),
            self.dictionary.Get_Bell_Attack_Cut: get_tiles_from_sheet('weapons/bell/bell_attack_cut.png', 9, 0, 0, 0, 32, 32),

            self.dictionary.Get_Sceptre: get_tiles_from_sheet('weapons/sceptre/sceptre.png', 7, 0, 0, 0, 32, 32),
            self.dictionary.Get_Sceptre_Attack_Cut: get_tiles_from_sheet('weapons/sceptre/sceptre_cut_attack.png', 9, 0, 0, 0, 32, 32),

            self.dictionary.Get_Scythe: get_tiles_from_sheet('weapons/scythe/scythe.png', 7, 0, 0, 0, 32, 32),
            self.dictionary.Get_Scythe_Attack_Cut: get_tiles_from_sheet('weapons/scythe/scythe_attack.png', 9, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)

    def Asset_Weapons_Effects(self):
        Weapons_assets = {
            self.dictionary.Get_Slash_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Slash_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Slash_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Get_Slash_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Slash_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Get_Blunt_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Blunt_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Blunt_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Get_Blunt_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Blunt_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Get_Electric_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Electric_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Electric_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Get_Electric_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Electric_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Get_Fire_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Fire_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Fire_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Get_Fire_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Fire_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Get_Frozen_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Frozen_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Frozen_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Get_Frozen_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Frozen_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Get_Poison_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Poison_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Poison_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Get_Poison_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Poison_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Get_Regen_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Regen_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Regen_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Get_Regen_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Regen_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Get_Vampiric_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Vampiric_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Get_Vampiric_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Get_Vampiric_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Vampiric_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_charge_attack.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)


    def Asset_Inventory(self):
        Weapon_Inventory_assets = {
            self.dictionary.Get_Sword_Shield: get_tiles_from_sheet('inventory/sword_shield.png', 2, 0, 0, 0, 34, 34),
            self.dictionary.Get_Duel_Wield: get_tiles_from_sheet('inventory/Duel_wield.png', 2, 0, 0, 0, 34, 34),
            self.dictionary.Get_Bow_Arrow: get_tiles_from_sheet('inventory/Bow_Arrow.png', 2, 0, 0, 0, 34, 34),
            self.dictionary.Get_Left_Right: get_tiles_from_sheet('inventory/left_right.png', 2, 0, 0, 0, 34, 34),
            self.dictionary.Get_Rune_Background: get_tiles_from_sheet('inventory/rune_background.png', 1, 0, 0, 0, 34, 34),
        }
        self.assets.update(Weapon_Inventory_assets)

    def Asset_Interative_Objects_List(self):
        white = (255,255,255)
        Objects_assets = {
            self.dictionary.Get_Chest: get_tiles_from_sheet('decoration/chest.png', 8, 0, 0, 0, 32, 32, white),
            self.dictionary.Get_Door_Basic: get_tiles_from_sheet('decoration/door/door_closed.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Rune_Shrine: get_tiles_from_sheet('decoration/shrine/rune_shrine.png', 3, 0, 0, 0, 64, 64),
            self.dictionary.Get_Portal_Shrine: get_tiles_from_sheet('decoration/shrine/portal_shrine.png', 3, 0, 0, 0, 64, 64),
            self.dictionary.Get_Bones: get_tiles_from_sheet('decoration/environment/bones.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(Objects_assets)




    def Asset_Environment_List(self):
        Environment_assets = {
            self.dictionary.Get_Lava_Env: get_tiles_from_sheet('environment/lava.png', 2, 0, 0, 0, 32, 32),
            self.dictionary.Get_Shawlow_Water_Env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 0, 32, 32),
            self.dictionary.Get_Medium_Water_Env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            self.dictionary.Get_Deep_Water_Env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            self.dictionary.Get_Shawlow_Ice_Env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 0, 32, 32),
            self.dictionary.Get_Medium_Ice_Env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
            self.dictionary.Get_Deep_Ice_Env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
        }
        self.assets.update(Environment_assets)


    def Asset_Decoration_List(self):
        decoration_assets = {
        }
        self.assets.update(decoration_assets)


    def Asset_Potion_List(self):
        potion_assets = {
            self.dictionary.Get_Empty_Bottle: get_tiles_from_sheet('Potions/Healing_potions/empty.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Invisibility_Full: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Invisibility_Half: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Invisibility_Low: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Healing_Full: get_tiles_from_sheet('Potions/Healing_potions/healing_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Healing_Half: get_tiles_from_sheet('Potions/Healing_potions/healing_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Healing_Low: get_tiles_from_sheet('Potions/Healing_potions/healing_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Increase_Souls_Full: get_tiles_from_sheet('Potions/soul_potions/soul_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Increase_Souls_Half: get_tiles_from_sheet('Potions/soul_potions/soul_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Increase_Souls_Low: get_tiles_from_sheet('Potions/soul_potions/soul_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.Get_Arcane_Hunger_Full: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Arcane_Hunger_Half: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Arcane_Hunger_Low: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Speed_Full: get_tiles_from_sheet('Potions/speed_potions/speed_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Speed_Half: get_tiles_from_sheet('Potions/speed_potions/speed_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Speed_Low: get_tiles_from_sheet('Potions/speed_potions/speed_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Green_Full: get_tiles_from_sheet('Potions/Greenpotions/green_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Green_Half: get_tiles_from_sheet('Potions/Greenpotions/green_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Green_Low: get_tiles_from_sheet('Potions/Greenpotions/green_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Increase_Strength_Full: get_tiles_from_sheet('Potions/strength_potions/strength_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Increase_Strength_Half: get_tiles_from_sheet('Potions/strength_potions/strength_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Increase_Strength_Low: get_tiles_from_sheet('Potions/strength_potions/strength_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Poison_Resistance_Full: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Poison_Resistance_Half: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Poison_Resistance_Low: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Purple_Full: get_tiles_from_sheet('Potions/Purplepotions/Purple_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Purple_Half: get_tiles_from_sheet('Potions/Purplepotions/Purple_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Purple_Low: get_tiles_from_sheet('Potions/Purplepotions/Purple_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Frozen_Resistance_Full: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Frozen_Resistance_Half: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Frozen_Resistance_Low: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Silence_Full: get_tiles_from_sheet('Potions/silence_potions/silence_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Silence_Half: get_tiles_from_sheet('Potions/silence_potions/silence_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Silence_Low: get_tiles_from_sheet('Potions/silence_potions/silence_low.png', 2, 2, 0, 0, 32, 32),
            
            self.dictionary.Get_Regen_Full: get_tiles_from_sheet('Potions/regen_potions/regen_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Regen_Half: get_tiles_from_sheet('Potions/regen_potions/regen_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.Get_Regen_Low: get_tiles_from_sheet('Potions/regen_potions/regen_low.png', 2, 2, 0, 0, 32, 32),
        }
        self.assets.update(potion_assets)



    def Asset_Loot(self):
        loot = {
            self.dictionary.Get_Gold: get_tiles_from_sheet('items/valuables/gold_coins.png', 3, 0, 0, 0, 16, 16),
            self.dictionary.Get_Echo_Bell: get_tiles_from_sheet('items/utility/echo_bell.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Shadow_Cloak: get_tiles_from_sheet('items/utility/shadow_cloak.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Lantern: get_tiles_from_sheet('items/passive/lantern.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Anchor_Stone: get_tiles_from_sheet('items/passive/anchor_stone.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Blood_Tomb: get_tiles_from_sheet('items/cursed/blood_tomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Faith_Pendant: get_tiles_from_sheet('items/passive/faith_pendant.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Lucky_Charm: get_tiles_from_sheet('items/passive/lucky_charm.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Magnet: get_tiles_from_sheet('items/passive/magnet.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Power_Totem: get_tiles_from_sheet('items/passive/power_totem.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Strength_Totem: get_tiles_from_sheet('items/passive/strength_totem.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Halo: get_tiles_from_sheet('items/passive/halo.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Muffled_Boots: get_tiles_from_sheet('items/passive/muffled_boots.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Demonic_Bargain: get_tiles_from_sheet('items/cursed/demonic_bargain.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Temptress_Embrace: get_tiles_from_sheet('items/cursed/temptress_embrace.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Blood_Coin: get_tiles_from_sheet('items/revive/blood_coin.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Blood_Pact: get_tiles_from_sheet('items/revive/blood_pact.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Phoenix_Feather: get_tiles_from_sheet('items/revive/phoenix_feather.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Light_Pendant: get_tiles_from_sheet('items/revive/light_pendant.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Faded_Hourglass: get_tiles_from_sheet('items/utility/faded_hourglass.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Get_Ethereal_Chains: get_tiles_from_sheet('items/utility/ethereal_chains.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Recall_Scroll: get_tiles_from_sheet('items/utility/recall_parchment.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Echo_Sigil: get_tiles_from_sheet('items/passive/echo_sigil.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)


    def Asset_Keys(self):
        loot = {
            self.dictionary.Get_Lockpick: get_tiles_from_sheet('items/keys/lockpick.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Blood_Key: get_tiles_from_sheet('items/keys/blood_key.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Skeleton_Key: get_tiles_from_sheet('items/keys/skeleton_key.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Soul_Key: get_tiles_from_sheet('items/keys/soul_key.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Cursed_Key: get_tiles_from_sheet('items/keys/cursed_key.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Bombs(self):
        loot = {
            self.dictionary.Get_Fire_Bomb: get_tiles_from_sheet('items/bombs/fire_bomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Frozen_Bomb: get_tiles_from_sheet('items/bombs/frozen_bomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Electric_Bomb: get_tiles_from_sheet('items/bombs/electric_bomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Poison_Bomb: get_tiles_from_sheet('items/bombs/poison_bomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Get_Vampiric_Bomb: get_tiles_from_sheet('items/bombs/vampiric_bomb.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Rune(self):
        rune = {
            self.dictionary.Get_Healing_Rune: get_tiles_from_sheet('runes/healing_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Regen_Rune: get_tiles_from_sheet('runes/regen_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Dash_Rune: get_tiles_from_sheet('runes/dash_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Arcane_Conduit_Rune: get_tiles_from_sheet('runes/arcane_conduit_rune.png', 1, 0, 0, 0, 32, 32),
            
            self.dictionary.Get_Fire_Circle_Rune: get_tiles_from_sheet('runes/fire/fire_cirlce_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Fire_Resistance_Rune: get_tiles_from_sheet('runes/fire/fire_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Fire_Shield_Rune: get_tiles_from_sheet('runes/fire/fire_shield_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Fire_Spray_Rune: get_tiles_from_sheet('runes/fire/fire_spray_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Fire_Ball_Rune: get_tiles_from_sheet('runes/fire/fire_ball_rune.png', 1, 0, 0, 0, 32, 32),

            self.dictionary.Get_Freeze_Circle_Rune: get_tiles_from_sheet('runes/frost/frost_circle_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Frozen_Resistance_Rune: get_tiles_from_sheet('runes/frost/frost_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Freeze_Storm_Rune: get_tiles_from_sheet('runes/frost/frost_storm_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Freeze_Spray_Rune: get_tiles_from_sheet('runes/frost/frost_spray_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Freeze_Ball_Rune: get_tiles_from_sheet('runes/frost/frost_ball_rune.png', 1, 0, 0, 0, 32, 32),
            
            self.dictionary.Get_Poison_Resistance_Rune: get_tiles_from_sheet('runes/poison/poison_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Poison_Ball_Rune: get_tiles_from_sheet('runes/poison/poison_ball_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Poison_Cloud_Rune: get_tiles_from_sheet('runes/poison/poison_cloud_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Poison_Plume_Rune: get_tiles_from_sheet('runes/poison/poison_plume_rune.png', 1, 0, 0, 0, 32, 32),

            self.dictionary.Get_Electric_Resistance_Rune: get_tiles_from_sheet('runes/electric/electric_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Electric_Ball_Rune: get_tiles_from_sheet('runes/electric/electric_ball_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Electric_Spray_Rune: get_tiles_from_sheet('runes/electric/electric_spray_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Chain_Lightning_Rune: get_tiles_from_sheet('runes/electric/chain_lightning_rune.png', 1, 0, 0, 0, 32, 32),
            
            self.dictionary.Get_Soul_Reap_Rune: get_tiles_from_sheet('runes/vampiric/soul_reap_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Soul_Pit_Rune: get_tiles_from_sheet('runes/vampiric/soul_pit_rune.png', 1, 0, 0, 0, 32, 32),

            self.dictionary.Get_Invisibility_Rune: get_tiles_from_sheet('runes/invisibility_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Key_Rune: get_tiles_from_sheet('runes/key_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Light_Rune: get_tiles_from_sheet('runes/light_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Resistance_Rune: get_tiles_from_sheet('runes/resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Shield_Rune: get_tiles_from_sheet('runes/shield_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Silence_Rune: get_tiles_from_sheet('runes/silence_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Speed_Rune: get_tiles_from_sheet('runes/speed_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Increase_Strength_Rune: get_tiles_from_sheet('runes/strength_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Vampiric_Rune: get_tiles_from_sheet('runes/vampiric_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Arcane_Hunger_Rune: get_tiles_from_sheet('runes/hunger_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Magnet_Rune: get_tiles_from_sheet('runes/magnet_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.Get_Invulnerable_Rune: get_tiles_from_sheet('runes/invulnerable_rune.png', 1, 0, 0, 0, 32, 32),
        }
        self.assets.update(rune)


    def Asset_Font(self):
        font = {
            self.dictionary.Get_Font: get_tiles_from_sheet('font/font.png', 7, 5, 0, 0, 16, 16),
            self.dictionary.Get_Player_Damage_Font: get_tiles_from_sheet('font/player_damage_font.png', 7, 5, 0, 0, 16, 16),
            self.dictionary.Get_Small_Font: get_tiles_from_sheet('font/small_font.png', 7, 5, 0, 0, 8, 8),
            self.dictionary.Get_Floating_E: get_tiles_from_sheet('font/floating_e.png', 1, 0, 0, 0, 16, 16),
            self.dictionary.Get_Symbols: get_tiles_from_sheet('font/symbols.png', 7, 5, 0, 0, 16, 16),
            self.dictionary.Get_Souls: get_tiles_from_sheet('font/souls.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(font)

    def Asset_Health_Bar(self):
        health_bars = {
            self.dictionary.Get_Healthbar_1: get_tiles_from_sheet('ui/healthbar_1.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_2: get_tiles_from_sheet('ui/healthbar_2.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_3: get_tiles_from_sheet('ui/healthbar_3.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_4: get_tiles_from_sheet('ui/healthbar_4.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_5: get_tiles_from_sheet('ui/healthbar_5.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_6: get_tiles_from_sheet('ui/healthbar_6.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_7: get_tiles_from_sheet('ui/healthbar_7.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_8: get_tiles_from_sheet('ui/healthbar_8.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_9: get_tiles_from_sheet('ui/healthbar_9.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Get_Healthbar_10: get_tiles_from_sheet('ui/healthbar_10.png', 5, 0, 0, 0, 64, 64),
        }
        self.assets.update(health_bars)

    def Asset_Menu(self):
        menu = {
            self.dictionary.Get_Loading_Bar: get_tiles_from_sheet('menu/loading_screen.png', 6, 0, 0, 0, 96, 96),
        }
        self.assets.update(menu)

    def Asset_Tooltips(self):
        tooltips = {
            self.dictionary.Get_Radius_Tooltip: get_tiles_from_sheet('items/tooltips/radius.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(tooltips)

