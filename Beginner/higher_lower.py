'''A guessing game.
Who has the most followers on Social media. The user should guess between two people. If the user guessed correctly, continue game and add to score. If input is wrong, stop game. Show score so far.'''

from art import higher_lower_logo, higher_lower_vs
from game_data import data
import random
import os

continue_game = True
score = 0
print(logo)  # artwork


def clear():
    return os.system('clear')


while continue_game:
    OPTION_A = random.choice(data)
    OPTION_B = random.choice(data)
    
    print(higher_lower_logo)
    
    # testing
    print(f"A: {OPTION_A['follower_count']}")
    print(f"B: {OPTION_B['follower_count']}")

    # TODO: Get everything on the console
    print(
        f"Compare persons A: {OPTION_A['name']}, {OPTION_A['description']}, from {OPTION_A['country']}.")
    print(higher_lower_vs)  # artwork
    print(
        f"vs B: {OPTION_B['name']}, {OPTION_B['description']}, from {OPTION_B['country']}.")

    # TODO: Get input from user
    guess = input("Type A or B: ").upper()

    # TODO: Is the user right or wrong?
    highest_followers = ''

    # who has the most followers
    if OPTION_A['follower_count'] > OPTION_B['follower_count']:
        highest_followers = 'A'
    elif OPTION_A['follower_count'] < OPTION_B['follower_count']:
        highest_followers = 'B'
    else:  # if its a draw
        highest_followers = ''

    if guess == highest_followers:
        score += 1
        clear()
        print("AGAIN!!!!")
    else:
        # end game, you lose!
        continue_game = False
        print(f"Your score is: {score}")
