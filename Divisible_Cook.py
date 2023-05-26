'''
Divisible
Samantha Cook
3/15/2023
Python II
'''

diviend = float(input("Enter the diviend >> "))
divisor = float(input("Enter the divisor >> "))
mod = diviend % divisor

if mod == 0:
    print(str(diviend) + " is divisble by " + str(divisor))
else:
    print(str(diviend)+ " is not divisble by " + str(divisor))