import math

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Right-angled"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def circumcenter_radius(a, b, c):
    if classify_triangle(a, b, c) == "Right-angled":
        hypotenuse = max(a, b, c)
        return hypotenuse / 2
    else:
        return -1

# Take input from the user
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if is_valid_triangle(a, b, c):
    triangle_type = classify_triangle(a, b, c)
    print(f"The triangle is {triangle_type}.")
    
    if triangle_type == "Right-angled":
        radius = circumcenter_radius(a, b, c)
        print(f"The radius of the circumcenter is: {radius}")
    else:
        print("-1")
else:
    print("The sides do not form a valid triangle.")
