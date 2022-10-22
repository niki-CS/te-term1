import random

class Player:
    def __init__(self,limit_l, limit_r):
        self.limit_l = limit_l
        self.limit_r = limit_r
        self.position = random.randint(limit_x,limit_y)
    
    def move_right(self):
        self.position = self.position + 1
        if self.position < self.limit.r:
            self.position = self.position + 1

    def move_left(self):
        self.position = self.position - 1
        if self.position > self.limit.l:
            self.position = self.position - 1
