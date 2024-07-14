# Taking the string as input from the user
input_string = input("Enter a string: ")

# Taking the index as input from the user
index = int(input("Enter an index: "))

# if condition to check index in in the range
if 0 <= index < len(input_string):
    # Printing the character at the specified index
    print(f"The character at index {index} is '{input_string[index]}'")
else:
    # Printing an error if the index is out of range
    print("Invalid index. Please enter an index within the valid range.")