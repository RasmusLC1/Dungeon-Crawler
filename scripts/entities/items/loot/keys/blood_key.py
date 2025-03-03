from scripts.entities.items.loot.keys.key import Key

class Blood_Key(Key):
    def __init__(self, game, pos):
        super().__init__(game, 'blood_key', pos)
        self.description = 'Sacrifice blood\nto open any door\n5 health'


    # Sacrifice 5 health to open door
    def Open_Door(self):
        self.game.player.Damage_Taken(5)