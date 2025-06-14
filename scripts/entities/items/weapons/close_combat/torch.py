from scripts.entities.items.weapons.weapon import Weapon
from scripts.entities.items.weapons.magic_attacks.fire.flame_thrower import Flame_Thrower
import random
from scripts.engine.assets.keys import keys


class Torch(Weapon):
    def __init__(self, game, pos):
        super().__init__(game, pos, keys.torch, 1, 2, 3, 100, 'one_handed_melee', keys.fire)
        self.max_animation = 5
        self.attack_animation_max = 5
        self.animation_cooldown_max = 40
        self.light_source = self.game.light_handler.Add_Light(self.pos, 8, self.tile)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)
        self.flame_thrower = Flame_Thrower(self.game)


    # Pick up the torch and update the general light in the area
    def Pick_Up(self):
        if not super().Pick_Up():
            return
        self.game.light_handler.Remove_Light(self.light_source)


    def Spawn_Fire_Particle(self):
        self.game.particle_handler.Activate_Particles(random.randint(1, 3), keys.fire_particle, self.rect().center, frame=random.randint(80, 90))

    
    def Set_Attack(self):
        if not super().Set_Attack():
            return False
        self.game.sound_handler.Play_Sound('torch_attack', 0.5)
        return True


    def Update_Animation(self):
        if self.animation_cooldown:
            self.animation_cooldown -= 1
        else:
            self.animation_cooldown = random.randint(self.animation_cooldown_max - 10, self.animation_cooldown_max)
            self.Spawn_Fire_Particle()

            self.animation = random.randint(0,self.max_animation)
            self.Set_Entity_Image()

    def Special_Attack(self):
        if self.special_attack <= 0 or not self.equipped:
            self.Reset_Special_Attack()
            return
        self.special_attack = self.flame_thrower.Particle_Creation(self.entity, self.special_attack)


    def Set_Special_Attack(self, offset = (0,0)):
        super().Set_Special_Attack(offset)

    def Set_Equip(self, state, entity):
        super().Set_Equip(state, entity)

        if state:
            self.game.player.Update_Light_Source(12)
        else:
            self.game.player.Update_Light_Source(self.game.player.default_light_level)
    
    def Update_Light_Level(self):
        return True

    def Place_Down(self):
        # Parent class Place_down function
        if not super().Place_Down():
            return False

        # Set the player light to False to trigger a general update of the light
        # levels around the player and move the torch light to the new location
        self.game.light_handler.Add_Light_Source(self.light_source)
        self.light_source.Move_Light(self.pos, self.tile)
        return True

    def Update_Dark_Surface(self):
        self.rendered_image = self.entity_image