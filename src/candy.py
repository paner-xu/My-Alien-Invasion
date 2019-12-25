import pygame
from pygame.sprite import Sprite
import random
import time
from function import Function


class Candy(Sprite, Function):
    "A class to manage the bonuses for the ship."

    def __init__(self, ai_game):
        """create a bonus object"""
        super().__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.ship = ai_game.ship
        self.candies = pygame.sprite.Group()
        self.candy_flag = False

        # sugar setting
        self.width = 25
        self.height = 30
        self.color = (255, 255, 0)
        self.candy_speed = 1
        self.candy_direction = 1
        self.candy_allowed = 2

        # create a sugar rect at the top of screen and then set correct position.
        self.random_x = random.randint(0, self.screen.get_rect().width)
        self.rect = pygame.Rect(
            self.random_x, 0, self.width, self.height)
        # store the candy's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def axis_update(self, ai_game):
        "update the position of the sugar."
        # update the sugar position.
        self.x += (self.candy_speed * self.candy_direction)
        self.y += self.candy_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, ai_game):
        """update position of bonuses and get rid of old bonuses."""
        self.check_edges()
        self.axis_update(ai_game)
        # look for collision between ship and bonus
        self.check_collisions(ai_game)
        # candies hitting the bottom of the screen
        self._check_candy_bottom()

    def draw(self):
        "draw the candy to the screen."
        pygame.draw.rect(self.screen, self.color, self.rect)

    def _check_candy_bottom(self):
        """Check if any candy have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for candy in self.candies:
            if candy.rect.bottom >= screen_rect.bottom:
                self.candies.remove(candy)

    def check_edges(self):
        """change candy durection if candy is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            self.candy_direction *= -1

    def check_collisions(self, ai_game):
        """respond to candy-ship collisions."""
        candy_group = pygame.sprite.Group()
        candy_group.add(ai_game.candy)
        ai_game.ship.ship_group.add(ai_game.ship)
        pygame.sprite.groupcollide(
            ai_game.ship.ship_group, candy_group, False, True)