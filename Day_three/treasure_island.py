#!/usr/bin/python3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Write your code below this line 👇

print("Jounery begins, you are at a crossroad...")
choice = input("Go left or right? ")
choice = choice.lower()

if choice == "right":
    print("you fell into a snake pit, game over")
elif choice == "left":

    print("There are three goblins on the way, you must fight them")
    fight_or_run = input("fight or run?: ")
    fight_or_run = fight_or_run.lower()
    if fight_or_run == "run":

        print("you ran away and fell off from a cliff, game over")
    elif fight_or_run == "fight":
        print("Your barely survived, you are at a river")

    print("you can swim or wait for a boat")
    swim_or_wait = input("swim or wait?: ")
    swim_or_wait = swim_or_wait.lower()
    if swim_or_wait == "swim":
        print("You were eaten by a shark, game over")
    elif swim_or_wait == "wait":
        print("You waited for a boat and reached the other side of the river")
        print("You have three doors in front of you, red, blue and yellow")
        which_door = input("Which door do you choose?: ")
        which_door = which_door.lower()
        if which_door == "red":
            print("You fell in a lava pit, game over")
        elif which_door == "blue":
            print("You were eaten by a beast, game over")
        elif which_door == "yellow":
            print("You found the treasure, you win!")
