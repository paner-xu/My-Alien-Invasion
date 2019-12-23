import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship
        self.bullets = pygame.sprite.Group()
        self.color = self.settings.bullet_color
        # create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self, ai_game):
        """update position of bullets and get rid of old bullets."""

        self.bullets.update()
        # get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions(ai_game)

    def _check_bullet_alien_collisions(self, ai_game):
        """respond to bullet-alien collisions."""
        # remove any bullets and aliens that have collided.
        conllisions = pygame.sprite.groupcollide(
            self.bullets, ai_game.alien.aliens, True, True)
        if not ai_game.alien.aliens:
            # destroy exiting bullets and create new fleet.
            self.bullets.empty()
            ai_game.alien._create_fleet()
