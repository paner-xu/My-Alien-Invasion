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
        self.fireFlag = False
        self.fireTime = int(time.time()) % 60

    def checkKeydownEvents(self, event):
        """Respond to keypress. """
        if self.candy.getId() >= 0 and self.fireFlag \
                and event.key == self.functions[self.candy.getId()].getKey():
            self.functions[self.candy.getId()].setFireFlag(True)

    def checkKeyupEvents(self, event):
        """Respond to key release."""
        if self.candy.getId() >= 0 and self.fireFlag \
                and event.key == self.functions[self.candy.getId()].getKey():
            self.functions[self.candy.getId()].setFireFlag(False)

    def drop_candy(self, ai_game):
        current_time = int(time.time()) % 60
        difference = abs(60 + current_time - self.program_StartTime) % 10

        # by add the candy_num make this if sentence run only once in the 0 ~ 5s
        if 0 <= difference < 5 and not self.candy.getShowFlag() and self.candy_num == 0:
            # reset the candy status
            self.candy.setRandomPosition()
            self.candy.setShowFlag(True)

            id = random.randint(0, 1)
            self.candy.setId(id)
            self.candy.setColor(self.functions[id].getColor())

            self.candy_num += 1
        if 5 <= difference < 10:
            # reset the candy_num
            self.candy_num = 0

    def update(self, ai_game):
        self.drop_candy(ai_game)
        if self.candy.getShowFlag():
            self.candy.update(ai_game)
        if self.candy.getId() >= 0 and self.candy.getCollisionFlag():
            self.fireFlag = True
            # make sure don't draw the functions at the moment of the candy dropping
            self.functions[self.candy.getId()].setFireFlag(False)
            self.candy.setCollisionFlag(False)
        if self.fireFlag:
            self.functions[self.candy.getId()].update(ai_game)
            current_time = int(time.time()) % 60
            difference = abs(60 + current_time - self.fireTime) % 10
            # hold the function 8s
            if difference >= 8:
                self.fireFlag = False

    def draw(self):
        if self.candy.getShowFlag():
            self.candy.draw()
        if self.candy.getId() >= 0 and self.fireFlag and self.functions[self.candy.getId()].getFireFlag():
            self.functions[self.candy.getId()].draw()
