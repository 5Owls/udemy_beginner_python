# FIRST VERSION

# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# list_message = []
# list_position_in_alphabet = []
# list_new_position = []
# list_new_message = []
# new_message = ''

# # get message from user
# list_message = list(input("What is your message? ").upper())
# shift = int(input("What shift value do you want to moe your message with? "))

# # find the index position of each letter in the alphabet
# for letter in list_message:
#     list_position_in_alphabet.append(alphabet.index(letter))

# # find new index postion of encoded message
# for value in list_position_in_alphabet:
#     list_new_position.append(value + shift)
# print(list_new_position)

# # look at index value and find ltter at that index.
# for value in list_new_position:
#     list_new_message.append(alphabet[value])

# new_message = ''.join(list_new_message)
# print(list_new_message)
# print(new_message)

# SECOND VERSION
from art import caesar_logo

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

use_app = True  # does the user want to continue with the app

# the functions combines encode and decode function to make it more concise


def caesar(plain_text, shift_amount, cipher_direction):
    # try using string manipulation
    end_text = ''
    if cipher_direction == "decode":
        shift_amount = shift_amount * (-1)
    for letter in plain_text:
        if letter not in alphabet:  # if user input is not in the alphabet
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
    print(f'Here is the {direction}d result: {end_text}')


# this is where the start of the program is||This is where the calling/invoking happens:
print(caesar_logo)

while use_app:
    direction = input("Type 'encode' to encrypt. Type 'decode' to decrypt:\n")
    text = input("Type your message:\n").upper()
    shift = int(input("Type the shift number:\n"))

    # if the user wants a shift number great than number of items in alphabet
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

    use_app_input = input(
        "Do you want to try again? Yes to continue, No to end\n").lower()
    if use_app_input == 'no':
        use_app = False
        print("Good bye. 5...4...3...2...1")


# notes to self:
# better names for variables
# string manipulation is probably better than first converting it to a list and then working with it.
