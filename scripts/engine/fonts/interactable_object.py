class Interactable_Object():
    def __init__(self, game):
        self.game = game
        self.active = False
        self.sprite = self.game.assets[game.dictionary.floating_E][0]


    def Set_Active(self, state):
        self.active = state

    def Render(self, surf, offset, entity):
        surf.blit(self.sprite, (entity.pos[0] + entity.size[0] // 4 - offset[0], entity.pos[1] - offset[1] - entity.size[0] // 2))

    