'''
Sum Range
Samantha Cook
3/17/2023
Python II
'''

number1 = int(input("Enter the first number in the range >> "))
number2 = int(input("Enter the last number in the range >> "))
total = 0


for numbers in range(number1, number2 + 1):
    total = total + numbers
print("The sum of the numberse between", number1, "and", number2, "is:", total)
