############DEBUGGING#####################
#Notes for future me

# # Describe Problem
# def my_function():
#     #print you've got it when we are at level 20
#     #it never reached 20 until we added one
#   for i in range(1, 20+1):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] #index 0 - 5
# #❗️dice_num = randint(1, 6) # a random number from 1 to 6 it 
# dice_num = randint(0, 5)
# print(dice_num)
# print(dice_imgs[dice_num])#index out of range error, there is no index 6

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# ❗️age = input("How old are you?")
# ✅age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #testing purpose:
# print(pages)
# #❗️word_per_page ❗️== int(input("Number of words per page: "))
# word_per_page ✅= int(input("Number of words per page: "))
# #testing
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)
  
print([1,2,3,5,8,13])
mutate([1,2,3,5,8,13])

