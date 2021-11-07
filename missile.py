import pygame


class Missile:
    """Creating missiles flying into the ship,"""
    def __init__(self, screen):
        """Initilize missiles."""
        self.screen = screen
        self.image = pygame.image.load("missile.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def show_missile(self, position_x, position_y):
        self.screen.blit(self.image, (position_x, position_y))
