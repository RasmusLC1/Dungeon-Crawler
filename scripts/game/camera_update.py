class Camera_Update():
    def __init__(self, game) -> None:
        self.game = game

    def Camera_Scroll(self):
        self.game.scroll[0] += (self.game.player.rect().centerx - self.game.display.get_width() / 2 - self.game.scroll[0]) / 25
        self.game.scroll[1] += (self.game.player.rect().centery - self.game.display.get_height() / 2 - self.game.scroll[1]) / 25
        self.game.render_scroll = (int(self.game.scroll[0]), int(self.game.scroll[1]))