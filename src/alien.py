import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.ship = ai_game.ship
		self.aliens = pygame.sprite.Group()
		# load the alien image and set its rect attribute.
		self.image = pygame.image.load("../images/alien.bmp")
		self.rect = self.image.get_rect()

		# start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# store the alien's exact horizonal position.
		self.x = float(self.rect.x)

	def check_edges(self):
		"""return True if alien is at edge of screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			# if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			# 	return True
			if alien.rect.right >= screen_rect.right or alien.rect.left <= 0:
				return True

	def update(self):
		"""move the alien right or left."""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x

	def create_fleet(self):
		"""create the fleet of aliens."""
		# create an alien and find the number of aliens in a row.
		# spacing between each alien is equal to one alien width.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien_width, alien_height = self.rect.size

		available_space_x = self.settings.screen_width - 2 * alien_width
		number_aliens_x = available_space_x // (2 * alien_width)

		# determine the number of rows of aliens that fit on the screen.
		ship_height = self.ship.rect.height
		available_space_y = self.settings.screen_height - \
			ship_height - (3 * alien_height)
		number_rows = available_space_y // (2 * alien_height)

		# create the full fleet of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		"""create an alien and place it in the row."""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien_height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def aliens_shoot_bullets(self):
		"""respond aliens shoot bullets to ship"""
		pass

	def _check_fleet_edges(self):
		"""respond appropriately if any aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if self.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def update_aliens(self,ai_game):
		"""Check if the fleet is at an edge, then update the positions of all aliens in the fleet."""
		self._check_fleet_edges()
		self.aliens.update()
		# look for alien-ship collisions.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			ai_game.ship_hit()

		# aliens hitting the bottom of the screen
		self._check_aliens_bottom(ai_game)

	def _check_aliens_bottom(self,ai_game):
		"""Check if any aliens have reached the bottom of the screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# Treat this the same as if the ship got hit.
				ai_game.ship_hit()
				break