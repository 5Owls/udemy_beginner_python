# intro to dictionaries

# programming_dictionary = {
#     "bug": "unexpected error",
#     "function": "a piece of code you can easily call over and over",
#     "loop": "the action of doing something over and over",
# }

# # calling a dictionary
# # print(programming_dictionary["loop"])

# for key in programming_dictionary:
#     print(f"{key} : {programming_dictionary[key]}")

# 🚨 dictionary assignment 1
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}


# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if (student_scores[key] >= 91) and (student_scores[key] <= 100):
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] >= 81 and student_scores[key] <= 90:
#         student_grades[key] = "Exceeds expectation"
#     elif student_scores[key] >= 71 and student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# for key in student_grades:
#     print(f"{key} : {student_grades[key]}")

# 🚨 Assignment 2
# travel_log = {
#     "France": {"cities_visit": ["Paris", "Lille", "Dijon"], "total_visits_per_city": [1, 2, 1]},
#     "Germany": ["Berlin", "Hamburg"]
# }

# 🚨Assignment 3
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# TODO: Write the function that will allow new countries to be added to the travel_log. 👇


def add_new_country(country, times_visited, cities_visited):
    # travel_log.append(
    #     {"country": country, "visits": times_visited, "cities": cities_visited})
    # OR
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
