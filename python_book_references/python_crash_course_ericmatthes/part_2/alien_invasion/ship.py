import pygame

class Ship:
    def __init__(self,ai_game):
        '''Initialize the starting postion of the ship'''

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.imgae = pygame.image.load("D:/03_Code\python\python_book_references\python_crash_course_ericmatthes\part_2/alien_invasion\images\ship.bmp")
        self.rect = self.imgae.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        '''draw the ship'''
        self.screen.blit(self.imgae,self.rect)