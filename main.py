import sys
import pygame
from pygame.sprite import Group

import sprites
from sprites import Missile, Explosion, draw_text, my_font, Ship, Letter, Lives

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


def create_letters(position_x, position_y, numb):
    """Make objects of class letters equal to the length of key_letters list"""
    # parameter to change position_x of each letter
    change_x = -10
    # create list of randomly chosen letters objects
    letters = sprites.choose_the_letter(numb)
    # create list of letters object
    letters_obj = []
    for letter in letters:
        # control the way letters obj are draw on the screen by changing position_x
        if letter in ["w", "m"]:
            letter = Letter(screen, (position_x + change_x), position_y, letter)
            letters_obj.append(letter)
            change_x += 30
        elif letter in ["i", "j", "l", "t", "f"]:
            letter = Letter(screen, (position_x + change_x), position_y, letter)
            letters_obj.append(letter)
            change_x += 13
        else:
            letter = Letter(screen, (position_x + change_x), position_y, letter)
            letters_obj.append(letter)
            change_x += 25
    return letters_obj


def create_collection_of_current_keys(collection_of_letters_objects):
    # create list of keys
    keys = []
    for letter in collection_of_letters_objects:
        key_letter = letter.letter
        keys.append(key_letter)

    return keys


# add function to erase all colors if the wrong letter is pressed
def check_key(collection_of_letters_objects, counter, bool_key):
    if bool_key:
        letter_counter = 0
        for letter in collection_of_letters_objects:
            if letter_counter < counter:
                letter.pressed_letter = True
            else:
                letter.pressed_letter = False
            letter_counter += 1
        bool_key = False
    return bool_key


def increase_dif_with_time(start_time, numb_of_letters, current_game_time):
    difference = current_game_time-start_time
    if difference > 10000:
        numb_of_letters += 1
        start_time = current_game_time
        print("10 sec")
    return numb_of_letters, start_time


# game
def game():
    # creating ship object
    ship = Ship(screen)

    # creating group of missiles objects
    missiles = Group()
    missile = Missile(screen, 1040, 450)
    missiles.add(missile)

    # add lives to the screen
    heart_1 = Lives(screen)
    heart_2 = Lives(screen)
    heart_3 = Lives(screen)

    # creating an explosion object
    explosion = Explosion(screen)

    # take time to move the ship up and down
    ship.create(pygame.time.get_ticks())

    # bool to check if the key is the same as pressed letter by the user
    right_key = False
    counter = 0

    # starting point for number of letters
    numb_of_letters = 1
    # starting point for counting time
    start_time = 0

    # create letter above the missile
    word = create_letters(missile.position_x, missile.position_y, numb_of_letters)
    # print(word)

    # initialize score value
    score = 0

    # control if player want to play
    running = True
    while running:
        # track current time
        current_time = pygame.time.get_ticks()
        # print(current_time)

        numb_of_letters, start_time = increase_dif_with_time(start_time, numb_of_letters, current_time)

        # screen refreshment
        screen.fill((102, 255, 255))

        # add score to the right top of the screen
        draw_text("Score: ", my_font, (102, 102, 255), screen, 1030, 30)
        draw_text(str(score), my_font, (102, 102, 255), screen, 1120, 30)
        timer = current_time*0.001
        draw_text(str(round(timer, 1)), my_font, (102, 102, 255), screen, 20, 30)

        # draw lives
        heart_1.draw(540)
        heart_2.draw(590)
        heart_3.draw(640)

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
            for letter in word:
                letter.draw()
                letter.update()

            if missile.position_x == 160:
                score -= 20
                # print(score)
                # missile come close to the ship missile remove
                missiles.remove(missile)

                # explosion.create function takes current positions and current time of missile remove event
                # to create longer blow effect
                explosion.create(position_x=missile.position_x+30,
                                 position_y=missile.position_y,
                                 time=current_time)
                # after removing create another missile and add it to the missile group
                missile = Missile(screen, 1040, 450)
                missiles.add(missile)

                # I don't have to remove letters from word because I overwrite thar list
                word = create_letters(missile.position_x, missile.position_y, numb_of_letters)
                # print(numb_of_letters)

        # print(len(missiles))

        # collections of keys
        keys = create_collection_of_current_keys(word)

        # waiting for press button or mouse button
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # escape to main menu
                    running = False
            # get the event of user pressing the button, and compare it with the key letter
            if event.type == pygame.KEYDOWN:
                # print(keys)
                # print(len(keys))

                if pygame.key.name(event.key) == keys[counter]:
                    right_key = True
                    counter += 1
                    # print(counter)
                    # print(pygame.key.name(event.key))
                else:
                    score -= 5

                if counter == (len(keys)):
                    # create function for that code because it is repeated
                    for missile in missiles.copy():
                        missiles.remove(missile)
                        counter = 0
                        score += 10
                        # print(score)

                        # explosion.create function takes current positions and current time of missile remove event
                        # to create longer blow effect
                        explosion.create(position_x=missile.position_x+30,
                                         position_y=missile.position_y,
                                         time=current_time)
                        # after removing create another missile and add it to the missile group
                        missile = Missile(screen, 1040, 450)
                        missiles.add(missile)

                        # I don't have to remove letters from word because I overwrite that list
                        word = create_letters(missile.position_x, missile.position_y, numb_of_letters)
                        print(numb_of_letters)

        # check_key function change the color of letters object
        check_key(word, counter, right_key)

        # display last changed screen
        pygame.display.update()
        # print(current_time)

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
