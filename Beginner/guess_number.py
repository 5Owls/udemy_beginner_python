""" A game: Guess the number the computer is thinking. It will give you either 5 clues(difficult) or 10 clues(easy)"""

import random
from art import guess_game_logo

def choice_difficulty():
    ''' 
    Prints how many guesses are allowed based on easy or difficult. 
    Returns an integer based on easy = 10 or difficult = 5.
    '''
    input_difficulty = input("Do you want it 'difficult' or 'easy': ").lower()
    number_of_guesses = 0

    if input_difficulty == 'easy':
        print("You have 10 guesses!")
        number_of_guesses = 10
        return number_of_guesses
    elif input_difficulty == 'difficult':
        print("You have 5 guesses!")
        number_of_guesses = 5
        return number_of_guesses
    else:
        print("Check your spelling, type again: ") #checks for spelling errors
        #❗️❗️❗️❗️this gives an error when user types in correct speling afterwards
        #❗️❗️❗️❗️TypeError: 'NoneType' object cannot be interpreted as an integer
        choice_difficulty()


def clues(para_input_guess):
    ''' Gives the user clues to get a better idea of what the random number is.'''
    if para_input_guess > RANDOM_NUMBER:
        print("Too high")
    else:
        print("Too low")

def generate_random_number():
    ''' the computer thinks of a random number between 0 and 100.'''
    return random.randint(0, 100)

print(guess_game_logo)

#Get user to input easy or difficult
level_difficulty = choice_difficulty()

print("I'm thinking of a number between 0 and 100, Guess!!")
RANDOM_NUMBER = generate_random_number()

#testing purposes
print(f"Pssst the number is:  {RANDOM_NUMBER}")


#give the right amount of clues
for i in range(0, level_difficulty): 
    count_down = level_difficulty - 1 - i
    #input of user
    input_guess = int(input("Guess a number:..."))
    #give clues to user
    if input_guess ==  RANDOM_NUMBER:
        print(f"You got it!! Great guess, the number was {RANDOM_NUMBER}")
        break 
    elif count_down == 0:
        print(f"Zero tries left! The number was {RANDOM_NUMBER} ")
    else:
        clues(input_guess)
        print(f"You have {count_down} left. ")
    



