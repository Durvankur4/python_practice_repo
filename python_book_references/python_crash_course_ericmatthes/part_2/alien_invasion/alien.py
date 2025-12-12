import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' A class to to rempresent a single alien in the fleet '''

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        
        #load alien image and its rect
        self.image = pygame.image.load("D:/03_Code\python\python_book_references\python_crash_course_ericmatthes\part_2/alien_invasion\images/alien(1).png")
        self.rect = self.image.get_rect()

        #start each new alien near the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's H position
        self.x = float(self.rect.x)