import pygame
from pygame.sprite import Sprite
from sugar import Sugar


class Laser(Sprite, Sugar):
    """A class to manage lasers fired from the ship"""

    def __init__(self, ai_game):
        """create a laser object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.groups = pygame.sprite.Group()
        self.fire_flag = False

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

    # def draw_laser(self):
    def draw(self):
        """draw the laser to the screen"""
        if self.fire_flag:
            pygame.draw.rect(self.screen, self.color, self.rect)

    def _update_laser(self, ai_game):
        """update position of laser"""
        self.update()
        # self._check_laser_alien_collisions(ai_game)
        self.check_collisions(ai_game)

    # def _check_laser_alien_collisions(self, ai_game):
    def check_collisions(self, ai_game):
        """respond to laser-alien collisions."""
        # remove any laser and aliens that have collided.
        if self.fire_flag:
            laser_group = pygame.sprite.Group()
            laser_group.add(ai_game.laser)
            conllisions = pygame.sprite.groupcollide(
                laser_group, ai_game.aliens, False, True)
            if not ai_game.aliens:
                # destroy exiting laser and create new fleet.
                ai_game._create_fleet()
