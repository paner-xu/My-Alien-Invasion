import pygame
import time
from laser import Laser
from guarder import Gaurder
from bonus import Bonus


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
        self.programStartTime = time.time()
        self.laser = Laser(self)
        self.guarder = Gaurder(self)
        self.bonus = Bonus(self)
        self.functions = (self.laser,self.guarder)

    def _update(self, ai_game):
        self.laser._update(ai_game)
        self.guarder._update(ai_game)
        self.bonus._update(ai_game)

    def _draw(self):
        self.laser.draw()
        self.guarder.draw()
        self.bonus.draw()
