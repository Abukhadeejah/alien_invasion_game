import pygame 

class Ship():
    """ Initialize the ship object on screen. """

    def __init__(self, screen):
        # Create screen object and place the ship at the bottom of the screen
        self.screen = screen

        # Load the image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # start new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def update(self):
        # Update the ships position  based on movement flag
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        # Draw the ship at its current position
        self.screen.blit(self.image, self.rect)