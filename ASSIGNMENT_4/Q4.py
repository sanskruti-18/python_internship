# Method 1
import math          # use math module

def is_perfect_square(num):
    # Check if the square root of the num is an integer
    sprt = math.sqrt(num)
    return sprt.is_integer()

# take inout from the user
num = int(input("Enter a num: "))

if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
