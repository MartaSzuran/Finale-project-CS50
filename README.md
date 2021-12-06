# Finale_project_CS50
## Video Demo: HERE&gt;
## Game: **"Shoot the letters!"**

## PLOT
Ship sails through the seas and in order to reach destination player has to protect it from the torpedoes using touch typing skills (typing without looking at the keyboard).

## DESCRIPTION
I have created this game to help people improve their touch typing skills.

This game is pushing the player to get the highest score he could, and to become competitive with other players!

The goal of the game is to type the letters printed above the torpedo, before it reach the ship.

For each destroyed torpedo player gets 10 points, but he needs to be careful because pressing wrong buttons makes his score smaller by 5 points!

Creating game **"Shoot the letters!"** gave me a lot of joy.

Good luck and have fun :)

## TECHNOLOGY STACK:
- **Python**
    Features: classes, strings, random, time
    Libraries:
        pygame:
            user input
            output graphics
            sprite

        sqllite3:
            create connection, cursor, close connection
            create database
            create table
            insert into
            delete
            searching through resultes with where
            sort results
      
- **Git**
    git clone
    git add
    git commit
    git push

- **GitHub**
    create a repository

##CHALLENGES
- managing complex project
- using external python libraraies
- searching through official documentations
- effectively searching for information on the internet
- managing drawing multiple items on the screen and their movement
- managing multiple objects interactions

## REFERENCES
I use some help from:
- CS50 course materials
- python documentation
- opis1 https://www.youtube.com/watch?v=byHcYRpMgI4
- opis2 https://www.youtube.com/watch?v=FfWpgLFMI7w
- opis3 https://www.youtube.com/watch?v=a5JWrd7Y_14
- sprites: wwww.flaticon.com

###### Detailed project architecture description:

Project contains three files:

**main.py**
contains:
* **main_menu()** function:
Create main menu with buttons:
+ game - start playing - run function *game()**
+ ranking - check top 10 scores - run function *score()**
+ exit - exit game - if pressed game is over

* **game()**:
    starts drawing screens and sprites, contain all game logic (score, creating torpedoes (missiles),
    loosing hearts when torpedoes reach the ship) with some helpful function
    (*create_letters()* - create letter above the torpedoes;
    *create_collection_of_current_keys()* and *check_key()* - to grab pressed buttons from events
    and check if player pressed appropiate once then change colour of letters to green;
    *increase_dif_with_time()* - add another letter above the torpedo.

--> after loosing all three hearts function *game_over()* launch:
    show "game over" screen,
    - if score is in top 10, ask player for name, after input,
    save it with score in ranking.db file and run *ranking()* function
    - else just inform that the game is over

* **ranking()**:
    open ranking.db file and print 10 highest scores (player name and score)

**sprites.py**
contains:
Create sprites using *Object Oriented Programming*.
Modules used: **time, string, random, pygame.font, pygame and pygame.sprite**

**database.py**
contains:
Work with sqlite3 module, contain many functions created to work with database like:
*insert_data_into_db(), print_table(), format_data()*