class GameStats():
    """Track statistics for game"""
    def __init__(self, settings):
        """Initialize statistics"""
        # Stats which we reset after every game
        self.level = None
        self.score = None
        self.ship_left = None
        # self.game_active_status = True
        self.settings = settings
        self.reset_stats()
        self.high_score = 0

        # Start Game in Inactive state
        self.game_active_status = False

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
