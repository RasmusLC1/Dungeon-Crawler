import pygame

class Renderer():
    def __init__(self, game) -> None:
        self.game = game
        self.back_ground_image = pygame.transform.scale(self.game.assets['background'], (self.game.screen_width/self.game.render_scale, self.game.screen_height/self.game.render_scale))


    def Render(self):
        self.game.display.blit(self.back_ground_image, (0, 0))
        
        self.game.ray_caster.Ray_Caster()
        self.game.tilemap.Render_Tiles(self.game.ray_caster.tiles, self.game.display, offset=self.game.render_scroll)


        self.game.souls_interface.Render(self.game.display)
        self.game.rune_handler.Render_Animation(self.game.display, self.game.render_scroll)
        self.game.entities_render.Render(self.game.display, self.game.render_scroll)
        for particle in self.game.particles:
            particle.Render(self.game.display, self.game.render_scroll)

        self.game.item_inventory.Render(self.game.display)
        self.game.weapon_inventory.Render(self.game.display)
        self.game.rune_inventory.Render(self.game.display)

        self.game.text_box_handler.Render(self.game.display, self.game.render_scroll)
        self.game.player.status_effects.Render_Effects_Symbols(self.game.display)
        self.game.health_bar.Health_Bar()

