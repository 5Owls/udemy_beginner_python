#back to basics with if and else statements
print("Welcome to Theme park")
height = int(input("What is you height in cm? "))

# if height == 120:
#     print("You can ride roller coaster")
# else:
#     print("Sorry, you need to grow taller")

# but what if the wanne-be rider is taller than 120?
if height >= 120:
    print("Enjoy the ride")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("grow a bit then you can ride")
