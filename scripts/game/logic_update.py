class Logic_Update():
    def __init__(self, game) -> None:
        self.game = game

    def Update(self):
            
            self.Check_Keyboard_Input()
            
            self.game.particle_handler.Particle_Update()
            self.game.trap_handler.Update()
            self.game.item_handler.Update(self.game.render_scroll)
            self.game.decoration_handler.Update()
            self.game.enemy_handler.Update()
            self.game.entities_render.Update()


            self.game.item_inventory.Update(self.game.render_scroll)
            self.game.weapon_inventory.Update(self.game.render_scroll)
            self.game.rune_inventory.Update(self.game.render_scroll)
            self.game.souls_interface.Update()
            self.game.rune_handler.Update(self.game.render_scroll)
            self.game.player.Update(self.game.tilemap, (self.game.movement[1] - self.game.movement[0], self.game.movement[3] - self.game.movement[2]), self.game.render_scroll)
            self.game.ray_caster.Update()

            self.game.mouse.Mouse_Update()
            self.game.text_box_handler.Update()

            self.game.health_bar.Update_Health()




            
    def Check_Keyboard_Input(self):
         if self.game.keyboard_handler.escape_pressed:
            self.game.keyboard_handler.Set_Escape_Key(False)
            self.game.state_machine.Set_State('pause_menu')