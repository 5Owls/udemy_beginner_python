#if divisible by three = fizz
#if divisble by 5 = buzz
#if divisble by 3 and 5 = fizz buzz

#as an extra: calculate how many fizzes, buzzes and fizz buzzes there are
fizzes = 0
buzzes = 0
fizz_buzzes = 0

for value in range(1, 101):
    if value%3 == 0 and value%5 == 0:
        fizz_buzzes = fizz_buzzes + 1
        print("fizz buzz")
    elif value%3 == 0:
        fizzes = fizzes + 1
        print("fizz")
    elif value%5 == 0:
        buzzes = buzzes + 1
        print("buzz")
    else:
        print(value)
print(f"There are {fizz_buzzes} fizz_buzzes, {fizzes} fizzes and {buzzes} buzzes.")
