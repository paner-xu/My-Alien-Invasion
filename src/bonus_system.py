import pygame
import time
import random
from laser import Laser
from guarder import Gaurder
from candy import Candy


class BonusSystem:
    "A class to manage the bonus functions."

    def __init__(self, ai_game):
        """create a BonusSystem object"""
        # super().__init__()
        self.screen = ai_game.screen
        self.screen_width = ai_game.screen_width
        self.screen_height = ai_game.screen_height
        self.ship = ai_game.ship
        self.ai_game = ai_game
        self.program_StartTime = time.time()
        self.laser = Laser(self)
        self.guarder = Gaurder(self)
        self.candy = Candy(self)
    
    def drop_candy(self,ai_game):
        # candy = Candy(self)
        current_time = time.time()
        if 9.9<current_time-self.program_StartTime<10.1:
            candy = Candy(self)
            candy.update(ai_game)

    def update(self, ai_game):
        self.laser.update(ai_game)
        self.guarder.update(ai_game)
        self.candy.update(ai_game)

    def draw(self):
        self.laser.draw()
        self.guarder.draw()
        self.candy.draw()
