'''A text based calculator'''
result = 0
continue_calc = True


def add(n1, n2):
    '''Returns sum of two values'''
    return n1 + n2


def subtract(n1, n2):
    '''Returns the subtraction of two numbers'''
    return n1 - n2


def multiply(n1, n2):
    '''Returns the multiplication of two numbers'''
    return n1 * n2


def divide(n1, n2):
    '''Returns number 1 divided by number 2 '''
    return n1/n2


operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

number1 = int(input("What is the first number? "))

# use for loop to print out each of the keys in operators dictionary
for key in operators:
    print(f'{key}')

operation_symbol = input(
    "What is the operation that you want to use? Use only those seen in the lines above. ")

# I'm placing the second number input after the operator input, for better use experience.
number2 = int(input("What is the second number? "))

calling_function = operators[operation_symbol]
number3 = calling_function(number1, number2)

print(f"{number1} {operation_symbol} {number2} = {number3}")

while continue_calc:
    continue_calc_input = input(
        "Do you want to continue calculations with value {number3}. Type 'y' to continue or 'n' to quit. ")

    if continue_calc_input == 'n':
        continue_calc = False
        break

    operation_symbol = input(
        "What is the operation that you want to use? Use only those seen in the lines above. ")

    calling_function = operators[operation_symbol]
    number4 = int(input("What is the next number? "))
    result = calling_function(number3, number4)

    print(f"{number3} {operation_symbol} {number4} = {result}")
