import pygame 

class Ship():
    """ Initialize the ship object on screen. """

    def __init__(self, ai_settings, screen):
        # Create screen object and place the ship at the bottom of the screen
        self.screen = screen
        self.ai_settings = ai_settings

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

        # store dcimal value for the ships center
        self.center = float(self.rect.centerx)


    def update(self):
        # Update the ships position  based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        # Draw the ship at its current position
        self.screen.blit(self.image, self.rect)