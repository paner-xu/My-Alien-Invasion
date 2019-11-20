class Setting:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's setting."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5

        # bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 1.5

        self.bullets_allowed = 15

        # alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        self.ships_limit = 3

