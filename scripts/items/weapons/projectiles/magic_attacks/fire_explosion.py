from scripts.items.item import Item
import pygame

class Fire_Explosion(Item):
    def __init__(self, game, pos, effect):
        super().__init__(game, 'fire_explosion', 'magic_attack', pos, (32, 32))
        self.max_animation = 7
        self.size = self.effect * self.size[0], self.effect * self.size[1]
        self.animation = 0
        self.animation_cooldown = 0
        self.animation_cooldown_max = 20
        self.delete_countdown = self.max_animation * self.animation_cooldown_max
        self.effect = effect
        self.Initialise_Explosion()

    def Initialise_Explosion(self):
        self.Find_Nearby_Entities(self.effect)
        for entity in self.nearby_entities:
            distance = self.Distance(self.pos, entity.pos)
            damage = min(5, self.effect * 32 - distance)
            entity.Damage_Taken(damage, (0,0))


    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):

        weapon_image = self.game.assets[self.type][self.animation].convert_alpha()
        weapon_image = pygame.transform.scale(weapon_image, self.size)

        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

