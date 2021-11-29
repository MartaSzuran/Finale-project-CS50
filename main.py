import sys
import pygame
from pygame.sprite import Group

import sprites
from sprites import Missile, Explosion, \
    draw_text, my_font, \
    Ship, Letter, Lives, Waves, Background, Clouds, Watch

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
                ranking()
        if button_3.collidepoint(mouse_x, mouse_y):
            if click:
                sys.exit()

        # draw buttons on the screen
        pygame.draw.rect(screen, (192, 192, 192), button_1)
        pygame.draw.rect(screen, (192, 192, 192), button_2)
        pygame.draw.rect(screen, (192, 192, 192), button_3)

        # draw text on the buttons
        draw_text("Play", my_font, (0, 102, 204), screen, 580, 208)
        draw_text("Ranking", my_font, (0, 102, 204), screen, 560, 308)
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
            change_x += 34
        elif letter in ["i", "j", "l", "t", "f", "r"]:
            letter = Letter(screen, (position_x + change_x), position_y, letter)
            letters_obj.append(letter)
            change_x += 16
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


def increase_dif_with_time(numb_of_letters, timer, time_delta):
    """Increasing difficulty with time."""
    if time_delta > 17:
        numb_of_letters += 1
        timer.reset()
    return numb_of_letters, timer


# game
def game():
    # initialize time
    timer = Watch()

    # creating ship object
    ship = Ship(screen)

    # creating group of missiles objects
    missiles = Group()
    missile = Missile(screen, 1040, 450)
    missiles.add(missile)

    # create group of hearts objects
    hearts = Group()
    for i in range(3):
        heart = Lives(screen)
        hearts.add(heart)

    # create waves objects and add it to the sprites group waves
    wave_image = pygame.image.load("wave.png")
    wave_1 = Waves(screen, wave_image, position_x=1150, position_y=530, speed=2.4)
    wave_2 = Waves(screen, wave_image, position_x=950, position_y=620, speed=2.4)
    wave_3 = Waves(screen, wave_image, position_x=750, position_y=710, speed=2.4)
    waves = Group(wave_1, wave_2, wave_3)

    # create clouds objects and add it to the clouds group
    cloud_image = pygame.image.load("cloud.png")
    cloud_1 = Clouds(screen, cloud_image, position_x=600, position_y=50, speed=1.4)
    cloud_2 = Clouds(screen, cloud_image, position_x=300, position_y=130, speed=1.4)
    cloud_3 = Clouds(screen, cloud_image, position_x=1020, position_y=210, speed=1.4)
    clouds = Group(cloud_1, cloud_2, cloud_3)

    # add island image and object
    island_image = pygame.image.load("island.png")
    island = Background(screen, island_image, position_x=1150, position_y=320, speed=0.3)

    # add big cloud image and object
    big_cloud_image = pygame.image.load("cloud-computing.png")
    big_cloud = Background(screen, big_cloud_image, position_x=850, position_y=80, speed=0.8)

    # creating an explosion object
    explosion = Explosion(screen)

    # take time to move the ship up and down
    ship.create(pygame.time.get_ticks())

    # bool to check if the key is the same as pressed letter by the user
    right_key = False
    counter = 0

    # starting point for number of letters
    numb_of_letters = 1

    # create letter above the missile
    word = create_letters(missile.position_x, missile.position_y, numb_of_letters)
    # print(word)

    # initialize score value
    score = 0

    # number of missiles that hit the ship
    missile_hit_the_ship = 0

    # control if player want to play
    running = True

    while running:
        time_delta = timer.measure()
        # print(time_delta)
        # track current time
        current_time = pygame.time.get_ticks()
        # print(current_time)

        # screen refreshment
        screen.fill((0, 128, 255))

        # color the screen sky
        sky = pygame.Rect((0, 0, 1200, 380))
        pygame.draw.rect(screen, (102, 255, 255), sky)

        island.draw()
        island.update()

        # add big cloud
        big_cloud.draw()
        big_cloud.update()

        # function which return number of letters increase by time
        numb_of_letters, timer = increase_dif_with_time(numb_of_letters, timer, time_delta)

        # add score to the right top of the screen
        draw_text("Score: ", my_font, (102, 102, 255), screen, 1030, 30)
        draw_text(str(score), my_font, (102, 102, 255), screen, 1120, 30)

        # draw lives
        # add creating hearts and add it to the sprite group
        # than use remove when missile hit the ship
        heart_position_x = 20
        for heart in hearts:
            x_pos_different = 50
            heart.draw(heart_position_x)
            # draw hearts in 3 different x locations
            heart_position_x += x_pos_different

        # draw waves on the screen
        for wave in waves:
            wave.draw()
            wave.update()

        # draw clouds on the screen
        for cloud in clouds:
            cloud.draw()
            cloud.update()

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

            if missile.position_x == 164:
                # count how many time missile get to the ship
                missile_hit_the_ship += 1

                # print(missile_hit_the_ship)
                # if missile get to the ship remove one heart from the screen
                if missile_hit_the_ship == 1:
                    hearts.remove(heart)
                elif missile_hit_the_ship == 2:
                    hearts.remove(heart)
                else:
                    draw_text("GAME OVER", pygame.font.SysFont("Verdana", 60), (0, 0, 0), screen, 420, 200)
                    pygame.display.flip()
                    timer.countdown(2)
                    running = False
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
                        # print(numb_of_letters)

        # check_key function change the color of letters object
        check_key(word, counter, right_key)

        # display last changed screen
        pygame.display.update()
        # print(current_time)

        # clock
        mainClock.tick(60)


# show rating screen
def ranking():
    running = True

    while running:
        # screen refreshment
        screen.fill((102, 255, 255))

        # add name to the option screen
        draw_text("Ranking", my_font, (102, 102, 255), screen, 535, 70)

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
