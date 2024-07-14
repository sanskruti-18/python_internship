# define the function
def count_alphabets(str):
    alphabet_count = 0
    for i in str:
        if i.isalpha():
            alphabet_count = alphabet_count + 1
        else:
            pass

    # print the output
    print(f"The number of alphabets is: {alphabet_count}")

# input the string
str = input("Enter a sentence:")
count_alphabets(str) # calling the function