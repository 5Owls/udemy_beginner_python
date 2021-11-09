highest = 0

print("What is the highest score for a list of student numbers:")
student_scores = input("Student scores seperated by a comma: ")

student_scores_list = student_scores.split(",")

for score in student_scores_list:
    score = int(score) + 0 # changing it to int so i can do a comparison
    if score >= highest:
        highest = score

#
print(f"The highest score is: {highest}")

#another way to do this:
highest = max(student_scores_list)
print(f"The max value: {highest}")
# student_score = input("Scores seperated by a comma: ").split(",")
#
# for item in range(0, len(student_score)):
#     student_score[item] = int(student_score[n])
#
# print(student_score)
