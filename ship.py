import pygame


class Ship:
    time = 0
    moving_ship = False
    """Creating ship class."""
    def __init__(self, screen):
        """Initialize sea ship."""
        self.screen = screen
        # loading ship image and load its rect
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def draw(self, game_time):
        """Drawing ship on the screen."""
        current_time = game_time
        if self.moving_ship:
            self.screen.blit(self.image, (60, 500))
        else:
            self.screen.blit(self.image, (60, 490))

        if (current_time - self.time) > 300:
            if self.moving_ship:
                self.moving_ship = False
            else:
                self.moving_ship = True

            self.time = current_time

    def create(self, game_time):
        self.time = game_time
        self.moving_ship = True

