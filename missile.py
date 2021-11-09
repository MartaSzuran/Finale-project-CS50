import pygame
from pygame.sprite import Sprite


class Missile(Sprite):
    """Creating missiles flying into the ship,"""
    def __init__(self, screen, position_x, position_y, missile_speed_factor):
        """Initialize missiles."""
        # simple syntax super().__init__()
        super(Missile, self).__init__()
        # creating missile
        self.screen = screen
        self.image = pygame.image.load("missile.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # position and speed
        self.missile_speed_factor = missile_speed_factor
        self.position_x = position_x
        self.position_y = position_y

    def update(self):
        # move missile to the left with particular speed
        self.position_x -= self.missile_speed_factor

    def show_missile(self):
        self.screen.blit(self.image, (self.position_x, self.position_y))


# change the image or get to know how to make image backgraound transparent
class Explosion:
    """Explosion image."""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        # using .convert_aplha make image background transparent
        self.image = pygame.image.load("explosion.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

    def show_explosion(self, position_x, position_y, time_to_blit):
        if time_to_blit:
            self.screen.blit(self.image, (position_x, position_y))
            if pygame.time.get_ticks() == time_to_blit:
                time_to_blit = None
        return time_to_blit
