# Finale_project_CS50
## Video Demo: HERE&gt;
## Game: **"Shoot the letters!"**

## TITLE
Game created to improve keyboard typing.

## PLOT
Ship swims through the seas and to get save to its destination player need to help it
and shoot the torpedoes.

To destroy them before they get to the ship player need to write appropiate letters,
printed above the torpedoes. For each destroyed torpedo player gets 10 points,
but he/she need to be careful because pressing wrong buttons makes your score smaller with 5 points!

The goal is to write letters without mistakes and get to the top 10 of the highest scores!

Good luck and have fun :)

## DESCRIPTION
Learning how to write on the keyboard properly and fast is really important nowadays.
I have created this game to encourage people (especially children), to grab the challenge and try to learn how to write,
later even rivalry with their friends in top 10 ranking. Creating game **"Shoot the letters!"** give me a lot of joy.

This game is pushing player to become perfectionist in case to get the highest score he could,
and to become competitive with other players! At the beginning above the torpedo is one letter,
but with time their amount increase.

## MAIN TOPICS:
- **Python**
    OOP
    modules: 
	string
	random
	time
	pygame
- **SQL**
    sqlite3 module
    create connection, cursor, close connection
    create database
    create table
    insert into
    delete
    searching through resultes with where
    sort results	
	
- **Git & Git workflow**
    git clone
    git add
    git commit
    git push

- **GitHub**
    create a repository

- **Pygame**
    pygame sprite class
    super()
    update()

## CHALLENGES
Working with that project was difficult for me because in many cases I need to learn new things,
especially within pygame. How to add move to sprites, how display screen works or timer.
The most difficult was adding logic to letters and changing their colour.
Working with events was also some new features that I needed to understand. Finally, I am really happy
and proud of myself that I am up to create such game. 

In future, I plan:
- make entire project as OOP.
- create website with overall ranking

## INSTALLATION
To play my game you need to download python, my code from github, and enjoy playing !

## HELPS
I use some help from:
- entire CS50 course
- python documentation
- https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
- https://www.youtube.com/watch?v=byHcYRpMgI4
- https://www.youtube.com/watch?v=FfWpgLFMI7w
- https://www.youtube.com/watch?v=a5JWrd7Y_14
- stack overflow

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
