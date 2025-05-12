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
            self.dictionary.Floor : get_tiles_from_sheet('crypt_assets/crypt_floor.png', 5, 1, 0, 0, 32, 32),
            self.dictionary.Wall_Top : get_tiles_from_sheet('crypt_assets/wall_top.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Wall_Left : get_tiles_from_sheet('crypt_assets/wall_left.png', 0, 3, 0, 0, 32, 32),
            self.dictionary.Wall_Right : get_tiles_from_sheet('crypt_assets/wall_right.png', 0, 3, 0, 0, 32, 32),
            self.dictionary.Wall_Middle : get_tiles_from_sheet('crypt_assets/wall_middle.png', 0, 3, 0, 0, 32, 32),
            self.dictionary.Wall_Bottom : get_tiles_from_sheet('crypt_assets/wall_bottom.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Wall_Bottom_Corner : get_tiles_from_sheet('crypt_assets/wall_bottom_corner.png', 2, 0, 0, 0, 32, 32),
        }
        self.assets.update(tiles_assets)

    def Asset_Trap_List(self):
        white = (255,255,255)
        trap_assets = {
            self.dictionary.Spike_Trap : get_tiles_from_sheet('traps/spike_trap.png', 6, 0, 0, 0, 32, 32, white),
            self.dictionary.Spike_Poison_Trap : get_tiles_from_sheet('traps/Spike_Trap_poison.png', 13, 0, 0, 0, 32, 32, white),
            self.dictionary.Pit_Trap : get_tiles_from_sheet('traps/Pit_Trap_Spikes.png', 1, 0, 0, 0, 32, 32, white),
            self.dictionary.Fire_Trap : get_tiles_from_sheet('traps/Fire_Trap.png', 13, 0, 0, 0, 32, 20, white),
            self.dictionary.Spider_Web_Trap : get_tiles_from_sheet('entities/enemies/spider/spider_web.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Poison_Plume_Trap : get_tiles_from_sheet('traps/poison_plume.png', 7, 0, 0, 0, 32, 32),
        }

        self.assets.update(trap_assets)

    def Asset_Particles_List(self):
        effect_assets = {
            self.dictionary.Dash_Particle : get_tiles_from_sheet('particles/general/dash.png', 5, 0, 0, 0, 5, 5),
            self.dictionary.Fire_Particle : get_tiles_from_sheet('particles/general/fire.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Spark_Particle : get_tiles_from_sheet('particles/general/spark.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Blood_Particle : get_tiles_from_sheet('particles/general/blood.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Bone_Particle : get_tiles_from_sheet('particles/general/bone.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Electric_Particle : get_tiles_from_sheet('particles/general/electric.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Frost_Particle : get_tiles_from_sheet('particles/general/frost.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Gold_Particle : get_tiles_from_sheet('particles/general/gold.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Poison_Particle : get_tiles_from_sheet('particles/general/poison.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Vampire_Particle : get_tiles_from_sheet('particles/general/vampire.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Soul_Particle : get_tiles_from_sheet('particles/general/soul.png', 5, 0, 0, 0, 3, 3),
            self.dictionary.Player_Particle : get_tiles_from_sheet('particles/general/player.png', 5, 0, 0, 0, 3, 3),
        }
        self.assets.update(effect_assets)

    def Asset_Effect_List(self):
        white = (255,255,255)
        effect_assets = {
            self.dictionary.Heart : load_image('heart.png'),
            self.dictionary.Coin : get_tiles_from_sheet('coin_.png', 3, 0, 0, 0, 13, 13, white),
            self.dictionary.Fire_Effect : get_tiles_from_sheet('particles/effects/fire/orange/loops/burning_loop_1.png', 7, 0, 0, 0, 32, 32, white),
            self.dictionary.Poison_Effect : get_tiles_from_sheet('particles/effects/poison.png', 2, 0, 0, 0, 32, 32, white),
            self.dictionary.Frozen_Effect : get_tiles_from_sheet('particles/effects/frozen.png', 2, 0, 0, 0, 32, 32, white),
            self.dictionary.Wet_Effect : get_tiles_from_sheet('particles/effects/wet.png', 2, 0, 0, 0, 32, 32),
            self.dictionary.Regen_Effect : get_tiles_from_sheet('particles/effects/regen.png', 2, 1, 0, 0, 32, 32),
            self.dictionary.Electric_Effect : get_tiles_from_sheet('particles/effects/electric.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Invincible_Effect : get_tiles_from_sheet('particles/effects/invincible.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(effect_assets)
    
    def Asset_Magic_Attack_List(self):
        particle_assets = {
       self.dictionary.Fire_Particle_Attack : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_particle.png', 3, 0, 0, 0, 4, 4),
       self.dictionary.Fire_Ball : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_ball.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Fire_Explosion : get_tiles_from_sheet('weapons/magic_attacks/fire/fire_explosion.png', 7, 0, 0, 0, 32, 32),

       self.dictionary.Ice_Particle_Attack : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_particle.png', 3, 0, 0, 0, 4, 4),
       self.dictionary.Ice_Ball : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_ball.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Ice_Explosion : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_explosion.png', 5, 0, 0, 0, 32, 32),
       self.dictionary.Ice_Storm : get_tiles_from_sheet('weapons/magic_attacks/ice/ice_storm.png', 9, 0, 0, 0, 32, 32),

       self.dictionary.Poison_Particle_Attack : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_particle.png', 3, 0, 0, 0, 4, 4),
       self.dictionary.Poison_Ball : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_ball.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Poison_Explosion : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_explosion.png', 5, 0, 0, 0, 32, 32),
       self.dictionary.Poison_Cloud : get_tiles_from_sheet('weapons/magic_attacks/poison/poison_cloud.png', 3, 0, 0, 0, 32, 32),


       self.dictionary.Electric_Particle_Attack : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_particle.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Electric_Ball : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_ball.png', 0, 0, 0, 0, 16, 16),
       self.dictionary.Electric_Explosion : get_tiles_from_sheet('weapons/magic_attacks/electric/electric_explosion.png', 5, 0, 0, 0, 32, 32),

        self.dictionary.Soul_Reap : get_tiles_from_sheet('weapons/magic_attacks/vampiric/soul_reap.png', 0, 0, 0, 0, 32, 32),
        self.dictionary.Vampiric_Ball : get_tiles_from_sheet('weapons/magic_attacks/vampiric/vampiric_ball.png', 0, 0, 0, 0, 16, 16),
        self.dictionary.Soul_Pit : get_tiles_from_sheet('weapons/magic_attacks/vampiric/soul_pit.png', 6, 0, 0, 0, 32, 32),
        
        }
        self.assets.update(particle_assets)


    def Asset_Player_List(self):
        entities_assets = {

            self.dictionary.Player_Idle_Down : get_tiles_from_sheet('entities/player/idle_down.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Player_Idle_Up : get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Player_Standing_Still_Down : get_tiles_from_sheet('entities/player/standing_still_down.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Player_Standing_Still_Up : get_tiles_from_sheet('entities/player/standing_still_up.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Player_Running_Down : get_tiles_from_sheet('entities/player/running_down.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Player_Running_Up : get_tiles_from_sheet('entities/player/running_up.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Player_Attack : get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 0, 32, 32),


        }
        
        self.assets.update(entities_assets)


    def Asset_Skeleton_Warrior_List(self):
        entities_assets = {
            self.dictionary.Skeleton_Warrior_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_1.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Warrior_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_1_attack.png', 6, 0, 0, 0, 32, 32),

            self.dictionary.Skeleton_Warrior_2: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_2.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Warrior_2_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_2_attack.png', 6, 0, 0, 0, 32, 32),

            self.dictionary.Skeleton_Warrior_3: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_3.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Warrior_3_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_warrior/skeleton_warrior_3_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Ranger_List(self):
        entities_assets = {
            self.dictionary.Skeleton_Ranger_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_1.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Ranger_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_1_attack.png', 6, 0, 0, 0, 32, 32),

            self.dictionary.Skeleton_Ranger_2: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_2.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Ranger_2_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_2_attack.png', 6, 0, 0, 0, 32, 32),

            self.dictionary.Skeleton_Ranger_3: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_3.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Ranger_3_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_ranger/skeleton_ranger_3_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Cleric_List(self):
        entities_assets = {
            self.dictionary.Skeleton_Cleric_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_cleric/skeleton_cleric_1.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Cleric_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_cleric/skeleton_cleric_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Bell_Toller_List(self):
        entities_assets = {
            self.dictionary.Skeleton_Bell_Toller_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_bell/skeleton_bell_1.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Bell_Toller_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_bell/skeleton_bell_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Undertaker_List(self):
        entities_assets = {
            self.dictionary.Skeleton_Undertaker_1: get_tiles_from_sheet('entities/enemies/undead/skeleton_undertaker/skeleton_undertaker_1.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Skeleton_Undertaker_1_Attack: get_tiles_from_sheet('entities/enemies/undead/skeleton_undertaker/skeleton_undertaker_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)



    def Asset_Fire_Spirit_List(self):
        entities_assets = {
            self.dictionary.Fire_Spirit_Idle: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_idle.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Fire_Spirit_Running: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_moving.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Fire_Spirit_Attack: get_tiles_from_sheet('entities/enemies/fire_spirit/fire_spirit_attacking.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Ice_Spirit_List(self):
        entities_assets = {
            self.dictionary.Ice_Spirit: get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Ice_Spirit_Attack: get_tiles_from_sheet('entities/enemies/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Wight_King_Spirit_List(self):
        entities_assets = {
            self.dictionary.Wight_King: get_tiles_from_sheet('entities/enemies/undead/wight_king/wight_king.png', 4, 0, 0, 0, 40, 40),
            self.dictionary.Wight_King_Attack: get_tiles_from_sheet('entities/enemies/undead/wight_king/wight_king_attack.png', 6, 0, 0, 0, 40, 40),
        }
        self.assets.update(entities_assets)

    def Asset_Spider_List(self):
        entities_assets = {
            self.dictionary.Spider_Idle: get_tiles_from_sheet('entities/enemies/spider/spider_idle.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Spider_Running: get_tiles_from_sheet('entities/enemies/spider/spider_running.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Friendly_Spider_Idle: get_tiles_from_sheet('entities/enemies/spider/friendly_spider_idle.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Friendly_Spider_Running: get_tiles_from_sheet('entities/enemies/spider/friendly_spider_running.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.Spider_Attack: get_tiles_from_sheet('entities/enemies/spider/spider_attacking.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Spider_Jumping: get_tiles_from_sheet('entities/enemies/spider/spider_jumping.png', 8, 0, 0, 0, 32, 32),
            self.dictionary.Spider_On_Back: get_tiles_from_sheet('entities/enemies/spider/spider_on_back.png', 8, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Enemy_Symbols_List(self):
        symbols_assets = {
            self.dictionary.Exclamation_Mark: get_tiles_from_sheet('entities/enemies/symbols/exclamation.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Health_Bar: get_tiles_from_sheet('entities/enemies/symbols/health_bar.png', 9, 0, 0, 0, 32, 32),
        }
        self.assets.update(symbols_assets)

    def Asset_Weapons_List(self):
        Weapons_assets = {
            self.dictionary.Sword: get_tiles_from_sheet('weapons/sword/sword.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Sword_Attack_Cut: get_tiles_from_sheet('weapons/sword/sword.png', 3, 0, 0, 0, 32, 32),
            self.dictionary.Sword_Attack_Stab: get_tiles_from_sheet('weapons/sword/sword_attack.png', 3, 0, 0, 0, 32, 32),
            
            self.dictionary.Torch: get_tiles_from_sheet('weapons/torch/torch.png', 8, 0, 0, 0, 32, 32),
            self.dictionary.Torch_Attack_Cut: get_tiles_from_sheet('weapons/torch/torch_attack.png', 8, 0, 0, 0, 32, 32),
            
            self.dictionary.Spear: get_tiles_from_sheet('weapons/spear/spear.png', 8, 0, 0, 0, 32, 32),
            self.dictionary.Spear_Attack_Stab: get_tiles_from_sheet('weapons/spear/spear.png', 8, 0, 0, 0, 32, 32),
            
            self.dictionary.Bow: get_tiles_from_sheet('weapons/bow/bow.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Bow_Attack: get_tiles_from_sheet('weapons/bow/bow_attack.png', 2, 0, 0, 0, 32, 32),
            
            self.dictionary.Arrow: get_tiles_from_sheet('weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Arrow_Attack: get_tiles_from_sheet('weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),

            self.dictionary.Shield: get_tiles_from_sheet('weapons/shield/shields.png', 4, 4, 0, 0, 32, 32),
            self.dictionary.Shield_Attack: get_tiles_from_sheet('weapons/shield/shields.png', 4, 4, 0, 0, 32, 32),

            self.dictionary.Halberd: get_tiles_from_sheet('weapons/halberd/halberd.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Halberd_Attack_Stab: get_tiles_from_sheet('weapons/halberd/halberd_stab_attack.png', 6, 0, 0, 0, 32, 50),
            self.dictionary.Halberd_Attack_Cut: get_tiles_from_sheet('weapons/halberd/halberd_cut_attack.png', 13, 0, 0, 0, 32, 32),

            self.dictionary.Battle_Axe: get_tiles_from_sheet('weapons/battle_axe/battle_axe.png', 5, 0, 0, 0, 32, 32),
            self.dictionary.Battle_Axe_Attack_Cut: get_tiles_from_sheet('weapons/battle_axe/battle_axe_cut_attack.png', 15, 0, 0, 0, 32, 32),
            
            self.dictionary.Hammer: get_tiles_from_sheet('weapons/hammer/hammer.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Hammer_Attack_Cut: get_tiles_from_sheet('weapons/hammer/hammer_cut_attack.png', 9, 0, 0, 0, 32, 32),

            self.dictionary.Hatchet: get_tiles_from_sheet('weapons/hatchet/hatchet.png', 7, 0, 0, 0, 32, 32),
            self.dictionary.Hatchet_Attack_Cut: get_tiles_from_sheet('weapons/hatchet/hatchet_cut_attack.png', 8, 0, 0, 0, 32, 32),

            self.dictionary.Warhammer: get_tiles_from_sheet('weapons/warhammer/warhammer.png', 6, 0, 0, 0, 32, 32),
            self.dictionary.Warhammer_Attack_Cut: get_tiles_from_sheet('weapons/warhammer/warhammer_cut_attack.png', 12, 0, 0, 0, 32, 32),

            self.dictionary.Crossbow: get_tiles_from_sheet('weapons/crossbow/crossbow.png', 8, 0, 0, 0, 32, 32),
            self.dictionary.Crossbow_Attack: get_tiles_from_sheet('weapons/crossbow/crossbow_attack.png', 2, 0, 0, 0, 32, 32),

            self.dictionary.Bell: get_tiles_from_sheet('weapons/bell/bell.png', 7, 0, 0, 0, 32, 32),
            self.dictionary.Bell_Attack_Cut: get_tiles_from_sheet('weapons/bell/bell_attack_cut.png', 9, 0, 0, 0, 32, 32),

            self.dictionary.Sceptre: get_tiles_from_sheet('weapons/sceptre/sceptre.png', 7, 0, 0, 0, 32, 32),
            self.dictionary.Sceptre_Attack_Cut: get_tiles_from_sheet('weapons/sceptre/sceptre_cut_attack.png', 9, 0, 0, 0, 32, 32),

            self.dictionary.Scythe: get_tiles_from_sheet('weapons/scythe/scythe.png', 7, 0, 0, 0, 32, 32),
            self.dictionary.Scythe_Attack_Cut: get_tiles_from_sheet('weapons/scythe/scythe_attack.png', 9, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)

    def Asset_Weapons_Effects(self):
        Weapons_assets = {
            self.dictionary.Slash_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Slash_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Slash_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Slash_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Slash_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/slash_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Blunt_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Blunt_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Blunt_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Blunt_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Blunt_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/blunt_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Electric_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Electric_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Electric_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Electric_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Electric_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/electric_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Fire_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Fire_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Fire_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Fire_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Fire_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/fire_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Frozen_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Frozen_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Frozen_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Frozen_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Frozen_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/frozen_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Poison_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Poison_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Poison_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Poison_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Poison_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/poison_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Regen_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Regen_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Regen_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Regen_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Regen_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/regen_charge_attack.png', 5, 0, 0, 0, 32, 32),

            self.dictionary.Vampiric_Cut_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_cut_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Vampiric_Stab_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_stab_attack.png', 6, 0, 0, 0, 64, 64),
            self.dictionary.Vampiric_Spin_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_spin_attack.png', 7, 0, 0, 0, 64, 64),
            self.dictionary.Vampiric_Smash_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_smash_attack.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.Vampiric_Charge_Effect: get_tiles_from_sheet('weapons/weapon_effects/vampiric_charge_attack.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)


    def Asset_Inventory(self):
        Weapon_Inventory_assets = {
            self.dictionary.Sword_Shield: get_tiles_from_sheet('inventory/sword_shield.png', 2, 0, 0, 0, 34, 34),
            self.dictionary.Duel_Wield: get_tiles_from_sheet('inventory/Duel_wield.png', 2, 0, 0, 0, 34, 34),
            self.dictionary.Bow_Arrow: get_tiles_from_sheet('inventory/Bow_Arrow.png', 2, 0, 0, 0, 34, 34),
            self.dictionary.Left_Right: get_tiles_from_sheet('inventory/left_right.png', 2, 0, 0, 0, 34, 34),
            self.dictionary.Rune_Background: get_tiles_from_sheet('inventory/rune_background.png', 1, 0, 0, 0, 34, 34),
        }
        self.assets.update(Weapon_Inventory_assets)

    def Asset_Interative_Objects_List(self):
        white = (255,255,255)
        Objects_assets = {
            self.dictionary.Chest: get_tiles_from_sheet('decoration/chest.png', 8, 0, 0, 0, 32, 32, white),
            self.dictionary.Door_Basic: get_tiles_from_sheet('decoration/door/door_closed.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.Rune_Shrine: get_tiles_from_sheet('decoration/shrine/rune_shrine.png', 3, 0, 0, 0, 64, 64),
            self.dictionary.Portal_Shrine: get_tiles_from_sheet('decoration/shrine/portal_shrine.png', 3, 0, 0, 0, 64, 64),
            self.dictionary.Bones: get_tiles_from_sheet('decoration/environment/bones.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(Objects_assets)




    def Asset_Environment_List(self):
        Environment_assets = {
            self.dictionary.Lava_Env: get_tiles_from_sheet('environment/lava.png', 2, 0, 0, 0, 32, 32),
            self.dictionary.Shawlow_Water_Env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 0, 32, 32),
            self.dictionary.Medium_Water_Env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            self.dictionary.Deep_Water_Env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            self.dictionary.Shawlow_Ice_Env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 0, 32, 32),
            self.dictionary.Medium_Ice_Env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
            self.dictionary.Deep_Ice_Env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
        }
        self.assets.update(Environment_assets)


    def Asset_Decoration_List(self):
        decoration_assets = {
        }
        self.assets.update(decoration_assets)


    def Asset_Potion_List(self):
        potion_assets = {
            self.dictionary.empty_bottle: get_tiles_from_sheet('Potions/Healing_potions/empty.png', 0, 0, 0, 0, 32, 32),

            self.dictionary.invisibility + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.invisibility + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.invisibility + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.healing + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/Healing_potions/healing_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.healing + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/Healing_potions/healing_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.healing + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/Healing_potions/healing_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.increase_souls + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/soul_potions/soul_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.increase_souls + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/soul_potions/soul_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.increase_souls + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/soul_potions/soul_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.arcane_hunger + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.arcane_hunger + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.arcane_hunger + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/soul_potions/arcane_hunger_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.speed + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/speed_potions/speed_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.speed + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/speed_potions/speed_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.speed + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/speed_potions/speed_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.green + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/Greenpotions/green_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.green + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/Greenpotions/green_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.green + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/Greenpotions/green_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.increase_strength + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/strength_potions/strength_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.increase_strength + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/strength_potions/strength_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.increase_strength + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/strength_potions/strength_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.poison_resistance + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.poison_resistance + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.poison_resistance + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/poison_resistance_potions/poison_resistance_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.purple + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/Purplepotions/Purple_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.purple + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/Purplepotions/Purple_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.purple + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/Purplepotions/Purple_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.frozen_resistance + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.frozen_resistance + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.frozen_resistance + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/freeze_resistance_potions/freeze_resistance_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.silence + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/silence_potions/silence_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.silence + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/silence_potions/silence_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.silence + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/silence_potions/silence_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.regen + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/regen_potions/regen_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.regen + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/regen_potions/regen_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.regen + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/regen_potions/regen_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.vampiric + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/vampiric_potions/vampiric_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.vampiric + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/vampiric_potions/vampiric_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.vampiric + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/vampiric_potions/vampiric_low.png', 2, 2, 0, 0, 32, 32),

            self.dictionary.fire_resistance + '_' + self.dictionary.full: get_tiles_from_sheet('Potions/fire_resistance_potions/fire_resistance_full.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.fire_resistance + '_' + self.dictionary.half: get_tiles_from_sheet('Potions/fire_resistance_potions/fire_resistance_half.png', 2, 2, 0, 0, 32, 32),
            self.dictionary.fire_resistance + '_' + self.dictionary.low: get_tiles_from_sheet('Potions/fire_resistance_potions/fire_resistance_low.png', 2, 2, 0, 0, 32, 32),
        }

        self.assets.update(potion_assets)




    def Asset_Loot(self):
        loot = {
            self.dictionary.gold: get_tiles_from_sheet('items/valuables/gold_coins.png', 3, 0, 0, 0, 16, 16),
            self.dictionary.echo_bell: get_tiles_from_sheet('items/utility/echo_bell.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.shadow_cloak: get_tiles_from_sheet('items/utility/shadow_cloak.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.lantern: get_tiles_from_sheet('items/passive/lantern.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.anchor_stone: get_tiles_from_sheet('items/passive/anchor_stone.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.blood_tomb: get_tiles_from_sheet('items/cursed/blood_tomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.faith_pendant: get_tiles_from_sheet('items/passive/faith_pendant.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.lucky_charm: get_tiles_from_sheet('items/passive/lucky_charm.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.magnet: get_tiles_from_sheet('items/passive/magnet.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.power_totem: get_tiles_from_sheet('items/passive/power_totem.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.strength_totem: get_tiles_from_sheet('items/passive/strength_totem.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.halo: get_tiles_from_sheet('items/passive/halo.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.muffled_boots: get_tiles_from_sheet('items/passive/muffled_boots.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.demonic_bargain: get_tiles_from_sheet('items/cursed/demonic_bargain.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.temptress_embrace: get_tiles_from_sheet('items/cursed/temptress_embrace.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.blood_coin: get_tiles_from_sheet('items/revive/blood_coin.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.blood_pact: get_tiles_from_sheet('items/revive/blood_pact.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.phoenix_feather: get_tiles_from_sheet('items/revive/phoenix_feather.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.light_pendant: get_tiles_from_sheet('items/revive/light_pendant.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.faded_hourglass: get_tiles_from_sheet('items/utility/faded_hourglass.png', 4, 0, 0, 0, 32, 32),
            self.dictionary.ethereal_chains: get_tiles_from_sheet('items/utility/ethereal_chains.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.recall_scroll: get_tiles_from_sheet('items/utility/recall_parchment.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.echo_sigil: get_tiles_from_sheet('items/passive/echo_sigil.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)


    def Asset_Keys(self):
        loot = {
            self.dictionary.lockpick: get_tiles_from_sheet('items/keys/lockpick.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.blood_key: get_tiles_from_sheet('items/keys/blood_key.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.skeleton_key: get_tiles_from_sheet('items/keys/skeleton_key.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.soul_key: get_tiles_from_sheet('items/keys/soul_key.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.cursed_key: get_tiles_from_sheet('items/keys/cursed_key.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Bombs(self):
        loot = {
            self.dictionary.fire_bomb: get_tiles_from_sheet('items/bombs/fire_bomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.frozen_bomb: get_tiles_from_sheet('items/bombs/frozen_bomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.electric_bomb: get_tiles_from_sheet('items/bombs/electric_bomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.poison_bomb: get_tiles_from_sheet('items/bombs/poison_bomb.png', 0, 0, 0, 0, 32, 32),
            self.dictionary.vampiric_bomb: get_tiles_from_sheet('items/bombs/vampiric_bomb.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Rune(self):
        rune = {
            self.dictionary.healing_rune: get_tiles_from_sheet('runes/healing_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.regen_rune: get_tiles_from_sheet('runes/regen_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.dash_rune: get_tiles_from_sheet('runes/dash_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.arcane_conduit_rune: get_tiles_from_sheet('runes/arcane_conduit_rune.png', 1, 0, 0, 0, 32, 32),
            
            self.dictionary.fire_cirlce_rune: get_tiles_from_sheet('runes/fire/fire_cirlce_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.fire_resistance_rune: get_tiles_from_sheet('runes/fire/fire_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.fire_shield_rune: get_tiles_from_sheet('runes/fire/fire_shield_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.fire_spray_rune: get_tiles_from_sheet('runes/fire/fire_spray_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.fire_ball_rune: get_tiles_from_sheet('runes/fire/fire_ball_rune.png', 1, 0, 0, 0, 32, 32),

            self.dictionary.freeze_circle_rune: get_tiles_from_sheet('runes/frost/frost_circle_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.frozen_resistance_rune: get_tiles_from_sheet('runes/frost/frost_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.freeze_storm_rune: get_tiles_from_sheet('runes/frost/frost_storm_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.freeze_spray_rune: get_tiles_from_sheet('runes/frost/frost_spray_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.freeze_ball_rune: get_tiles_from_sheet('runes/frost/frost_ball_rune.png', 1, 0, 0, 0, 32, 32),
            
            self.dictionary.poison_resistance_rune: get_tiles_from_sheet('runes/poison/poison_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.poison_ball_rune: get_tiles_from_sheet('runes/poison/poison_ball_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.poison_cloud_rune: get_tiles_from_sheet('runes/poison/poison_cloud_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.poison_plume_rune: get_tiles_from_sheet('runes/poison/poison_plume_rune.png', 1, 0, 0, 0, 32, 32),

            self.dictionary.electric_resistance_rune: get_tiles_from_sheet('runes/electric/electric_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.electric_ball_rune: get_tiles_from_sheet('runes/electric/electric_ball_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.electric_spray_rune: get_tiles_from_sheet('runes/electric/electric_spray_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.chain_lightning_rune: get_tiles_from_sheet('runes/electric/chain_lightning_rune.png', 1, 0, 0, 0, 32, 32),
            
            self.dictionary.soul_reap_rune: get_tiles_from_sheet('runes/vampiric/soul_reap_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.soul_pit_rune: get_tiles_from_sheet('runes/vampiric/soul_pit_rune.png', 1, 0, 0, 0, 32, 32),

            self.dictionary.invisibility_rune: get_tiles_from_sheet('runes/invisibility_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.key_rune: get_tiles_from_sheet('runes/key_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.light_rune: get_tiles_from_sheet('runes/light_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.resistance_rune: get_tiles_from_sheet('runes/resistance_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.shield_rune: get_tiles_from_sheet('runes/shield_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.silence_rune: get_tiles_from_sheet('runes/silence_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.speed_rune: get_tiles_from_sheet('runes/speed_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.increase_strength_rune: get_tiles_from_sheet('runes/strength_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.vampiric_rune: get_tiles_from_sheet('runes/vampiric_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.arcane_hunger_rune: get_tiles_from_sheet('runes/hunger_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.magnet_rune: get_tiles_from_sheet('runes/magnet_rune.png', 1, 0, 0, 0, 32, 32),
            self.dictionary.invulnerable_rune: get_tiles_from_sheet('runes/invulnerable_rune.png', 1, 0, 0, 0, 32, 32),
        }
        self.assets.update(rune)


    def Asset_Font(self):
        font = {
            self.dictionary.font: get_tiles_from_sheet('font/font.png', 7, 5, 0, 0, 16, 16),
            self.dictionary.player_damage_font: get_tiles_from_sheet('font/player_damage_font.png', 7, 5, 0, 0, 16, 16),
            self.dictionary.small_font: get_tiles_from_sheet('font/small_font.png', 7, 5, 0, 0, 8, 8),
            self.dictionary.floating_E: get_tiles_from_sheet('font/floating_e.png', 1, 0, 0, 0, 16, 16),
            self.dictionary.symbols: get_tiles_from_sheet('font/symbols.png', 7, 5, 0, 0, 16, 16),
            self.dictionary.souls: get_tiles_from_sheet('font/souls.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(font)
    
    def Asset_Health_Bar(self):
        health_bars = {
            self.dictionary.healthbar_1: get_tiles_from_sheet('ui/healthbar_1.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_2: get_tiles_from_sheet('ui/healthbar_2.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_3: get_tiles_from_sheet('ui/healthbar_3.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_4: get_tiles_from_sheet('ui/healthbar_4.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_5: get_tiles_from_sheet('ui/healthbar_5.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_6: get_tiles_from_sheet('ui/healthbar_6.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_7: get_tiles_from_sheet('ui/healthbar_7.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_8: get_tiles_from_sheet('ui/healthbar_8.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_9: get_tiles_from_sheet('ui/healthbar_9.png', 5, 0, 0, 0, 64, 64),
            self.dictionary.healthbar_10: get_tiles_from_sheet('ui/healthbar_10.png', 5, 0, 0, 0, 64, 64),
        }
        self.assets.update(health_bars)

    def Asset_Menu(self):
        menu = {
            self.dictionary.loading_bar: get_tiles_from_sheet('menu/loading_screen.png', 6, 0, 0, 0, 96, 96),
        }
        self.assets.update(menu)

    def Asset_Tooltips(self):
        tooltips = {
            self.dictionary.radius_tooltip: get_tiles_from_sheet('items/tooltips/radius.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(tooltips)

