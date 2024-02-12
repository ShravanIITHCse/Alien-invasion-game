class Settings():
    """Class containing all settings required for game"""

    def __init__(self):
        """Initialize all game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)
        self.pause_screen_color = (200, 200, 200)

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 3

        # Alien settings
        self.alien_speed = 1
        self.alien_drop_rate = 10
        # 1 for right and -1 for left
        self.alien_direction = 1

        # Button Settings
        self.button_height = 50
        self.button_width = 200
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)
        self.button_text_font_style = "arial"
        self.button_text_size = 48

        # Speedup factor
        self.sf_bullet_speed = 1.25
        self.sf_ship_speed = 1.25
        self.sf_alien_speed = 1.25
        self.sf_bullet_width = 1.25
        self.sf_alien_points = 2

        # Points
        self.alien_points = 50

    def return_to_default(self):
        self.bullet_width = 5
        self.ship_speed = 3
        self.alien_speed = 1
        self.bullet_speed = 1
        self.alien_points = 50

    def level_up(self):
        self.alien_speed *= self.sf_alien_speed
        self.ship_speed *= self.sf_ship_speed
        self.bullet_speed *= self.sf_bullet_speed
        self.bullet_width *= self.sf_bullet_width
        self.alien_points *= self.sf_alien_points
        # print(str(settings.alien_speed) + " " + str(settings.ship_speed) + " " + str(settings.bullet_speed))
