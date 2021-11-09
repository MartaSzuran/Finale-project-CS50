import pygame


class Ship:
    """Creating ship class."""

    def __init__(self, screen):
        """Initialize sea ship."""
        self.screen = screen
        # loading ship image and load its rect
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def show_ship(self, position_x, position_y):
        """Drawing ship on the screen."""
        self.screen.blit(self.image, (position_x, position_y))

