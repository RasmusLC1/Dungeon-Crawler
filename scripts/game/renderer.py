import pygame

class Renderer():
    def __init__(self, game) -> None:
        self.game = game

    def Render(self):
        self.game.display.blit(self.game.assets['background'], (0, 0))
        
        self.game.ray_caster.Ray_Caster()
        self.game.tilemap.render_tiles(self.game.ray_caster.tiles, self.game.display, offset=self.game.render_scroll)

        self.game.trap_handler.Render(self.game.ray_caster.traps, self.game.display, self.game.render_scroll)

        self.game.health_bar.Health_Bar()
        self.game.souls_interface.Render(self.game.display)
        self.game.entities_render.Render(self.game.display, self.game.render_scroll)
        for particle in self.game.particles:
            particle.Render(self.game.display, self.game.render_scroll)

        self.game.item_inventory.Render(self.game.display)
        self.game.weapon_inventory.Render(self.game.display)
        self.game.rune_inventory.Render(self.game.display)

        self.game.text_box_handler.Render(self.game.display, self.game.render_scroll)
        self.game.player.status_effects.Render_Effects_Symbols(self.game.display)
        self.game.rune_handler.Render(self.game.display, self.game.render_scroll)

        self.game.screen.blit(pygame.transform.scale(self.game.display, self.game.screen.get_size()), (0,0))
