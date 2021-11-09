#practicing some more logic
print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, L: ")
add_pepi = input("Do you want Pepperoni? Y, N: ")
extra_cheese = input("Do you want cheese? Y, N: ")

total = 0

if size == "S":
    total = total + 15
    if add_pepi == "Y":
        total = total + 2

if size == "M":
    total = total + 20
    if add_pepi == "Y":
        total = total + 3

if size == "L":
    total = total + 25
    if add_pepi == "Y":
        total = total + 3

if extra_cheese == "Y":
    total = total + 1

print(f"Your total for your pizza: {total:0.2f}")
