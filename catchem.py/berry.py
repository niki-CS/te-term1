import random
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

class Berry:
    def __init__(self,color,speed,value):
        self.color = color
        self.speed = .5
        self.position = random.randint(0,7)
        self.value = value
        self.pos_X = random.randint(0,7)
        self.pos_Y = 0

    def drop(self):
        sleep(self.speed)
        if self.pos_Y < 7:
            self.pos_Y += 1  
        self.display()     
    
    def display(self):
        x = self.pos_X
        y = self.pos_Y
        sense.set_pixel(x, y-1, (0,0,0))
        sense.set_pixel(x, y, (255,0,0))
        #print("berry moved")
        
