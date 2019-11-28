import pygame
from pygame.sprite import Sprite
import random


class Bonus(Sprite):
    "A class to manage the bonuses for the ship."

    def __init__(self, ai_game):
        """create a bonus object"""
        super().__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.bonuses = pygame.sprite.Group()

        # sugar setting
        self.width = 25
        self.height = 30
        self.color = (255, 255, 0)
        self.bonus_speed = 1
        self.bonus_direction = 1
        self.bonus_allowed = 2

        # create a sugar rect at the top of screen and then set correct position.
        self.random_x = random.randint(0, self.screen.get_rect().width)
        self.rect = pygame.Rect(
            self.random_x, 0, self.width, self.height)
        # store the sugar's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # def _create_bonus_group(self):
        # add bonus into bonus group
    #     if len(self.bonuses) < self.bonus_allowed:
    #         new_bonus = Bonus(self)
    #         self.bonuses.add(new_bonus)

    def update(self, ai_game):
        "update the position of the sugar."
        # update the sugar position.
        self.x += (self.bonus_speed * self.bonus_direction)
        self.y += self.bonus_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bonus(self):
        "draw the bonus to the screen."
        pygame.draw.rect(self.screen, self.color, self.rect)

    def _check_bonus_bottom(self):
        """Check if any bonus have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for bonus in self.bonuses.sprites():
            if bonus.rect.bottom >= screen_rect.bottom:
                self.bonuses.remove(bonus)

    def check_edges(self):
        """change bonus durection if bonus is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            self.bonus_direction *= -1

    def _check_bonus_ship_collisions(self):
        """respond to bonus-ship collisions."""
        # look for bonus-ship collisions.
        pygame.sprite.spritecollideany(self.ai_game.ship, self.bonuses)
