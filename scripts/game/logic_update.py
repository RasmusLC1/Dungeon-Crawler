import pygame
import sys


class Logic_Update():
    def __init__(self, game) -> None:
        self.game = game

    def Update(self):
            fps = int(self.game.clock.get_fps())
            pygame.display.set_caption('Dungeons of Madness             FPS: ' + str(fps))
            
            self.game.player.Update(self.game.tilemap, (self.game.movement[1] - self.game.movement[0], self.game.movement[3] - self.game.movement[2]), self.game.render_scroll)
            self.game.particle_handler.particle_update(self.game.render_scroll)
            self.game.trap_handler.Update()
            self.game.decoration_handler.Update()
            self.game.item_handler.Update(self.game.render_scroll)
            self.game.enemy_handler.Update()
            self.game.entities_render.Update()


            self.game.item_inventory.Update(self.game.render_scroll)
            self.game.weapon_inventory.Update(self.game.render_scroll)
            self.game.spell_inventory.Update(self.game.render_scroll)
            self.game.souls_interface.Update()
            self.game.ray_caster.Update(self.game)

            self.game.mouse.Mouse_Update()
            self.game.text_box_handler.Update()

            