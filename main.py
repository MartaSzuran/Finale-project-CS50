import sys
import pygame
import pygame.font
from pygame.sprite import Group
import random

from settings import Settings
from ship import Ship
from missile import Missile, Explosion

# know more about the clocks
mainClock = pygame.time.Clock()
pygame.init()

# create new object on which I can call the render method.
# or use pygame.freetype.Font if the font is inside my director
my_font = pygame.font.SysFont("Times New Roman", 30)

# Settings object
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), 0, 32)
pygame.display.set_caption("Shoot the words")

# adding variable click to control players clicking
click = False


def draw_text(text, font, color, surface, x, y):
    # drawing text by creating local variable text_surface
    # font.render (text = what we want to say, 1 (or True) = is for anti-aliasing, color = text color)
    text_surface = font.render(text, 1, color)
    # getting dimensions of the rect
    text_rect = text_surface.get_rect()
    # text position inside rectangular = assigns an x and y position to the center of the rectangle
    # we can also use f.e. topleft
    text_rect.topleft = (x, y)
    # put text onto our canvas
    surface.blit(text_surface, text_rect)


def main_menu():
    while True:
        # screen refreshment
        screen.fill((102, 255, 255))

        # font_obj_name.render_to( where = screen, position(x=550, y=40), text to render= "Main menu", color = red)
        draw_text("Main Menu", my_font, (102, 102, 255), screen, 535, 70)

        # mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # buttons rectangular objets = button_2 = pygame.Rect(50, 100, 200, 50)
        # to write a text on those buttons need to make it as a surface
        button_1 = pygame.Rect(505, 200, 200, 50)
        button_2 = pygame.Rect(505, 300, 200, 50)
        button_3 = pygame.Rect(505, 400, 200, 50)

        # if mouse is on the buttons do smth
        if button_1.collidepoint(mouse_x, mouse_y):
            if click:
                game()
        if button_2.collidepoint(mouse_x, mouse_y):
            if click:
                rating()
        if button_3.collidepoint(mouse_x, mouse_y):
            if click:
                sys.exit()

        # draw buttons on the screen
        pygame.draw.rect(screen, (192, 192, 192), button_1)
        pygame.draw.rect(screen, (192, 192, 192), button_2)
        pygame.draw.rect(screen, (192, 192, 192), button_3)

        # draw text on the buttons
        draw_text("Play", my_font, (0, 102, 204), screen, 580, 208)
        draw_text("Rating", my_font, (0, 102, 204), screen, 567, 308)
        draw_text("Exit", my_font, (0, 102, 204), screen, 580, 408)

        # set click to False
        click = False

        # waiting for press button or mouse button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.K_DOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # display last changed screen
        pygame.display.update()

        # clock
        mainClock.tick(60)


# game
def game():
    # creating ship object
    ship = Ship(screen)

    # creating group of missiles objects
    missiles = Group()
    missile = Missile(screen, 1040, 450, 4)
    missiles.add(missile)

    # creating an explosion object
    explosion = Explosion(screen)

    running = True
    while running:

        # track current time
        current_time = pygame.time.get_ticks()

        # screen refreshment
        screen.fill((102, 255, 255))

        # add score to the right top of the screen
        draw_text("Score: ", my_font, (102, 102, 255), screen, 1030, 30)

        # draw the ship on the game screen
        ship.draw(60, 500)

        # draw the explosion
        explosion.draw(current_time)

        for missile in missiles.copy():
            missile.show_missile()
            missiles.update()
            if missile.position_x == 160:
                # missile come close to the ship missile remove
                missiles.remove(missile)
                explosion.create(position_x=missile.position_x,
                                 position_y=missile.position_y,
                                 time=current_time)
                # after removing create another missile and add it to the missile group
                missile = Missile(screen, 1040, 450, 4)
                missiles.add(missile)

        # follow number of missiles in missiles group in terminal window
        # print(len(missiles))

        # waiting for press button or mouse button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # escape to main menu
                    running = False

        # display last changed screen
        pygame.display.update()

        # clock
        mainClock.tick(60)


# show rating screen
def rating():
    running = True
    while running:
        # screen refreshment
        screen.fill((102, 255, 255))

        # add name to the option screen
        draw_text("Rating", my_font, (102, 102, 255), screen, 535, 70)

        # waiting for press button or mouse button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # escape to main menu
                    running = False

        # display last changed screen
        pygame.display.update()

        # clock
        mainClock.tick(60)


main_menu()
