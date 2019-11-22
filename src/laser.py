import pygame


class Laser:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.laser_color
        self.laser_rect = pygame.Rect(
            0, 0, self.settings.laser_width, self.settings.laser_height)
        self.laser_rect.height = self.screen.get_rect().height
        self.x = float(self.laser_rect.x)

    def draw_laser(self):
        """draw the laser to the screen."""
        pygame.draw.rect(self.screen, self.color, self.laser_rect)
