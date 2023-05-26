'''
MinMax
Samantha Cook
3/17/2023
Python II
'''

number = input("Enter a number >> ")
min = number
max = number
repeat = input("Do you want to repeat again")
while repeat == "y":
    number = input("Enter a number >> ")
    if min > number:
         min = number
    if max < number:
        max = number
    repeat = input("Do you want to repeat again")
else:
        print("The max number is", max)
        print("The min number is", min)
