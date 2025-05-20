import pygame
from scripts.engine.utility.utils import load_image, load_images, Animation, get_tiles_from_sheet
from scripts.engine.assets.keys import keys

class Audio_Loader:
    def Run_All(self):
        self.sfx = {}
        Audio_Loader.Chest_Effects(self)
        Audio_Loader.Weapons_Effects(self)
        Audio_Loader.Magic_Effects(self)
        Audio_Loader.Loot_Effects(self)
        Audio_Loader.Effect_Effects(self)


    def Chest_Effects(self):
        chest_effects ={
            'chest_open' : pygame.mixer.Sound('data/sounds/decorations/chest/chest_open.wav'),
            'chest_break' : pygame.mixer.Sound('data/sounds/decorations/chest/chest_break.wav'),
            'vase_break' : pygame.mixer.Sound('data/sounds/decorations/chest/vase_break.wav'),
            'door_open' : pygame.mixer.Sound('data/sounds/decorations/door_open.wav'),
            'soul_well' : pygame.mixer.Sound('data/sounds/decorations/soul_well.wav'),
            'teleportation' : pygame.mixer.Sound('data/sounds/decorations/teleportation.wav'),
            'boss_spawning' : pygame.mixer.Sound('data/sounds/decorations/shrine/boss_spawning.wav'),
        }
        self.sfx.update(chest_effects)
        self.sfx['chest_open'].set_volume(0.1)
        self.sfx['chest_break'].set_volume(0.2)
        self.sfx['vase_break'].set_volume(0.2)
        self.sfx['door_open'].set_volume(0.4)
        self.sfx['teleportation'].set_volume(0.4)
        self.sfx['soul_well'].set_volume(0.6)
        self.sfx['boss_spawning'].set_volume(0.4)

    def Weapons_Effects(self):
        weapon_effects ={
            'sword_impact_wall' : pygame.mixer.Sound('data/sounds/weapons/sword_impact_wall.wav'),
            'bow_draw' : pygame.mixer.Sound('data/sounds/weapons/bow_draw.wav'),
            'arrow_shot' : pygame.mixer.Sound('data/sounds/weapons/arrow_shot.wav'),
            'torch_fire_ball' : pygame.mixer.Sound('data/sounds/weapons/torch_fire_ball.wav'),
            'projectile_impact' : pygame.mixer.Sound('data/sounds/weapons/projectile_impact.wav'),
            'stab_attack_impact' : pygame.mixer.Sound('data/sounds/weapons/stab_attack_impact.wav'),
            'torch_attack' : pygame.mixer.Sound('data/sounds/weapons/torch_attack.wav'),
            'torch_equipped' : pygame.mixer.Sound('data/sounds/weapons/torch_equipped.wav'),
            'sword_swing' : pygame.mixer.Sound('data/sounds/weapons/sword_swing.wav'),
        }

        self.sfx.update(weapon_effects)

        self.sfx['sword_impact_wall'].set_volume(0.2)
        self.sfx['bow_draw'].set_volume(0.3)
        self.sfx['arrow_shot'].set_volume(0.4)
        self.sfx['torch_fire_ball'].set_volume(0.2)
        self.sfx['projectile_impact'].set_volume(0.3)
        self.sfx['stab_attack_impact'].set_volume(0.2)
        self.sfx['torch_attack'].set_volume(0.2)
        self.sfx['torch_equipped'].set_volume(0.2)
        self.sfx['sword_swing'].set_volume(0.2)

    def Magic_Effects(self):
        weapon_effects ={
            keys.electric_ball : pygame.mixer.Sound('data/sounds/magic/electric/electric_ball.wav'),
            keys.electric_explosion : pygame.mixer.Sound('data/sounds/magic/electric/electric_explosion.wav'),
            keys.fire_ball : pygame.mixer.Sound('data/sounds/magic/fire/fire_ball.wav'),
            keys.fire_explosion : pygame.mixer.Sound('data/sounds/magic/fire/fire_explosion.wav'),
            keys.fire_particle : pygame.mixer.Sound('data/sounds/magic/fire/fire_particle.wav'),
            'frozen_explosion' : pygame.mixer.Sound('data/sounds/magic/frozen/frozen_explosion.wav'),
            'frozen_projectile' : pygame.mixer.Sound('data/sounds/magic/frozen/frozen_projectile.wav'),
            keys.poison_cloud : pygame.mixer.Sound('data/sounds/magic/poison/poison_cloud.wav'),
            'poison_plume' : pygame.mixer.Sound('data/sounds/magic/poison/poison_plume.wav'),
            keys.vampiric_ball : pygame.mixer.Sound('data/sounds/magic/vampiric/vampiric_ball.wav'),
            'vampiric_explosion' : pygame.mixer.Sound('data/sounds/magic/vampiric/vampiric_explosion.wav'),
            'vampiric_projectile' : pygame.mixer.Sound('data/sounds/magic/vampiric/vampiric_projectile.wav'),
        }

        self.sfx.update(weapon_effects)

        self.sfx[keys.electric_ball].set_volume(0.2)
        self.sfx[keys.electric_explosion].set_volume(0.3)
        self.sfx[keys.fire_ball].set_volume(0.4)
        self.sfx[keys.fire_explosion].set_volume(0.2)
        self.sfx[keys.fire_particle].set_volume(0.3)
        self.sfx['frozen_explosion'].set_volume(0.2)
        self.sfx['frozen_projectile'].set_volume(0.2)
        self.sfx[keys.poison_cloud].set_volume(0.2)
        self.sfx['poison_plume'].set_volume(0.2)
        self.sfx[keys.vampiric_ball].set_volume(0.2)
        self.sfx['vampiric_explosion'].set_volume(0.2)
        self.sfx['vampiric_projectile'].set_volume(0.2)


    def Loot_Effects(self):
        weapon_effects ={
            'bell' : pygame.mixer.Sound('data/sounds/loot/items/bell.wav'),
            'recall_scroll' : pygame.mixer.Sound('data/sounds/loot/items/recall_scroll.wav'),
            'faded_hourglass' : pygame.mixer.Sound('data/sounds/loot/items/faded_hourglass.wav'),
            'ethereal_chains' : pygame.mixer.Sound('data/sounds/loot/items/ethereal_chains.wav'),
            'item_pickup' : pygame.mixer.Sound('data/sounds/loot/general/item_pickup.wav'),
            'item_placedown' : pygame.mixer.Sound('data/sounds/loot/general/item_placedown.wav'),
        }

        self.sfx.update(weapon_effects)

        self.sfx['bell'].set_volume(0.2)
        self.sfx['recall_scroll'].set_volume(0.3)
        self.sfx['faded_hourglass'].set_volume(0.3)
        self.sfx['ethereal_chains'].set_volume(0.3)
        self.sfx['item_pickup'].set_volume(0.5)
        self.sfx['item_placedown'].set_volume(0.3)

    
    def Effect_Effects(self):
        weapon_effects ={
            keys.healing : pygame.mixer.Sound('data/sounds/effects/healing.wav'),
            # 'slow' : pygame.mixer.Sound('data/sounds/effects/slow.wav'),
            keys.speed : pygame.mixer.Sound('data/sounds/effects/speed.wav'),
            'generic_effect' : pygame.mixer.Sound('data/sounds/effects/general_effect.wav'),
        }

        self.sfx.update(weapon_effects)

        self.sfx[keys.healing].set_volume(0.2)
        # self.sfx['slow'].set_volume(0.1)
        self.sfx[keys.speed].set_volume(0.3)
        self.sfx['generic_effect'].set_volume(0.2)

    

    