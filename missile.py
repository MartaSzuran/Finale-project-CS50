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


# change the image or get to know how to make image background transparent
class Explosion:
    """Creating explosion animation."""
    # position took from the main game loop
    position_x = 0
    position_y = 0
    # time get from pygame.time.get_tick()
    # current time when draw image
    time = 0
    # bool variable for control time of drawing image
    draw_image = False

    def __init__(self, screen):
        """Initialize explosion object."""
        super().__init__()
        self.screen = screen
        # using .convert_alpha make image background transparent
        self.image = pygame.image.load("explosion.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

    def draw(self, time):
        current_time = time
        # if difference between current_time and time taken from missile.remove() function
        # is bigger than 300 stop drawing image
        if (current_time - self.time) > 300:
            self.draw_image = False

        # if draw_image in True draw image
        if self.draw_image:
            self.screen.blit(self.image, (self.position_x, self.position_y))

    def create(self, position_x, position_y, time):
        # take positions, time from from the moment missile is removed from the screen and set draw_image to True
        self.position_x = position_x
        self.position_y = position_y
        self.time = time
        self.draw_image = True
