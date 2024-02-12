import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """A class to represent scoring information"""

    def __init__(self, window, settings, game_stats):
        """Initialize score keeping attributes"""
        self.screen = window
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = game_stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(settings.button_text_font_style, 48)

        # Prepare the score
        self.update_score()
        self.update_high_score()
        self.update_level()
        self.update_ships()

    def update_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            temp_ship = Ship(self.screen, self.settings)
            temp_ship.ship_rect.top = 10
            temp_ship.ship_rect.left = 10 + ship_number * temp_ship.ship_rect.width
            self.ships.add(temp_ship)

    def update_score(self):
        """Turn the score into rendered image"""
        # Render the image of score and then get the rectangle of the image
        self.score_str = "{:,}".format(int(round(self.stats.score, -1)))
        self.score_img = self.font.render(self.score_str, True, self.text_color, self.settings.screen_color)
        self.score_rect = self.score_img.get_rect()

        # Position the rectangle to appropriate position
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def update_high_score(self):
        """Turn the high score into rendered image"""
        # Render the image of high score and then get the rectangle of the image
        self.high_score_str = "{:,}".format(int(round(self.stats.high_score, -1)))
        self.high_score_img = self.font.render(self.high_score_str, True, self.text_color, self.settings.screen_color)
        self.high_score_rect = self.high_score_img.get_rect()

        # Position the rectangle to appropriate position
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

    def update_level(self):
        """Turn the level into rendered image"""
        # Render the image of level and then get the rectangle of the image
        self.level_str = "{:,}".format(int(self.stats.level))
        self.level_img = self.font.render(self.level_str, True, self.text_color, self.settings.screen_color)
        self.level_rect = self.level_img.get_rect()

        # Position the rectangle to appropriate position
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score_board(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        for ship_t in self.ships:
            ship_t.draw_ship()
