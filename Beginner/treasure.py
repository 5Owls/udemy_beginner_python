print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
******************************************************************************* ''')

print("Welcome to Treasure Island.")
direction = input("Do you want to go left or right? ")
lowercase_direction = direction.lower()

if lowercase_direction == 'right':
    print("Oeps, you fell off a clive. Game over!")
else:
    river = input("There is a river. Do you wait for a boat or swim across? ")
    lower_river = river.lower()
    if lower_river == 'swim':
        print("A shark ate you. Game over!")
    else:
        door = input("You arrive on the other side. There are 3 doors. Yellow, Blue or Red. Pick one: ")
        lower_door = door.lower()
        if lower_door == 'red' or lower_door == 'blue':
            print("Game over!")
        else:
            print("Congrats! you win the treasure!")