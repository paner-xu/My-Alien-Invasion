import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from settings import Setting
from ship import Ship
from candy import Candy
from bonus_system import BonusSystem


class AlienInvasion:
    """Overall class to manage game asets and behavior."""

    def __init__(self):
        """Initialize the game, and creat game resources."""
        pygame.init()
        self.settings = Setting()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        # create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.candy = Candy(self)
        self.bonus_system = BonusSystem(self)
        self.alien = Alien(self)
        self.bullet = Bullet(self)
        # create fleet
        self.alien.create_fleet()
        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.bullet.update_bullets(self)
                self.alien.update_aliens(self)
                self.bonus_system.update(self)
                self.bonus_system.drop_candy(self)
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress. """
        if event.key == pygame.K_l:
            self.bonus_system.laser.fire_flag = True
        if event.key == pygame.K_g:
            self.bonus_system.guarder.fire_flag = True
        if event.key == pygame.K_SPACE:
            self.bullet.fire_bullet()
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key release."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_l:
            self.bonus_system.laser.fire_flag = False
        if event.key == pygame.K_g:
            self.bonus_system.guarder.fire_flag = False

    def ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ship_left > 0:
            # decrement ships_left.
            self.stats.ship_left -= 1
            # Get rid of any remaining aliens and bullets.
            self.alien.aliens.empty()
            self.bullet.bullets.empty()
            self.candy.candies.empty()

            # Create a new fleet and center the ship.
            self.alien.create_fleet()
            self.ship.center_ship()

            # pause.
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new ship."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.bullets.sprites():
            bullet.draw()
        self.alien.aliens.draw(self.screen)
        self.bonus_system.draw()
        pygame.display.flip()
