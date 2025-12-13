class Setting:
    """Initializing settings in the Game"""

    def __init__(self):
        self.sceen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        ##Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien
        self.alien_speed = 3
        self.fleet_drop_speed = 100
        self.fleet_direction = 1  # 1 is right -1 is left

        # Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3
