class Sound_Handler():
    def __init__(self, game) -> None:
        self.game = game

    def Play_Sound(self, sound_name, volume):
        # Disable all sounds if the player is silenced
        if self.game.player.status_effects.silence:
            return
        try:
            self.game.sfx[sound_name].set_volume(volume)
            self.game.sfx[sound_name].play()
        except Exception as e:
            print(f"Wrong sound input {e}", sound_name, volume)