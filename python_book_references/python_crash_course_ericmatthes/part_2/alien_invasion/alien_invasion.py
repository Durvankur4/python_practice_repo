# ALIEN INVASION

import sys
from time import sleep

import pygame

from settings import Setting
from ship import Ship
from bullets import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        print("Initializing game")
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.sceen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.sb = Scoreboard(self)

        self._create_fleet()

        self.play_button = Button(self, "Play")

        # Draw the score information:

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_alien()
                self._update_bullets()

            self._update_screen()

    def _check_events(self):
        """responds to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            print("Game exited successfully! Thanks for playing.")
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        else:
            pass

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        else:
            pass

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        self._update_screen()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """respond to alien alien collision"""
        # check for any bullet that have hit alien
        # if so then get rid of the aien and the bullet
        # true for disappering the sprite after collision
        collisoions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisoions:
            for aliens in collisoions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # destroy exixting bulets and create a new group
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # increase speed
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        """updated images on the sceeen and flips to a new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _create_fleet(self):
        # the alien png is effectively 100*100px
        """create fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.sceen_width - (2 * alien_width)
        # subtracting 200px from each side
        # avalilable screen space divide by 200 gives no of aliens
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows of alien that fit on screen
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_numebr, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_numebr
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

        alien = Alien(self)
        self.aliens.add(alien)

    def _update_alien(self):
        """check if the fleet is at an edge,
        update postion of al alien in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # look for alien bottom contact
        self._check_alien_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the entire fleet and change directions"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:

            # Decrement ships
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # Create new fleet and centre the ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_alien_bottom(self):
        """check if any alien have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """start new game when player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            self.settings.initalize_dynamic_settings()
            # reset the game statistics
            self.stats.reset_status()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # get rid of any alien and bullets
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
