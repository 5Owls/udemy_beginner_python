import random

rock = "ROCK" # 0
paper = "PAPER" #1
scissors = "SCISSORS" #2

#user chooses rock, paper, scissors
user_input = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors: "))

print("\nYou choose:")
if (user_input == 0):
    print(rock)
elif (user_input == 1):
    print(paper)
else:
    print(scissors)

#computer randomly chooses rock, paper, scissors
print("\nComputer chooses: ")
computer_input = random.randint(0,2) #randomly choose between 0, 1, 2

if (computer_input == 0):
    print(rock)
elif (computer_input == 1):
    print(paper)
else:
    print(scissors)

if (user_input == computer_input):
    print("\nIt's a Draw!!")

#user inputs rock and its not a draw
if ((user_input == 0) and (computer_input == 2)): # user chooses rock, computer chooses scissors
    print("\nYou WIN!!")
elif((user_input == 0)) and (computer_input == 1): #user chooses rock, computer chooses paper
    print("\nYou LOSE!!")

# user inputs scissors
if ((user_input == 2) and (computer_input == 1)):# user chooses scissors, computer chooses paper
    print("\nYou WIN!!")
elif((user_input ==  2) and (computer_input == 0)):#user chooses scissors, computer chooses paper
    print("\nYou LOSE!!")

#user inputs PAPER
if ((user_input == 1) and (computer_input == 0)):#user chooses paper, computer chooses ROCK
    print("\nYou WIN!!")
elif ((user_input ==  1) and (computer_input == 2)):#user chooses paper, computer chooses scissors
    print("\nYou LOSE!!")
