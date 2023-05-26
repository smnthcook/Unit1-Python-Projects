'''
Factors
Samantha Cook
3/17/2023
Python II
'''
number = int(input("Enter a number to get the factors >> "))

for i in range(1, number + 1):
    mod = number % i
    if mod == 0:
        print(i)
    