'''
TriangleClassification
Samantha Cook
3.15.2023
Python II
'''

first_side = float(input("What is the lenght of the first side? >> "))
second_side = float(input("What is the length of the second side? >> "))
third_side = float(input("What is the length of the third side? >> "))

if first_side == second_side == third_side:
    print("That is an equilateral triangle.")
elif first_side == second_side or second_side == third_side or third_side == first_side:
    print("That is an isosceles triangle.")
else:
    print("That is a scalene triangle")