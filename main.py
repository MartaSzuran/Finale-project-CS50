import sys
import pygame
from pygame.sprite import Group

import sprites
from sprites import Missile, Explosion, draw_text, my_font, Ship, Letter

# get to know more about the clocks
mainClock = pygame.time.Clock()
pygame.init()

# create screen
screen = pygame.display.set_mode((1200, 800), 0, 32)
pygame.display.set_caption("Shoot the words")

# adding variable click to control players clicking
click = False


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


def create_letters(position_x, position_y):
    # make objects of class letters
    # equal to the length of key_letters list
    letters_list = sprites.choose_the_letter()
    # parameter to change position_x of each letter
    change_x = -10
    # create list of letters object
    letters_obj = Group()
    for letter in letters_list:
        # control the way letters obj are draw on the screen by changing position_x
        if letter in ["w", "m"]:
            letter = Letter(screen, (position_x + change_x), position_y, letter)
            letters_obj.add(letter)
            change_x += 30
        elif letter in ["i", "j", "l"]:
            letter = Letter(screen, (position_x + change_x), position_y, letter)
            letters_obj.add(letter)
            change_x += 18
        else:
            letter = Letter(screen, (position_x + change_x), position_y, letter)
            letters_obj.add(letter)
            change_x += 23
    return letters_obj


# game
def game():
    # creating ship object
    ship = Ship(screen)

    # creating group of missiles objects
    missiles = Group()
    missile = Missile(screen, 1040, 450)
    missiles.add(missile)

    # creating an explosion object
    explosion = Explosion(screen)

    # take time to move the ship up and down
    ship.create(pygame.time.get_ticks())

    missile_letters = create_letters(missile.position_x, missile.position_y)

    # control if player want to play
    running = True

    while running:
        # track current time
        current_time = pygame.time.get_ticks()

        # screen refreshment
        screen.fill((102, 255, 255))

        # add score to the right top of the screen
        draw_text("Score: ", my_font, (102, 102, 255), screen, 1030, 30)

        # draw the ship on the game screen
        ship.draw(current_time)

        # draw the explosion
        explosion.draw(current_time)

        for missile in missiles.copy():
            # show missile on the screen
            missile.draw()
            # move the missile
            missiles.update()

            # draw letter above the missile
            for letter in missile_letters.copy():
                letter.draw()
                letter.update()

            if missile.position_x == 160:
                # missile come close to the ship missile remove
                missiles.remove(missile)

                # remove the letters with the missile
                for letter in missile_letters.copy():
                    letter.kill()

                # explosion.create function takes current positions and current time of missile remove event
                # to create longer blow effect
                explosion.create(position_x=missile.position_x,
                                 position_y=missile.position_y,
                                 time=current_time)
                # after removing create another missile and add it to the missile group
                missile = Missile(screen, 1040, 450)
                missiles.add(missile)

                missile_letters = create_letters(missile.position_x, missile.position_y)

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

            # get the event of user pressing the button, and compare it with the key letter
            #if event.type == pygame.KEYDOWN:
                #if pygame.key.name(event.key) == letter.letter:
                    #missile.player_key()
                    #print(pygame.key.name(event.key))

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
