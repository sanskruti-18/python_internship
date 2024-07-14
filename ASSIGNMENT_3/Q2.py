# define and use if condition to compare
def compare_lenght_of_strings(str1, str2):
    if len(str1) > len(str2):
        print("The string with max length is:", str1)
    elif len(str1) < len(str2):
        print("The string with max length is:", str2)
    else:
        print("Both strings have the same length:")
        print(str1)
        print(str2)

# take input of two strings
str1 = input("Enter the 1st string: ")
str2 = input("Enter the 2nd string: ")

# calling the function
compare_lenght_of_strings(str1, str2)