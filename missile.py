import pygame
from pygame.sprite import Sprite


class Missile(Sprite):
    """Creating missiles flying into the ship,"""
    def __init__(self, screen, position_x, position_y, missile_speed_factor):
        """Initialize missiles."""
        super(Missile, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("missile.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.missile_speed_factor = missile_speed_factor
        self.position_x = position_x
        self.position_y = position_y

    def show_missile(self):
        self.position_x -= self.missile_speed_factor
        self.screen.blit(self.image, (self.position_x, self.position_y))
