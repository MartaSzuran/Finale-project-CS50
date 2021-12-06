# Finale_project_CS50
#### Video Demo:  <URL HERE>
Game: "Shoot the letters!"

TITLE
Game created to improve keyboard typing.

PLOT
Ship swims through the seas and to get save to its destinacion player need to help it
and shoot the torpedos.

To destroy them before they get to the ship player need to write propiate letters,
printed above the torpedos. For each destroyed torpedo player gets 10 points, 
but he/she need to be carefull because pressing wrong once makes your score smaller with 5 points!

The goal is to write letters without mistakes and get to the top 10 of the highest scores! 

Good luck and have fun :)

DESCRIPTION
Learning how to wirte on the keyboard properly and fast is really important nowadays.
Creating game "Shoot the letters!" give me a lot of joy and on the other hand 
was truly very challenging. 

This game is pushing player to become perfectionist in case to get the highest score he could, 
and to become competitive with other players! At the beggining above the torpedo is one letter, 
but with time thier amonut increase.

To create this project I used python, pygame and sqlite3. 

Project has 3 files:

main.py 
contain: 

main_menu() function:
Create main menu with buttons:
+ game - start playing - run function game()* 
+ ranking - check top 10 scores - run function score()* 
+ exit - exit game - if pressed game is over

* game():
	starts drawing screens and sprites, contain all game logic (score, creating torpedos (missiles), 
	loosing hearts when torpedos reach the ship) with some helpfull function 
	(create_letters() - create letter abouve the torpedos; create_collection_of_current_keys() 
	and check_key() - to grab pressed buttons from events and check if player pressed 
	propiate once; increase_dif_with_time() - add another letter above the torpedo.
	
--> after loosing all three hearts function game_over() launch:
	show game over screen, 
	- if your score is in top 10, ask you for name, after input,
 	save it with score in ranking.db file and run ranking() function
	- else just inform that the game is over

* ranking():
	open ranking.db file and print 10 highest scores (player name and score)

sprites.py
contain: 
Create sprites using Object Oriented Programming.
Modules used: time, string, random, pygame.font, pygame and pygame.sprite

database.py
contain: 
Work with sqlite3 module, contain many functions created to work with database like:
insert_data_into_db(), print_table(), format_data()





	








 

