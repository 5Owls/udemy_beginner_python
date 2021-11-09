year = int(input("What year? "))

if year%4 == 0:
    if year%100 != 0:
        print("It's a leap year")
    elif year%100 == 0 and year%400 == 0:
        print("It's a leap year")
    else:
        print("It's a not leap year")
else:
    print("Its NOT a leap year")
