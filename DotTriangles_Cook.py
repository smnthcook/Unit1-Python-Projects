'''
DotTriangles
Samantha Cook
3/17/2023
Python II
'''

repeat = "y"
while repeat == "y": 
    height = int(input("Enter the height of the triangle >> "))
    for rows in range(height):
        for columns in range (rows + 1):
            print("* ", end="")
        print()
    repeat = input("Do you want to draw another triangle (y/n) >> ")
    