# calculate gcd of two numbers
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating the GCD
gcd = calculate_gcd(num1, num2)

# Displaying the result
print(f"The GCD of {num1} and {num2} is {gcd}")
