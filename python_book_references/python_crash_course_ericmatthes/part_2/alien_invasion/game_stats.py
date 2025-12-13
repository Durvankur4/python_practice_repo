class GameStats:
    """track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_status()

    def reset_status(self):
        """initailize the staistics of the game."""
        self.ships_left = self.settings.ship_limit

        # start alien invasion in active state
        self.game_active = True
