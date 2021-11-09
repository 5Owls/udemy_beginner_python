#Calculating BMI and giving correct diagnoses
# weight = int(input("What is your weight in kg? "))
# height = int(input("What is your height in m? "))
# bmi = height / (weight ** 2)
bmi = 60
if bmi <= 18.5:
    print(f"Your BMI is {bmi:0.2f}. You are UNDERWEIGHT")
elif bmi <= 25:
    print(f"Your BMI is {bmi:0.2f}. You are NORMAL weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi:0.2f}. You are OVER weight")
elif bmi <= 35:
    print(f"Your BMI is {bmi:0.2f}. You are OBESE")
else:
    print(f"Your BMI is {bmi:0.2f}. You are CLINICALLY obese")
