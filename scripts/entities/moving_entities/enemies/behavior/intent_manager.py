from scripts.entities.moving_entities.enemies.behavior.Dash import Dash
import random

class Intent_Manager():
    def __init__(self, game, entity, intent_cooldown_max, intent) -> None:
        self.game = game
        self.entity = entity

        self.intent = intent # Enemy's attack pattern and intent
        self.intent_index = 0
        self.intent_length = len(self.intent)
        self.intent_cooldown = 0
        self.intent_cooldown_max = intent_cooldown_max
        self.dash = Dash(game, entity)
        self.base_cooldown = {
            "direct": 0,
            "charge": 0,
            "attack": 0,
            'long_range': self.intent_cooldown_max * 2,
            "medium_range": self.intent_cooldown_max * 1.5,
            "short_range": self.intent_cooldown_max,
            "keep_position": self.intent_cooldown_max * 2,
        }


    def Increment_Intent(self):
        self.intent_index += 1
        # Cycle back to the beginning if index exceeds length
        if self.intent_index >= self.intent_length:
            self.intent_index = 0

    # def Set_Intent_Cooldown(self):
    #     self.intent_cooldown = random.randint(self.intent_cooldown_max, round(self.intent_cooldown_max * 1.3))

    def Set_Intent_Cooldown(self):
        max_cooldown = self.base_cooldown.get(self.intent[self.intent_index], self.intent_cooldown_max)
        if not max_cooldown:
            return
        self.intent_cooldown = random.randint(max_cooldown, round(max_cooldown * 1.3))

    # Return false on when cooldown is active
    def Update_Intent_Cooldown(self):
        if not self.intent_cooldown:
            return True
        self.intent_cooldown = max(0, self.intent_cooldown - 1)
        return False
        
    def Set_Intent_Index(self, index):
        if index >= self.intent_length:
            print("index exceed intent length", index, self.intent_length)
            return
        self.intent_index = index

    def Update_Behavior(self):
        # print(self.intent[self.intent_index])
        if not self.Update_Intent_Cooldown():
            return
        
        match self.intent[self.intent_index]:
            # Handle movement logic
            case "long_range" | "medium_range" | "short_range" | "keep_position":
                self.entity.Set_Attack_Strategy(self.intent[self.intent_index])
                self.Set_Intent_Cooldown()
                self.Increment_Intent()
            case "direct":
                self.entity.Set_Attack_Strategy(self.intent[self.intent_index])
                self.Increment_Intent()
            case "charge":
                self.Handle_Charge()
            case "attack":
                self.Handle_Attack()
            case _:
                print("intent missing:\t", self.intent[self.intent_index])
        
        return

    def Handle_Charge(self):
        if not self.dash.dashing:
            self.dash.Dash()

        self.dash.Dashing_Update()

        if self.dash.dashing == 1:
            self.Increment_Intent()
        return

    def Handle_Attack(self):
        # print(self.entity.attack_strategy)
        if self.entity.distance_to_player < self.entity.attack_distance:
            # increment the intent when enemy attacks
            if self.entity.Attack():
                self.Increment_Intent()
            return

        if self.entity.distance_to_player > self.entity.disengage_distance and self.entity.charge:
            self.entity.charge = 0

        return