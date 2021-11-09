# import random
#
# print("Who will pay for this meal? ")
# names = input("Put all the names seperated by a comma and space: ")
# list_names = names.split(", ")
# #print(list_names)
# number_of_people = len(list_names) - 1
# #print(number_of_people)
# random_number = random.randint(0, number_of_people)
#
# print(f"{list_names[random_number]} is going to pay for the meal.")

# practising nested lists:

name = ['rosie', 'reinhard', 'micah']
job = ['coder', 'writer', 'player']

combo = [name, job]
#print(combo)

print(combo[1][2])
print(combo[1][1])
#how to get a value inside nested list??
#combo_list_name([list_number][item_number])
