# ALIEN INVASION

import sys
import pygame
from settings import Setting
from ship import Ship
from bullets import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        print("Initializing game")
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.sceen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
       
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
    
    
        
    def _check_events(self):
        '''responds to keypress and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q :
            print("Game exited successfully! Thanks for playing.")
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        else:
            pass
    
    def _check_keyup_events(self,event):
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
        self._update_screen()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        

    def _update_screen(self):
        '''updated images on the sceeen and flips to a new screen.'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self) :
        #the alien png is effectively 100*100px
        '''create fleet of aliens'''
        alien = Alien(self)
        alien_width ,alien_height = alien.rect.size
        available_space_x = self.settings.sceen_width - (2 * alien_width) #subtracting 200px from each side
        #avalilable screen space divide by 200 gives no of aliens
        number_aliens_x = available_space_x // (2 * alien_width)

        #determine the number of rows of alien that fit on screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height)-ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x) :
                self._create_alien(alien_number,row_number)

        
            
    def _create_alien(self,alien_numebr,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_numebr
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

        alien = Alien(self)
        self.aliens.add(alien)

    


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()


    
    

