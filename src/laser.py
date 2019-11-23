import pygame
from pygame.sprite import Sprite


class Laser(Sprite):
    """A class to manage lasers fired from the ship"""

    def __init__(self, ai_game):
        """create a laser object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game

        # laser settings
        self.color = (70, 70, 70)
        self.width = 5
        self.height = ai_game.screen_height - ai_game.ship.rect.height

        # create a laser rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = ai_game.ship.rect.centerx

    def update(self):
        """move the laser with the ship"""
        # update the rect position
        self.rect.x = self.ai_game.ship.x + \
            self.ai_game.ship.rect.width / 2 - self.width / 2

    def draw_laser(self):
        """draw the laser to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
