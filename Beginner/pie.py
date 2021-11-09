# fruits = ['cherry', 'apple', 'coco']
# pie = []
#
# for fruit in fruits:
#     pie.append(fruit + 'pie')
#
# print(pie)

student_height = []
sum_total = 0

user_input_height = input("What are the heights that we should calculate the average for, seperated by a comma: ")
student_height = user_input_height.split(",")

amount_of_students = len(student_height)

for student in student_height:
    sum_total = sum_total + int(student)

average = sum_total/amount_of_students

print(f"The average is: {average}")
