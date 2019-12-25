import pygame
from pygame.sprite import Sprite
from function import Function
import math


class Gaurder(Sprite, Function):
    """A class to manage guader to protect the ship"""

    def __init__(self, ai_game):
        """create a guader object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.groups = pygame.sprite.Group()
        self.fire_flag = False

        # guader settings
        self.color = (70, 70, 70)
        self.width = 2
        self.start_angle = math.radians(0)
        self.stop_angle = math.radians(180)
        self.height = ai_game.screen_height - ai_game.ship.rect.height

        # create a laser rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, ai_game.ship.rect.width*2, ai_game.ship.rect.width*2)
        self.rect.centerx = ai_game.ship.rect.centerx
        self.rect.centery = ai_game.ship.rect.centery

    def axis_update(self):
        """move the guarder with the ship"""
        # update the circle position
        self.rect.x = self.ai_game.ship.x + \
            self.ai_game.ship.rect.width / 2 - self.rect.width / 2

    # def draw_guarder(self):
    def draw(self):
        """draw the guarder to the screen"""
        if self.fire_flag:
            pygame.draw.arc(self.screen, self.color, self.rect,
                            self.start_angle, self.stop_angle, self.width)

    def update(self, ai_game):
        """update position of laser"""
        self.axis_update()
        # self._check_laser_alien_collisions(ai_game)
        self.check_collisions(ai_game)

    # def _check_laser_alien_collisions(self, ai_game):
    def check_collisions(self, ai_game):
        """respond to guarder-alien collisions."""
        # remove any guarder and aliens that have collided.
        if self.fire_flag:
            guarder_group = pygame.sprite.Group()
            # guarder_group.add(ai_game.guarder)
            guarder_group.add(ai_game.bonus_system.guarder)
            conllisions = pygame.sprite.groupcollide(
                guarder_group, ai_game.alien.aliens, False, True)
            if not ai_game.alien.aliens:
                # destroy exiting guarder and create new fleet.
                ai_game.alien.create_fleet()
