class GameStats():
    """Track statistics for game"""
    def __init__(self, settings):
        """Initialize statistics"""
        self.ship_left = None
        # self.game_active_status = True
        self.settings = settings
        self.reset_stats()

        # Start Game in Inactive state
        self.game_active_status = False

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit
