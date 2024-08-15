from scripts.decoration.decoration import Decoration
from scripts.entities.player.items.item import Item
from scripts.entities.player.items.weapons.weapon import Weapon
import random
import pygame


class Spear(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 8, 10, 'two_handed_melee')
        self.max_animation = 3
        self.attack_animation_max = 3
        self.return_to_holder = False
        self.distance_from_player = 0
        



    def Place_Down(self):
        # Parent class Place_down function
        super().Place_Down()
        return False

    def Set_Attack(self):
        super().Set_Attack()
        self.attack_animation_time = int(self.attacking / self.range / self.attack_animation_time) 
        

    def Update_Attack_Animation(self, entity):
        super().Update_Attack_Animation(entity)
        # Reset the attack logic
        if not self.attacking:
            self.return_to_holder = False
            self.distance_from_player = 0
            print(self.game.player.attack_direction)
            return
        
        # Not updating the animation as the timer hasn't been hit yet
        if not self.attack_animation_counter >= self.attack_animation_time - 1:
            return
        
        
        self.Attack_Direction(entity)
        if not self.return_to_holder:
            self.distance_from_player += 1
            if self.distance_from_player <= self.range:
                return
            elif self.distance_from_player > self.range:
                self.return_to_holder = True
                return
        else:
            self.distance_from_player -= 1


            if self.distance_from_player <= 0:
                self.return_to_holder = False
                
            
    def Attack_Direction(self, entity):
            attack_direction = entity.attack_direction
            if abs(attack_direction[0]) >= abs(attack_direction[1]):                
                if attack_direction[0] >= 0:
                    self.rotate = 0
                    self.Move((self.pos[0] + self.distance_from_player, self.pos[1] + 5))
                else:
                    self.rotate = 0
                    self.flip_image = True
                    self.Move((self.pos[0] - self.distance_from_player, self.pos[1] + 5))
            else:
                
                if attack_direction[1] >= 0:
                    self.rotate = -90
                    self.Move((self.pos[0] - 5, self.pos[1] + self.distance_from_player))
                else:
                    self.rotate = 90
                    self.Move((self.pos[0] - 5, self.pos[1] - self.distance_from_player))