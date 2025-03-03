from scripts.entities.items.loot.keys.key import Key

class Soul_Key(Key):
    def __init__(self, game, pos):
        super().__init__(game, 'soul_key', pos)
        self.description = 'Pay souls to\nopen any door.\nsouls 30'

    # Cost souls to open door
    def Open_Door(self):
        self.game.player.Decrease_Souls(30)