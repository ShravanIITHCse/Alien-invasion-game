class Settings():
    """Class containing all settings required for game"""

    def __init__(self):
        """Initialize all game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3

        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 3
