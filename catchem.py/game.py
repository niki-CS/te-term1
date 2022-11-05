from sense_hat import SenseHat
import random
import time
from player import Player
from berry import Berry

sense = SenseHat()
points = 0

class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.speed = .5
        self.berry = Berry(0,7,sense)
        self.player = Player(56,63,sense)

    def start(self):
        sense.show_message("Catchem", text_colour = (255,0,0), scroll_speed= 0.05)
    
    def play(self):
        self.start()
        while not self.game_over:
            self.player.display(0)
            self.berry.drop()
            for event in sense.stick.get_events():
                if event.action == "pressed" and event.direction == "left":
                    self.player.move_left()
                elif event.action == "pressed" and event.direction == "right":
                    self.player.move_right()
           # if self.player.position == self.berry.pos_X:
           #     points += 1
           #     self.berry.drop()
                #clear berry
           # if self.player.position != self.berry.pos_Y:
           #     sense.show_message(f"Game Over. Points: {points}", text_colour = (255,0,0), scroll_speed= 0.05)
           #     self.game_over = True
           #     active = False
