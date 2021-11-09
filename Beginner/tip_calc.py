'''Practicing what ive learnt so far in python course concentrating on formating
and PEMDAS.'''

#input
total_bill = int(input("What is the total bill? "))
total_eaters = int(input("What is the total number of people? "))
tip_percentage = int(input("What tip do you want to give? 10, 12, 15 "))

total_amount_to_pay = total_bill + (total_bill * (tip_percentage/100))
each_should_pay = round(total_amount_to_pay/total_eaters,2)

print(f"Each should pay: {each_should_pay:0.2f}")
