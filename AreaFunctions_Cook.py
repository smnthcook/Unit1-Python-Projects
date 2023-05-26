'''
AreaFunctions
Samantha Cook
3/21/2023
Python II
'''
def square_area(x):
    area = x*x
    return area

def circle_area(x):
    area = 3.14 * (x**2)
    return area

def triangle_area(base, height):
    area = ((.5 * base) * height)
    return area

print(square_area(4))
print(square_area(5))
print(triangle_area(7, 2))