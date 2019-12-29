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
        self.program_StartTime = int(time.time()) % 60
        self.functions = [Laser(ai_game), Gaurder(ai_game)]
        self.candy = Candy(ai_game)
        self.candy_num = 0

    def checkKeydownEvents(self, event):
        """Respond to keypress. """
        if self.candy.ID >= 0 and self.candy.collision_flag \
                and event.key == self.functions[self.candy.ID].key:
            self.functions[self.candy.ID].fire_flag = True

    def checkKeyupEvents(self, event):
        """Respond to key release."""
        if self.candy.ID >= 0 and self.candy.collision_flag \
                and event.key == self.functions[self.candy.ID].key:
            self.functions[self.candy.ID].fire_flag = False

    def drop_candy(self, ai_game):
        current_time = int(time.time()) % 60
        difference = abs(current_time - self.program_StartTime) % 10
        if 0 <= difference < 5 and not self.candy.show_flag and self.candy_num == 0:
            self.candy.show_flag = True
            self.candy_num += 1
            ID = random.randint(0, 1)
            self.candy.ID = ID
            self.candy.change_color(self.functions[ID].color)
            self.candy.random_position()
        if 5 <= difference < 10:
            self.candy_num = 0

    def update(self, ai_game):
        self.drop_candy(ai_game)
        if self.candy.show_flag:
            self.candy.update(ai_game)
        if self.candy.ID >= 0 and self.candy.collision_flag:
            self.functions[self.candy.ID].update(ai_game)

    def draw(self):
        if self.candy.show_flag:
            self.candy.draw()
        if self.candy.ID >= 0 and self.candy.collision_flag:
            self.functions[self.candy.ID].draw()
