import pygame
from ship import Ship
from laser import Laser
from alien import Alien


class BonusSystem:
    """a class to give some bonus to ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.laser = Laser(self)
        self.ship = Ship(self)
        self.color = self.settings.sugar_color
        # create a sugar rect at (0,0) and then set corret position.
        self.sugar_rect = pygame.Rect(
            0, 0, self.settings.sugar_width, self.settings.sugar_height)
        # store the sugar's position as a decimal value.
        self.x = float(self.sugar_rect.x)
        self.y = float(self.sugar_rect.y)

    def update_sugar(self):
        # move the sugar at the screen.
        self.x += self.settings.sugar_speed
        self.y += self.settings.sugar_speed
        self.sugar_rect.x = self.x
        self.sugar_rect.y = self.y

    # def _check_laser_alien_collisions(self):
    #     """respond to laser-alien collisions."""
    #     # remove any aliens that have collided.
    #     for alien in self.ai_game.aliens.sprites():
    #         if alien.rect.x == self.laser.laser_rect.x:
    #             self.ai_game.aliens.remove(alien)
    #     if not self.ai_game.aliens:
    #         self.laser.laser_rect.empty()
    #         self.ai_game._create_fleet()

    # def shoot_laser(self):
    #     if self.sugar_rect.bottom == self.ship.rect.top:
    #         self.update_laser()

    # def update_laser(self):
    #     self.laser.x = self.ship.rect.x
    #     self.laser.laser_rect.x = self.laser.x
    #     self.ai_game._check_laser_alien_collisions()

    def draw_sugar(self):
        # draw the sugar.
        pygame.draw.rect(self.screen, self.color, self.sugar_rect)
