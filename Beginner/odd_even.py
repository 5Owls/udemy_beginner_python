number = int(input("Give me a number? "))

# is this number odd or even, odd wil have remainder, even will not
remainder = number % 2

if remainder == 0:
    print(f"The remainder is: {remainder} thus it is an EVEN number")
else:
    print(f"The remainder is: {remainder} thus it is an ODD number")
