import pygame
import random
from bonus_system import BonusSystem


class Sugar:
    """a class to drop sugar for ship."""

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bonus_system = BonusSystem()
        self.screen_rect = ai_game.screen.get_rect()
        # create a sugar rect at (0,0) and then set corret position.
        self.sugar_rect = pygame.Rect(
            0, 0, self.bonus_system.sugar_width, self.bonus_system.sugar_height)
        # store the sugar's position as a decimal value.
        self.y = float(self.sugar_rect.y)
        self.sugar_rect.midtop = self.screen_rect.midtop

    def update(self):
        """move the sugar down the screen"""
        self.y += self.bonus_system.sugar_speed

        self.sugar_rect.y = self.y
        # self.sugar_rect.x = random.randint(0,self.screen_rect.width)

    def draw_sugar(self):
        """draw the sugar to the screen."""
        pygame.draw.rect(
            self.screen, self.bonus_system.sugar_color, self.sugar_rect)
