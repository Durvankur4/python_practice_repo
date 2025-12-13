import pygame


class Ship:
    def __init__(self, ai_game):
        """Initialize the starting postion of the ship"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.imgae = pygame.image.load(
            "D:/03_Code\python\python_book_references\python_crash_course_ericmatthes\part_2/alien_invasion\images\ship.bmp"
        )
        self.rect = self.imgae.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        ### movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ships postion"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """draw the ship"""
        self.screen.blit(self.imgae, self.rect)
