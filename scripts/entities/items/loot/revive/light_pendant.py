from scripts.entities.items.loot.loot import Loot
import random


class Light_Pendant(Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'light_pendant', pos, (16, 16), 10, 'revive')
        self.description = f"Revive for\n{self.game.player.max_health * 2} soul"


    # Revive the player and scale the cost with the player's max health, then
    # restore half health
    def Revive(self):
        player = self.game.player
        revive_cost =  player.max_health * 2
        if player.Get_Total_Available_Souls() < revive_cost:
            return False
        self.game.particle_handler.Activate_Particles(20, 'gold', player.rect().center, frame=random.randint(40, 60))
        player.Set_Health(player.max_health // 2)
        player.Decrease_Souls(revive_cost)

        player.damage_cooldown = 100
        
        return True
    
        