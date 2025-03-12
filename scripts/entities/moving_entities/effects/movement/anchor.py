from scripts.entities.moving_entities.effects.effect import Effect
import random

# Set entity movement speed to zero
class Anchor(Effect):
    def __init__(self, entity):
        description = 'Prevents pushing'
        super().__init__(entity, 'anchor', 0, 0, (200, 250), description)

    
    def Push(self, direction):
        self.entity.Set_Frame_movement((0, 0)) # Cancel frame movement