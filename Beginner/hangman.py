import random
from hangman_words import word_list
from art import hangman_stages_death, hangman_logo


dashed_word = []
end_of_game = False
lives = 6
guessed_list = []

print(hangman_logo)
random_word = random.choice(word_list)
print(f"Psst the word is: {random_word}")

for letter in random_word:
    dashed_word.append('_')

print(f"The word is: {dashed_word}")

# test code
# print(random_word)
# print(dashed_word)

while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in guessed_list:
        print("You've already used this letter. Try something else")
    else:
        guessed_list.append(guess_letter)

    # user wants to know where the letter is, if correctly guessed
    for index in range(0, len(random_word)):
        if guess_letter == random_word[index]:
            dashed_word[index] = guess_letter

    if guess_letter not in random_word:
        print(f"This letter *{guess_letter}* is not in the word. ")
        lives -= 1
        print(hangman_stages_death[lives])

    print(f"{''.join(dashed_word)}")

    if '_' not in dashed_word:
        end_of_game = True
        print("You've won!!")

    if lives == 0:
        end_of_game = True
        print("Game over!!")
