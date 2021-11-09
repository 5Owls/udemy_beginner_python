import random

letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','v','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','+','&','*','(',')']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letter would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

# random_value_letters = []
# random_value_numbers = []
# random_value_symbols = []
unscrambled_password = []
for value in range(0, nr_letters): #randomly get LETTERS
    random_value_letters.append(random.randint(0, 51))
    #random_value_letters += random.choice(letters)

for value in range(0, nr_numbers): #randomly get NUMBERS
    random_value_numbers.append(random.randint(0, 9))
    #random_value_numbers += random.choice(numbers)

for value in range(0, nr_symbols): # randomly get SYMBOLS
    random_value_symbols.append(random.randint(0, 8))
    #random_value_symbols += random.choice(symbols)

 #save the letters,numbers and symbols

for value in random_value_letters:#gothrough randomlist values
    unscrambled_password.append(letters[value])#get a value from letters at random index

for value in random_value_numbers:
    unscrambled_password.append(numbers[value])

for value in random_value_symbols:
    unscrambled_password.append(symbols[value])

print(unscrambled_password)


# scrambled_password = []
# password = ''
# for value in range(0, len(unscrambled_password)):
#     random_number = random.randint(0, len(unscrambled_password)-1)#minus one or index out of bounds
#     scrambled_password.append(unscrambled_password[random_number])
#     unscrambled_password.pop(random_number)#remove so we dont use it again
#
# print(len(scrambled_password))
# print(password.join(scrambled_password))
