import random

letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','v','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','+','&','*','(',')']

nr_letters = int(input("How many letters do you want in your password? "))
nr_numbers = int(input("How many numbers do you want in your password? "))
nr_symbols = int(input("How many symbols do you want in your password? "))

password = []
new_password = ''

for i in range(0, nr_letters):
    password += random.choice(letters)
#print(password)

for i in range(0 , nr_numbers):
    password += random.choice(numbers)

for i in range(0, nr_symbols):
    password += random.choice(symbols)

random.shuffle(password)

print(f'Your new password is: {new_password.join(password)}')
