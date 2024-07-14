# Method 1
# define a function
def is_palindrome(string):
    if string == reversed_string:
        print("The string is a palindrome")
    else:
        print("The string is not palindrome")

# Taking the string as input from the user
string = input("Enter a string: ")

# Reversing the string using slicing
reversed_string = string[::-1]

# calling the function
is_palindrome(string)

# method 2
def palindrome(string):
    for i in range(0, int(len(string)/2)):
        if string[i] == string[len(string)-i-1]:
            return True
        else:
            return False
        
a = palindrome(string)

if(a):
    print("It's a palindrome")
else:
    print("It's not a plaindrome")