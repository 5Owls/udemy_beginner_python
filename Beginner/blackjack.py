import random
from art import blackjack_logo
import os

continue_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 , 10]

def clear():
    return os.system('clear')

def tally_cards(card1, card2):
    ''' Sum cards together'''
    return card1 + card2

def get_card():
    ''' randomly chooses ONE cards from cards list(deck)'''
    return random.choice(cards)

def compare(para_user_tally, para_dealer_tally):
    ''' Compare hand of cards. Determines if its a draw or who wins '''
    if para_dealer_tally == para_user_tally:#Draw
        print(f"Draw, you both have: {para_dealer_tally}")
    elif para_user_tally > 21:#user is over 21
        print(f"You lose!! your tally is: {para_user_tally}")
    elif para_dealer_tally > 21:
        print(f"Dealer loses!! Its tally: {para_dealer_tally}")
    elif para_user_tally > para_dealer_tally:#user has more than dealer
        print(f"You WIN!! Your tally is: {para_user_tally}, it's tally: {para_dealer_tally}")
    elif para_dealer_tally > para_user_tally:#dealer has more than user
        print(f"Dealer wins!! It's tally: {para_dealer_tally}, Your tally: {para_user_tally}")

def play_game():
    while continue_game:
        #printlogo
        print(blackjack_logo)

        #give hand of cards
        user_cards = [get_card(), get_card()]
        dealer_cards = [get_card(), get_card()]

        #sum hand of cards
        user_tally = tally_cards(user_cards[0], user_cards[1])
        dealer_tally = tally_cards(dealer_cards[0], dealer_cards[1])

        print(f"Your cards: {user_cards}, your tally: {user_tally}")
        print(f"Dealers card: {dealer_cards[0]}")

        #get extra card for user and dealer
        #ask user if they want an extra card
        get_another_card_input = input("Do you want another card? 'y' for yes, 'n' for no... ")

        if get_another_card_input == 'y': 
            user_cards.append(get_card())
            #tally in extra card
            user_tally = tally_cards(user_tally, user_cards[2])

        #dealer extra card if it has less than 17
        if dealer_tally < 17:
            dealer_cards.append(get_card())
            #tally in extra card
            dealer_tally = tally_cards(dealer_tally, dealer_cards[2])

        #end of game
        
        #we show all cards
        print(f"Your cards: {user_cards}. Dealer's cards: {dealer_cards}")

        #who won?
        compare(user_tally, dealer_tally)

        #does the user want to play again?
        play_again = input("Do you want to play again? 'y' for yes, 'n' for no... ")
        if play_again =='y':
            clear()
            play_game()
        else:
            break

play_game()





