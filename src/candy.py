import pygame
from pygame.sprite import Sprite
import random
import math

class Candy(Sprite):
    "A class to manage the bonuses for the ship."

    def __init__(self, ai_game):
        """create a bonus object"""
        super().__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.ship = ai_game.ship
        self.collision_flag = False
        self.show_flag = False
        self.ID = -1

        # sugar setting
        self.width = 25
        self.height = 30
        self.candy_speed = 0.5
        self.candy_direction = 1
        self.color = (255, 255, 0)

        # create a sugar rect at the top of screen and then set correct position.
        self.rect = pygame.Rect(0.0, 0.0, self.width, self.height)

    def axis_update(self):
        "update the position of the sugar."
        # update the sugar position.
        self.rect.x += math.ceil(self.candy_speed) * self.candy_direction
        self.rect.y += math.ceil(self.candy_speed)

    def update(self, ai_game):
        """update position of bonuses and get rid of old bonuses."""
        if self.show_flag:
            self.check_edges()
            self.axis_update()
            # look for collision between ship and bonus
            self.check_collisions(ai_game)
            # candies hitting the bottom of the screen
            self._check_candy_bottom()

    def draw(self):
        "draw the candy to the screen."
        if self.show_flag:
            pygame.draw.rect(self.screen, self.color, self.rect)

    def _check_candy_bottom(self):
        """Check if any candy have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            self.show_flag = False

    def check_edges(self):
        """change candy durection if candy is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            self.candy_direction *= -1

    def check_collisions(self, ai_game):
        """respond to candy-ship collisions."""
        candy_group = pygame.sprite.Group()
        candy_group.add(self)
        if pygame.sprite.spritecollideany(self.ship, candy_group):
            self.collision_flag = True
            self.show_flag = False
            self.random_position()
            candy_group.empty()

    def random_position(self):
        self.random_x = random.randint(0, self.screen.get_rect().width - self.width)
        self.rect = pygame.Rect(self.random_x, 0, self.width, self.height)

    def change_color(self, color):
        self.color = color
