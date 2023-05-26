'''
BMI
Samantha Cook
3/15/2023
Python II
'''


print("Enter your height in feet and inches.")

feet = int(input("Feet >> "))
inches = int(input("Inches >> "))
weight = int(input("Enter your weight in pounds >> "))
height = (feet*12) + inches

BMI = (weight / height**2) * 703

if BMI < 18.5:
    print("You are underweight.")
elif BMI >= 18.5 and BMI <= 25:
    print("You are normal")
elif BMI >= 25 and BMI <=30:
    print("You are overweight")
elif BMI >= 30 and BMI <=35:
    print("You are obese.")
else:
    print("You are extremely obese")
    

    