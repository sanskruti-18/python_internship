# Taking the string as input from the user
input_string = input("Enter a string: ")

# Taking the starting index as input from the user
start_index = int(input("Enter the starting index: "))

# Taking the ending index as input from the user
end_index = int(input("Enter the ending index: "))

# Extracting the substring between the indices
substring = input_string[start_index:end_index]

# Printing the substring
print(f"The substring from index {start_index} to {end_index} is: {substring}")