import os
from art import auction_logo_hammer

continue_bidding = True
highest_value = 0
highest_name = ''
silent_auction_dict = {}


def clear():
    return os.system('clear')


def find_highest_bidder(dict_auction):
    for key in silent_auction_dict:

        if silent_auction_dict[key] >= highest_value:
            highest_value = silent_auction_dict[key]
            highest_name = key

    print(f"The winner is: {highest_name} with a payment of ${highest_value}")


while continue_bidding:
    name = input("What is your name? ")
    amount = int(input("What is the amount you want to bid? $ "))

    silent_auction_dict[name] = amount
    input_continue = input("Do you want to continue? yes or no\n").lower()

    if input_continue == 'no':
        continue_bidding = False
    else:
        # calling the clear function to clear the screen so previous users info isnt visible.
        clear()
    find_highest_bidder(silent_auction_dict)


# ❗️❗️ NOTES TO SELF:
# Include commentary tests during coding
# use functions
