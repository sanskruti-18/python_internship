# calculate the area of the square 
def square_area(side_length):
    area = side_length ** 2
    return area

# Taking input from the user
side_length = float(input("Enter the side length of the square: "))

# Calculating the area
area = square_area(side_length)

# Displaying the result
print(f"The area of the square with side length {side_length} is {area}")
