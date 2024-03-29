import time
import pygame
from pygame.sprite import Sprite
import string
import random
import pygame.font

pygame.init()

# create new object on which I can call the render method.
# or use pygame.freetype.Font if the font is inside my director
my_font = pygame.font.SysFont("Times New Roman", 30)

# remember when changing speed the position_x need to be divide by it f.e. 160/ 2,
# if 160/3 the missile will fly away
SPEED = 2


def draw_text(text, font, color, surface, x, y):
    # drawing text by creating local variable text_surface
    # font.render (text = what we want to say, 1 (or True) = is for anti-aliasing, color = text color)
    text_surface = font.render(text, 1, color)
    # getting dimensions of the rect
    text_rect = text_surface.get_rect()
    # text position inside rectangular = assigns an x and y position to the center of the rectangle
    # we can also use f.e. top left
    text_rect.topleft = (x, y)
    # put text onto our canvas
    surface.blit(text_surface, text_rect)


def choose_the_letter(number):
    alpha_letters = list(string.ascii_lowercase)

    # create list of letter above the missile
    key_letters = []

    # add randomly chosen letters to the list of missile letters
    # later add rounds which control quantity of letters in word
    for letter in range(number):
        letter = random.choice(alpha_letters)
        key_letters.append(letter)
        # print(len(letters))
    return key_letters


class Background(Sprite):
    """Create base class background."""
    def __init__(self, screen, image, position_x, position_y, speed):
        # take all the components which need background objects
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed

    def update(self):
        self.position_x -= self.speed
        if self.position_x <= -30:
            self.position_x = 1150

    def draw(self):
        self.screen.blit(self.image, (self.position_x, self.position_y))


class Clouds(Background):
    """Change update in class Background."""
    def update(self):
        super().update()
        if self.position_x <= -100:
            position_x_list = (1200, 1050, 1100)
            self.position_x = random.choice(position_x_list)
            position_y_list = (50, 150, 250)
            self.position_y = random.choice(position_y_list)


class Waves(Background):
    """Create waves class based on the Background claas."""
    def update(self):
        super().update()
        if self.position_x <= -10:
            position_x_list = (1150, 950, 750)
            self.position_x = random.choice(position_x_list)
            position_y_list = (530, 620, 710)
            self.position_y = random.choice(position_y_list)


class Lives(Sprite):
    """Create hearts objects on the screen."""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        # using .convert_alpha make image background transparent
        self.image = pygame.image.load("sprites/heart.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.position_y = 30

    def draw(self, position_x):
        self.screen.blit(self.image, (position_x, self.position_y))


class Letter(Sprite):
    pressed_letter = False
    """Create letter object."""
    def __init__(self, screen, position_x, position_y, letter):
        super().__init__()
        self.screen = screen
        self.letter = letter
        self.position_x = position_x
        self.position_y = position_y

    def update(self):
        # move missile to the left with particular speed
        self.position_x -= SPEED

    def draw(self):
        # draw one letter
        # choose different font
        letter_font = pygame.font.SysFont("Sans", 40)
        # use draw_text to create a letter above the missile
        # check if user pressed the letter on the keyboard if he has set color to green, otherwise black
        if self.pressed_letter:
            draw_text(self.letter, letter_font, (0, 255, 0), self.screen, self.position_x + 10,
                      self.position_y - 20)
        else:
            draw_text(self.letter, letter_font, (0, 0, 0), self.screen, self.position_x + 10,
                      self.position_y - 20)

    def change_color(self):
        self.pressed_letter = True
        return self.pressed_letter


class Missile(Sprite):
    """Creating missiles flying into the ship,"""
    def __init__(self, screen, position_x, position_y):
        super().__init__()
        """Initialize missiles."""
        # simple syntax super().__init__()
        # creating missile
        self.screen = screen
        self.image = pygame.image.load("sprites/missile.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # position and speed
        self.position_x = position_x
        self.position_y = position_y

    def update(self):
        # move missile to the left with particular speed
        self.position_x -= SPEED

    def draw(self):
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
        self.screen = screen
        # using .convert_alpha make image background transparent
        self.image = pygame.image.load("sprites/explosion.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

    def draw(self, time):
        current_time = time
        # if difference between current_time and time taken from missile.remove() function
        # is bigger than 300 stop drawing image
        if (current_time - self.time) > 200:
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


class Ship:
    time = 0
    moving_ship = False
    """Creating ship class."""
    def __init__(self, screen):
        """Initialize sea ship."""
        self.screen = screen
        # loading ship image and load its rect
        self.image = pygame.image.load("sprites/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def draw(self, game_time):
        """Drawing ship on the screen."""
        current_time = game_time
        if self.moving_ship:
            self.screen.blit(self.image, (60, 400))
        else:
            self.screen.blit(self.image, (60, 390))

        if (current_time - self.time) > 300:
            if self.moving_ship:
                self.moving_ship = False
            else:
                self.moving_ship = True

            self.time = current_time

    def create(self, game_time):
        self.time = game_time
        self.moving_ship = True


class Watch:
    """Class for measure the time."""
    def __init__(self):
        self.time = round(time.time(), 2)

    def __str__(self):
        return str(self.time)

    def measure(self):
        first_time = self.time
        second_time = time.time()
        delta_time = second_time - first_time
        return delta_time

    def reset(self):
        self.time = round(time.time(), 2)

    def countdown(self, time_to_wait):
        time.sleep(time_to_wait)
