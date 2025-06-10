import random

class Damage_Text():
    def __init__(self):
        self.Reset()

    def Update(self):
        if not self.Cooldown_Handler():
            self.Reset()
            return False

        return True

    def Reset(self):
        self.text = None
        self.pos = None
        self.offset = 0
        self.cooldown = 0

    def Activate(self, pos, text, queue_length):
        self.text = text
        self.pos = (pos[0] + random.randint(-5, 5), pos[1] + random.randint(-5, 5))
        self.Set_Cooldown(queue_length)


    def Cooldown_Handler(self):
        if self.cooldown:
            self.cooldown -= 1
            return True
        
        return False
    
    def Set_Cooldown(self, queue_length):
        self.offset = random.randint(15, 25)
        self.cooldown = max(5, random.randint(20 - queue_length, 30 - queue_length))
